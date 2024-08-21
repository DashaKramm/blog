async function makeRequest(url, method = "POST", data = {}) {
    const response = await fetch(url, {method: method, body: JSON.stringify(data)});
    if (response.ok) {
        return await response.json();
    } else {
        const errorText = await response.text();
        let errorMessage = 'Unknown error occurred';
        const errorJson = JSON.parse(errorText);
        if (errorJson.error) {
            errorMessage = errorJson.error;
        }
        throw new Error(errorMessage);
    }
}

async function onClickCalculator(event) {
    event.preventDefault();
    const button = event.currentTarget;
    const url = button.dataset.url;
    const A = parseFloat(document.getElementById('inputA').value);
    const B = parseFloat(document.getElementById('inputB').value);
    if (isNaN(A) || isNaN(B)) {
        updateResult('Error: Both A and B must be valid numbers.', 'error');
        return;
    }
    try {
        const response = await makeRequest(url, 'POST', {A, B});
        if (response.error) {
            updateResult(`Error: ${response.error}`, 'error');
        } else {
            updateResult(`Result: ${response.answer}`, 'success');
        }
    } catch (error) {
        updateResult(`Error: ${error.message}`, 'error');
    }
}

function updateResult(message, type) {
    const resultDiv = document.getElementById('result');
    resultDiv.textContent = message;
    resultDiv.classList.remove('error', 'success');
    resultDiv.classList.add('result', type);
}

function onLoad() {
    const calculatorButtons = document.querySelectorAll('[data-js="calculator-button"]');
    for (const button of calculatorButtons) {
        button.addEventListener('click', onClickCalculator);
    }
}

window.addEventListener('load', onLoad);
