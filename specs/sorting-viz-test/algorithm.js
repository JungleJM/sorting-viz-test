// Sorting algorithms implementation
class SortingAlgorithms {
    constructor() {
        this.comparisons = 0;
        this.swaps = 0;
    }

    generateArray(length) {
        const array = [];
        for (let i = 0; i < length; i++) {
            array.push(Math.floor(Math.random() * 100) + 1);
        }
        return array;
    }

    bubbleSort(array) {
        let n = array.length;
        this.comparisons = 0;
        this.swaps = 0;

        for (let i = 0; i < n - 1; i++) {
            for (let j = 0; j < n - i - 1; j++) {
                this.comparisons++;
                if (array[j] > array[j + 1]) {
                    // Swap
                    let temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                    this.swaps++;
                }
            }
        }
        return array;
    }

    quickSort(array) {
        this.comparisons = 0;
        this.swaps = 0;

        function partition(start, end) {
            const pivotValue = array[end];
            let pivotIndex = start;

            for (let i = start; i < end; i++) {
                this.comparisons++;
                if (array[i] < pivotValue) {
                    // Swap
                    let temp = array[i];
                    array[i] = array[pivotIndex];
                    array[pivotIndex] = temp;
                    pivotIndex++;
                    this.swaps++;
                }
            }

            // Swap pivot to its correct position
            let temp = array[pivotIndex];
            array[pivotIndex] = array[end];
            array[end] = temp;
            this.swaps++;

            return pivotIndex;
        }

        function quickSortHelper(start, end) {
            if (start >= end) return;

            const pivotIndex = partition(start, end);
            quickSortHelper(start, pivotIndex - 1);
            quickSortHelper(pivotIndex + 1, end);
        }

        quickSortHelper(0, array.length - 1);
        return array;
    }

    mergeSort(array) {
        this.comparisons = 0;
        this.swaps = 0;

        function merge(left, right) {
            let resultArray = [];
            let leftIndex = 0;
            let rightIndex = 0;

            while (leftIndex < left.length && rightIndex < right.length) {
                this.comparisons++;
                if (left[leftIndex] < right[rightIndex]) {
                    resultArray.push(left[leftIndex]);
                    leftIndex++;
                } else {
                    resultArray.push(right[rightIndex]);
                    rightIndex++;
                }
            }

            return resultArray
                .concat(left.slice(leftIndex))
                .concat(right.slice(rightIndex));
        }

        function mergeSortHelper(array) {
            if (array.length <= 1) return array;

            const middle = Math.floor(array.length / 2);
            const left = array.slice(0, middle);
            const right = array.slice(middle);

            return merge(mergeSortHelper(left), mergeSortHelper(right));
        }

        return mergeSortHelper(array);
    }
}
