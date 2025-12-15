# SmartDine – AI-Powered Food Discovery Assistant

SmartDine is an AI-powered food discovery application that helps users find nearby restaurants based on natural language or voice-based food preferences. It combines AI intelligence, rule-based recommendations, and location awareness to simplify everyday food decisions.

---

## Features

-  Natural language food search (e.g., “something cheesy but not too expensive”)
-  Voice-based food input using browser speech recognition
-  AI-powered intent understanding using Groq LLM
-  Explainable restaurant recommendations
-  Location intelligence with OpenStreetMap and Leaflet
-  Popular Right Now section (top-rated restaurants)
-  Surprise Me option for random recommendations

---

## How It Works

1. User enters a text or voice prompt  
2. Voice input is converted to text using Web Speech API  
3. Prompt is sent to Groq LLM for intent understanding  
4. A rule-based scoring algorithm filters and ranks restaurants  
5. Nearby restaurants are visualized on the map using OpenStreetMap  

---

## Tech Stack

### Frontend
- React.js
- Axios
- Leaflet.js
- Custom CSS

### Backend
- FastAPI (Python)
- Groq LLM API
- SQLAlchemy ORM

### Maps & Geo
- OpenStreetMap
- Haversine Formula

### Database
- SQLite

---

## 📐 Recommendation Logic

Restaurants are ranked based on:
- Cuisine match
- Budget suitability
- Mood relevance
- User ratings
- Distance from the user

Distance is calculated using the Haversine formula and used as a ranking factor.

---

## ▶️ How to Run the Project

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

### Run Frontend Locally
```bash
cd frontend
npm install
npm run dev
