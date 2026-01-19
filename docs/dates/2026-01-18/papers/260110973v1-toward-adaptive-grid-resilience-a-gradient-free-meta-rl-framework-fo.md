---
layout: default
title: Toward Adaptive Grid Resilience: A Gradient-Free Meta-RL Framework for Critical Load Restoration
---

# Toward Adaptive Grid Resilience: A Gradient-Free Meta-RL Framework for Critical Load Restoration
**arXiv**：[2601.10973v1](https://arxiv.org/abs/2601.10973) · [PDF](https://arxiv.org/pdf/2601.10973.pdf)  
**作者**：Zain ul Abdeen, Waris Gill, Ming Jin  

**一句话要点**：提出元引导无梯度强化学习框架，以提升配电网在极端事件后的关键负荷恢复自适应能力。

**关键词**：配电网恢复, 元强化学习, 无梯度优化, 自适应控制, 可再生能源集成

## 3 点简述
- 核心问题：配电网在可再生能源不确定性和非线性动态下，关键负荷恢复面临自适应控制挑战。
- 方法要点：结合元学习和进化策略，实现无梯度可迁移初始化，快速适应新场景。
- 实验或效果：在IEEE测试系统中，优于标准RL、MAML和模型预测控制，提升恢复速度和适应性。

## 摘要（原文）

> Restoring critical loads after extreme events demands adaptive control to maintain distribution-grid resilience, yet uncertainty in renewable generation, limited dispatchable resources, and nonlinear dynamics make effective restoration difficult. Reinforcement learning (RL) can optimize sequential decisions under uncertainty, but standard RL often generalizes poorly and requires extensive retraining for new outage configurations or generation patterns. We propose a meta-guided gradient-free RL (MGF-RL) framework that learns a transferable initialization from historical outage experiences and rapidly adapts to unseen scenarios with minimal task-specific tuning. MGF-RL couples first-order meta-learning with evolutionary strategies, enabling scalable policy search without gradient computation while accommodating nonlinear, constrained distribution-system dynamics. Experiments on IEEE 13-bus and IEEE 123-bus test systems show that MGF-RL outperforms standard RL, MAML-based meta-RL, and model predictive control across reliability, restoration speed, and adaptation efficiency under renewable forecast errors. MGF-RL generalizes to unseen outages and renewable patterns while requiring substantially fewer fine-tuning episodes than conventional RL. We also provide sublinear regret bounds that relate adaptation efficiency to task similarity and environmental variation, supporting the empirical gains and motivating MGF-RL for real-time load restoration in renewable-rich distribution grids.

