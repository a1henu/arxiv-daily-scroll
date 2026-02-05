---
layout: default
title: A principled framework for uncertainty decomposition in TabPFN
---

# A principled framework for uncertainty decomposition in TabPFN
**arXiv**：[2602.04596v1](https://arxiv.org/abs/2602.04596) · [PDF](https://arxiv.org/pdf/2602.04596.pdf)  
**作者**：Sandra Fortini, Kenyon Ng, Sonia Petrone, Judith Rousseau, Susan Wei  

**一句话要点**：提出TabPFN的不确定性分解框架，基于贝叶斯预测推断解决监督表格任务中的不确定性量化问题。

**关键词**：不确定性分解, 贝叶斯预测推断, 监督表格学习, Transformer模型, 预测中心极限定理, 认知不确定性

## 3 点简述
- TabPFN作为Transformer模型，在监督表格任务中表现优异，但缺乏不确定性分解方法。
- 将分解问题建模为贝叶斯预测推断，通过证明预测中心极限定理，推导基于预测更新波动的方差估计器。
- 所得可信带快速计算，针对认知不确定性，在分类任务中实现基于熵的分解，达到接近名义频率覆盖。

## 摘要（原文）

> TabPFN is a transformer that achieves state-of-the-art performance on supervised tabular tasks by amortizing Bayesian prediction into a single forward pass. However, there is currently no method for uncertainty decomposition in TabPFN. Because it behaves, in an idealised limit, as a Bayesian in-context learner, we cast the decomposition challenge as a Bayesian predictive inference (BPI) problem. The main computational tool in BPI, predictive Monte Carlo, is challenging to apply here as it requires simulating unmodeled covariates. We therefore pursue the asymptotic alternative, filling a gap in the theory for supervised settings by proving a predictive CLT under quasi-martingale conditions. We derive variance estimators determined by the volatility of predictive updates along the context. The resulting credible bands are fast to compute, target epistemic uncertainty, and achieve near-nominal frequentist coverage. For classification, we further obtain an entropy-based uncertainty decomposition.

