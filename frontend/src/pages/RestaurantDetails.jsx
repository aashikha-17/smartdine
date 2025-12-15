import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "../utils/leafletIcon";

export default function RestaurantDetails() {
  const { id } = useParams();
  const [restaurant, setRestaurant] = useState(null);

  useEffect(() => {
    axios
      .get(`http://localhost:8000/restaurants/${id}`)
      .then(res => setRestaurant(res.data))
      .catch(err => console.error(err));
  }, [id]);

  if (!restaurant) return <p>Loading...</p>;

  return (
    <div>
      {/* HERO */}
      <div
        className="details-hero"
        style={{ backgroundImage: `url(${restaurant.image_url})` }}
      >
        <div className="overlay">
          <h1>{restaurant.name}</h1>
          <span>⭐ {restaurant.rating}</span>
        </div>
      </div>

     
      <div className="details-container">
      
        <div className="details-left">
          <h2>About</h2>
<p>
  Quick, delicious, and portable – the perfect on-the-go meal.
  Wrapped in flaky paratha with your choice of filling and tangy chutneys.
</p>


          

         

          <h2>Known For</h2>
<div className="tags">
  <span className="tag">{restaurant.cuisine}</span>
  <span className="tag">quick bite</span>
  <span className="tag">street food</span>
  <span className="tag">{restaurant.price_range}budget</span>
   <span className="tag">{restaurant.rating} Ratings</span>

</div>

<div className="quick-info">
  <h3 >Quick Info</h3>

  <div className="info-row">
    <span>Price Range</span>
    <span>{restaurant.price_range} Budget Friendly</span>
  </div>

  <div className="info-row">
    <span>Cuisine</span>
    <span>{restaurant.cuisine}</span>
  </div>

  <div className="info-row">
    <span>Rating</span>
    <span>⭐ {restaurant.rating}</span>
  </div>

  <div className="info-row">
    <span>Reviews</span>
    <span>412</span>
  </div>
</div>

        </div>

       
        <div className="details-right">
          <h3>Location & Info</h3>
          <p>📍 Bus Stand Area</p>
<p>Near Bus Stand, Corner Shop</p>
<p>🕒 <span style={{color: "green"}}>Open Now</span></p>
<p>10:00 - 23:00</p>


          <p>💰 {restaurant.price_range}</p>

          
          <div className="map-box">
            <MapContainer
              center={[restaurant.latitude, restaurant.longitude]}
              zoom={15}
              scrollWheelZoom={false}
              style={{ height: "220px", width: "100%", borderRadius: "12px" }}
            >
              <TileLayer
                attribution='&copy; OpenStreetMap'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
              />
              <Marker position={[restaurant.latitude, restaurant.longitude]}>
                <Popup>{restaurant.name}</Popup>
              </Marker>
            </MapContainer>
          </div>

          <a
            href={`https://www.google.com/maps?q=${restaurant.latitude},${restaurant.longitude}`}
            target="_blank"
            rel="noopener noreferrer"
          >
            <button className="primary-btn" style={{ width: "100%", marginTop: "12px" }}>
              Get Directions
            </button>
          </a>
          
        </div>
      </div>
    </div>
  );
}
