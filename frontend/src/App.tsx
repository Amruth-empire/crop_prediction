import { useState } from 'react'
import CropYieldPredictor from './components/CropYieldPredictor'
import CropRecommendation from './components/CropRecommendation'
import './App.css'

function App() {
  const [activeTab, setActiveTab] = useState<'yield' | 'recommendation'>('yield')

  return (
    <div className="app">
      <header className="app-header">
        <h1>🌾 Crop Prediction System</h1>
        <p>AI-Powered Crop Yield Prediction & Recommendation for Indian Agriculture</p>
      </header>

      <div className="tabs">
        <button
          className={`tab ${activeTab === 'yield' ? 'active' : ''}`}
          onClick={() => setActiveTab('yield')}
        >
          📊 Yield Prediction
        </button>
        <button
          className={`tab ${activeTab === 'recommendation' ? 'active' : ''}`}
          onClick={() => setActiveTab('recommendation')}
        >
          🌱 Crop Recommendation
        </button>
      </div>

      <main className="app-content">
        {activeTab === 'yield' ? <CropYieldPredictor /> : <CropRecommendation />}
      </main>

      <footer className="app-footer">
        <p>Built with React, FastAPI & Machine Learning | Data-driven agriculture solutions</p>
      </footer>
    </div>
  )
}

export default App
