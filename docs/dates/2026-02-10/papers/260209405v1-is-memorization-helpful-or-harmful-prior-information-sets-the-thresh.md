---
layout: default
title: Is Memorization Helpful or Harmful? Prior Information Sets the Threshold
---

# Is Memorization Helpful or Harmful? Prior Information Sets the Threshold
**arXiv**：[2602.09405v1](https://arxiv.org/abs/2602.09405) · [PDF](https://arxiv.org/pdf/2602.09405.pdf)  
**作者**：Chen Cheng, Rina Foygel Barber  

**一句话要点**：在贝叶斯过参数化线性模型中，基于先验分布分析训练误差与泛化误差的关系，确定记忆化必要或有害的阈值条件。

**关键词**：贝叶斯线性模型, 过参数化, 泛化误差, 先验分布, Fisher信息, 记忆化阈值

## 3 点简述
- 核心问题：探讨训练误差与泛化误差在过参数化线性模型中的联系，关注记忆化（过拟合）对泛化的影响。
- 方法要点：在贝叶斯框架下，利用先验分布π的固有因素，推导出基于Fisher信息和先验方差的阈值条件。
- 实验或效果：给出明确条件，当噪声达到阈值时，最优泛化需要训练误差接近噪声水平或接近插值状态。

## 摘要（原文）

> We examine the connection between training error and generalization error for arbitrary estimating procedures, working in an overparameterized linear model under general priors in a Bayesian setup. We find determining factors inherent to the prior distribution $π$, giving explicit conditions under which optimal generalization necessitates that the training error be (i) near interpolating relative to the noise size (i.e., memorization is necessary), or (ii) close to the noise level (i.e., overfitting is harmful). Remarkably, these phenomena occur when the noise reaches thresholds determined by the Fisher information and the variance parameters of the prior $π$.

