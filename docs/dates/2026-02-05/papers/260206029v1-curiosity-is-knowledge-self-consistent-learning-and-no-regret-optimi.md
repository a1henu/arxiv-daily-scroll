---
layout: default
title: Curiosity is Knowledge: Self-Consistent Learning and No-Regret Optimization with Active Inference
---

# Curiosity is Knowledge: Self-Consistent Learning and No-Regret Optimization with Active Inference
**arXiv**：[2602.06029v1](https://arxiv.org/abs/2602.06029) · [PDF](https://arxiv.org/pdf/2602.06029.pdf)  
**作者**：Yingke Li, Anjali Parashar, Enlu Zhou, Chuchu Fan  

**一句话要点**：提出基于充分好奇度的理论保证，确保主动推理在混合学习优化中实现自洽学习与无遗憾决策。

**关键词**：主动推理, 好奇度平衡, 贝叶斯学习, 无遗憾优化, 混合学习优化, 理论保证

## 3 点简述
- 核心问题：主动推理中好奇度平衡不当导致学习不一致或决策效率低下。
- 方法要点：理论证明充分好奇度可同时保证贝叶斯后验一致性和有界累积遗憾。
- 实验或效果：理论转化为实践指南，通过真实实验验证了好奇度调优的有效性。

## 摘要（原文）

> Active inference (AIF) unifies exploration and exploitation by minimizing the Expected Free Energy (EFE), balancing epistemic value (information gain) and pragmatic value (task performance) through a curiosity coefficient. Yet it has been unclear when this balance yields both coherent learning and efficient decision-making: insufficient curiosity can drive myopic exploitation and prevent uncertainty resolution, while excessive curiosity can induce unnecessary exploration and regret. We establish the first theoretical guarantee for EFE-minimizing agents, showing that a single requirement--sufficient curiosity--simultaneously ensures self-consistent learning (Bayesian posterior consistency) and no-regret optimization (bounded cumulative regret). Our analysis characterizes how this mechanism depends on initial uncertainty, identifiability, and objective alignment, thereby connecting AIF to classical Bayesian experimental design and Bayesian optimization within one theoretical framework. We further translate these theories into practical design guidelines for tuning the epistemic-pragmatic trade-off in hybrid learning-optimization problems, validated through real-world experiments.

