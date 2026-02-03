---
layout: default
title: Reward-free Alignment for Conflicting Objectives
---

# Reward-free Alignment for Conflicting Objectives
**arXiv**：[2602.02495v1](https://arxiv.org/abs/2602.02495) · [PDF](https://arxiv.org/pdf/2602.02495.pdf)  
**作者**：Peter Chen, Xiaopeng Li, Xi Chen, Tianyi Lin  

**一句话要点**：提出无奖励对齐框架RACO，通过冲突规避梯度下降解决多目标冲突问题。

**关键词**：多目标对齐, 冲突规避梯度下降, 无奖励对齐, 帕累托优化, 大语言模型对齐

## 3 点简述
- 核心问题：多目标对齐中偏好冲突导致训练不稳定和权衡不佳。
- 方法要点：利用成对偏好数据，采用裁剪冲突规避梯度下降优化。
- 实验或效果：在总结和安全对齐任务中，优于基线实现更好帕累托权衡。

## 摘要（原文）

> Direct alignment methods are increasingly used to align large language models (LLMs) with human preferences. However, many real-world alignment problems involve multiple conflicting objectives, where naive aggregation of preferences can lead to unstable training and poor trade-offs. In particular, weighted loss methods may fail to identify update directions that simultaneously improve all objectives, and existing multi-objective approaches often rely on explicit reward models, introducing additional complexity and distorting user-specified preferences. The contributions of this paper are two-fold. First, we propose a Reward-free Alignment framework for Conflicted Objectives (RACO) that directly leverages pairwise preference data and resolves gradient conflicts via a novel clipped variant of conflict-averse gradient descent. We provide convergence guarantees to Pareto-critical points that respect user-specified objective weights, and further show that clipping can strictly improve convergence rate in the two-objective setting. Second, we improve our method using some heuristics and conduct experiments to demonstrate the compatibility of the proposed framework for LLM alignment. Both qualitative and quantitative evaluations on multi-objective summarization and safety alignment tasks across multiple LLM families (Qwen 3, Llama 3, Gemma 3) show that our method consistently achieves better Pareto trade-offs compared to existing multi-objective alignment baselines.

