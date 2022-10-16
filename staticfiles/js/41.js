document.getElementById('41').addEventListener('change', function (e) {
  document.getElementById('product-button').disabled = !e.target.checked
})