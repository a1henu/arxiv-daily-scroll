---
layout: default
title: CADO: From Imitation to Cost Minimization for Heatmap-based Solvers in Combinatorial Optimization
---

# CADO: From Imitation to Cost Minimization for Heatmap-based Solvers in Combinatorial Optimization
**arXiv**：[2602.08210v1](https://arxiv.org/abs/2602.08210) · [PDF](https://arxiv.org/pdf/2602.08210.pdf)  
**作者**：Hyungseok Song, Deunsol Yoon, Kanghoon Lee, Han-Seul Jeong, Soonyoung Lee, Woohyung Lim  

**一句话要点**：提出CADO强化学习微调框架，以解决基于热图的组合优化求解器中目标不匹配问题。

**关键词**：组合优化, 热图求解器, 强化学习微调, 扩散模型, 成本最小化

## 3 点简述
- 核心问题：监督学习训练导致解码器盲视和成本盲视，限制性能上限。
- 方法要点：将扩散去噪过程建模为MDP，直接优化解码后解的成本，引入标签中心奖励。
- 实验或效果：在多个基准测试中达到最先进性能，验证目标对齐的重要性。

## 摘要（原文）

> Heatmap-based solvers have emerged as a promising paradigm for Combinatorial Optimization (CO). However, we argue that the dominant Supervised Learning (SL) training paradigm suffers from a fundamental objective mismatch: minimizing imitation loss (e.g., cross-entropy) does not guarantee solution cost minimization. We dissect this mismatch into two deficiencies: Decoder-Blindness (being oblivious to the non-differentiable decoding process) and Cost-Blindness (prioritizing structural imitation over solution quality). We empirically demonstrate that these intrinsic flaws impose a hard performance ceiling. To overcome this limitation, we propose CADO (Cost-Aware Diffusion models for Optimization), a streamlined Reinforcement Learning fine-tuning framework that formulates the diffusion denoising process as an MDP to directly optimize the post-decoded solution cost. We introduce Label-Centered Reward, which repurposes ground-truth labels as unbiased baselines rather than imitation targets, and Hybrid Fine-Tuning for parameter-efficient adaptation. CADO achieves state-of-the-art performance across diverse benchmarks, validating that objective alignment is essential for unlocking the full potential of heatmap-based solvers.

