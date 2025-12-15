import React from "react";

const suggestions = [
  "Something cheesy but not too expensive",
  "Comfort food after a rough day",
  "Late night cravings open now"

  
  
];

export default function SuggestionChips({ setPrompt, onSearch }) {
  return (
    <div className="chips">
      {suggestions.map((text, index) => (
        <button
          key={index}
          className="chip"
          onClick={() => {
            setPrompt(text);
            onSearch(text);
          }}
        >
          {text}
        </button>
      ))}
    </div>
  );
}
