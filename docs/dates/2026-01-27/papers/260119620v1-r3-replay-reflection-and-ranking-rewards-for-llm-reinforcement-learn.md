---
layout: default
title: R^3: Replay, Reflection, and Ranking Rewards for LLM Reinforcement Learning
---

# R^3: Replay, Reflection, and Ranking Rewards for LLM Reinforcement Learning
**arXiv**：[2601.19620v1](https://arxiv.org/abs/2601.19620) · [PDF](https://arxiv.org/pdf/2601.19620.pdf)  
**作者**：Zhizheng Jiang, Kang Zhao, Weikai Xu, Xinkui Lin, Wei Liu, Jian Luan, Shuo Shang, Peng Han  

**一句话要点**：提出R^3强化学习机制以解决大推理模型在组策略优化中优势崩溃问题

**关键词**：大推理模型, 强化学习, 组策略优化, 优势估计, 数学推理, 结构熵

## 3 点简述
- 核心问题：组策略优化方法依赖批内高质量样本的优势差距，在挑战性任务中易导致优势崩溃，训练脆弱低效。
- 方法要点：引入跨上下文回放、上下文内自反思和结构熵排序奖励，分别维持组内优势、利用失败改进输出和基于熵模式分配相对奖励。
- 实验或效果：在数学领域DeepscaleR-40k数据集上训练，多个数学基准测试达到最先进性能，推理令牌更少。

## 摘要（原文）

> Large reasoning models (LRMs) aim to solve diverse and complex problems through structured reasoning. Recent advances in group-based policy optimization methods have shown promise in enabling stable advantage estimation without reliance on process-level annotations. However, these methods rely on advantage gaps induced by high-quality samples within the same batch, which makes the training process fragile and inefficient when intra-group advantages collapse under challenging tasks. To address these problems, we propose a reinforcement learning mechanism named \emph{\textbf{R^3}} that along three directions: (1) a \emph{cross-context \underline{\textbf{R}}eplay} strategy that maintains the intra-group advantage by recalling valuable examples from historical trajectories of the same query, (2) an \emph{in-context self-\underline{\textbf{R}}eflection} mechanism enabling models to refine outputs by leveraging past failures, and (3) a \emph{structural entropy \underline{\textbf{R}}anking reward}, which assigns relative rewards to truncated or failed samples by ranking responses based on token-level entropy patterns, capturing both local exploration and global stability. We implement our method on Deepseek-R1-Distill-Qwen-1.5B and train it on the DeepscaleR-40k in the math domain. Experiments demonstrate our method achieves SoTA performance on several math benchmarks, representing significant improvements and fewer reasoning tokens over the base models. Code and model will be released.

