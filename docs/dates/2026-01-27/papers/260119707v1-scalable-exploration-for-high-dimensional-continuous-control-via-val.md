---
layout: default
title: Scalable Exploration for High-Dimensional Continuous Control via Value-Guided Flow
---

# Scalable Exploration for High-Dimensional Continuous Control via Value-Guided Flow
**arXiv**：[2601.19707v1](https://arxiv.org/abs/2601.19707) · [PDF](https://arxiv.org/pdf/2601.19707.pdf)  
**作者**：Yunyue Wei, Chenhui Zuo, Yanan Sui  

**一句话要点**：提出Qflex方法，通过价值引导的概率流在高维连续控制中进行可扩展探索。

**关键词**：高维连续控制, 强化学习探索, 概率流, 价值函数引导, 可扩展性, 样本效率

## 3 点简述
- 核心问题：高维状态-动作空间中的探索效率低下，传统方法如降维限制策略表达。
- 方法要点：Qflex基于学习到的价值函数诱导概率流，在原生高维动作空间进行定向探索。
- 实验或效果：在多个高维连续控制基准上超越基线，并在人体肌肉骨骼模型中实现复杂运动控制。

## 摘要（原文）

> Controlling high-dimensional systems in biological and robotic applications is challenging due to expansive state-action spaces, where effective exploration is critical. Commonly used exploration strategies in reinforcement learning are largely undirected with sharp degradation as action dimensionality grows. Many existing methods resort to dimensionality reduction, which constrains policy expressiveness and forfeits system flexibility. We introduce Q-guided Flow Exploration (Qflex), a scalable reinforcement learning method that conducts exploration directly in the native high-dimensional action space. During training, Qflex traverses actions from a learnable source distribution along a probability flow induced by the learned value function, aligning exploration with task-relevant gradients rather than isotropic noise. Our proposed method substantially outperforms representative online reinforcement learning baselines across diverse high-dimensional continuous-control benchmarks. Qflex also successfully controls a full-body human musculoskeletal model to perform agile, complex movements, demonstrating superior scalability and sample efficiency in very high-dimensional settings. Our results indicate that value-guided flows offer a principled and practical route to exploration at scale.

