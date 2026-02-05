---
layout: default
title: Conditional Counterfactual Mean Embeddings: Doubly Robust Estimation and Learning Rates
---

# Conditional Counterfactual Mean Embeddings: Doubly Robust Estimation and Learning Rates
**arXiv**：[2602.04736v1](https://arxiv.org/abs/2602.04736) · [PDF](https://arxiv.org/pdf/2602.04736.pdf)  
**作者**：Thatchanon Anancharoenkij, Donlapark Ponnoprat  

**一句话要点**：提出条件反事实均值嵌入框架，用于估计异质性处理效应的条件分布，具备双重稳健性。

**关键词**：条件反事实均值嵌入, 异质性处理效应, 再生核希尔伯特空间, 双重稳健估计, 分布嵌入, 元估计器

## 3 点简述
- 核心问题：异质性处理效应需刻画潜在结果的完整条件分布，现有方法可能不足。
- 方法要点：在再生核希尔伯特空间中嵌入条件分布，开发两阶段元估计器及三种实用估计器。
- 实验或效果：实验显示估计器能准确恢复条件反事实分布的多模态结构等特征。

## 摘要（原文）

> A complete understanding of heterogeneous treatment effects involves characterizing the full conditional distribution of potential outcomes. To this end, we propose the Conditional Counterfactual Mean Embeddings (CCME), a framework that embeds conditional distributions of counterfactual outcomes into a reproducing kernel Hilbert space (RKHS). Under this framework, we develop a two-stage meta-estimator for CCME that accommodates any RKHS-valued regression in each stage. Based on this meta-estimator, we develop three practical CCME estimators: (1) Ridge Regression estimator, (2) Deep Feature estimator that parameterizes the feature map by a neural network, and (3) Neural-Kernel estimator that performs RKHS-valued regression, with the coefficients parameterized by a neural network. We provide finite-sample convergence rates for all estimators, establishing that they possess the double robustness property. Our experiments demonstrate that our estimators accurately recover distributional features including multimodal structure of conditional counterfactual distributions.

