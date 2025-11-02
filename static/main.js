document.getElementById('shuffleButton').addEventListener('click', () => {
    fetch('/api/shuffle')
        .then(response => response.json())
        .then(board => {
            const boardContainer = document.getElementById('board');
            boardContainer.innerHTML = '';

            board.forEach(row => {
                const rowDiv = document.createElement('div');
                rowDiv.classList.add('board-row');

                row.forEach(({tile, number}) => {
                    const tileDiv = document.createElement('div');
                    tileDiv.classList.add('tile', tile);

                    const numSpan = document.createElement('span');
                    numSpan.classList.add('tile-number');
                    if (number === 6 || number === 8) {
                        numSpan.classList.add('red');
                    }
                    numSpan.textContent = number || '-';

                    tileDiv.appendChild(numSpan);
                    rowDiv.appendChild(tileDiv);
                });
                boardContainer.appendChild(rowDiv);
            });
        });
});
