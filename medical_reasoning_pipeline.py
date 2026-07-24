import time
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()

# ==============================================================================
# RESEARCH GAP CONTEXT:
# Paper: Health-LLM (2025)
# Gap: Standard LLMs predict diseases based on features but lack an explicit,
#      human-readable "Clinical Chain of Thought" (black box).
# Solution: DeepSeek-R1 Integration. We force the model to use <think> tags to 
#           generate verifiable clinical reasoning before outputting the diagnosis.
# ==============================================================================

# Mock Patient Data
patient_data = {
    "age": 45,
    "symptoms": "Frequent urination, excessive thirst, blurred vision, fatigue.",
    "vitals": "BP: 135/85, HR: 78",
    "lab_results": "Fasting Glucose: 185 mg/dL, HbA1c: 8.2%"
}

def standard_llm_prediction(patient):
    """
    Simulates a standard LLM (e.g., Llama-3-8B-Instruct or GPT-3.5)
    in the original Health-LLM pipeline.
    """
    console.print("\n[bold yellow]Running Standard LLM (Baseline)...[/bold yellow]")
    time.sleep(1.5)
    
    # Standard models immediately output the prediction without showing their work
    output = """
**Diagnosis Prediction:** Type 2 Diabetes Mellitus
**Probability:** 89%
**Recommended Action:** Consult an endocrinologist and begin Metformin treatment.
    """
    return output

def deepseek_r1_reasoning_prediction(patient):
    """
    Simulates DeepSeek-R1 (e.g., DeepSeek-R1-Distill-Qwen-7B).
    Fills the gap by providing Explainable AI (XAI) for doctors.
    """
    console.print("\n[bold green]Running DeepSeek-R1 (Reasoning-Augmented Adapter)...[/bold green]")
    time.sleep(2)
    
    # DeepSeek-R1 generates a <think> trace first
    output = """
<think>
1. Analyze the patient profile: 45-year-old presenting with polyuria (frequent urination), polydipsia (excessive thirst), blurred vision, and fatigue.
2. These are classic symptoms of hyperglycemia.
3. Review lab results: Fasting Glucose is 185 mg/dL. According to ADA guidelines, fasting plasma glucose >= 126 mg/dL indicates diabetes.
4. Review HbA1c: 8.2%. ADA guidelines state HbA1c >= 6.5% confirms diabetes.
5. The patient's age (45) and symptom profile strongly suggest Type 2 Diabetes Mellitus, rather than Type 1 (which typically presents earlier with weight loss/ketoacidosis).
6. Blood pressure is borderline high (135/85), indicating potential metabolic syndrome.
7. Conclusion: The diagnosis is definitively Type 2 Diabetes. 
8. Formulate final output for the Health-LLM classifier pipeline.
</think>

**Diagnosis Prediction:** Type 2 Diabetes Mellitus
**Probability:** 98% (High Confidence based on dual ADA criteria: FPG and HbA1c)
**Recommended Action:** Initiate lifestyle interventions and consult for primary pharmacological therapy (e.g., Metformin).
    """
    return output

if __name__ == "__main__":
    console.print(Panel.fit("[bold blue]Health-LLM Gap Bridging: Clinical Reasoning XAI[/bold blue]"))
    
    console.print("\n[bold]Patient Input:[/bold]")
    console.print(patient_data)
    
    # Run Baseline
    baseline_result = standard_llm_prediction(patient_data)
    console.print(Panel(Markdown(baseline_result), title="Standard LLM Output (Black Box)", border_style="yellow"))
    
    # Run AI Solution
    r1_result = deepseek_r1_reasoning_prediction(patient_data)
    console.print(Panel(Markdown(r1_result), title="DeepSeek-R1 Output (Explainable Clinical Reasoning)", border_style="green"))
    
    console.print("\n[bold cyan]GAP FILLED:[/bold cyan] DeepSeek-R1 provides a verifiable clinical thought process, increasing doctor trust in the Health-LLM predictions.")
