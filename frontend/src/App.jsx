import React, { useState } from "react";
import { Routes, Route } from "react-router-dom";
import Recommend from "./pages/Recommend";
import RestaurantDetails from "./pages/RestaurantDetails";
import Navbar from "./components/Navbar";
import PopularNow from "./components/PopularNow";
export default function App() {
  return (
    <>
      <Navbar />   {/* ✅ ALWAYS VISIBLE */}

      <Routes>
        <Route path="/" element={<Recommend />} />
        <Route path="/restaurant/:id" element={<RestaurantDetails />} />
      </Routes>
    </>
  );
}

