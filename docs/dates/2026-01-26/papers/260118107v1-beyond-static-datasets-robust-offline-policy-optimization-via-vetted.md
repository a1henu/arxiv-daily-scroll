---
layout: default
title: Beyond Static Datasets: Robust Offline Policy Optimization via Vetted Synthetic Transitions
---

# Beyond Static Datasets: Robust Offline Policy Optimization via Vetted Synthetic Transitions
**arXiv**：[2601.18107v1](https://arxiv.org/abs/2601.18107) · [PDF](https://arxiv.org/pdf/2601.18107.pdf)  
**作者**：Pedram Agand, Mo Chen  

**一句话要点**：提出MoReBRAC框架，通过不确定性感知潜在合成解决离线强化学习中的分布偏移问题。

**关键词**：离线强化学习, 模型基础方法, 不确定性估计, 数据合成, 分布偏移, VAE应用

## 3 点简述
- 核心问题：离线强化学习中静态数据集与学习策略间的分布偏移限制策略改进。
- 方法要点：使用双循环世界模型合成高保真转移，并通过分层不确定性管道确保合成数据可靠性。
- 实验或效果：在D4RL Gym-MuJoCo基准测试中，尤其在随机和次优数据场景下，性能显著提升。

## 摘要（原文）

> Offline Reinforcement Learning (ORL) holds immense promise for safety-critical domains like industrial robotics, where real-time environmental interaction is often prohibitive. A primary obstacle in ORL remains the distributional shift between the static dataset and the learned policy, which typically mandates high degrees of conservatism that can restrain potential policy improvements. We present MoReBRAC, a model-based framework that addresses this limitation through Uncertainty-Aware latent synthesis. Instead of relying solely on the fixed data, MoReBRAC utilizes a dual-recurrent world model to synthesize high-fidelity transitions that augment the training manifold. To ensure the reliability of this synthetic data, we implement a hierarchical uncertainty pipeline integrating Variational Autoencoder (VAE) manifold detection, model sensitivity analysis, and Monte Carlo (MC) dropout. This multi-layered filtering process guarantees that only transitions residing within high-confidence regions of the learned dynamics are utilized. Our results on D4RL Gym-MuJoCo benchmarks reveal significant performance gains, particularly in ``random'' and ``suboptimal'' data regimes. We further provide insights into the role of the VAE as a geometric anchor and discuss the distributional trade-offs encountered when learning from near-optimal datasets.

