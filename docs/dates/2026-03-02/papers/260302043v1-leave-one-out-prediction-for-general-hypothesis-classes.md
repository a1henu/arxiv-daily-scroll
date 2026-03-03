---
layout: default
title: Leave-One-Out Prediction for General Hypothesis Classes
---

# Leave-One-Out Prediction for General Hypothesis Classes
**arXiv**：[2603.02043v1](https://arxiv.org/abs/2603.02043) · [PDF](https://arxiv.org/pdf/2603.02043.pdf)  
**作者**：Jian Qian, Jiachen Xu  

**一句话要点**：提出中位数水平集聚合方法，为一般假设类的留一预测提供泛化保证

**关键词**：留一预测, 转导学习, 泛化保证, 经验风险最小化, 水平集分析, 复杂度缩放

## 3 点简述
- 研究留一预测在完全转导设置下的泛化保证问题，现有理论局限于特定模型
- 引入基于经验风险水平集的中位数水平集聚合方法，建立乘性oracle不等式
- 在VC类、有限假设类、逻辑回归等典型设置中验证复杂度缩放性质

## 摘要（原文）

> Leave-one-out (LOO) prediction provides a principled, data-dependent measure of generalization, yet guarantees in fully transductive settings remain poorly understood beyond specialized models. We introduce Median of Level-Set Aggregation (MLSA), a general aggregation procedure based on empirical-risk level sets around the ERM. For arbitrary fixed datasets and losses satisfying a mild monotonicity condition, we establish a multiplicative oracle inequality for the LOO error of the form \[ LOO_S(\hat{h}) \;\le\; C \cdot \frac{1}{n} \min_{h\in H} L_S(h) \;+\; \frac{Comp(S,H,\ell)}{n}, \qquad C>1. \]
>   The analysis is based on a local level-set growth condition controlling how the set of near-optimal empirical-risk minimizers expands as the tolerance increases. We verify this condition in several canonical settings. For classification with VC classes under the 0-1 loss, the resulting complexity scales as $O(d \log n)$, where $d$ is the VC dimension. For finite hypothesis and density classes under bounded or log loss, it scales as $O(\log \|H\|)$ and $O(\log \|P\|)$, respectively. For logistic regression with bounded covariates and parameters, a volumetric argument based on the empirical covariance matrix yields complexity scaling as $O(d \log n)$ up to problem-dependent factors.

