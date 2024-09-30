
document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/ping')
    .then(response => response.json())
    .then(data => {
        document.getElementById('ping-value').textContent = data.ping;
        document.getElementById('uptime-value').textContent = data.uptime;
    });
});
