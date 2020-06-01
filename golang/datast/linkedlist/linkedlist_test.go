package linkedlist

import "testing"

func TestDummy(t *testing.T) {
	l := New()

	if !l.IsEmpty() {
		t.Errorf("expected to be empty")
	}

	if actual := l.Len(); actual != 0 {
		t.Errorf("expected length be %d, but got %d", 0, actual)
	}

	l.PushFront(10)
	if length := l.Len(); length != 1 {
		t.Errorf("expected length to be %d, but got %d", length, l.Len())
	}

	if front := l.Front().Value(); front != 10 {
		t.Errorf("expected value at front to be %d, but got %d", front, l.Len())
	}

	l.PushFront(20)
	if length := l.Len(); length != 2 {
		t.Errorf("expected length to be %d, but got %d", length, l.Len())
	}

	if front := l.Front().Value(); front != 20 {
		t.Errorf("expected value at front to be %d, but got %d", front, l.Len())
	}

	l.PushFront(30)
	l.PushFront(40)
	l.PushBack(0)
	l.PushBack(-10)
	l.PushFront(50)
	expectedValues := []int{50, 40, 30, 20, 10, 0, -10}
	for i, n := 0, l.Front(); n != nil; i, n = i+1, n.Next() {
		if actual, expected := n.Value(), expectedValues[i]; actual != expected {
			t.Errorf("expected value at index %d to be %d, but got %d", i, expected, n.Value())
		}
	}

	if expected, actual := len(expectedValues), l.Len(); expected != actual {
		t.Errorf("expected length to be %d, but got %d", expected, actual)
	}

	// Pop value from the back
	if expected, actual := expectedValues[len(expectedValues)-1], l.PopBack().Value(); expected != actual {
		t.Errorf("expected last value to be %d, but got %d", expected, actual)
	}

	if expected, actual := len(expectedValues)-1, l.Len(); expected != actual {
		t.Errorf("expected length to be %d, but got %d", expected, actual)
	}

	// Pop value from the front
	if expected, actual := expectedValues[0], l.PopFront().Value(); expected != actual {
		t.Errorf("expected first value to be %d, but got %d", expected, actual)
	}

	if expected, actual := len(expectedValues)-2, l.Len(); expected != actual {
		t.Errorf("expected length to be %d, but got %d", expected, actual)
	}

}
