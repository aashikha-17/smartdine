import React from "react";
import ReactMarkdown from "react-markdown";


function formatAIText(text) {
  if (!text) return "";

  return text
    .replace(/\*\*(.*?)\*\*/g, "## $1")
    .replace(/(\d+)\.\s/g, "\n$1. ")
    .replace(/:\s/g, ":\n");
}

export default function ChatHistory({ chats }) {
  return (
    <div className="chat-history">
      {chats.map((c, i) => (
        <div
          key={i}
          style={{
            textAlign: c.role === "user" ? "right" : "left",
            marginBottom: "14px",
          }}
        >
          <div
            style={{
              display: "inline-block",
              padding: "14px 18px",
              borderRadius: "14px",
              maxWidth: "85%",
              background: c.role === "user" ? "#DCF8C6" : "#F4F4F4",
              lineHeight: "1.6",
              fontSize: "15px",
            }}
          >
            <ReactMarkdown>
              {formatAIText(c.text)}
            </ReactMarkdown>
          </div>
        </div>
      ))}
    </div>
  );
}
