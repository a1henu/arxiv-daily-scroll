---
layout: default
title: Beyond Sliding Windows: Learning to Manage Memory in Non-Markovian Environments
---

# Beyond Sliding Windows: Learning to Manage Memory in Non-Markovian Environments
**arXiv**：[2512.19154v1](https://arxiv.org/abs/2512.19154) · [PDF](https://arxiv.org/pdf/2512.19154.pdf)  
**作者**：Geraud Nangue Tasse, Matthew Riemer, Benjamin Rosman, Tim Klinger  

**一句话要点**：提出自适应堆叠元算法以解决非马尔可夫环境中计算与内存限制问题

**关键词**：非马尔可夫环境, 自适应记忆管理, 计算效率优化, 元算法, 序列模型

## 3 点简述
- 核心问题：非马尔可夫依赖导致滑动窗口方法计算和内存需求过高
- 方法要点：自适应维护小型记忆堆栈，减少每步观察数量，保证收敛
- 实验或效果：在控制非马尔可夫依赖的任务中验证算法能有效移除无关记忆

## 摘要（原文）

> Recent success in developing increasingly general purpose agents based on sequence models has led to increased focus on the problem of deploying computationally limited agents within the vastly more complex real-world. A key challenge experienced in these more realistic domains is highly non-Markovian dependencies with respect to the agent's observations, which are less common in small controlled domains. The predominant approach for dealing with this in the literature is to stack together a window of the most recent observations (Frame Stacking), but this window size must grow with the degree of non-Markovian dependencies, which results in prohibitive computational and memory requirements for both action inference and learning. In this paper, we are motivated by the insight that in many environments that are highly non-Markovian with respect to time, the environment only causally depends on a relatively small number of observations over that time-scale. A natural direction would then be to consider meta-algorithms that maintain relatively small adaptive stacks of memories such that it is possible to express highly non-Markovian dependencies with respect to time while considering fewer observations at each step and thus experience substantial savings in both compute and memory requirements. Hence, we propose a meta-algorithm (Adaptive Stacking) for achieving exactly that with convergence guarantees and quantify the reduced computation and memory constraints for MLP, LSTM, and Transformer-based agents. Our experiments utilize popular memory tasks, which give us control over the degree of non-Markovian dependencies. This allows us to demonstrate that an appropriate meta-algorithm can learn the removal of memories not predictive of future rewards without excessive removal of important experiences. Code: https://github.com/geraudnt/adaptive-stacking

