---
layout: default
title: SAFE: Stable Alignment Finetuning with Entropy-Aware Predictive Control for RLHF
---

# SAFE: Stable Alignment Finetuning with Entropy-Aware Predictive Control for RLHF
**arXiv**：[2602.04651v1](https://arxiv.org/abs/2602.04651) · [PDF](https://arxiv.org/pdf/2602.04651.pdf)  
**作者**：Dipan Maity  

**一句话要点**：提出SAFE算法以解决RLHF中PPO的稳定性问题，通过熵感知控制实现稳定对齐微调。

**关键词**：强化学习对齐, 熵感知控制, 稳定优化, 语言模型微调, RLHF算法

## 3 点简述
- 核心问题：PPO在RLHF中因启发式KL约束导致奖励振荡、熵崩溃和策略发散，需频繁重启。
- 方法要点：结合双软最小批评家进行悲观值估计，并引入熵门控KL调节与PID控制自适应阈值。
- 实验或效果：在3B参数模型上，SAFE比PPO训练平均奖励提升5.15%，奖励崩溃可忽略，KL控制更优。

## 摘要（原文）

> Optimization (PPO) has been positioned by recent literature as the canonical method for the RL part of RLHF. PPO performs well empirically but has a heuristic motivation and handles the KL-divergence constraint used in LM-RLHF in an ad-hoc manner and suffers form reward oscillations, entropy collapse, value function drift, and sudden policy divergence that require frequent restarts and extensive hyperparameter tuning. In this paper, we develop a new pure on policy actor-critic RL method for the LM-RLHF setting. We present SAFE (Stable Alignment Finetuning with Entropy-aware control),a novel RLHF algorithm that combines a Double Soft-Min Critic for pessimistic value estimation with a new multi-layer stabilization framework combining entropy-gated KL regulation, and PID-controlled adaptive thresholds. Unlike standard PPO's symmetric KL penalties, SAFE distinguishes high-entropy exploration from low-entropy mode collapse and adjusts penalties dynamically based on reward velocity. Experiments on a 3B parameter model show SAFE achieves +5.15\% training-average reward than PPO (0.725 vs 0.689), negligible reward crashes, and superior KL control than ppo . Our method adds minimal computational overhead and provides an interpretable, crash-resistant RLHF framework that maintains aggressive learning speed while ensuring stable long-horizon optimization suitable for production deployment. Code is available at https://github.com/ryyzn9/SAFE

