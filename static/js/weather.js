fetch("/fetch_weather_data")
  .then(response => response.json())
  .then(weatherData => {
    const weatherWrapper = weatherData.map(data => `
    <div class="weather-wrapper">
      <button class="weather-btn">${data.location}</button>
      <table class="weather-table">
        <tr>
          <th>Temperature</th>
          <td>${data.temperature}</td>
        </tr>
        <tr>
          <th>Feels Like</th>
          <td>${data.feels_like}</td>
        </tr>
        <tr>
          <th>Sky</th>
          <td>${data.sky}</td>
        </tr>
        <tr>
          <th>Wind</th>
          <td>${data.wind}</td>
        </tr>
        <tr>
          <th>Humidity</th>
          <td>${data.humidity}</td>
        </tr>
        <tr>
          <th>Sunrise</th>
          <td>${data.sunrise}</td>
        </tr>
        <tr>
          <th>Sunset</th>
          <td>${data.sunset}</td>
        </tr>
      </table>
    </div>
    `).join('');

    document.getElementById('weatherWrapper').innerHTML = weatherWrapper;

    // Adding event listeners to the buttons
    const locationBtns = document.querySelectorAll('.weather-btn');
    locationBtns.forEach(btn => {
      btn.addEventListener('click', function () {
        const weatherTable = this.nextElementSibling;
        if (weatherTable.style.display === 'table') {
          weatherTable.style.display = 'none';
        } else {
          weatherTable.style.display = 'table';
        }
      });
    });
  });

