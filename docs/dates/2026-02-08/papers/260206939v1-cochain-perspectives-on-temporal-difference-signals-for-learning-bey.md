---
layout: default
title: Cochain Perspectives on Temporal-Difference Signals for Learning Beyond Markov Dynamics
---

# Cochain Perspectives on Temporal-Difference Signals for Learning Beyond Markov Dynamics
**arXiv**：[2602.06939v1](https://arxiv.org/abs/2602.06939) · [PDF](https://arxiv.org/pdf/2602.06939.pdf)  
**作者**：Zuyuan Zhang, Sizhe Tang, Tian Lan  

**一句话要点**：提出HodgeFlow策略搜索，通过拓扑视角分解TD误差以提升非马尔可夫强化学习性能。

**关键词**：强化学习, 非马尔可夫动态, 拓扑视角, TD误差分解, 策略搜索

## 3 点简述
- 核心问题：非马尔可夫动态下Bellman方程近似有效，现有方法理论分析不足。
- 方法要点：将TD误差视为1-上链，通过Bellman-de Rham投影分解为可积分量与拓扑残差。
- 实验或效果：HFPS在非马尔可夫环境中显著提升强化学习性能，具有稳定性保证。

## 摘要（原文）

> Non-Markovian dynamics are commonly found in real-world environments due to long-range dependencies, partial observability, and memory effects. The Bellman equation that is the central pillar of Reinforcement learning (RL) becomes only approximately valid under Non-Markovian. Existing work often focus on practical algorithm designs and offer limited theoretical treatment to address key questions, such as what dynamics are indeed capturable by the Bellman framework and how to inspire new algorithm classes with optimal approximations. In this paper, we present a novel topological viewpoint on temporal-difference (TD) based RL. We show that TD errors can be viewed as 1-cochain in the topological space of state transitions, while Markov dynamics are then interpreted as topological integrability. This novel view enables us to obtain a Hodge-type decomposition of TD errors into an integrable component and a topological residual, through a Bellman-de Rham projection. We further propose HodgeFlow Policy Search (HFPS) by fitting a potential network to minimize the non-integrable projection residual in RL, achieving stability/sensitivity guarantees. In numerical evaluations, HFPS is shown to significantly improve RL performance under non-Markovian.

