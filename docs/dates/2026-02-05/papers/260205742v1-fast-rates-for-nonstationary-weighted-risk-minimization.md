---
layout: default
title: Fast Rates for Nonstationary Weighted Risk Minimization
---

# Fast Rates for Nonstationary Weighted Risk Minimization
**arXiv**：[2602.05742v1](https://arxiv.org/abs/2602.05742) · [PDF](https://arxiv.org/pdf/2602.05742.pdf)  
**作者**：Tobias Brock, Thomas Nagler  

**一句话要点**：提出加权经验风险最小化的非平稳性误差分解与学习界，以解决分布漂移下的预测问题。

**关键词**：加权经验风险最小化, 分布漂移, 非平稳性, 学习界, 回归问题, 神经网络

## 3 点简述
- 研究加权经验风险最小化在非平稳分布下的样本外预测误差。
- 提供超额风险的通用分解为学习项和分布漂移误差项，并在混合条件下证明学习界。
- 在线性模型、基逼近和神经网络回归中验证结果，恢复极小极大最优率。

## 摘要（原文）

> Weighted empirical risk minimization is a common approach to prediction under distribution drift. This article studies its out-of-sample prediction error under nonstationarity. We provide a general decomposition of the excess risk into a learning term and an error term associated with distribution drift, and prove oracle inequalities for the learning error under mixing conditions. The learning bound holds uniformly over arbitrary weight classes and accounts for the effective sample size induced by the weight vector, the complexity of the weight and hypothesis classes, and potential data dependence. We illustrate the applicability and sharpness of our results in (auto-) regression problems with linear models, basis approximations, and neural networks, recovering minimax-optimal rates (up to logarithmic factors) when specialized to unweighted and stationary settings.

