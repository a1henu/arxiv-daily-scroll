---
layout: default
title: Learning Potentials for Dynamic Matching and Application to Heart Transplantation
---

# Learning Potentials for Dynamic Matching and Application to Heart Transplantation
**arXiv**：[2602.08878v1](https://arxiv.org/abs/2602.08878) · [PDF](https://arxiv.org/pdf/2602.08878.pdf)  
**作者**：Itai Zilberstein, Ioannis Anagnostides, Zachary W. Sollie, Arman Kilic, Tuomas Sandholm  

**一句话要点**：提出基于势能学习的非近视动态匹配框架，应用于心脏移植分配以优化群体结果。

**关键词**：动态匹配, 势能学习, 心脏移植分配, 非近视策略优化, 自监督模仿学习

## 3 点简述
- 核心问题：心脏移植中器官稀缺与动态匹配效率低，现有政策未充分适应器官到达和候选者组成变化。
- 方法要点：通过自监督模仿学习训练高维势能，模拟全知算法以优化非近视匹配策略。
- 实验或效果：基于真实历史数据，新策略显著优于现有方法，包括美国现状和连续分布框架。

## 摘要（原文）

> Each year, thousands of patients in need of heart transplants face life-threatening wait times due to organ scarcity. While allocation policies aim to maximize population-level outcomes, current approaches often fail to account for the dynamic arrival of organs and the composition of waitlisted candidates, thereby hampering efficiency. The United States is transitioning from rigid, rule-based allocation to more flexible data-driven models. In this paper, we propose a novel framework for non-myopic policy optimization in general online matching relying on potentials, a concept originally introduced for kidney exchange. We develop scalable and accurate ways of learning potentials that are higher-dimensional and more expressive than prior approaches. Our approach is a form of self-supervised imitation learning: the potentials are trained to mimic an omniscient algorithm that has perfect foresight. We focus on the application of heart transplant allocation and demonstrate, using real historical data, that our policies significantly outperform prior approaches -- including the current US status quo policy and the proposed continuous distribution framework -- in optimizing for population-level outcomes. Our analysis and methods come at a pivotal moment in US policy, as the current heart transplant allocation system is under review. We propose a scalable and theoretically grounded path toward more effective organ allocation.

