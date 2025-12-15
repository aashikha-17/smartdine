
import React, { useState } from "react";
import "../index.css";

export default function ChatBox({ onSend }) {
  const [msg, setMsg] = useState("");

  const send = () => {
    if (!msg.trim()) return;
    onSend(msg);
    setMsg("");
  };

  const voice = () => {
    const SpeechRecognition =
      window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
      alert("Voice input not supported in this browser");
      return;
    }

    const rec = new SpeechRecognition();
    rec.lang = "en-IN";
    rec.start();

    rec.onresult = (e) => {
      setMsg(e.results[0][0].transcript);
    };
  };

  return (
    <div className="chatbox-container">
      <textarea
        className="chatbox-input"
        placeholder="Tell me what you're craving… 🍕"
        value={msg}
        onChange={(e) => setMsg(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && !e.shiftKey && send()}
      />

      <div className="chatbox-actions">
        <button className="mic-btn" onClick={voice} title="Voice input">
          🎤
        </button>

        <button className="send-btn" onClick={send}>
          Send
        </button>
      </div>
    </div>
  );
}
