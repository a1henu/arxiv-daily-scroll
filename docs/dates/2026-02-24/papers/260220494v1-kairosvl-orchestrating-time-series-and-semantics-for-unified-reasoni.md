---
layout: default
title: KairosVL: Orchestrating Time Series and Semantics for Unified Reasoning
---

# KairosVL: Orchestrating Time Series and Semantics for Unified Reasoning
**arXiv**：[2602.20494v1](https://arxiv.org/abs/2602.20494) · [PDF](https://arxiv.org/pdf/2602.20494.pdf)  
**作者**：Haotian Si, Changhua Pei, Xiao He, Zeyan Li, Zhe Xie, Zexin Wang, Jiyao Hu, Zhaoyang Yu, Tieying Zhang, Dan Pei, Jianhui Li, Gaogang Xie  

**一句话要点**：提出KairosVL框架，结合语义与时间序列进行统一推理，以解决复杂决策导向的时间序列分析问题。

**关键词**：时间序列分析, 语义推理, 强化学习, 泛化能力, 决策支持

## 3 点简述
- 核心问题：传统时间序列分析缺乏语义理解，难以应对复杂决策需求，需扩展至语义条件推理。
- 方法要点：采用两轮强化学习框架，首轮增强时间基元感知，次轮聚焦语义条件推理，提升模型推理能力。
- 实验或效果：在合成和真实任务中表现优异，增强性能、保持推理能力，并显著提升对未知场景的泛化性。

## 摘要（原文）

> Driven by the increasingly complex and decision-oriented demands of time series analysis, we introduce the Semantic-Conditional Time Series Reasoning task, which extends conventional time series analysis beyond purely numerical modeling to incorporate contextual and semantic understanding. To further enhance the mode's reasoning capabilities on complex time series problems, we propose a two-round reinforcement learning framework: the first round strengthens the mode's perception of fundamental temporal primitives, while the second focuses on semantic-conditioned reasoning. The resulting model, KairosVL, achieves competitive performance across both synthetic and real-world tasks. Extensive experiments and ablation studies demonstrate that our framework not only boosts performance but also preserves intrinsic reasoning ability and significantly improves generalization to unseen scenarios. To summarize, our work highlights the potential of combining semantic reasoning with temporal modeling and provides a practical framework for real-world time series intelligence, which is in urgent demand.

