import React, { useState } from "react";
import api from "../api/axios";

import HeroSearch from "../components/HeroSearch";
import RestaurantCard from "../components/RestaurantCard";
import SuggestionChips from "../components/SuggestionChips";
import PopularNow from "../components/PopularNow";
import Features from "../components/Features";

import "../styles/main.css";

export default function Recommend() {
  const [prompt, setPrompt] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const recommend = async (customPrompt) => {
    const finalPrompt = customPrompt || prompt;
    if (!finalPrompt) return;

    try {
      setLoading(true);
      const res = await api.get("/recommend", {
        params: {
          prompt: finalPrompt,
          user_lat: 11.0168,
          user_lon: 76.9558,
        },
      });
      setResults(res.data);
    } catch (err) {
      console.error("Recommend error:", err);
    } finally {
      setLoading(false);
    }
  };

  const surprise = async () => {
    try {
      setLoading(true);
      const res = await api.get("/surprise");
      setResults([res.data]);
    } catch (err) {
      console.error("Surprise error:", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <HeroSearch
        prompt={prompt}
        setPrompt={setPrompt}
        onSearch={() => recommend()}
        onSurprise={surprise}
      />

      <SuggestionChips setPrompt={setPrompt} onSearch={recommend} />

      {loading && <p style={{ textAlign: "center" }}>Finding great food… 🍽️</p>}
      {!loading && results.length > 0 && (
  <div className="ai-explanation">
    
    <div>
      
      <h4>
        ✨ Found {results.length} spot{results.length > 1 ? "s" : ""} for
        <span> "{prompt}"</span>
      </h4>
      <p>
  Based on your craving, we matched restaurants using cuisine, price,
  ratings, and distance - prioritizing the best fit for you.
</p>
    </div>
  </div>
)}


      <div className="card-grid">
        {results.map((r) => (
          <RestaurantCard key={r.id} restaurant={r} />
        ))}
      </div>
      

      {!loading && results.length === 0 && (
        <p style={{ textAlign: "center", marginTop: 30 }}>
          Start by telling us what you're craving 😊
        </p>
      )}
      

   
      <PopularNow />
      <Features />
    </div>
  );
}
