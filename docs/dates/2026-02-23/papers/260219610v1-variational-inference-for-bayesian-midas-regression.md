---
layout: default
title: Variational Inference for Bayesian MIDAS Regression
---

# Variational Inference for Bayesian MIDAS Regression
**arXiv**：[2602.19610v1](https://arxiv.org/abs/2602.19610) · [PDF](https://arxiv.org/pdf/2602.19610.pdf)  
**作者**：Luigi Simeone  

**一句话要点**：提出坐标上升变分推断算法以高效求解贝叶斯MIDAS回归模型

**关键词**：变分推断, 贝叶斯回归, 混合数据采样, 坐标上升, 不确定性传播, 金融预测

## 3 点简述
- 针对贝叶斯混合数据采样回归模型，其双线性结构使通用哈密顿蒙特卡洛采样不可靠
- 开发坐标上升变分推断算法，利用条件共轭性实现闭式更新，传播不确定性
- 在模拟和实证应用中，算法速度提升显著，与吉布斯采样结果相近，但区间校准存在权衡

## 摘要（原文）

> We develop a Coordinate Ascent Variational Inference (CAVI) algorithm for Bayesian Mixed Data Sampling (MIDAS) regression with linear weight parameteri zations. The model separates impact coe cients from weighting function parameters through a normalization constraint, creating a bilinear structure that renders generic Hamiltonian Monte Carlo samplers unreliable while preserving conditional conju gacy exploitable by CAVI. Each variational update admits a closed-form solution: Gaussian for regression coe cients and weight parameters, Inverse-Gamma for the error variance. The algorithm propagates uncertainty across blocks through second moments, distinguishing it from naive plug-in approximations. In a Monte Carlo study spanning 21 data-generating con gurations with up to 50 predictors, CAVI produces posterior means nearly identical to a block Gibbs sampler benchmark while achieving speedups of 107x to 1,772x (Table 9). Generic automatic di eren tiation VI (ADVI), by contrast, produces bias 714 times larger while being orders of magnitude slower, con rming the value of model-speci c derivations. Weight function parameters maintain excellent calibration (coverage above 92%) across all con gurations. Impact coe cient credible intervals exhibit the underdispersion characteristic of mean- eld approximations, with coverage declining from 89% to 55% as the number of predictors grows a documented trade-o between speed and interval calibration that structured variational methods can address. An empirical application to realized volatility forecasting on S&P 500 daily returns con rms that CAVI and Gibbs sampling yield virtually identical point forecasts, with CAVI completing each monthly estimation in under 10 milliseconds.

