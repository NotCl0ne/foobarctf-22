#!/usr/bin/env node
const rl = require('readline').createInterface(process.stdin, process.stdout)

require = undefined
module = undefined

const flag = 'GLUG{H4!l_hydr4}'

rl.question('Whats your order sir?\n', (input) => {
    if (/[\'\"\`]/g .test(input)) {
        console.log('Access Denied.')
    } else if ((() => {
        for (let i = 0; i < input.length; i++) {
            if ((input[i] ^ (+[])) !== (input[i % Infinity] & 255)) {
                return true
            }
            return false
        }
    })()) {
        console.log('Access Denied.')
    } else {
        try {
            console.log('Executing...', eval(`'use strict'; (() => { return 0 /* ${input} */ })()`));
        } catch (error) {
            console.log('Access Denied.', error.message)
        }
    }
    rl.close()
})
