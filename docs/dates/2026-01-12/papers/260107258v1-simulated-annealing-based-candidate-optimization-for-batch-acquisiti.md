---
layout: default
title: Simulated Annealing-based Candidate Optimization for Batch Acquisition Functions
---

# Simulated Annealing-based Candidate Optimization for Batch Acquisition Functions
**arXiv**：[2601.07258v1](https://arxiv.org/abs/2601.07258) · [PDF](https://arxiv.org/pdf/2601.07258.pdf)  
**作者**：Sk Md Ahnaf Akif Alvi, Raymundo Arróyave, Douglas Allaire  

**一句话要点**：提出基于模拟退火的候选优化方法以提升多目标贝叶斯优化性能

**关键词**：贝叶斯优化, 多目标优化, 模拟退火, 批量采集函数, 超体积改进

## 3 点简述
- 传统梯度方法在复杂多目标优化中易陷入局部最优
- 采用模拟退火替代连续优化进行批量采集函数优化
- 在多个基准问题上超体积性能优于SLSQP，探索更优帕累托前沿

## 摘要（原文）

> Bayesian Optimization with multi-objective acquisition functions such as q-Expected Hypervolume Improvement (qEHVI) requires efficient candidate optimization to maximize acquisition function values. Traditional approaches rely on continuous optimization methods like Sequential Least Squares Programming (SLSQP) for candidate selection. However, these gradient-based methods can become trapped in local optima, particularly in complex or high-dimensional objective landscapes. This paper presents a simulated annealing-based approach for candidate optimization in batch acquisition functions as an alternative to conventional continuous optimization methods. We evaluate our simulated annealing approach against SLSQP across four benchmark multi-objective optimization problems: ZDT1 (30D, 2 objectives), DTLZ2 (7D, 3 objectives), Kursawe (3D, 2 objectives), and Latent-Aware (4D, 2 objectives). Our results demonstrate that simulated annealing consistently achieves superior hypervolume performance compared to SLSQP in most test functions. The improvement is particularly pronounced for DTLZ2 and Latent-Aware problems, where simulated annealing reaches significantly higher hypervolume values and maintains better convergence characteristics. The histogram analysis of objective space coverage further reveals that simulated annealing explores more diverse and optimal regions of the Pareto front. These findings suggest that metaheuristic optimization approaches like simulated annealing can provide more robust and effective candidate optimization for multi-objective Bayesian optimization, offering a promising alternative to traditional gradient-based methods for batch acquisition function optimization.

