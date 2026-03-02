import numpy as np
import time
from typing import Dict

def generate_mock_wbans_data(num_samples: int = 1000) -> Dict:
    """Generate realistic mock WBAN sensor data: ECG, neural spikes, and biofield coherence metric."""
    t = np.linspace(0, 10, num_samples)
    
    # ECG-like heartbeat with natural variability
    ecg = np.sin(2 * np.pi * 1.2 * t) + 0.3 * np.random.randn(num_samples)
    
    # Neural spike train (simulating brain activity)
    neural = np.random.poisson(lam=8, size=num_samples)
    
    # Simulated biofield coherence (0-1) — this is our inner quantum shield metric
    biofield_coherence = 0.75 + 0.2 * np.sin(2 * np.pi * 0.1 * t) + 0.05 * np.random.randn(num_samples)
    biofield_coherence = np.clip(biofield_coherence, 0.0, 1.0)
    
    return {
        "timestamp": time.time(),
        "ecg": ecg.tolist(),
        "neural_spikes": neural.tolist(),
        "biofield_coherence": biofield_coherence.tolist(),
        "metadata": {"sensor_count": 4, "threat_level": "normal"}
    }
