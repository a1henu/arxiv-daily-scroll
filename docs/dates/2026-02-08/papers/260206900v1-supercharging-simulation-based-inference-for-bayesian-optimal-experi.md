---
layout: default
title: Supercharging Simulation-Based Inference for Bayesian Optimal Experimental Design
---

# Supercharging Simulation-Based Inference for Bayesian Optimal Experimental Design
**arXiv**：[2602.06900v1](https://arxiv.org/abs/2602.06900) · [PDF](https://arxiv.org/pdf/2602.06900.pdf)  
**作者**：Samuel Klein, Willie Neiswanger, Daniel Ratner, Michael Kagan, Sean Gasiorowski  

**一句话要点**：提出基于神经似然估计的贝叶斯最优实验设计方法，提升仿真推理性能

**关键词**：贝叶斯最优实验设计, 仿真推理, 神经似然估计, 期望信息增益, 梯度优化

## 3 点简述
- 贝叶斯最优实验设计需估计期望信息增益，但似然函数常难处理
- 利用仿真推理工具，扩展期望信息增益的多种形式，包括神经后验、似然和比率估计
- 通过多起点并行梯度上升优化，在标准基准上性能提升高达22%

## 摘要（原文）

> Bayesian optimal experimental design (BOED) seeks to maximize the expected information gain (EIG) of experiments. This requires a likelihood estimate, which in many settings is intractable. Simulation-based inference (SBI) provides powerful tools for this regime. However, existing work explicitly connecting SBI and BOED is restricted to a single contrastive EIG bound. We show that the EIG admits multiple formulations which can directly leverage modern SBI density estimators, encompassing neural posterior, likelihood, and ratio estimation. Building on this perspective, we define a novel EIG estimator using neural likelihood estimation. Further, we identify optimization as a key bottleneck of gradient based EIG maximization and show that a simple multi-start parallel gradient ascent procedure can substantially improve reliability and performance. With these innovations, our SBI-based BOED methods are able to match or outperform by up to $22\%$ existing state-of-the-art approaches across standard BOED benchmarks.

