#!/usr/bin/env python3
import os
import re
import threading
import yaml


def get_categories():
    """
    Each category is in it's own directory,
    so get the names of all directories that do not begin with `.`.
    """
    denylist_regex = r'\..*'

    categories = [
        name for name
        in os.listdir(".") if os.path.isdir(name)
        and not re.match(denylist_regex, name)
    ]
    print("Found categories: " + ", ".join(categories))
    return categories


def get_challenges(category):
    """
    Each challenge is in it's own directory,
    so get the names of all directories.
    """
    challenges = [
        f"{category}/{name}" for name
        in os.listdir(f"./{category}") if os.path.isdir(f"{category}/{name}")
    ]
    return challenges


def sync(category):
    """
    Synchronize all challenges in the given category,
    where each challenge is in it's own folder, to CTFd via ctfcli.
    """
    for challenge in get_challenges():
        if os.path.exists(f"{challenge}/challenge.yml"):
            print(f"Syncing challenge: {challenge}")
            os.system(
                f"ctf challenge sync '{challenge}'; ctf challenge install '{challenge}'"
            )


def firewall(visible, hidden):
    """
    Change `Firewall` rules for visible and hidden challenges
    """
    rules = os.popen("gcloud compute firewall-rules --format=json list").read()

    for category in visible:
        for challenge in visible[category]:
            if challenge['port'] and challenge['name'] not in rules:
                os.system(
                    f"gcloud compute firewall-rules create {challenge['name']}"
                    f" --allow tcp:{challenge['port']}"
                     " --priority 1000"
                     " --target-tags challs"
                )
                print(f"Created firewall rules for: {challenge['name']}")

    for category in hidden:
        for challenge in hidden[category]:
            if challenge['port'] and challenge['name'] in rules:
                os.system(
                    "echo -e 'Y\n' | "
                    f"gcloud compute firewall-rules delete {challenge['name']}"
                )
                print(f"Deleted firewall rules for: {challenge['name']}")


def change_state(waves, state):
    """
    Change the state of certain waves of challenges
    """
    if state not in ['visible', 'hidden']:
        raise Exception("state must be 'visible' or 'hidden'")

    visible = {}
    hidden = {}

    categories = get_categories()

    for category in categories:
        visible[category] = []
        hidden[category] = []

    with open('challenge-waves.yml') as file:
        challenge_waves = yaml.load(file, Loader=yaml.FullLoader)

    for wave in [wave for wave in challenge_waves if wave in waves]:
        for category in challenge_waves[wave]:
            for challenge in challenge_waves[wave][category]:
                with open(f'{category}/{challenge}/challenge.yml', 'r') as file:
                    challenge_yml = yaml.load(file, Loader=yaml.FullLoader)
                challenge_yml['state'] = state
                with open(f'{category}/{challenge}/challenge.yml', 'w') as file:
                    yaml.dump(challenge_yml, file, sort_keys=False)

                name = challenge_yml['name'].lower().replace(' ', '-')
                if state == 'visible':
                    if 'expose' in challenge_yml:
                        visible[category].append({
                            "name": name,
                            "port": challenge_yml['expose'][0]['nodePort']
                        })
                    else:
                        visible[category].append({
                            "name": name,
                            "port": None
                        })
                else:
                    if 'expose' in challenge_yml:
                        hidden[category].append({
                            "name": name,
                            "port": challenge_yml['expose'][0]['nodePort']
                        })
                    else:
                        hidden[category].append({
                            "name": name,
                            "port": None
                        })

    return visible, hidden


def init():
    """
    Initialize ctfcli with the CTFD_TOKEN and CTFD_URL.
    """
    CTFD_TOKEN = os.getenv("CTFD_TOKEN", default=None)
    CTFD_URL = os.getenv("CTFD_URL", default=None)

    if not CTFD_TOKEN or not CTFD_URL:
        print("CTFD_TOKEN or CTFD_URL missing.")
        exit(1)

    os.system(f"echo '{CTFD_URL}\n{CTFD_TOKEN}\ny' | ctf init")


if __name__ == "__main__":
    visible, hidden = change_state('wave1', 'visible')

    init()

    # Synchronize each category in it's own thread.
    jobs = []
    for category in get_categories():
        jobs.append(threading.Thread(target=sync, args=(category, )))
    for job in jobs:
        job.start()
    for job in jobs:
        job.join()

    print(
        "Synchronized successfully!\n"
        "The following challenges are now visible:"
    )
    for category in visible:
        print(
            f"\n## {category}"
             "\n- ".join([challenge['name'] for challenge in visible[category]])
        )
