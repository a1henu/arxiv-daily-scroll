---
layout: default
title: Simplicial Embeddings Improve Sample Efficiency in Actor-Critic Agents
---

# Simplicial Embeddings Improve Sample Efficiency in Actor-Critic Agents
**arXiv**：[2510.13704v1](https://arxiv.org/abs/2510.13704) · [PDF](https://arxiv.org/pdf/2510.13704.pdf)  
**作者**：Johan Obando-Ceron, Walter Mayor, Samuel Lavoie, Scott Fujimoto, Aaron Courville, Pablo Samuel Castro  

**一句话要点**：提出单纯形嵌入以提升演员-评论家方法的样本效率

**关键词**：单纯形嵌入, 演员-评论家方法, 样本效率, 强化学习, 几何归纳偏置

## 3 点简述
- 问题：大规模并行化训练仍需要大量环境交互才能达到性能目标
- 方法：引入单纯形嵌入，约束嵌入为单纯形结构，提供几何归纳偏置
- 效果：在多种环境中提高样本效率和最终性能，不损失运行速度

## 摘要（原文）

> Recent works have proposed accelerating the wall-clock training time of
> actor-critic methods via the use of large-scale environment parallelization;
> unfortunately, these can sometimes still require large number of environment
> interactions to achieve a desired level of performance. Noting that
> well-structured representations can improve the generalization and sample
> efficiency of deep reinforcement learning (RL) agents, we propose the use of
> simplicial embeddings: lightweight representation layers that constrain
> embeddings to simplicial structures. This geometric inductive bias results in
> sparse and discrete features that stabilize critic bootstrapping and strengthen
> policy gradients. When applied to FastTD3, FastSAC, and PPO, simplicial
> embeddings consistently improve sample efficiency and final performance across
> a variety of continuous- and discrete-control environments, without any loss in
> runtime speed.

