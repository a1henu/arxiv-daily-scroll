---
layout: default
title: genriesz: A Python Package for Automatic Debiased Machine Learning with Generalized Riesz Regression
---

# genriesz: A Python Package for Automatic Debiased Machine Learning with Generalized Riesz Regression
**arXiv**：[2602.17543v1](https://arxiv.org/abs/2602.17543) · [PDF](https://arxiv.org/pdf/2602.17543.pdf)  
**作者**：Masahiro Kato  

**一句话要点**：提出genriesz Python包，通过广义Riesz回归实现自动去偏机器学习，用于因果和结构参数估计。

**关键词**：去偏机器学习, Riesz回归, 因果推断, Python包, 参数估计, 自动平衡

## 3 点简述
- 核心问题：自动化估计因果和结构参数，需处理去偏和Riesz表示器计算。
- 方法要点：基于Bregman散度最小化统一框架，自动构建兼容链接函数实现平衡最优条件。
- 实验或效果：提供模块化接口，支持多种估计器，应用于ATE、ATT等典型问题，开源可用。

## 摘要（原文）

> Efficient estimation of causal and structural parameters can be automated using the Riesz representation theorem and debiased machine learning (DML). We present genriesz, an open-source Python package that implements automatic DML and generalized Riesz regression, a unified framework for estimating Riesz representers by minimizing empirical Bregman divergences. This framework includes covariate balancing, nearest-neighbor matching, calibrated estimation, and density ratio estimation as special cases. A key design principle of the package is automatic regressor balancing (ARB): given a Bregman generator $g$ and a representer model class, genriesz} automatically constructs a compatible link function so that the generalized Riesz regression estimator satisfies balancing (moment-matching) optimality conditions in a user-chosen basis. The package provides a modulr interface for specifying (i) the target linear functional via a black-box evaluation oracle, (ii) the representer model via basis functions (polynomial, RKHS approximations, random forest leaf encodings, neural embeddings, and a nearest-neighbor catchment basis), and (iii) the Bregman generator, with optional user-supplied derivatives. It returns regression adjustment (RA), Riesz weighting (RW), augmented Riesz weighting (ARW), and TMLE-style estimators with cross-fitting, confidence intervals, and $p$-values. We highlight representative workflows for estimation problems such as the average treatment effect (ATE), ATE on treated (ATT), and average marginal effect estimation. The Python package is available at https://github.com/MasaKat0/genriesz and on PyPI.

