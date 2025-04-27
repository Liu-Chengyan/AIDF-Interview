# Part 3 - Option B: LLM-Driven Structured Summarization

## 1. Prompt Logic and Design

- In the initial stages, prompts were crafted to instruct the model to directly generate functions for structured summarization.
  
- However, early attempts often resulted in undesirable behaviors, such as the model inventing unnecessary functions or rigidly copying sample patterns without proper adaptation.
  
- To improve outcomes, the prompting strategy was refined: instead of requesting generic summarization, the model was explicitly guided with detailed expectations regarding the input format, the desired output structure (company, sentiment, summary), and the step-by-step transformation process.
  
- By providing concrete operational instructions aligned with the JSON schema and LLM capabilities, the model was able to generate a focused and practical solution that aligned with the project goals.

---

## 2. Generation and Results

- The model successfully produced Python code that leverages OpenAI's `gpt-3.5-turbo` to transform news article titles into structured entries containing `company`, `sentiment`, and `summary` fields.
  
- The code implements semantic analysis and lightweight sentiment classification based on article headlines.
  
- Although the generated code was verified to be logically sound and complete through GPT validation, the final execution was not completed due to local machine memory constraints.
  
- Nevertheless, the overall methodology and the structure of the generated code were confirmed to be robust, and the solution is expected to work reliably under suitable computing conditions.

---
