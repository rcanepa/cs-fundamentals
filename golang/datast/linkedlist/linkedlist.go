package linkedlist

import (
	"fmt"
)

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

// LinkedList provides a constructor for a linked list
type LinkedList struct {
	head *Node
	size int
}

// lastNode returns a pointer to the last Node
func (l *LinkedList) lastNode() *Node {
	if l.head == nil {
		return nil
	}
	curr := l.head
	for curr.Next() != nil {
		curr = curr.Next()
	}
	return curr
}

// New creates a new LinkedList instance
func New() LinkedList {
	ll := LinkedList{
		size: 0,
	}
	return ll
}

// Len returns the number of Nodes the LinkedList has
func (l *LinkedList) Len() int {
	return l.size
}

// IsEmpty returns `true` if the LinkedList has no Nodes
func (l *LinkedList) IsEmpty() bool {
	return l.size == 0
}

// Front returns the first Node of a LinkedList
func (l *LinkedList) Front() *Node {
	return l.head
}

// PushFront inserts a Node at the front of a LinkedList
func (l *LinkedList) PushFront(value int) *Node {
	node := Node{value: value}
	if l.head == nil {
		l.head = &node
	} else {
		node.next = l.head
		l.head = &node
	}
	l.size++
	return &node
}

// PushBack inserts a Node at the end of the LinkedList
func (l *LinkedList) PushBack(value int) *Node {
	if l.head == nil {
		return l.PushFront(value)
	}
	lastNode := l.lastNode()
	node := Node{value: value}
	lastNode.next = &node
	l.size++
	return &node
}

// PopFront removes and returns the first Node of the LinkedList
func (l *LinkedList) PopFront() *Node {
	if l.head == nil {
		return nil
	}
	n := l.head
	l.head = l.head.next
	l.size--
	return n
}

// PopBack removes and returns the last Node of the LinkedList
func (l *LinkedList) PopBack() *Node {
	if l.head == nil {
		return nil
	}
	if l.head.Next() == nil {
		return l.PopFront()
	}
	curr := l.head
	for curr.Next().Next() != nil {
		curr = curr.Next()
	}
	last := curr.Next()
	curr.next = nil
	l.size--
	return last
}

// String prints a string representation
func (l *LinkedList) String() string {
	s := fmt.Sprintf("LinkedList{size: %d, Nodes: ", l.Len())
	for n := l.Front(); n != nil; n = n.Next() {
		s += fmt.Sprintf("%d->", n.Value())
	}
	return s + fmt.Sprintf("}")
}
