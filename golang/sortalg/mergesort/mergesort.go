package mergesort

// Merging works by moving temp elements, in order, from both array
// to a temporary one that can hold len(left) + len(right) elements.
// Then, elements are copied back to each array in the right order.
func merge(left, right []int) {
	tlength := len(left) + len(right)
	temp := make([]int, tlength)

	// Move the smtempest from both array to the temporary array
	i1, i2, j1, j2, k := 0, 0, len(left), len(right), 0
	for i1 < j1 && i2 < j2 {
		v1, v2 := left[i1], right[i2]
		if v1 <= v2 {
			temp[k] = v1
			i1++
		} else {
			temp[k] = v2
			i2++
		}
		k++
	}

	// Move everything we didn't move from left to temporary
	for i1 < j1 {
		temp[k] = left[i1]
		i1++
		k++
	}

	// Move everything we didn't move from right to temporary
	for i2 < j2 {
		temp[k] = right[i2]
		i2++
		k++
	}

	// Move everything back to each array
	for i, v := range temp {
		if i < j1 {
			left[i] = v
		} else {
			right[i-j1] = v
		}
	}
}

// Sort a slice of integers using the mergesort algorithm
func Sort(elements []int) {
	if len(elements) <= 1 {
		return
	}
	mid := len(elements) / 2
	left, right := elements[:mid], elements[mid:]
	Sort(left)
	Sort(right)
	merge(left, right)
}
