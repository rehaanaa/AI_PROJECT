async function predictPrice() {
    const size = document.getElementById('size').value;
    const bedrooms = document.getElementById('bedrooms').value;

    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            size: parseInt(size),
            bedrooms: parseInt(bedrooms)
        })
    });

    const data = await response.json();
    document.getElementById('result').innerText = `Predicted Price: ₹${data.predicted_price}`;
}
