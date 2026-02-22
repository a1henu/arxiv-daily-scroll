---
layout: default
title: RLGT: A reinforcement learning framework for extremal graph theory
---

# RLGT: A reinforcement learning framework for extremal graph theory
**arXiv**：[2602.17276v1](https://arxiv.org/abs/2602.17276) · [PDF](https://arxiv.org/pdf/2602.17276.pdf)  
**作者**：Ivan Damnjanović, Uroš Milivojević, Irena Đorđević, Dragan Stevanović  

**一句话要点**：提出RLGT强化学习框架以系统化支持极值图论研究

**关键词**：强化学习, 极值图论, 组合优化, 图表示, 模块化框架, 计算性能优化

## 3 点简述
- 核心问题：极值图论中的组合优化问题，如拉普拉斯谱半径不等式、拉姆齐数下界和Turán型极值问题
- 方法要点：基于Wagner工作，构建模块化RL框架，支持无向/有向图、带/不带环和多边色
- 实验或效果：框架优化计算性能，促进未来RL在极值图论中的应用，已用于反驳不等式和获得新下界

## 摘要（原文）

> Reinforcement learning (RL) is a subfield of machine learning that focuses on developing models that can autonomously learn optimal decision-making strategies over time. In a recent pioneering paper, Wagner demonstrated how the Deep Cross-Entropy RL method can be applied to tackle various problems from extremal graph theory by reformulating them as combinatorial optimization problems. Subsequently, many researchers became interested in refining and extending the framework introduced by Wagner, thereby creating various RL environments specialized for graph theory. Moreover, a number of problems from extremal graph theory were solved through the use of RL. In particular, several inequalities concerning the Laplacian spectral radius of graphs were refuted, new lower bounds were obtained for certain Ramsey numbers, and contributions were made to the Turán-type extremal problem in which the forbidden structures are cycles of length three and four. Here, we present Reinforcement Learning for Graph Theory (RLGT), a novel RL framework that systematizes the previous work and provides support for both undirected and directed graphs, with or without loops, and with an arbitrary number of edge colors. The framework efficiently represents graphs and aims to facilitate future RL-based research in extremal graph theory through optimized computational performance and a clean and modular design.

