---
layout: default
title: Towards a Neural Debugger for Python
---

# Towards a Neural Debugger for Python
**arXiv**：[2603.09951v1](https://arxiv.org/abs/2603.09951) · [PDF](https://arxiv.org/pdf/2603.09951.pdf)  
**作者**：Maximilian Beck, Jonas Gehring, Jannik Kossen, Gabriel Synnaeve  

**一句话要点**：提出神经调试器以增强语言模型在Python程序调试中的交互控制能力

**关键词**：神经调试器, 条件执行建模, Python程序调试, 语言模型微调, 交互控制

## 3 点简述
- 核心问题：现有神经解释器缺乏类似传统调试器的交互控制，如断点设置和步进操作。
- 方法要点：通过微调大型语言模型或从头预训练小模型，实现支持步进、断点等操作的神经调试器。
- 实验或效果：在CruxEval评估中，模型在输出和输入预测任务上表现强劲，验证了条件执行建模的鲁棒性。

## 摘要（原文）

> Training large language models (LLMs) on Python execution traces grounds them in code execution and enables the line-by-line execution prediction of whole Python programs, effectively turning them into neural interpreters (FAIR CodeGen Team et al., 2025). However, developers rarely execute programs step by step; instead, they use debuggers to stop execution at certain breakpoints and step through relevant portions only while inspecting or modifying program variables. Existing neural interpreter approaches lack such interactive control. To address this limitation, we introduce neural debuggers: language models that emulate traditional debuggers, supporting operations such as stepping into, over, or out of functions, as well as setting breakpoints at specific source lines. We show that neural debuggers -- obtained via fine-tuning large LLMs or pre-training smaller models from scratch -- can reliably model both forward execution (predicting future states and outputs) and inverse execution (inferring prior states or inputs) conditioned on debugger actions. Evaluated on CruxEval, our models achieve strong performance on both output and input prediction tasks, demonstrating robust conditional execution modeling. Our work takes first steps towards future agentic coding systems in which neural debuggers serve as a world model for simulated debugging environments, providing execution feedback or enabling agents to interact with real debugging tools. This capability lays the foundation for more powerful code generation, program understanding, and automated debugging.

