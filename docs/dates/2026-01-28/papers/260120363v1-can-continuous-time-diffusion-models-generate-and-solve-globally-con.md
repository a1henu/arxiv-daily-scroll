---
layout: default
title: Can Continuous-Time Diffusion Models Generate and Solve Globally Constrained Discrete Problems? A Study on Sudoku
---

# Can Continuous-Time Diffusion Models Generate and Solve Globally Constrained Discrete Problems? A Study on Sudoku
**arXiv**：[2601.20363v1](https://arxiv.org/abs/2601.20363) · [PDF](https://arxiv.org/pdf/2601.20363.pdf)  
**作者**：Mariia Drozdova  

**一句话要点**：研究连续时间扩散模型能否生成和求解全局约束离散问题，以数独为例

**关键词**：连续时间扩散模型, 全局约束离散问题, 数独生成, 概率求解, 流匹配, 基于分数模型

## 3 点简述
- 核心问题：连续时间生成模型能否表示支持集为稀疏全局约束离散分布的分布
- 方法要点：训练流匹配和基于分数的模型，比较确定性ODE、随机SDE和DDPM采样
- 实验或效果：随机采样优于确定性流，基于分数采样器最可靠，DDPM采样整体有效性最高

## 摘要（原文）

> Can standard continuous-time generative models represent distributions whose support is an extremely sparse, globally constrained discrete set? We study this question using completed Sudoku grids as a controlled testbed, treating them as a subset of a continuous relaxation space. We train flow-matching and score-based models along a Gaussian probability path and compare deterministic (ODE) sampling, stochastic (SDE) sampling, and DDPM-style discretizations derived from the same continuous-time training. Unconditionally, stochastic sampling substantially outperforms deterministic flows; score-based samplers are the most reliable among continuous-time methods, and DDPM-style ancestral sampling achieves the highest validity overall. We further show that the same models can be repurposed for guided generation: by repeatedly sampling completions under clamped clues and stopping when constraints are satisfied, the model acts as a probabilistic Sudoku solver. Although far less sample-efficient than classical solvers and discrete-geometry-aware diffusion methods, these experiments demonstrate that classic diffusion/flow formulations can assign non-zero probability mass to globally constrained combinatorial structures and can be used for constraint satisfaction via stochastic search.

