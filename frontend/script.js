const map = L.map("map").setView([-5.0, 120.0], 7);
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(map);

async function fetchData() {
  const res = await fetch("http://127.0.0.1:5000/api/fish-locations", {
    credentials: "include",
  });
  if (!res.ok) {
    alert("Silakan login terlebih dahulu.");
    window.location.href = "login.html";
    return;
  }

  const data = await res.json();
  data.locations.forEach((point) => {
    const color = point.sonar_signal ? "green" : "red";
    L.circleMarker([point.lat, point.lng], {
      radius: 8,
      fillColor: color,
      fillOpacity: 0.7,
      color: "#000",
      weight: 1,
    }).addTo(map).bindPopup(`
      <b>Temp:</b> ${point.temperature}°C<br>
      <b>Current:</b> ${point.current} m/s<br>
      <b>Sonar:</b> ${point.sonar_signal ? "Fish Detected" : "No Fish"}
    `);
  });
}

fetchData();
setInterval(fetchData, 10000);
