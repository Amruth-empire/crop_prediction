import { useState } from 'react';
import './CropRecommendation.css';

interface RecommendationResult {
  recommended_crop: string;
  confidence: number;
  message: string;
}

const CropRecommendation = () => {
  const [formData, setFormData] = useState({
    nitrogen: '',
    phosphorus: '',
    potassium: '',
    temperature: '',
    humidity: '',
    ph: '',
    rainfall: ''
  });
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<RecommendationResult | null>(null);
  const [error, setError] = useState<string>('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setResult(null);

    try {
      const response = await fetch('http://localhost:8000/recommend-crop', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          nitrogen: parseFloat(formData.nitrogen),
          phosphorus: parseFloat(formData.phosphorus),
          potassium: parseFloat(formData.potassium),
          temperature: parseFloat(formData.temperature),
          humidity: parseFloat(formData.humidity),
          ph: parseFloat(formData.ph),
          rainfall: parseFloat(formData.rainfall)
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Recommendation failed');
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  return (
    <div className="recommendation-container">
      <div className="recommendation-card">
        <h2>🌱 Crop Recommendation</h2>
        <p className="subtitle">Get crop recommendations based on soil and climate conditions</p>
        
        <form onSubmit={handleSubmit}>
          <div className="form-row">
            <div className="form-group">
              <label htmlFor="nitrogen">Nitrogen (N)</label>
              <input
                type="number"
                id="nitrogen"
                name="nitrogen"
                value={formData.nitrogen}
                onChange={handleChange}
                placeholder="0-140 kg/ha"
                step="0.1"
                min="0"
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="phosphorus">Phosphorus (P)</label>
              <input
                type="number"
                id="phosphorus"
                name="phosphorus"
                value={formData.phosphorus}
                onChange={handleChange}
                placeholder="0-145 kg/ha"
                step="0.1"
                min="0"
                required
              />
            </div>
          </div>

          <div className="form-row">
            <div className="form-group">
              <label htmlFor="potassium">Potassium (K)</label>
              <input
                type="number"
                id="potassium"
                name="potassium"
                value={formData.potassium}
                onChange={handleChange}
                placeholder="0-205 kg/ha"
                step="0.1"
                min="0"
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="ph">pH Level</label>
              <input
                type="number"
                id="ph"
                name="ph"
                value={formData.ph}
                onChange={handleChange}
                placeholder="3.5-9.9"
                step="0.1"
                min="0"
                max="14"
                required
              />
            </div>
          </div>

          <div className="form-row">
            <div className="form-group">
              <label htmlFor="temperature">Temperature (°C)</label>
              <input
                type="number"
                id="temperature"
                name="temperature"
                value={formData.temperature}
                onChange={handleChange}
                placeholder="e.g., 25"
                step="0.1"
                required
              />
            </div>

            <div className="form-group">
              <label htmlFor="humidity">Humidity (%)</label>
              <input
                type="number"
                id="humidity"
                name="humidity"
                value={formData.humidity}
                onChange={handleChange}
                placeholder="0-100%"
                step="0.1"
                min="0"
                max="100"
                required
              />
            </div>
          </div>

          <div className="form-group full-width">
            <label htmlFor="rainfall">Rainfall (mm)</label>
            <input
              type="number"
              id="rainfall"
              name="rainfall"
              value={formData.rainfall}
              onChange={handleChange}
              placeholder="e.g., 200"
              step="0.1"
              min="0"
              required
            />
          </div>

          <button type="submit" className="submit-btn" disabled={loading}>
            {loading ? '🔄 Processing...' : '🌾 Get Recommendation'}
          </button>
        </form>

        {error && (
          <div className="error-message">
            <strong>❌ Error:</strong> {error}
          </div>
        )}

        {result && (
          <div className="result-card">
            <h3>✅ Recommended Crop</h3>
            <div className="result-content">
              <div className="crop-name">{result.recommended_crop}</div>
              <div className="confidence">
                Confidence: <strong>{result.confidence.toFixed(1)}%</strong>
              </div>
              <p className="result-message">{result.message}</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default CropRecommendation;
