# Extending Health-LLM: Integrating DeepSeek-R1 for Clinical Explainability 🏥

## 📖 Academic Research Context
**Inspired by:** *Health-LLM: Personalized Retrieval-Augmented Disease Prediction System* (Accepted at ACL 2025).

### 🚨 The Research Problem (Identified Gap)
The original **Health-LLM** paper successfully utilizes standard LLMs (like Llama-3 or GPT-4) combined with machine learning classifiers for disease prediction. However, a critical gap remains for real-world clinical deployment: **The Black Box Problem**. Standard LLMs output a final disease prediction based on feature extraction, but they fail to provide an explicit, verifiable, and transparent "Clinical Chain of Thought." Doctors cannot trust a high-probability prediction without seeing the medical logic behind it.

### 💡 My Proposed Research Solution
To bridge this gap, I propose integrating **DeepSeek-R1** (released Jan 2025), a state-of-the-art pure reasoning model. In this project, I modified the prediction pipeline to force the model into a `<think>` phase *before* final classification. 
This generates a detailed, step-by-step clinical reasoning trace (Explainable AI / XAI) that maps patient symptoms and lab results to established medical guidelines (e.g., ADA guidelines for Diabetes) before making the final prediction.

---

## 🛠️ Project Implementation
This repository contains the Python pipeline demonstrating this architectural improvement.

### Files Included:
- `medical_reasoning_pipeline.py`: The core code comparing the baseline Health-LLM approach vs. my Reasoning-Augmented approach.
- `results_comparison.md`: A detailed breakdown of how the reasoning trace fills the explainability gap.
- `requirements.txt`: Dependencies.

### How to Run:
```bash
pip install -r requirements.txt
python medical_reasoning_pipeline.py
```
