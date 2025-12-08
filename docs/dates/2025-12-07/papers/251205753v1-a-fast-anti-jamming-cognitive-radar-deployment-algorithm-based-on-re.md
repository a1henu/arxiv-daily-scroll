---
layout: default
title: A Fast Anti-Jamming Cognitive Radar Deployment Algorithm Based on Reinforcement Learning
---

# A Fast Anti-Jamming Cognitive Radar Deployment Algorithm Based on Reinforcement Learning
**arXiv**：[2512.05753v1](https://arxiv.org/abs/2512.05753) · [PDF](https://arxiv.org/pdf/2512.05753.pdf)  
**作者**：Wencheng Cai, Xuchao Gao, Congying Han, Mingqiang Li, Tiande Guo  

**一句话要点**：提出基于强化学习的快速抗干扰认知雷达部署算法，以解决传统进化算法耗时且易陷局部最优的问题。

**关键词**：认知雷达部署, 强化学习, 抗干扰, 端到端任务, 热图感知, 快速部署算法

## 3 点简述
- 核心问题：认知雷达快速部署以对抗干扰是现代战争中的关键挑战，现有进化算法效率低且易陷局部最优。
- 方法要点：将雷达部署建模为端到端任务，设计深度强化学习算法，集成神经模块感知热图信息并创新奖励格式。
- 实验或效果：方法覆盖性能与进化算法相当，部署速度提升约7000倍，消融实验验证各组件必要性。

## 摘要（原文）

> The fast deployment of cognitive radar to counter jamming remains a critical challenge in modern warfare, where more efficient deployment leads to quicker detection of targets. Existing methods are primarily based on evolutionary algorithms, which are time-consuming and prone to falling into local optima. We tackle these drawbacks via the efficient inference of neural networks and propose a brand new framework: Fast Anti-Jamming Radar Deployment Algorithm (FARDA). We first model the radar deployment problem as an end-to-end task and design deep reinforcement learning algorithms to solve it, where we develop integrated neural modules to perceive heatmap information and a brand new reward format. Empirical results demonstrate that our method achieves coverage comparable to evolutionary algorithms while deploying radars approximately 7,000 times faster. Further ablation experiments confirm the necessity of each component of FARDA.

