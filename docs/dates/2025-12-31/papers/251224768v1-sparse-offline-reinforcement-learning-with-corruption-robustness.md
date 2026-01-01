---
layout: default
title: Sparse Offline Reinforcement Learning with Corruption Robustness
---

# Sparse Offline Reinforcement Learning with Corruption Robustness
**arXiv**：[2512.24768v1](https://arxiv.org/abs/2512.24768) · [PDF](https://arxiv.org/pdf/2512.24768.pdf)  
**作者**：Nam Phuong Tran, Andi Nika, Goran Radanovic, Long Tran-Thanh, Debmalya Mandal  

**一句话要点**：提出基于稀疏鲁棒估计器的演员-评论家方法，以解决高维稀疏离线强化学习中的数据污染问题。

**关键词**：离线强化学习, 稀疏马尔可夫决策过程, 数据污染鲁棒性, 演员-评论家方法, 高维统计学习

## 3 点简述
- 研究高维稀疏马尔可夫决策过程中的离线强化学习，对抗性数据污染下估计最优策略。
- 分析标准方法LSVI在稀疏性下失效，提出避免悲观奖励的演员-评论家方法，提供非平凡保证。
- 在单策略集中覆盖和强污染设置下，算法保持鲁棒性，优于传统技术。

## 摘要（原文）

> We investigate robustness to strong data corruption in offline sparse reinforcement learning (RL). In our setting, an adversary may arbitrarily perturb a fraction of the collected trajectories from a high-dimensional but sparse Markov decision process, and our goal is to estimate a near optimal policy. The main challenge is that, in the high-dimensional regime where the number of samples $N$ is smaller than the feature dimension $d$, exploiting sparsity is essential for obtaining non-vacuous guarantees but has not been systematically studied in offline RL. We analyse the problem under uniform coverage and sparse single-concentrability assumptions. While Least Square Value Iteration (LSVI), a standard approach for robust offline RL, performs well under uniform coverage, we show that integrating sparsity into LSVI is unnatural, and its analysis may break down due to overly pessimistic bonuses. To overcome this, we propose actor-critic methods with sparse robust estimator oracles, which avoid the use of pointwise pessimistic bonuses and provide the first non-vacuous guarantees for sparse offline RL under single-policy concentrability coverage. Moreover, we extend our results to the contaminated setting and show that our algorithm remains robust under strong contamination. Our results provide the first non-vacuous guarantees in high-dimensional sparse MDPs with single-policy concentrability coverage and corruption, showing that learning a near-optimal policy remains possible in regimes where traditional robust offline RL techniques may fail.

