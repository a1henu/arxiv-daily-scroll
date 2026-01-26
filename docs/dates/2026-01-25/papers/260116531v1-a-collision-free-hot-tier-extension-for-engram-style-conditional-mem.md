---
layout: default
title: A Collision-Free Hot-Tier Extension for Engram-Style Conditional Memory: A Controlled Study of Training Dynamics
---

# A Collision-Free Hot-Tier Extension for Engram-Style Conditional Memory: A Controlled Study of Training Dynamics
**arXiv**：[2601.16531v1](https://arxiv.org/abs/2601.16531) · [PDF](https://arxiv.org/pdf/2601.16531.pdf)  
**作者**：Tao Lin  

**一句话要点**：提出Engram-Nine碰撞无关热层扩展，研究Engram式条件记忆中碰撞瓶颈与训练动态

**关键词**：条件记忆, 哈希碰撞, 训练动态, 正则化, 门控机制, 路由分层评估

## 3 点简述
- 研究Engram式条件记忆中高频键碰撞是否为性能瓶颈，通过碰撞无关设计隔离影响
- 引入Engram-Nine：使用最小完美哈希函数映射高频n-gram，保留原始多头哈希查找作为冷层
- 发现碰撞无关设计未持续改善验证损失，碰撞可能提供有益的正则化效果

## 摘要（原文）

> We investigate whether high-frequency key collisions are a primary bottleneck in Engram-style conditional memory. To isolate the effect of collisions, we introduce Engram-Nine, a collision-free hot-tier extension that maps the most frequent n-grams through a Minimal Perfect Hash Function (MPHF) while retaining the original multi-head hashed lookup as a cold tier. Under a strictly iso-parameter setup, the collision-free design does not consistently improve validation loss.
>   Through route-stratified evaluation (decomposing per-token loss into hot/cold contributions), we uncover a consistent "hot-to-cold advantage flip" during training: hot (high-frequency) positions initially have lower loss, but cold positions eventually surpass them. Crucially, collision-free configurations flip earlier than collision-prone baselines, suggesting that collisions act as implicit regularization. We also identify a gating mismatch: the gate learns to favor hot positions early in training, but this preference persists even after the flip, assigning higher weights to positions with higher loss.
>   Our findings suggest that improving lookup precision alone does not guarantee better training outcomes. The dominant limitation may lie in gating credit assignment rather than index accuracy, and collision-induced noise may provide beneficial regularization that should not be naively eliminated.

