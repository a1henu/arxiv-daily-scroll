---
layout: default
title: Generative Modeling with Continuous Flows: Sample Complexity of Flow Matching
---

# Generative Modeling with Continuous Flows: Sample Complexity of Flow Matching
**arXiv**：[2512.01286v1](https://arxiv.org/abs/2512.01286) · [PDF](https://arxiv.org/pdf/2512.01286.pdf)  
**作者**：Mudit Gaur, Prashant Trivedi, Shuchin Aeron, Amrit Singh Bedi, George K. Atia, Vaneet Aggarwal  

**一句话要点**：分析流匹配生成模型的样本复杂度，首次提供无经验风险最小化假设的理论保证。

**关键词**：流匹配, 生成模型, 样本复杂度, Wasserstein距离, 速度场估计, 理论分析

## 3 点简述
- 核心问题：流匹配生成模型缺乏样本复杂度的理论分析，尤其在无经验风险最小化假设下。
- 方法要点：在标准假设下，通过分解速度场估计误差为近似、统计和优化误差，证明神经网络可学习速度场。
- 实验或效果：理论证明使用O(ε⁻⁴)样本，学习分布与真实分布的Wasserstein-2距离小于O(ε)。

## 摘要（原文）

> Flow matching has recently emerged as a promising alternative to diffusion-based generative models, offering faster sampling and simpler training by learning continuous flows governed by ordinary differential equations. Despite growing empirical success, the theoretical understanding of flow matching remains limited, particularly in terms of sample complexity results. In this work, we provide the first analysis of the sample complexity for flow-matching based generative models without assuming access to the empirical risk minimizer (ERM) of the loss function for estimating the velocity field. Under standard assumptions on the loss function for velocity field estimation and boundedness of the data distribution, we show that a sufficiently expressive neural network can learn a velocity field such that with $\mathcal{O}(ε^{-4})$ samples, such that the Wasserstein-2 distance between the learned and the true distribution is less than $\mathcal{O}(ε)$. The key technical idea is to decompose the velocity field estimation error into neural-network approximation error, statistical error due to the finite sample size, and optimization error due to the finite number of optimization steps for estimating the velocity field. Each of these terms are then handled via techniques that may be of independent interest.

