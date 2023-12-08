async function classifyText() {
    const text = document.getElementById('textInput').value;
    const apiChoice = document.getElementById('apiSelection').value;
    const apiUrl = `http://localhost:8080/${apiChoice}`;

    const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 'message': text })
    });
    const data = await response.json();
    let resultMessage = '';

    if (apiChoice == 'prediction_sexism') {
        if (data.prediction == 'not_sexist')
            resultMessage = 'The message has been categorized as not sexist.';
        else
            resultMessage = 'The message has been categorized as sexist.';
    } else {
        if (data.prediction == '1')
            resultMessage = 'The category of sexism is prejudiced discussions.';
        else if (data.prediction == '2')
            resultMessage = 'The category of sexism is animosity.';
        else if (data.prediction == '3')
            resultMessage = 'The category of sexism is derogation.';
        else
            resultMessage = 'The category of sexism is threats.';
    }

    document.getElementById('result').style.backgroundColor = 'white';
    document.getElementById('result').innerHTML = `Risultato: ${resultMessage}`;
}
