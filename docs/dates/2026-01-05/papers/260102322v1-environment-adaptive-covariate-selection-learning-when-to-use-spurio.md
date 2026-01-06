---
layout: default
title: Environment-Adaptive Covariate Selection: Learning When to Use Spurious Correlations for Out-of-Distribution Prediction
---

# Environment-Adaptive Covariate Selection: Learning When to Use Spurious Correlations for Out-of-Distribution Prediction
**arXiv**：[2601.02322v1](https://arxiv.org/abs/2601.02322) · [PDF](https://arxiv.org/pdf/2601.02322.pdf)  
**作者**：Shuozhi Zuo, Yixin Wang  

**一句话要点**：提出环境自适应协变量选择算法，以优化分布外预测中协变量的使用策略

**关键词**：分布外预测, 协变量选择, 环境自适应, 虚假关联, 因果推断, 机器学习

## 3 点简述
- 核心问题：传统因果或不变协变量方法在部分原因未观测时，可能因忽略虚假关联而性能不足
- 方法要点：基于协变量分布特征，动态选择环境特定协变量集，并整合先验因果知识作为约束
- 实验或效果：在模拟和应用数据集中，EACS算法在多种分布偏移下优于静态因果、不变和ERM预测器

## 摘要（原文）

> Out-of-distribution (OOD) prediction is often approached by restricting models to causal or invariant covariates, avoiding non-causal spurious associations that may be unstable across environments. Despite its theoretical appeal, this strategy frequently underperforms empirical risk minimization (ERM) in practice. We investigate the source of this gap and show that such failures naturally arise when only a subset of the true causes of the outcome is observed. In these settings, non-causal spurious covariates can serve as informative proxies for unobserved causes and substantially improve prediction, except under distribution shifts that break these proxy relationships. Consequently, the optimal set of predictive covariates is neither universal nor necessarily exhibits invariant relationships with the outcome across all environments, but instead depends on the specific type of shift encountered. Crucially, we observe that different covariate shifts induce distinct, observable signatures in the covariate distribution itself. Moreover, these signatures can be extracted from unlabeled data in the target OOD environment and used to assess when proxy covariates remain reliable and when they fail. Building on this observation, we propose an environment-adaptive covariate selection (EACS) algorithm that maps environment-level covariate summaries to environment-specific covariate sets, while allowing the incorporation of prior causal knowledge as constraints. Across simulations and applied datasets, EACS consistently outperforms static causal, invariant, and ERM-based predictors under diverse distribution shifts.

