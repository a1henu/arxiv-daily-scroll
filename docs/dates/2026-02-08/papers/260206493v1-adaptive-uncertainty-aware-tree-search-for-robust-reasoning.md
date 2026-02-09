---
layout: default
title: Adaptive Uncertainty-Aware Tree Search for Robust Reasoning
---

# Adaptive Uncertainty-Aware Tree Search for Robust Reasoning
**arXiv**：[2602.06493v1](https://arxiv.org/abs/2602.06493) · [PDF](https://arxiv.org/pdf/2602.06493.pdf)  
**作者**：Zeen Song, Zihao Ma, Wenwen Qiang, Changwen Zheng, Gang Hua  

**一句话要点**：提出不确定性感知树搜索以缓解过程奖励模型在分布外推理中的误差影响

**关键词**：不确定性感知推理, 树搜索, 过程奖励模型, 分布外泛化, 强化学习控制, 蒙特卡洛Dropout

## 3 点简述
- 核心问题：过程奖励模型在评估分布外推理路径时存在高不确定性，导致标准搜索方法性能下降
- 方法要点：通过蒙特卡洛Dropout估计不确定性，并基于强化学习控制器动态分配计算预算
- 实验或效果：广泛实验表明该方法有效减轻分布外错误，提升推理鲁棒性

## 摘要（原文）

> Inference-time reasoning scaling has significantly advanced the capabilities of Large Language Models (LLMs) in complex problem-solving. A prevalent approach involves external search guided by Process Reward Models (PRMs). However, a fundamental limitation of this framework is the epistemic uncertainty of PRMs when evaluating reasoning paths that deviate from their training distribution. In this work, we conduct a systematic analysis of this challenge. We first provide empirical evidence that PRMs exhibit high uncertainty and unreliable scoring on out-of-distribution (OOD) samples. We then establish a theoretical framework proving that while standard search incurs linear regret accumulation, an uncertainty-aware strategy can achieve sublinear regret. Motivated by these findings, we propose Uncertainty-Aware Tree Search (UATS), a unified method that estimates uncertainty via Monte Carlo Dropout and dynamically allocates compute budget using a reinforcement learning-based controller. Extensive experiments demonstrate that our approach effectively mitigates the impact of OOD errors.

