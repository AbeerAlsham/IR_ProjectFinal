// Fetch suggestions from the server
async function fetchSuggestions() {
    const query = document.getElementById('searchBox').value;
    const dataset = document.getElementById('datasetSelector').value;
    const language = document.getElementById('languageSelector').value;
    const spellcheck = document.getElementById('spellcheckSelector').value;

    try {
        const response = await fetch('/suggest', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query, dataset, language, spellcheck }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const suggestions = await response.json();
        updateSuggestionsList(suggestions);
    } catch (error) {
        console.error('Fetch error:', error);
    }
}

// Update the suggestions list in the DOM
function updateSuggestionsList(suggestions) {
    const suggestionsList = document.getElementById('suggestionsList');
    suggestionsList.innerHTML = suggestions.map(suggestion =>
        `<div class="suggestion-item" data-suggestion="${suggestion}">${suggestion}</div>`
    ).join('');
}

// Set the search query to the clicked suggestion
function setSearchQuery(suggestion) {
    document.getElementById('searchBox').value = suggestion;
}

// Event delegation for suggestion items
document.getElementById('suggestionsList').addEventListener('click', function (event) {
    const { target } = event;
    if (target.classList.contains('suggestion-item')) {
        const suggestion = target.getAttribute('data-suggestion');
        setSearchQuery(suggestion);
    }
});
