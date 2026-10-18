document.getElementById('scanBtn').addEventListener('click', async () => {
    const urlInput = document.getElementById('urlInput').value.trim();
    const loadingDiv = document.getElementById('loading');
    const resultCard = document.getElementById('resultCard');
    const statusText = document.getElementById('statusText');
    const scoreText = document.getElementById('scoreText');
    const warningsList = document.getElementById('warningsList');

    if (!urlInput) {
        alert('Please enter a URL first.');
        return;
    }

    // Reset and show loading
    resultCard.classList.add('hidden');
    loadingDiv.classList.remove('hidden');
    warningsList.innerHTML = '';

    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url: urlInput })
        });

        const data = await response.json();
        loadingDiv.classList.add('hidden');

        if (response.ok) {
            statusText.textContent = data.status;
            scoreText.textContent = data.risk_score;
            
            data.warnings.forEach(warning => {
                const li = document.createElement('li');
                li.textContent = warning;
                warningsList.appendChild(li);
            });

            resultCard.classList.remove('hidden');
        } else {
            alert(data.error || 'Something went wrong.');
        }
    } catch (err) {
        loadingDiv.classList.add('hidden');
        alert('Failed to connect to the server.');
    }
});