import React from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import L from "leaflet";


delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl:
    "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png",
  iconUrl:
    "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png",
  shadowUrl:
    "https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png",
});

export default function MapView({ places = [], loc }) {
  if (!loc) return null;

  return (
    <MapContainer
      center={[loc.lat, loc.lon]}
      zoom={14}
      style={{ height: "350px", width: "100%", marginTop: "20px" }}
    >
      
      <TileLayer
        attribution="© OpenStreetMap"
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />

      {/* User location */}
      <Marker position={[loc.lat, loc.lon]}>
        <Popup>You are here</Popup>
      </Marker>

      {/* Restaurant markers */}
      {places.map((p, i) => (
        <Marker key={i} position={[p.lat, p.lon]}>
          <Popup>
            <strong>{p.name}</strong>
            <br />
            {p.address}
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  );
}
