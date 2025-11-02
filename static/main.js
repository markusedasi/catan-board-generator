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

                    const numberSpan = document.createElement('span');
                    numberSpan.classList.add('tile-number');
                    numberSpan.textContent = number || '-';

                    tileDiv.appendChild(numberSpan);
                    rowDiv.appendChild(tileDiv);
                });
                boardContainer.appendChild(rowDiv);
            });
        });
});
