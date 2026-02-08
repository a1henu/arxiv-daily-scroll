---
layout: default
title: Learning Event-Based Shooter Models from Virtual Reality Experiments
---

# Learning Event-Based Shooter Models from Virtual Reality Experiments
**arXiv**：[2602.06023v1](https://arxiv.org/abs/2602.06023) · [PDF](https://arxiv.org/pdf/2602.06023.pdf)  
**作者**：Christopher A. McClurg, Alan R. Wagner  

**一句话要点**：提出基于虚拟现实数据驱动的离散事件模拟器，以评估学校安全干预策略。

**关键词**：虚拟现实, 离散事件模拟, 学校安全, 数据驱动建模, 干预策略评估

## 3 点简述
- 核心问题：虚拟现实评估学校安全措施需招募新参与者，难以大规模迭代学习干预策略。
- 方法要点：从VR实验学习射击者行为作为随机过程，构建离散事件模拟器作为可扩展替代。
- 实验或效果：模拟器重现关键经验模式，用于评估机器人干预策略，支持自主安全干预开发。

## 摘要（原文）

> Virtual reality (VR) has emerged as a powerful tool for evaluating school security measures in high-risk scenarios such as school shootings, offering experimental control and high behavioral fidelity. However, assessing new interventions in VR requires recruiting new participant cohorts for each condition, making large-scale or iterative evaluation difficult. These limitations are especially restrictive when attempting to learn effective intervention strategies, which typically require many training episodes. To address this challenge, we develop a data-driven discrete-event simulator (DES) that models shooter movement and in-region actions as stochastic processes learned from participant behavior in VR studies. We use the simulator to examine the impact of a robot-based shooter intervention strategy. Once shown to reproduce key empirical patterns, the DES enables scalable evaluation and learning of intervention strategies that are infeasible to train directly with human subjects. Overall, this work demonstrates a high-to-mid fidelity simulation workflow that provides a scalable surrogate for developing and evaluating autonomous school-security interventions.

