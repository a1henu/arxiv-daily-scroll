---
layout: default
title: Distribution-Free Robust Functional Predict-Then-Optimize
---

# Distribution-Free Robust Functional Predict-Then-Optimize
**arXiv**：[2602.08215v1](https://arxiv.org/abs/2602.08215) · [PDF](https://arxiv.org/pdf/2602.08215.pdf)  
**作者**：Yash Patel, Ambuj Tewari  

**一句话要点**：提出基于保形预测的分布无关不确定性量化方法，用于神经算子代理模型在决策任务中的鲁棒优化。

**关键词**：保形预测, 神经算子, 不确定性量化, 鲁棒优化, 函数空间, 决策任务

## 3 点简述
- 核心问题：神经算子代理模型缺乏校准的不确定性量化，现有方法依赖分布假设或可扩展性不足。
- 方法要点：应用保形预测在函数空间进行分布无关不确定性量化，结合Danskin定理和变分法实现鲁棒决策优化。
- 实验或效果：在多个工程任务中，该方法优于高斯过程等限制性模型，提供正式后悔表征。

## 摘要（原文）

> The solution of PDEs in decision-making tasks is increasingly being undertaken with the help of neural operator surrogate models due to the need for repeated evaluation. Such methods, while significantly more computationally favorable compared to their numerical counterparts, fail to provide any calibrated notions of uncertainty in their predictions. Current methods approach this deficiency typically with ensembling or Bayesian posterior estimation. However, these approaches either require distributional assumptions that fail to hold in practice or lack practical scalability, limiting their applications in practice. We, therefore, propose a novel application of conformal prediction to produce distribution-free uncertainty quantification over the function spaces mapped by neural operators. We then demonstrate how such prediction regions enable a formal regret characterization if leveraged in downstream robust decision-making tasks. We further demonstrate how such posited robust decision-making tasks can be efficiently solved using an infinite-dimensional generalization of Danskin's Theorem and calculus of variations and empirically demonstrate the superior performance of our proposed method over more restrictive modeling paradigms, such as Gaussian Processes, across several engineering tasks.

