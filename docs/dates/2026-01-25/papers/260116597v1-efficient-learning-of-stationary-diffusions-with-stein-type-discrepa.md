---
layout: default
title: Efficient Learning of Stationary Diffusions with Stein-type Discrepancies
---

# Efficient Learning of Stationary Diffusions with Stein-type Discrepancies
**arXiv**：[2601.16597v1](https://arxiv.org/abs/2601.16597) · [PDF](https://arxiv.org/pdf/2601.16597.pdf)  
**作者**：Fabian Bleile, Sarah Lumpp, Mathias Drton  

**一句话要点**：提出Stein型核偏差从平稳性以高效学习平稳扩散，降低计算成本并保持准确性。

**关键词**：平稳扩散学习, Stein偏差, 核偏差从平稳性, 随机微分方程, 参数估计, 计算效率

## 3 点简述
- 核心问题：学习平稳扩散需估计随机微分方程参数，使平稳分布匹配目标分布。
- 方法要点：基于核偏差从平稳性，引入Stein型核偏差，证明其能保证平稳分布对齐，且具有凸性或准凸性。
- 实验或效果：SKDS在准确性上与KDS相当，计算成本显著降低，优于多数竞争基线。

## 摘要（原文）

> Learning a stationary diffusion amounts to estimating the parameters of a stochastic differential equation whose stationary distribution matches a target distribution. We build on the recently introduced kernel deviation from stationarity (KDS), which enforces stationarity by evaluating expectations of the diffusion's generator in a reproducing kernel Hilbert space. Leveraging the connection between KDS and Stein discrepancies, we introduce the Stein-type KDS (SKDS) as an alternative formulation. We prove that a vanishing SKDS guarantees alignment of the learned diffusion's stationary distribution with the target. Furthermore, under broad parametrizations, SKDS is convex with an empirical version that is $ε$-quasiconvex with high probability. Empirically, learning with SKDS attains comparable accuracy to KDS while substantially reducing computational cost and yields improvements over the majority of competitive baselines.

