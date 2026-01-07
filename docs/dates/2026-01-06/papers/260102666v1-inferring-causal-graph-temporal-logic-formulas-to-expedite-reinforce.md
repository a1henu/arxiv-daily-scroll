---
layout: default
title: Inferring Causal Graph Temporal Logic Formulas to Expedite Reinforcement Learning in Temporally Extended Tasks
---

# Inferring Causal Graph Temporal Logic Formulas to Expedite Reinforcement Learning in Temporally Extended Tasks
**arXiv**：[2601.02666v1](https://arxiv.org/abs/2601.02666) · [PDF](https://arxiv.org/pdf/2601.02666.pdf)  
**作者**：Hadi Partovi Aria, Zhe Xu  

**一句话要点**：提出GTL-CIRL框架，通过因果图时序逻辑公式加速图时空任务中的强化学习

**关键词**：因果图时序逻辑, 强化学习, 图时空任务, 贝叶斯优化, 可解释性

## 3 点简述
- 核心问题：黑盒强化学习在图时空任务中忽视局部变化传播，导致样本效率低和可解释性差
- 方法要点：结合策略学习和因果图时序逻辑挖掘，利用鲁棒性奖励、反例收集和高斯过程贝叶斯优化
- 实验或效果：在基因和电力网络案例中，相比标准基线实现更快学习和更清晰可验证行为

## 摘要（原文）

> Decision-making tasks often unfold on graphs with spatial-temporal dynamics. Black-box reinforcement learning often overlooks how local changes spread through network structure, limiting sample efficiency and interpretability. We present GTL-CIRL, a closed-loop framework that simultaneously learns policies and mines Causal Graph Temporal Logic (Causal GTL) specifications. The method shapes rewards with robustness, collects counterexamples when effects fail, and uses Gaussian Process (GP) driven Bayesian optimization to refine parameterized cause templates. The GP models capture spatial and temporal correlations in the system dynamics, enabling efficient exploration of complex parameter spaces. Case studies in gene and power networks show faster learning and clearer, verifiable behavior compared to standard RL baselines.

