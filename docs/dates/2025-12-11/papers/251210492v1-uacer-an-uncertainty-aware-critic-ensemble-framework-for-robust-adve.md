---
layout: default
title: UACER: An Uncertainty-Aware Critic Ensemble Framework for Robust Adversarial Reinforcement Learning
---

# UACER: An Uncertainty-Aware Critic Ensemble Framework for Robust Adversarial Reinforcement Learning
**arXiv**：[2512.10492v1](https://arxiv.org/abs/2512.10492) · [PDF](https://arxiv.org/pdf/2512.10492.pdf)  
**作者**：Jiaxi Wu, Tiantian Zhang, Yuxing Wang, Yongzhe Chang, Xueqian Wang  

**一句话要点**：提出UACER框架以解决对抗强化学习中训练不稳定问题

**关键词**：对抗强化学习, 评论家集成, 不确定性感知, 训练稳定性, 探索-利用权衡, MuJoCo控制

## 3 点简述
- 核心问题：对抗强化学习中对手可训练性导致学习动态非平稳，加剧训练不稳定和收敛困难
- 方法要点：采用多样化评论家集成和基于方差的Q值聚合策略，结合认知不确定性动态调节探索-利用权衡
- 实验或效果：在多个MuJoCo控制问题上验证，在性能、稳定性和效率方面优于现有方法

## 摘要（原文）

> Robust adversarial reinforcement learning has emerged as an effective paradigm for training agents to handle uncertain disturbance in real environments, with critical applications in sequential decision-making domains such as autonomous driving and robotic control. Within this paradigm, agent training is typically formulated as a zero-sum Markov game between a protagonist and an adversary to enhance policy robustness. However, the trainable nature of the adversary inevitably induces non-stationarity in the learning dynamics, leading to exacerbated training instability and convergence difficulties, particularly in high-dimensional complex environments. In this paper, we propose a novel approach, Uncertainty-Aware Critic Ensemble for robust adversarial Reinforcement learning (UACER), which consists of two strategies: 1) Diversified critic ensemble: a diverse set of K critic networks is exploited in parallel to stabilize Q-value estimation rather than conventional single-critic architectures for both variance reduction and robustness enhancement. 2) Time-varying Decay Uncertainty (TDU) mechanism: advancing beyond simple linear combinations, we develop a variance-derived Q-value aggregation strategy that explicitly incorporates epistemic uncertainty to dynamically regulate the exploration-exploitation trade-off while simultaneously stabilizing the training process. Comprehensive experiments across several MuJoCo control problems validate the superior effectiveness of UACER, outperforming state-of-the-art methods in terms of overall performance, stability, and efficiency.

