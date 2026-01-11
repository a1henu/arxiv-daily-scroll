---
layout: default
title: Estimating Causal Effects in Gaussian Linear SCMs with Finite Data
---

# Estimating Causal Effects in Gaussian Linear SCMs with Finite Data
**arXiv**：[2601.04673v1](https://arxiv.org/abs/2601.04673) · [PDF](https://arxiv.org/pdf/2601.04673.pdf)  
**作者**：Aurghya Maiti, Prateek Jain  

**一句话要点**：提出集中化高斯线性结构因果模型以解决有限数据下因果效应估计的过参数化问题

**关键词**：因果推断, 高斯线性结构因果模型, 有限数据估计, EM算法, 因果效应识别

## 3 点简述
- 核心问题：高斯线性结构因果模型在有限数据下因过参数化导致参数估计不可行
- 方法要点：引入集中化高斯线性结构因果模型子类，保持因果效应可识别性，并设计基于EM的估计算法
- 实验或效果：在合成数据和基准因果图上验证算法能准确恢复因果分布

## 摘要（原文）

> Estimating causal effects from observational data remains a fundamental challenge in causal inference, especially in the presence of latent confounders. This paper focuses on estimating causal effects in Gaussian Linear Structural Causal Models (GL-SCMs), which are widely used due to their analytical tractability. However, parameter estimation in GL-SCMs is often infeasible with finite data, primarily due to overparameterization. To address this, we introduce the class of Centralized Gaussian Linear SCMs (CGL-SCMs), a simplified yet expressive subclass where exogenous variables follow standardized distributions. We show that CGL-SCMs are equally expressive in terms of causal effect identifiability from observational distributions and present a novel EM-based estimation algorithm that can learn CGL-SCM parameters and estimate identifiable causal effects from finite observational samples. Our theoretical analysis is validated through experiments on synthetic data and benchmark causal graphs, demonstrating that the learned models accurately recover causal distributions.

