---
layout: default
title: Enhanced Convergence in p-bit Based Simulated Annealing with Partial Deactivation for Large-Scale Combinatorial Optimization Problems
---

# Enhanced Convergence in p-bit Based Simulated Annealing with Partial Deactivation for Large-Scale Combinatorial Optimization Problems
**arXiv**：[2601.15561v1](https://arxiv.org/abs/2601.15561) · [PDF](https://arxiv.org/pdf/2601.15561.pdf)  
**作者**：Naoya Onizawa, Takahiro Hanyu  

**一句话要点**：提出TApSA和SpSA算法，通过部分去激活p-bit解决大规模组合优化问题中的模拟退火振荡问题

**关键词**：概率比特模拟退火, 组合优化, 振荡抑制, 部分去激活, 最大割问题, 能量收敛

## 3 点简述
- 分析pSA中p-bit意外振荡导致能量停滞的根本原因，归因于反馈机制
- 基于部分p-bit去激活设计TApSA和SpSA算法，以抑制振荡并提升收敛
- 在最大割基准测试中，新算法平均提升归一化割值0.8%至98.4%

## 摘要（原文）

> This article critically investigates the limitations of the simulated annealing algorithm using probabilistic bits (pSA) in solving large-scale combinatorial optimization problems. The study begins with an in-depth analysis of the pSA process, focusing on the issues resulting from unexpected oscillations among p-bits. These oscillations hinder the energy reduction of the Ising model and thus obstruct the successful execution of pSA in complex tasks. Through detailed simulations, we unravel the root cause of this energy stagnation, identifying the feedback mechanism inherent to the pSA operation as the primary contributor to these disruptive oscillations. To address this challenge, we propose two novel algorithms, time average pSA (TApSA) and stalled pSA (SpSA). These algorithms are designed based on partial deactivation of p-bits and are thoroughly tested using Python simulations on maximum cut benchmarks that are typical combinatorial optimization problems. On the 16 benchmarks from 800 to 5,000 nodes, the proposed methods improve the normalized cut value from 0.8% to 98.4% on average in comparison with the conventional pSA.

