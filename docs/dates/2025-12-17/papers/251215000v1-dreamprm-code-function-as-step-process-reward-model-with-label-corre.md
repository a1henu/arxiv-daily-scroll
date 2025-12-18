---
layout: default
title: DreamPRM-Code: Function-as-Step Process Reward Model with Label Correction for LLM Coding
---

# DreamPRM-Code: Function-as-Step Process Reward Model with Label Correction for LLM Coding
**arXiv**：[2512.15000v1](https://arxiv.org/abs/2512.15000) · [PDF](https://arxiv.org/pdf/2512.15000.pdf)  
**作者**：Ruiyi Zhang, Peijia Qin, Qi Cao, Pengtao Xie  

**一句话要点**：提出DreamPRM-Code，以函数为步骤的过程奖励模型，通过标签校正提升LLM编码性能。

**关键词**：过程奖励模型, 大语言模型编码, 链式函数提示, 标签校正, 元学习优化, 代码生成

## 3 点简述
- 核心问题：现有过程奖励模型在编码任务中因步骤分解困难和标签噪声而效果有限。
- 方法要点：采用链式函数提示策略，将函数视为推理步骤，并引入元学习校正机制优化中间标签。
- 实验或效果：在LiveCodeBench上实现80.9% pass@1率，超越OpenAI o4-mini，达到先进水平。

## 摘要（原文）

> Process Reward Models (PRMs) have become essential for improving Large Language Models (LLMs) via test-time scaling, yet their effectiveness in coding remains limited due to the lack of meaningful step decompositions in code and the noise of Monte-Carlo-generated partial labels. We propose DreamPRM-Code, a coding-focused PRM that treats functions as reasoning steps using a Chain-of-Function prompting strategy to induce modular code generation, enabling PRM training and application analogous to mathematical reasoning tasks. To address label noise, DreamPRM-Code introduces a meta-learning-based correction mechanism that leverages clean final-solution unit-test labels and performs bi-level optimization to refine intermediate labels. Applying on test-time scaling, DreamPRM-Code achieved state-of-the-art performance on LiveCodeBench with 80.9 pass@1 rate, surpassing OpenAI o4-mini.

