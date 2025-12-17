---
layout: default
title: ChartAgent: A Chart Understanding Framework with Tool Integrated Reasoning
---

# ChartAgent: A Chart Understanding Framework with Tool Integrated Reasoning
**arXiv**：[2512.14040v1](https://arxiv.org/abs/2512.14040) · [PDF](https://arxiv.org/pdf/2512.14040.pdf)  
**作者**：Boran Wang, Xinming Wang, Yi Chen, Xiang Li, Jian Xu, Jing Yuan, Chenglin Liu  

**一句话要点**：提出ChartAgent框架，通过工具集成推理解决图表理解在稀疏标注下的鲁棒性问题。

**关键词**：图表理解, 工具集成推理, 多模态大语言模型, 稀疏标注, 可解释性, 模块化工具库

## 3 点简述
- 核心问题：现有多模态大语言模型依赖文本标注，在关键数字缺失时性能显著下降。
- 方法要点：基于工具集成推理，将图表分析分解为可观察步骤，使用模块化工具库进行动态编排。
- 实验或效果：在稀疏标注设置下大幅提升鲁棒性，提供可追溯和可复现的中间输出支持。

## 摘要（原文）

> With their high information density and intuitive readability, charts have become the de facto medium for data analysis and communication across disciplines. Recent multimodal large language models (MLLMs) have made notable progress in automated chart understanding, yet they remain heavily dependent on explicit textual annotations and the performance degrades markedly when key numerals are absent. To address this limitation, we introduce ChartAgent, a chart understanding framework grounded in Tool-Integrated Reasoning (TIR). Inspired by human cognition, ChartAgent decomposes complex chart analysis into a sequence of observable, replayable steps. Supporting this architecture is an extensible, modular tool library comprising more than a dozen core tools, such as keyelement detection, instance segmentation, and optical character recognition (OCR), which the agent dynamically orchestrates to achieve systematic visual parsing across diverse chart types. Leveraging TIRs transparency and verifiability, ChartAgent moves beyond the black box paradigm by standardizing and consolidating intermediate outputs into a structured Evidence Package, providing traceable and reproducible support for final conclusions. Experiments show that ChartAgent substantially improves robustness under sparse annotation settings, offering a practical path toward trustworthy and extensible systems for chart understanding.

