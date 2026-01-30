---
layout: default
title: SAGE: Sequence-level Adaptive Gradient Evolution for Generative Recommendation
---

# SAGE: Sequence-level Adaptive Gradient Evolution for Generative Recommendation
**arXiv**：[2601.21452v1](https://arxiv.org/abs/2601.21452) · [PDF](https://arxiv.org/pdf/2601.21452.pdf)  
**作者**：Yu Xie, Xing Kai Ren, Ying Qi, Hu Yao  

**一句话要点**：提出SAGE优化框架以解决生成式推荐中梯度边界对称保守和奖励崩溃问题

**关键词**：生成式推荐, 序列级优化, 梯度演化, 冷启动问题, 多样性维持

## 3 点简述
- 核心问题：OneRec的GBPO策略存在对称保守性，抑制冷启动项更新并导致多样性崩溃
- 方法要点：引入序列级信号解耦和不对称自适应动态，消除令牌级方差并动态调整梯度
- 实验或效果：理论分析和实证显示SAGE有效解锁冷启动流量并维持推荐多样性

## 摘要（原文）

> While works such as OneRec have validated the scaling laws of Large Language Models (LLMs) in recommender systems, they rely on a cumbersome separate vocabulary. This dependency prevents the model architecture from reusing native LLM vocabularies, resulting in high maintenance costs and poor scalability. In response, we aim to efficiently reuse open-source LLM architectures without constructing a separate tokenization vocabulary. Furthermore, we identify that the optimization strategy of OneRec Gradient Bounded Policy Optimization (GBPO),suffers from a "Symmetric Conservatism" problem: its static gradient boundaries structurally suppress the update momentum required for cold-start items and fail to prevent diversity collapse in high-noise environments.To address this issue, we propose SAGE (Sequence-level Adaptive Gradient Evolution), a unified optimization framework tailored for list-wise generative recommendation. SAGE introduces two key innovations:(1) Sequence-level Signal Decoupling: By combining a geometric mean importance ratio with decoupled multi-objective advantages, we eliminate token-level variance and resolve the "Reward Collapse" problem. (2) Asymmetric Adaptive Dynamics: We construct a dynamic gradient manifold that applies a "Boost Factor" to high-potential cold start items to achieve super-linear updates and employs an "Entropy Aware Penalty" to break information cocoons. Theoretical analysis and empirical results demonstrate that SAGE effectively unblocks cold-start traffic and sustains recommendation diversity, all while retaining the numerical stability of GBPO.

