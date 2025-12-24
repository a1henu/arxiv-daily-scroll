---
layout: default
title: Recurrent Off-Policy Deep Reinforcement Learning Doesn't Have to be Slow
---

# Recurrent Off-Policy Deep Reinforcement Learning Doesn't Have to be Slow
**arXiv**：[2512.20513v1](https://arxiv.org/abs/2512.20513) · [PDF](https://arxiv.org/pdf/2512.20513.pdf)  
**作者**：Tyler Clark, Christine Evers, Jonathon Hare  

**一句话要点**：提出RISE框架以解决循环离策略深度强化学习在图像任务中的高计算成本问题。

**关键词**：循环强化学习, 离策略学习, 图像任务, 计算效率, 编码层优化, Atari基准

## 3 点简述
- 核心问题：循环离策略深度强化学习在图像任务中性能优异但计算需求高，常被弃用。
- 方法要点：RISE通过结合可学习和不可学习编码层，在图像任务中高效集成循环网络，无显著计算开销。
- 实验或效果：集成RISE后，Atari基准上非循环离策略算法性能提升35.6%（人类归一化IQM）。

## 摘要（原文）

> Recurrent off-policy deep reinforcement learning models achieve state-of-the-art performance but are often sidelined due to their high computational demands. In response, we introduce RISE (Recurrent Integration via Simplified Encodings), a novel approach that can leverage recurrent networks in any image-based off-policy RL setting without significant computational overheads via using both learnable and non-learnable encoder layers. When integrating RISE into leading non-recurrent off-policy RL algorithms, we observe a 35.6% human-normalized interquartile mean (IQM) performance improvement across the Atari benchmark. We analyze various implementation strategies to highlight the versatility and potential of our proposed framework.

