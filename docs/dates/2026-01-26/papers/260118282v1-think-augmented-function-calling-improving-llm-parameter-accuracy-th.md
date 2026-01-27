---
layout: default
title: Think-Augmented Function Calling: Improving LLM Parameter Accuracy Through Embedded Reasoning
---

# Think-Augmented Function Calling: Improving LLM Parameter Accuracy Through Embedded Reasoning
**arXiv**：[2601.18282v1](https://arxiv.org/abs/2601.18282) · [PDF](https://arxiv.org/pdf/2601.18282.pdf)  
**作者**：Lei Wei, Jinpeng Ou, Xiao Peng, Bin Wang  

**一句话要点**：提出Think-Augmented Function Calling框架，通过嵌入推理提升LLM函数调用参数准确性

**关键词**：函数调用, 参数推理, 大语言模型, AI代理, 可解释性

## 3 点简述
- 当前LLM函数调用机制缺乏参数生成时的显式推理透明度，尤其在复杂参数场景下
- TAFC引入通用'think'参数增强，支持函数和参数级推理，并动态优化描述以提升推理质量
- 在ToolBench评估中，TAFC显著提高了多参数函数的参数生成准确性和推理连贯性

## 摘要（原文）

> Large language models (LLMs) have demonstrated remarkable capabilities in function calling for autonomous agents, yet current mechanisms lack explicit reasoning transparency during parameter generation, particularly for complex functions with interdependent parameters. While existing approaches like chain-of-thought prompting operate at the agent level, they fail to provide fine-grained reasoning guidance for individual function parameters. To address these limitations, we propose Think-Augmented Function Calling (TAFC), a novel framework that enhances function calling accuracy through explicit reasoning at both function and parameter levels. Our method introduces a universal "think" parameter augmentation that enables models to articulate their decision-making process, with dynamic optimization for parameter descriptions to improve reasoning quality. For complex parameters, TAFC automatically triggers granular reasoning based on complexity scoring, ensuring appropriate justification for critical decisions. Additionally, we propose reasoning-guided optimization to align generated reasoning with human expectations. TAFC requires no architectural modifications to existing LLMs while maintaining full API compatibility. Evaluation on ToolBench across proprietary and open-source models demonstrates significant improvements in parameter generation accuracy and reasoning coherence for multi-parameter functions, while providing enhanced interpretability for debugging AI agent behaviors.

