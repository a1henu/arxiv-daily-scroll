---
layout: default
title: Zeroth-Order Stackelberg Control in Combinatorial Congestion Games
---

# Zeroth-Order Stackelberg Control in Combinatorial Congestion Games
**arXiv**：[2602.23277v1](https://arxiv.org/abs/2602.23277) · [PDF](https://arxiv.org/pdf/2602.23277.pdf)  
**作者**：Saeed Masiha, Sepehr Elahi, Negar Kiyavash, Patrick Thiran  

**一句话要点**：提出ZO-Stackelberg方法，用于组合拥塞博弈中网络参数的Stackelberg控制，避免均衡微分。

**关键词**：组合拥塞博弈, Stackelberg控制, 零阶优化, Frank-Wolfe方法, 均衡求解, 网络参数调整

## 3 点简述
- 研究组合拥塞博弈中网络参数（如收费、容量）的Stackelberg调整，系统目标在均衡处非光滑。
- 结合无投影Frank-Wolfe均衡求解器和零阶外更新，避免通过均衡微分，证明收敛到广义Goldstein稳定点。
- 实验显示在真实网络上比基于微分基线快几个数量级，同时收敛到跟随者均衡。

## 摘要（原文）

> We study Stackelberg (leader--follower) tuning of network parameters (tolls, capacities, incentives) in combinatorial congestion games, where selfish users choose discrete routes (or other combinatorial strategies) and settle at a congestion equilibrium. The leader minimizes a system-level objective (e.g., total travel time) evaluated at equilibrium, but this objective is typically nonsmooth because the set of used strategies can change abruptly. We propose ZO-Stackelberg, which couples a projection-free Frank--Wolfe equilibrium solver with a zeroth-order outer update, avoiding differentiation through equilibria. We prove convergence to generalized Goldstein stationary points of the true equilibrium objective, with explicit dependence on the equilibrium approximation error, and analyze subsampled oracles: if an exact minimizer is sampled with probability $κ_m$, then the Frank--Wolfe error decays as $\mathcal{O}(1/(κ_m T))$. We also propose stratified sampling as a practical way to avoid a vanishing $κ_m$ when the strategies that matter most for the Wardrop equilibrium concentrate in a few dominant combinatorial classes (e.g., short paths). Experiments on real-world networks demonstrate that our method achieves orders-of-magnitude speedups over a differentiation-based baseline while converging to follower equilibria.

