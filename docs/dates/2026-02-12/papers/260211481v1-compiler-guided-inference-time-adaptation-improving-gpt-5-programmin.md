---
layout: default
title: Compiler-Guided Inference-Time Adaptation: Improving GPT-5 Programming Performance in Idris
---

# Compiler-Guided Inference-Time Adaptation: Improving GPT-5 Programming Performance in Idris
**arXiv**：[2602.11481v1](https://arxiv.org/abs/2602.11481) · [PDF](https://arxiv.org/pdf/2602.11481.pdf)  
**作者**：Minda Li, Bhaskar Krishnamachari  

**一句话要点**：提出编译器引导的推理时适应方法，提升GPT-5在Idris编程中的性能

**关键词**：推理时适应, 编译器反馈, 低资源编程语言, 迭代提示, GPT-5, Idris编程

## 3 点简述
- 核心问题：GPT-5在低资源语言Idris中表现不佳，零样本提示仅解决22/56练习
- 方法要点：通过迭代提示结合本地编译错误反馈，结构化引导模型适应
- 实验或效果：使用错误引导优化后，GPT-5解决54/56问题，性能显著提升

## 摘要（原文）

> GPT-5, a state of the art large language model from OpenAI, demonstrates strong performance in widely used programming languages such as Python, C++, and Java; however, its ability to operate in low resource or less commonly used languages remains underexplored. This work investigates whether GPT-5 can effectively acquire proficiency in an unfamiliar functional programming language, Idris, through iterative, feedback driven prompting. We first establish a baseline showing that with zero shot prompting the model solves only 22 out of 56 Idris exercises using the platform Exercism, substantially underperforming relative to higher resource languages (45 out of 50 in Python and 35 out of 47 in Erlang). We then evaluate several refinement strategies, including iterative prompting based on platform feedback, augmenting prompts with documentation and error classification guides, and iterative prompting using local compilation errors and failed test cases. Among these approaches, incorporating local compilation errors yields the most substantial improvements. Using this structured, error guided refinement loop, GPT-5 performance increased to an impressive 54 solved problems out of 56. These results suggest that while large language models may initially struggle in low resource settings, structured compiler level feedback can play a critical role in unlocking their capabilities.

