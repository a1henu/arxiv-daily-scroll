---
layout: default
title: Not All Code Is Equal: A Data-Centric Study of Code Complexity and LLM Reasoning
---

# Not All Code Is Equal: A Data-Centric Study of Code Complexity and LLM Reasoning
**arXiv**：[2601.21894v1](https://arxiv.org/abs/2601.21894) · [PDF](https://arxiv.org/pdf/2601.21894.pdf)  
**作者**：Lukas Twist, Shu Yang, Hanqi Yan, Jingzhi Gong, Di Wang, Helen Yannakoudakis, Jie M. Zhang  

**一句话要点**：研究代码结构复杂性对LLM推理能力的影响，提出数据为中心的训练优化路径

**关键词**：代码复杂性, LLM推理, 数据为中心训练, 微调优化, 结构分析

## 3 点简述
- 核心问题：现有研究将代码视为通用训练信号，未明确代码的哪些属性提升LLM推理能力
- 方法要点：通过代码结构复杂性（如圈复杂度和逻辑代码行数）构建控制数据集，分析其对推理的影响
- 实验或效果：在83%实验中，限制微调数据到特定结构复杂性范围优于使用结构多样代码，提升推理性能

## 摘要（原文）

> Large Language Models (LLMs) increasingly exhibit strong reasoning abilities, often attributed to their capacity to generate chain-of-thought-style intermediate reasoning. Recent work suggests that exposure to code can further enhance these skills, but existing studies largely treat code as a generic training signal, leaving open the question of which properties of code actually contribute to improved reasoning. To address this gap, we study the structural complexity of code, which captures control flow and compositional structure that may shape how models internalise multi-step reasoning during fine-tuning. We examine two complementary settings: solution-driven complexity, where complexity varies across multiple solutions to the same problem, and problem-driven complexity, where complexity reflects variation in the underlying tasks. Using cyclomatic complexity and logical lines of code to construct controlled fine-tuning datasets, we evaluate a range of open-weight LLMs on diverse reasoning benchmarks. Our findings show that although code can improve reasoning, structural properties strongly determine its usefulness. In 83% of experiments, restricting fine-tuning data to a specific structural complexity range outperforms training on structurally diverse code, pointing to a data-centric path for improving reasoning beyond scaling.

