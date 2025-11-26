---
layout: default
title: Quantum-Enhanced Reinforcement Learning for Accelerating Newton-Raphson Convergence with Ising Machines: A Case Study for Power Flow Analysis
---

# Quantum-Enhanced Reinforcement Learning for Accelerating Newton-Raphson Convergence with Ising Machines: A Case Study for Power Flow Analysis
**arXiv**：[2511.20237v1](https://arxiv.org/abs/2511.20237) · [PDF](https://arxiv.org/pdf/2511.20237.pdf)  
**作者**：Zeynab Kaseb, Matthias Moller, Lindsay Spoor, Jerry J. Guo, Yu Xiang, Peter Palensky, Pedro P. Vergara  

**一句话要点**：提出量子增强强化学习优化牛顿-拉夫森初始化，以加速电力潮流分析收敛。

**关键词**：强化学习, 量子计算, 电力潮流分析, 牛顿-拉夫森法, 优化初始化

## 3 点简述
- 牛顿-拉夫森法在电力潮流分析中初始化不佳时收敛慢或发散。
- 使用强化学习优化初始化，量子退火器求解二次无约束二元优化问题。
- 实验显示收敛速度提升、迭代次数减少，增强不同工况鲁棒性。

## 摘要（原文）

> The Newton-Raphson (NR) method is widely used for solving power flow (PF) equations due to its quadratic convergence. However, its performance deteriorates under poor initialization or extreme operating scenarios, e.g., high levels of renewable energy penetration. Traditional NR initialization strategies often fail to address these challenges, resulting in slow convergence or even divergence. We propose the use of reinforcement learning (RL) to optimize the initialization of NR, and introduce a novel quantum-enhanced RL environment update mechanism to mitigate the significant computational cost of evaluating power system states over a combinatorially large action space at each RL timestep by formulating the voltage adjustment task as a quadratic unconstrained binary optimization problem. Specifically, quantum/digital annealers are integrated into the RL environment update to evaluate state transitions using a problem Hamiltonian designed for PF. Results demonstrate significant improvements in convergence speed, a reduction in NR iteration counts, and enhanced robustness under different operating conditions.

