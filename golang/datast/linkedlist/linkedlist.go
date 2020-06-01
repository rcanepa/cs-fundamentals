package linkedlist

import (
	"fmt"
)

/*

// Inspired by Golang official implementation[1]

func main() {
	// Create a new list and put some numbers in it.
	l := list.New()
	e4 := l.PushBack(4)
	e1 := l.PushFront(1)
	l.InsertBefore(3, e4)
	l.InsertAfter(2, e1)

	// Iterate through list and print its contents.
	for e := l.Front(); e != nil; e = e.Next() {
		fmt.Println(e.Value)
	}
}

// [1] https://golang.org/pkg/container/list/
*/

type Node struct {
	value int
	next  *Node
}

func (n *Node) Next() *Node {
	return n.next
}

func (n *Node) Value() int {
	return n.value
}

func newNode(value int) Node {
	return Node{value: value}
}

// LinkedList provides a constructor for a linked list
type LinkedList struct {
	Head    *Node
	Next    *Node
	Size    int
	IsEmpty func() bool
}

// lastNode returns a pointer to the last Node
func (l *LinkedList) lastNode() *Node {
	if l.Head == nil {
		return nil
	}
	curr := l.Head
	for curr.Next() != nil {
		curr = curr.Next()
	}
	return curr
}

// New creates a new LinkedList instance
func New() LinkedList {
	ll := LinkedList{
		Size: 0,
	}
	return ll
}

// Front returns the first Node of a LinkedList
func (l *LinkedList) Front() *Node {
	return l.Head
}

// PushFront inserts a Node at the front of a LinkedList
func (l *LinkedList) PushFront(value int) *Node {
	node := newNode(value)
	if l.Head == nil {
		l.Head = &node
	} else {
		node.next = l.Head
		l.Head = &node
	}
	l.Size++
	return &node
}

// PushBack inserts a Node at the end of the LinkedList
func (l *LinkedList) PushBack(value int) *Node {
	if l.Head == nil {
		return l.PushFront(value)
	}
	lastNode := l.lastNode()
	node := newNode(value)
	lastNode.next = &node
	l.Size++
	return &node
}

// ToString prints a string representation
func (l *LinkedList) ToString() string {
	s := fmt.Sprintf("LinkedList{Size: %d, Nodes: ", l.Size)
	for n := l.Front(); n != nil; n = n.Next() {
		s += fmt.Sprintf("%d->", n.Value())
	}
	return s + fmt.Sprintf("}")
}

// PopFront removes and returns the first Node of the LinkedList
func (l *LinkedList) PopFront() *Node {
	if l.Head == nil {
		return nil
	}
	n := l.Head
	l.Head = l.Head.next
	l.Size--
	return n
}
