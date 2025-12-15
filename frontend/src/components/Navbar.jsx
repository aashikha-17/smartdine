import React from "react";
import { Link } from "react-router-dom";
import "../styles/navbar.css";

export default function Navbar() {
  return (
    <nav className="navbar">
      <div className="nav-left">
        <div className="logo-icon">🍴</div>
        <span className="logo-text">SmartDine</span>
      </div>

      <div className="nav-right">
        <Link to="/" className="nav-link">Home</Link>
        
      </div>
    </nav>
  );
}
