---
layout: default
title: ETS: Energy-Guided Test-Time Scaling for Training-Free RL Alignment
---

# ETS: Energy-Guided Test-Time Scaling for Training-Free RL Alignment
**arXiv**：[2601.21484v1](https://arxiv.org/abs/2601.21484) · [PDF](https://arxiv.org/pdf/2601.21484.pdf)  
**作者**：Xiuyu Li, Jinkai Zhang, Mingyang Yi, Yu Li, Longqiang Wang, Yue Wang, Ju Fan  

**一句话要点**：提出ETS方法以解决RL对齐训练成本高和不稳定的问题，通过训练免费推理直接采样最优策略。

**关键词**：强化学习对齐, 训练免费推理, 能量引导采样, 蒙特卡洛估计, 语言模型优化

## 3 点简述
- 核心问题：RL后训练对齐成本高且不稳定，训练过程复杂。
- 方法要点：基于参考策略和能量项构建转移概率，在线蒙特卡洛估计能量项，确保收敛。
- 实验或效果：在推理、编码和科学基准上，ETS提升生成质量，验证有效性。

## 摘要（原文）

> Reinforcement Learning (RL) post-training alignment for language models is effective, but also costly and unstable in practice, owing to its complicated training process. To address this, we propose a training-free inference method to sample directly from the optimal RL policy. The transition probability applied to Masked Language Modeling (MLM) consists of a reference policy model and an energy term. Based on this, our algorithm, Energy-Guided Test-Time Scaling (ETS), estimates the key energy term via online Monte Carlo, with a provable convergence rate. Moreover, to ensure practical efficiency, ETS leverages modern acceleration frameworks alongside tailored importance sampling estimators, substantially reducing inference latency while provably preserving sampling quality. Experiments on MLM (including autoregressive models and diffusion language models) across reasoning, coding, and science benchmarks show that our ETS consistently improves generation quality, validating its effectiveness and design.

