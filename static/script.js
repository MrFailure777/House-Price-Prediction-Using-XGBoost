function predictPrice() {
  const area = parseFloat(document.getElementById("area").value);
  const grade = parseFloat(document.getElementById("grade").value);
  const lat = parseFloat(document.getElementById("lat").value);
  const lon = parseFloat(document.getElementById("lon").value);

  fetch("/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      "living area": area,
      "grade of the house": grade,
      "Lattitude": lat,
      "Longitude": lon
    })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("priceResult").textContent = `₹${data.price.toLocaleString()}`;
    document.getElementById("popup").style.display = "block";
  })
  .catch(err => {
    alert("Prediction failed. Make sure your server is running.");
    console.error(err);
  });
}
function showPopup(price) {
  document.getElementById("priceResult").innerText = `₹${price.toLocaleString()}`;
  document.getElementById("popup").style.display = "block";
}

function closePopup() {
  document.getElementById("popup").style.display = "none";
}




