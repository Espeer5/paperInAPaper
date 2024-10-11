# Model Selection

## 10/7/2024

I need to select an LLM to use as a partner for creating the paper. The model should be a well known and respected LLM, probably one of the several most common ones. Open/closed source is not relevant here, and most technical details of the model are not relevant either, as long as the model represents the state of LLMs in 2024. The most important factors I will weigh are the quality of the content generated through personal testing and the way I can interact with the model. Perhaps most critical is that I need to be able to save the outputs easily for analysis/recall/supplements. I will need to do further research into the workflow and writing capabilities, but the long list consist of:
1) Latest OpenAI GPT
2) Gemini
3) Llama
4) Claude

## 10/8/2024

I've decided to form a shortlist of models with strong APIs. The reason is that using an API allows you to pay for exactly the amount of content you need, and it will also allow me to easily save all outputs for analysis in a structured way. Both of the entries in the shortlist have strong APIs implemented in Python and are commonly used LLMs. 
- Model shortlist formed: 

  - GPT-4o
    - Most cost effective of free models
    - Strong API with great documentation
    - Personal familiarity with GPT prompt engineering
    - Most commonly used LLM (arguably) which could generate interest in project
  - Llama 2
    - Open source and geared towards research
    - Strong API with great documentation
    - FREE for research purposes
    - Tunable (!!)

While Claude and Gemini also provide strong APIs, the expense of Claude does not scale to the experience that I had testing the model. In personal experience, Gemini was the least helpful in generating new writing - it may simply be personal preference, but I didn't care for the writing style and the "ideas" it suggested were the least new, least complex, and least interesting.

## 10/10/2024

- Model selected: Llama 2

  - Reasoning:
    - Llama 2 is free for research and open source - to me this is the kind of product I would prefer to support
    - Strong API, great documentation, community of research users and hobbyist who might find this project interesting
    - Tunable, which is a huge advantage. I would argue that the tunability is essential to this project - a model that can be tuned to generate more complex and interesting writing is a huge advantage. A model that hasn't been tuned is probably not going to generate the best paper that can be written using current LLM technology.
    - Personal testing showed at least as good performance/usability as GPT-4o, making the cost of GPT-4o unnecessary