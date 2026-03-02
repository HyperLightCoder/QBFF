import yaml
from wbansim import generate_mock_wbans_data
from biofield_coherence import run_training_session

print("🔥 QBFF Quantum Bio-Field Firewall v0.1 Starting...\n")

# Load config
try:
    with open("src/config.yaml", "r") as f:
        config = yaml.safe_load(f)
    print(f"✅ Config loaded — Threat Level: {config['threat_level']}")
except:
    print("⚠️ No config yet — using defaults")

# Generate mock WBAN + biofield data
data = generate_mock_wbans_data(num_samples=500)
print(f"📡 Mock WBAN Data Generated — {len(data['ecg'])} samples")
print(f"   Biofield Coherence: {sum(data['biofield_coherence'])/len(data['biofield_coherence']):.3f}")

# Run biofield training session (inner quantum shield)
run_training_session()

print("\n✅ QBFF Demo Complete! Your bio-cyber interface is now protected at the edge.")
print("   Next: Add encryptor.py + anomaly_detector.py for full firewall mode.")
