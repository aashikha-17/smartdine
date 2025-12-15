import React, { useEffect, useState } from "react";
import api from "../api/axios";
import RestaurantCard from "./RestaurantCard";

export default function PopularNow() {
  const [popular, setPopular] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get("/restaurants/popular")
      .then(res => {
        setPopular(res.data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Popular fetch error:", err);
        setLoading(false);
      });
  }, []);

  if (loading) return null;

  return (
    <section style={{ padding: "40px 30px" }}>
      <h2 style={{ fontSize: "28px", fontWeight: "700" }}>
        Popular Right Now 🔥
      </h2>
      <p style={{ color: "#666", marginBottom: "20px" }}>
        Top picks from our highest-rated restaurants
      </p>

      <div className="card-grid">
        {popular.map(r => (
          <RestaurantCard key={r.id} restaurant={r} />
        ))}
      </div>
    </section>
  );
}
