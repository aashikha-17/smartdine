import React from "react";
import { useNavigate } from "react-router-dom";

export default function RestaurantCard({ restaurant }) {
  const navigate = useNavigate(); 

  return (
    <div
      className="restaurant-card"
      onClick={() => navigate(`/restaurant/${restaurant.id}`)}
    >
      <img
        src={restaurant.image_url}
        alt={restaurant.name}
        className="restaurant-image"
      />

      <div className="card-body">
        <div className="tags">
          <span className="tag">{restaurant.cuisine}</span>
          <span className="tag">{restaurant.price_range} Budget Friendly</span>
        </div>

        <h3 className="restaurant-name">{restaurant.name}</h3>
        <p className="reason">{restaurant.reason}</p>

        <div className="card-footer">
          <span>⭐ {restaurant.rating}</span>
          <span>📍 Nearby</span>
        </div>
      </div>
      
    </div>
    
  );
}
