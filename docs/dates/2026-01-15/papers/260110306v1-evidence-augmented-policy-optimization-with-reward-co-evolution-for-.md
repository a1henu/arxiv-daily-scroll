---
layout: default
title: Evidence-Augmented Policy Optimization with Reward Co-Evolution for Long-Context Reasoning
---

# Evidence-Augmented Policy Optimization with Reward Co-Evolution for Long-Context Reasoning
**arXiv**：[2601.10306v1](https://arxiv.org/abs/2601.10306) · [PDF](https://arxiv.org/pdf/2601.10306.pdf)  
**作者**：Xin Guan, Zijian Li, Shen Huang, Pengjun Xie, Jingren Zhou, Jiuxin Cao  

**一句话要点**：提出证据增强策略优化与奖励协同进化方法，以解决长上下文推理中奖励稀疏问题。

**关键词**：长上下文推理, 强化学习, 证据检索, 奖励模型, 过程监督, 策略优化

## 3 点简述
- 核心问题：长上下文推理中奖励稀疏，无法有效监督证据检索过程，导致无根据猜测未被惩罚。
- 方法要点：引入证据增强推理范式，通过组相对证据奖励提供密集过程监督，并结合自适应奖励-策略协同进化机制迭代优化奖励模型。
- 实验或效果：在八个基准测试中，EAPO显著优于现有最先进基线，提升长上下文推理性能。

## 摘要（原文）

> While Reinforcement Learning (RL) has advanced LLM reasoning, applying it to long-context scenarios is hindered by sparsity of outcome rewards. This limitation fails to penalize ungrounded "lucky guesses," leaving the critical process of needle-in-a-haystack evidence retrieval largely unsupervised. To address this, we propose EAPO (Evidence-Augmented Policy Optimization). We first establish the Evidence-Augmented Reasoning paradigm, validating via Tree-Structured Evidence Sampling that precise evidence extraction is the decisive bottleneck for long-context reasoning. Guided by this insight, EAPO introduces a specialized RL algorithm where a reward model computes a Group-Relative Evidence Reward, providing dense process supervision to explicitly improve evidence quality. To sustain accurate supervision throughout training, we further incorporate an Adaptive Reward-Policy Co-Evolution mechanism. This mechanism iteratively refines the reward model using outcome-consistent rollouts, sharpening its discriminative capability to ensure precise process guidance. Comprehensive evaluations across eight benchmarks demonstrate that EAPO significantly enhances long-context reasoning performance compared to SOTA baselines.

