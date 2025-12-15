import React, { useState } from "react";
export default function Features() {
  return (
    <div className="features">
      <div className="feature-card">
        <span>✨</span>
        <h4>Smart Recommendations</h4>
        <p>
          Our AI understands your cravings and matches you with the perfect
          restaurant.
        </p>
      </div>

      <div className="feature-card">
        <span>🍴</span>
        <h4>Curated Selection</h4>
        <p>
          Hand-picked local eateries with verified reviews and honest ratings.
        </p>
      </div>

      <div className="feature-card">
        <span>👥</span>
        <h4>Student-Friendly</h4>
        <p>
          Budget-conscious options and quick bites perfect for busy schedules.
        </p>
      </div>
    </div>
  );
}
