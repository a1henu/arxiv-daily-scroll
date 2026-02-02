---
layout: default
title: Calibrated Multivariate Distributional Regression with Pre-Rank Regularization
---

# Calibrated Multivariate Distributional Regression with Pre-Rank Regularization
**arXiv**：[2601.22895v1](https://arxiv.org/abs/2601.22895) · [PDF](https://arxiv.org/pdf/2601.22895.pdf)  
**作者**：Aya Laajil, Elnura Zhalieva, Naomi Desobry, Souhaib Ben Taieb  

**一句话要点**：提出基于预排序正则化的校准多变量分布回归方法，以提升多变量校准性

**关键词**：多变量校准, 分布回归, 预排序正则化, PCA预排序, 概率预测

## 3 点简述
- 核心问题：多变量概率预测中校准性难以实现，现有方法多限于事后评估。
- 方法要点：在训练中通过预排序函数正则化强制多变量校准，并引入基于PCA的新预排序。
- 实验或效果：在模拟和18个真实数据集上显著改善校准性，且不损害预测准确性。

## 摘要（原文）

> The goal of probabilistic prediction is to issue predictive distributions that are as informative as possible, subject to being calibrated. Despite substantial progress in the univariate setting, achieving multivariate calibration remains challenging. Recent work has introduced pre-rank functions, scalar projections of multivariate forecasts and observations, as flexible diagnostics for assessing specific aspects of multivariate calibration, but their use has largely been limited to post-hoc evaluation. We propose a regularization-based calibration method that enforces multivariate calibration during training of multivariate distributional regression models using pre-rank functions. We further introduce a novel PCA-based pre-rank that projects predictions onto principal directions of the predictive distribution. Through simulation studies and experiments on 18 real-world multi-output regression datasets, we show that the proposed approach substantially improves multivariate pre-rank calibration without compromising predictive accuracy, and that the PCA pre-rank reveals dependence-structure misspecifications that are not detected by existing pre-ranks.

