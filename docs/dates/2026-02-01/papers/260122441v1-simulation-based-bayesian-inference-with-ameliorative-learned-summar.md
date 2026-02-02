---
layout: default
title: Simulation-based Bayesian inference with ameliorative learned summary statistics -- Part I
---

# Simulation-based Bayesian inference with ameliorative learned summary statistics -- Part I
**arXiv**：[2601.22441v1](https://arxiv.org/abs/2601.22441) · [PDF](https://arxiv.org/pdf/2601.22441.pdf)  
**作者**：Getachew K. Befekadu  

**一句话要点**：提出基于模拟的贝叶斯推断框架，利用学习摘要统计量作为经验似然，处理难以获得精确似然函数的问题。

**关键词**：模拟推断, 贝叶斯推断, 摘要统计量, 经验似然, 分布式计算, Cressie-Read准则

## 3 点简述
- 核心问题：当观测数据与模拟模型的精确似然函数难以获取或计算不可行时，如何有效进行贝叶斯推断。
- 方法要点：使用Cressie-Read差异准则在矩约束下转换数据为学习摘要统计量，以保持推断统计功效。
- 实验或效果：框架可扩展处理弱依赖观测数据，并适合分布式计算实现，支持大规模数据集。

## 摘要（原文）

> This paper, which is Part 1 of a two-part paper series, considers a simulation-based inference with learned summary statistics, in which such a learned summary statistic serves as an empirical-likelihood with ameliorative effects in the Bayesian setting, when the exact likelihood function associated with the observation data and the simulation model is difficult to obtain in a closed form or computationally intractable. In particular, a transformation technique which leverages the Cressie-Read discrepancy criterion under moment restrictions is used for summarizing the learned statistics between the observation data and the simulation outputs, while preserving the statistical power of the inference. Here, such a transformation of data-to-learned summary statistics also allows the simulation outputs to be conditioned on the observation data, so that the inference task can be performed over certain sample sets of the observation data that are considered as an empirical relevance or believed to be particular importance. Moreover, the simulation-based inference framework discussed in this paper can be extended further, and thus handling weakly dependent observation data. Finally, we remark that such an inference framework is suitable for implementation in distributed computing, i.e., computational tasks involving both the data-to-learned summary statistics and the Bayesian inferencing problem can be posed as a unified distributed inference problem that will exploit distributed optimization and MCMC algorithms for supporting large datasets associated with complex simulation models.

