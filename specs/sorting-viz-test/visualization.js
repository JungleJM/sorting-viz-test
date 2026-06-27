// Visualization implementation
document.addEventListener('DOMContentLoaded', function() {
    const sortingAlgorithms = new SortingAlgorithms();
    let currentArray = [];
    let isAnimating = false;

    // DOM elements
    const arrayContainer = document.getElementById('arrayContainer');
    const generateBtn = document.getElementById('generate');
    const bubbleSortBtn = document.getElementById('bubbleSort');
    const quickSortBtn = document.getElementById('quickSort');
    const mergeSortBtn = document.getElementById('mergeSort');
    const resetBtn = document.getElementById('reset');
    const arrayLengthSpan = document.getElementById('arrayLength');
    const comparisonsSpan = document.getElementById('comparisons');
    const swapsSpan = document.getElementById('swaps');

    // Initialize
    updateStats();

    generateBtn.addEventListener('click', () => {
        if (isAnimating) return;
        currentArray = sortingAlgorithms.generateArray(20);
        renderArray();
        updateStats();
    });

    bubbleSortBtn.addEventListener('click', () => {
        if (isAnimating || currentArray.length === 0) return;
        isAnimating = true;
        animateSort(sortingAlgorithms.bubbleSort.bind(sortingAlgorithms), currentArray);
    });

    quickSortBtn.addEventListener('click', () => {
        if (isAnimating || currentArray.length === 0) return;
        isAnimating = true;
        animateSort(sortingAlgorithms.quickSort.bind(sortingAlgorithms), currentArray);
    });

    mergeSortBtn.addEventListener('click', () => {
        if (isAnimating || currentArray.length === 0) return;
        isAnimating = true;
        animateSort(sortingAlgorithms.mergeSort.bind(sortingAlgorithms), currentArray);
    });

    resetBtn.addEventListener('click', () => {
        if (isAnimating) return;
        currentArray = [];
        renderArray();
        updateStats();
    });

    function renderArray() {
        arrayContainer.innerHTML = '';
        currentArray.forEach(value => {
            const bar = document.createElement('div');
            bar.className = 'bar';
            bar.style.height = `${value * 2}px`;
            arrayContainer.appendChild(bar);
        });
    }

    function updateStats() {
        arrayLengthSpan.textContent = currentArray.length;
        comparisonsSpan.textContent = sortingAlgorithms.comparisons;
        swapsSpan.textContent = sortingAlgorithms.swaps;
    }

    async function animateSort(sortFunction, array) {
        const bars = document.querySelectorAll('.bar');
        let sortedIndices = new Set();

        // Reset animation state
        bars.forEach(bar => bar.classList.remove('comparing', 'sorted'));

        // Make a copy of the array to sort
        const arrayToSort = [...array];

        // Sort with animation
        for (let i = 0; i < arrayToSort.length - 1; i++) {
            for (let j = 0; j < arrayToSort.length - i - 1; j++) {
                sortingAlgorithms.comparisons++;
                bars[j].classList.add('comparing');
                bars[j + 1].classList.add('comparing');

                await new Promise(resolve => setTimeout(resolve, 50));

                if (arrayToSort[j] > arrayToSort[j + 1]) {
                    // Swap
                    [arrayToSort[j], arrayToSort[j + 1]] = [arrayToSort[j + 1], arrayToSort[j]];
                    sortingAlgorithms.swaps++;

                    // Update bars visually
                    const tempHeight = bars[j].style.height;
                    bars[j].style.height = bars[j + 1].style.height;
                    bars[j + 1].style.height = tempHeight;
                }

                bars[j].classList.remove('comparing');
                bars[j + 1].classList.remove('comparing');

                // Mark as sorted
                if (i === arrayToSort.length - 2 && j === i) {
                    bars[j].classList.add('sorted');
                    bars[j + 1].classList.add('sorted');
                }
            }
        }

        // Mark all bars as sorted at the end
        bars.forEach(bar => bar.classList.add('sorted'));

        currentArray = arrayToSort;
        updateStats();
        isAnimating = false;
    }
});
