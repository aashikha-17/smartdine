import React from "react";

export default function HeroSearch({ prompt, setPrompt, onSearch, onSurprise }) {
  return (
    <div className="hero">
      <h1>
        Find Your Perfect <span>Meal</span>
      </h1>
      <p className="subtitle">
        Tell us what you're craving, and SmartDine will recommend the best spots for you.
      </p>

      <div className="search-box">
        <input
          type="text"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Craving something cheesy but cheap?"
        />
        <button className="primary-btn" onClick={onSearch}>
          Find Food
        </button>
        <button className="secondary-btn" onClick={onSurprise}>
          🎲 Surprise Me
        </button>
      </div>
    </div>
  );
}
