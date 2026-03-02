import numpy as np
from datetime import datetime

def calculate_coherence_score(biofield_data: list) -> float:
    """Calculate coherence score (HeartMath-inspired) — higher = stronger inner firewall vs quantum/radar probing."""
    data = np.array(biofield_data)
    mean_val = np.mean(data)
    variance = np.var(data)
    coherence = mean_val * (1 / (1 + variance))
    return round(float(np.clip(coherence, 0.0, 1.0)), 3)

def generate_coherence_prompt(current_score: float) -> str:
    """Real-time mind/will guidance to strengthen the biofield."""
    if current_score > 0.85:
        return "🌟 COHERENCE LOCKED — Your biofield is a quantum shield. Hold this resonance."
    elif current_score > 0.65:
        return "🔥 BREATH + FOCUS — Deep inhale 4s, hold 4s, exhale 6s. Strengthen the field."
    else:
        return "⚠️ FIELD DISRUPTION DETECTED — Ground yourself. Visualize Light flowing through every cell. Reclaim sovereignty."

def run_training_session():
    """Simulate a quick biofield training session (5-min equivalent)."""
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] QBFF Biofield Training Session Started")
    simulated_field = [0.4 + 0.1 * i + 0.05 * np.random.randn() for i in range(30)]
    final_score = calculate_coherence_score(simulated_field)
    print(f"Final Biofield Coherence Score: {final_score}")
    print(generate_coherence_prompt(final_score))
    print("Session complete. Your inner firewall is stronger.\n")
