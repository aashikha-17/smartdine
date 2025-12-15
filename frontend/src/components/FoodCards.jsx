import React from "react";
export default function FoodCards({ foods }) {
  if (!foods.length) return null;

  return (
    <div style={{ marginTop: "12px" }}>
      <h3>🍽️ Suggested Foods</h3>
      {foods.map((f, i) => (
        <div
          key={i}
          style={{
            background: "#fff",
            padding: "12px",
            marginBottom: "8px",
            borderRadius: "10px",
            boxShadow: "0 1px 5px rgba(0,0,0,0.08)",
          }}
        >
          <strong>{i + 1}. {f}</strong>
        </div>
      ))}
    </div>
  );
}
