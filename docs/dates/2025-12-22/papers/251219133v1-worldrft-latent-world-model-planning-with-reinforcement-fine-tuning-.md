---
layout: default
title: WorldRFT: Latent World Model Planning with Reinforcement Fine-Tuning for Autonomous Driving
---

# WorldRFT: Latent World Model Planning with Reinforcement Fine-Tuning for Autonomous Driving
**arXiv**：[2512.19133v1](https://arxiv.org/abs/2512.19133) · [PDF](https://arxiv.org/pdf/2512.19133.pdf)  
**作者**：Pengxuan Yang, Ben Lu, Zhongpu Xia, Chao Han, Yinfeng Gao, Teng Zhang, Kun Zhan, XianPeng Lang, Yupeng Zheng, Qichao Zhang  

**一句话要点**：提出WorldRFT框架，通过规划导向的潜在世界模型和强化学习微调，提升自动驾驶的安全性和性能。

**关键词**：自动驾驶, 潜在世界模型, 强化学习微调, 规划导向表示, 安全策略优化, 端到端驾驶

## 3 点简述
- 核心问题：潜在世界模型的重建导向表示学习导致感知与规划任务纠缠，规划优化不足。
- 方法要点：采用分层规划分解和局部感知交互细化机制，结合强化学习微调（GRPO）优化驾驶策略。
- 实验或效果：在nuScenes和NavSim基准上实现SOTA，碰撞率降低83%，仅用相机输入接近激光雷达SOTA性能。

## 摘要（原文）

> Latent World Models enhance scene representation through temporal self-supervised learning, presenting a perception annotation-free paradigm for end-to-end autonomous driving. However, the reconstruction-oriented representation learning tangles perception with planning tasks, leading to suboptimal optimization for planning. To address this challenge, we propose WorldRFT, a planning-oriented latent world model framework that aligns scene representation learning with planning via a hierarchical planning decomposition and local-aware interactive refinement mechanism, augmented by reinforcement learning fine-tuning (RFT) to enhance safety-critical policy performance. Specifically, WorldRFT integrates a vision-geometry foundation model to improve 3D spatial awareness, employs hierarchical planning task decomposition to guide representation optimization, and utilizes local-aware iterative refinement to derive a planning-oriented driving policy. Furthermore, we introduce Group Relative Policy Optimization (GRPO), which applies trajectory Gaussianization and collision-aware rewards to fine-tune the driving policy, yielding systematic improvements in safety. WorldRFT achieves state-of-the-art (SOTA) performance on both open-loop nuScenes and closed-loop NavSim benchmarks. On nuScenes, it reduces collision rates by 83% (0.30% -> 0.05%). On NavSim, using camera-only sensors input, it attains competitive performance with the LiDAR-based SOTA method DiffusionDrive (87.8 vs. 88.1 PDMS).

