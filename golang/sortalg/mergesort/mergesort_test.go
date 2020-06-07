package mergesort

import (
	"math/rand"
	"sort"
	"testing"
)

func genRandIntSlice(size int) []int {
	s := make([]int, size)
	for i := range s {
		s[i] = rand.Intn(100000)
	}
	return s
}

// Verifies if two slices are equal by comparing their elements
func notEqual(a []int, b []int) bool {
	if len(a) != len(b) {
		return true
	}
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			return true
		}
	}
	return false
}

func TestSuite(t *testing.T) {
	var actual, expected []int

	actual, expected = []int{}, []int{}
	Sort(actual)
	if notEqual(actual, expected) {
		t.Errorf("expected a to be %v, but got %v", expected, actual)
	}

	actual, expected = []int{1}, []int{1}
	Sort(actual)
	if notEqual(actual, expected) {
		t.Errorf("expected a to be %v, but got %v", expected, actual)
	}

	actual, expected = []int{1, 2}, []int{1, 2}
	Sort(actual)
	if notEqual(actual, expected) {
		t.Errorf("expected a to be %v, but got %v", expected, actual)
	}

	actual, expected = []int{2, 1}, []int{1, 2}
	Sort(actual)
	if notEqual(actual, expected) {
		t.Errorf("expected a to be %v, but got %v", expected, actual)
	}

	actual, expected = []int{2, 3, 1}, []int{1, 2, 3}
	Sort(actual)
	if notEqual(actual, expected) {
		t.Errorf("expected a to be %v, but got %v", expected, actual)
	}

	actual, expected = []int{2, 3, 1, 4}, []int{1, 2, 3, 4}
	Sort(actual)
	if notEqual(actual, expected) {
		t.Errorf("expected a to be %v, but got %v", expected, actual)
	}

	actual, expected = []int{2, 3, 5, 1, 4}, []int{1, 2, 3, 4, 5}
	Sort(actual)
	if notEqual(actual, expected) {
		t.Errorf("expected a to be %v, but got %v", expected, actual)
	}

	actual, expected = []int{6, 2, 3, 5, 1, 4}, []int{1, 2, 3, 4, 5, 6}
	Sort(actual)
	if notEqual(actual, expected) {
		t.Errorf("expected a to be %v, but got %v", expected, actual)
	}

	actual, expected = []int{6, 7, 2, 3, 5, 1, 4}, []int{1, 2, 3, 4, 5, 6, 7}
	Sort(actual)
	if notEqual(actual, expected) {
		t.Errorf("expected a to be %v, but got %v", expected, actual)
	}

	actual = genRandIntSlice(100000)
	expected = make([]int, len(actual))
	copy(expected, actual)
	sort.Ints(expected)
	Sort(actual)
	if notEqual(actual, expected) {
		t.Errorf("expected a to be %v, but got %v", expected, actual)
	}

}
