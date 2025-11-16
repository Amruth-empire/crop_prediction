import { useState } from 'react';
import './CropYieldPredictor.css';

interface PredictionResult {
  prediction: number;
  unit: string;
  message: string;
}

const CropYieldPredictor = () => {
  const [formData, setFormData] = useState({
    state: '',
    district: '',
    season: '',
    crop: '',
    area: ''
  });
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<PredictionResult | null>(null);
  const [error, setError] = useState<string>('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setResult(null);

    try {
      const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000';
      const response = await fetch(`${apiUrl}/api/predict-yield`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          state: formData.state,
          district: formData.district,
          season: formData.season,
          crop: formData.crop,
          area: parseFloat(formData.area)
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Prediction failed');
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  return (
    <div className="predictor-container">
      <div className="predictor-card">
        <h2>🌾 Crop Yield Prediction</h2>
        <p className="subtitle">Predict crop yield based on location and crop type</p>
        
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="state">State Name</label>
            <input
              type="text"
              id="state"
              name="state"
              value={formData.state}
              onChange={handleChange}
              placeholder="e.g., Punjab, Maharashtra"
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="district">District Name</label>
            <input
              type="text"
              id="district"
              name="district"
              value={formData.district}
              onChange={handleChange}
              placeholder="e.g., Amritsar, Pune"
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="season">Season</label>
            <select
              id="season"
              name="season"
              value={formData.season}
              onChange={handleChange}
              required
            >
              <option value="">Select Season</option>
              <option value="Kharif">Kharif (Monsoon)</option>
              <option value="Rabi">Rabi (Winter)</option>
              <option value="Zaid">Zaid (Summer)</option>
              <option value="Whole Year">Whole Year</option>
              <option value="Autumn">Autumn</option>
              <option value="Summer">Summer</option>
              <option value="Winter">Winter</option>
            </select>
          </div>

          <div className="form-group">
            <label htmlFor="crop">Crop Name</label>
            <input
              type="text"
              id="crop"
              name="crop"
              value={formData.crop}
              onChange={handleChange}
              placeholder="e.g., Rice, Wheat, Cotton"
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="area">Area (in hectares)</label>
            <input
              type="number"
              id="area"
              name="area"
              value={formData.area}
              onChange={handleChange}
              placeholder="e.g., 100"
              step="0.01"
              min="0"
              required
            />
          </div>

          <button type="submit" className="submit-btn" disabled={loading}>
            {loading ? '🔄 Predicting...' : '📊 Predict Yield'}
          </button>
        </form>

        {error && (
          <div className="error-message">
            <strong>❌ Error:</strong> {error}
          </div>
        )}

        {result && (
          <div className="result-card">
            <h3>✅ Prediction Result</h3>
            <div className="result-content">
              <div className="result-value">
                <span className="value">{result.prediction.toFixed(2)}</span>
                <span className="unit">{result.unit}</span>
              </div>
              <p className="result-message">{result.message}</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default CropYieldPredictor;
