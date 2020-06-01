package main

import (
	"fmt"

	"github.com/rcanepa/cs-fundamentals/datast/linkedlist"
)

func main() {
	l := linkedlist.New()
	fmt.Println(l.ToString())
	l.PushFront(10)
	fmt.Println(l.ToString())
	l.PushFront(20)
	fmt.Println(l.ToString())
	l.PushBack(30)
	l.PushFront(0)
	l.PushBack(50)
	fmt.Println(l.ToString())
	fmt.Println("Romoving ", l.PopBack().Value(), " from the back")
	fmt.Println(l.ToString())
	l.PushBack(200)
	fmt.Println("Romoving ", l.PopBack().Value(), " from the back")
	fmt.Println(l.ToString())
	l.PushBack(60)
	for n := l.PopFront(); n != nil; n = l.PopFront() {
		fmt.Println("Removing ", n.Value(), " the front")
		fmt.Println(l.ToString())
	}
}
