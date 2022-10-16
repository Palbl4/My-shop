document.getElementById('45').addEventListener('change', function (e) {
  document.getElementById('product-button').disabled = !e.target.checked
})