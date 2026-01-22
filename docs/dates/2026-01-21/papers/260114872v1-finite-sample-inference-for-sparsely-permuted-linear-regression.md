---
layout: default
title: Finite-Sample Inference for Sparsely Permuted Linear Regression
---

# Finite-Sample Inference for Sparsely Permuted Linear Regression
**arXiv**：[2601.14872v1](https://arxiv.org/abs/2601.14872) · [PDF](https://arxiv.org/pdf/2601.14872.pdf)  
**作者**：Hirofumi Ota, Masaaki Imaizumi  

**一句话要点**：提出基于重抽样方法的有限样本推断框架，解决稀疏置换线性回归中的置换与系数推断问题。

**关键词**：置换线性回归, 有限样本推断, 重抽样方法, 蒙特卡洛检验, 线性分配问题, 稀疏置换

## 3 点简述
- 研究带未知置换的噪声线性观测模型，置换作为离散参数导致统计推断困难。
- 开发局部化步骤缩减置换空间，基于候选集提供条件蒙特卡洛检验与系数推断。
- 模拟与北京空气质量数据应用验证有限样本有效性、强检测能力及计算可扩展性。

## 摘要（原文）

> We study a noisy linear observation model with an unknown permutation called permuted/shuffled linear regression, where responses and covariates are mismatched and the permutation forms a discrete, factorial-size parameter. This unknown permutation is a key component of the data-generating process, yet its statistical investigation remains challenging due to its discrete nature. In this study, we develop a general statistical inference framework on the permutation and regression coefficients. First, we introduce a localization step that reduces the permutation space to a small candidate set building on recent advances in the repro samples method, whose miscoverage decays polynomially with the number of Monte Carlo samples. Then, based on this localized set, we provide statistical inference procedures: a conditional Monte Carlo test of permutation structures with valid finite-sample Type-I error control. We also develop coefficient inference that remains valid under alignment uncertainty of permutations. For computational purposes, we develop a linear assignment problem computable in polynomial time complexity and demonstrate that its solution asymptotically converges to that of the conventional least squares problem with large computational cost. Extensions to partially permuted designs and ridge regularization are also discussed. Extensive simulations and an application to Beijing air-quality data corroborate finite-sample validity, strong power to detect mismatches, and practical scalability.

