---
layout: default
title: OBLR-PO: A Theoretical Framework for Stable Reinforcement Learning
---

# OBLR-PO: A Theoretical Framework for Stable Reinforcement Learning
**arXiv**：[2511.23310v1](https://arxiv.org/abs/2511.23310) · [PDF](https://arxiv.org/pdf/2511.23310.pdf)  
**作者**：Zixun Huang, Jiayi Sheng, Zeyu Zheng  

**一句话要点**：提出OBLR-PO框架以稳定大语言模型强化学习后训练

**关键词**：强化学习后训练, 策略梯度估计, 方差优化, 自适应学习率, 大语言模型优化, 理论框架

## 3 点简述
- 现有RL后训练方法缺乏理论指导，影响梯度估计器理解和优化稳定性
- 建立统一理论框架分析策略梯度估计器统计性质，推导方差和收敛保证
- 实验在Qwen3模型上验证OBLR-PO优于现有方法，提升训练稳定性和性能

## 摘要（原文）

> Existing reinforcement learning (RL)-based post-training methods for large language models have advanced rapidly, yet their design has largely been guided by heuristics rather than systematic theoretical principles. This gap limits our understanding of the properties of the gradient estimators and the associated optimization algorithms, thereby constraining opportunities to improve training stability and overall performance. In this work, we provide a unified theoretical framework that characterizes the statistical properties of commonly used policy-gradient estimators under mild assumptions. Our analysis establishes unbiasedness, derives exact variance expressions, and yields an optimization-loss upper bound that enables principled reasoning about learning dynamics. Building on these results, we prove convergence guarantees and derive an adaptive learning-rate schedule governed by the signal-to-noise ratio (SNR) of gradients. We further show that the variance-optimal baseline is a gradient-weighted estimator, offering a new principle for variance reduction and naturally enhancing stability beyond existing methods. These insights motivate Optimal Baseline and Learning-Rate Policy Optimization (OBLR-PO), an algorithm that jointly adapts learning rates and baselines in a theoretically grounded manner. Experiments on Qwen3-4B-Base and Qwen3-8B-Base demonstrate consistent gains over existing policy optimization methods, validating that our theoretical contributions translate into practical improvements in large-scale post-training.

