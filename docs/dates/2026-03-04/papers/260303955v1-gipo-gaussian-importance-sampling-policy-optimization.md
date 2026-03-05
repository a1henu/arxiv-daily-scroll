---
layout: default
title: GIPO: Gaussian Importance Sampling Policy Optimization
---

# GIPO: Gaussian Importance Sampling Policy Optimization
**arXiv**：[2603.03955v1](https://arxiv.org/abs/2603.03955) · [PDF](https://arxiv.org/pdf/2603.03955.pdf)  
**作者**：Chengxuan Lu, Zhenquan Zhang, Shukuan Wang, Qunzhi Lin, Baigui Sun, Yang Liu  

**一句话要点**：提出GIPO以解决强化学习中数据效率低和过时数据问题，通过高斯重要性采样优化策略。

**关键词**：强化学习, 策略优化, 重要性采样, 高斯信任权重, 样本效率, 训练稳定性

## 3 点简述
- 核心问题：强化学习在数据稀缺和快速过时场景下数据效率低。
- 方法要点：基于截断重要性采样，用高斯信任权重软阻尼极端重要性比率，保持非零梯度。
- 实验或效果：在广泛回放缓冲区大小下实现最优性能，提升样本效率和训练稳定性。

## 摘要（原文）

> Post-training with reinforcement learning (RL) has recently shown strong promise for advancing multimodal agents beyond supervised imitation. However, RL remains limited by poor data efficiency, particularly in settings where interaction data are scarce and quickly become outdated. To address this challenge, GIPO (Gaussian Importance sampling Policy Optimization) is proposed as a policy optimization objective based on truncated importance sampling, replacing hard clipping with a log-ratio-based Gaussian trust weight to softly damp extreme importance ratios while maintaining non-zero gradients. Theoretical analysis shows that GIPO introduces an implicit, tunable constraint on the update magnitude, while concentration bounds guarantee robustness and stability under finite-sample estimation. Experimental results show that GIPO achieves state-of-the-art performance among clipping-based baselines across a wide range of replay buffer sizes, from near on-policy to highly stale data, while exhibiting superior bias--variance trade-off, high training stability and improved sample efficiency.

