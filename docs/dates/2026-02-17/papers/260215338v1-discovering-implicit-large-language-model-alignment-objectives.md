---
layout: default
title: Discovering Implicit Large Language Model Alignment Objectives
---

# Discovering Implicit Large Language Model Alignment Objectives
**arXiv**：[2602.15338v1](https://arxiv.org/abs/2602.15338) · [PDF](https://arxiv.org/pdf/2602.15338.pdf)  
**作者**：Edward Chen, Sanmi Koyejo, Carlos Guestrin  

**一句话要点**：提出Obj-Disco框架以自动分解大语言模型对齐奖励信号为可解释目标

**关键词**：大语言模型对齐, 奖励信号解释, 可解释人工智能, 目标分解, 迭代贪婪算法

## 3 点简述
- 问题：大语言模型对齐依赖复杂奖励信号，易导致错位和奖励黑客风险，现有方法难以全面识别因果目标。
- 方法：采用迭代贪婪算法分析训练检查点行为变化，分解奖励信号为稀疏加权自然语言目标组合。
- 效果：在多样任务和模型上验证，捕获超90%奖励行为，并能识别潜在错位激励。

## 摘要（原文）

> Large language model (LLM) alignment relies on complex reward signals that often obscure the specific behaviors being incentivized, creating critical risks of misalignment and reward hacking. Existing interpretation methods typically rely on pre-defined rubrics, risking the omission of "unknown unknowns", or fail to identify objectives that comprehensively cover and are causal to the model behavior. To address these limitations, we introduce Obj-Disco, a framework that automatically decomposes an alignment reward signal into a sparse, weighted combination of human-interpretable natural language objectives. Our approach utilizes an iterative greedy algorithm to analyze behavioral changes across training checkpoints, identifying and validating candidate objectives that best explain the residual reward signal. Extensive evaluations across diverse tasks, model sizes, and alignment algorithms demonstrate the framework's robustness. Experiments with popular open-source reward models show that the framework consistently captures > 90% of reward behavior, a finding further corroborated by human evaluation. Additionally, a case study on alignment with an open-source reward model reveals that Obj-Disco can successfully identify latent misaligned incentives that emerge alongside intended behaviors. Our work provides a crucial tool for uncovering the implicit objectives in LLM alignment, paving the way for more transparent and safer AI development.

