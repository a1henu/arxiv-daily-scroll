---
layout: default
title: Data-Driven Conditional Flexibility Index
---

# Data-Driven Conditional Flexibility Index
**arXiv**：[2601.16028v1](https://arxiv.org/abs/2601.16028) · [PDF](https://arxiv.org/pdf/2601.16028.pdf)  
**作者**：Moritz Wedemeyer, Eike Cramer, Alexander Mitsos, Manuel Dahmen  

**一句话要点**：提出条件灵活性指数以利用历史数据和上下文信息改进过程调度决策。

**关键词**：条件灵活性指数, 数据驱动不确定性集, 归一化流, 过程调度, 安全约束机组组合

## 3 点简述
- 核心问题：传统灵活性指数未考虑上下文信息如预测，导致不确定性集定义不精确。
- 方法要点：通过归一化流学习数据驱动的参数化不确定性集，并使其条件化于上下文。
- 实验或效果：应用于安全约束机组组合示例，证明能提高调度质量，但性能提升非绝对。

## 摘要（原文）

> With the increasing flexibilization of processes, determining robust scheduling decisions has become an important goal. Traditionally, the flexibility index has been used to identify safe operating schedules by approximating the admissible uncertainty region using simple admissible uncertainty sets, such as hypercubes. Presently, available contextual information, such as forecasts, has not been considered to define the admissible uncertainty set when determining the flexibility index. We propose the conditional flexibility index (CFI), which extends the traditional flexibility index in two ways: by learning the parametrized admissible uncertainty set from historical data and by using contextual information to make the admissible uncertainty set conditional. This is achieved using a normalizing flow that learns a bijective mapping from a Gaussian base distribution to the data distribution. The admissible latent uncertainty set is constructed as a hypersphere in the latent space and mapped to the data space. By incorporating contextual information, the CFI provides a more informative estimate of flexibility by defining admissible uncertainty sets in regions that are more likely to be relevant under given conditions. Using an illustrative example, we show that no general statement can be made about data-driven admissible uncertainty sets outperforming simple sets, or conditional sets outperforming unconditional ones. However, both data-driven and conditional admissible uncertainty sets ensure that only regions of the uncertain parameter space containing realizations are considered. We apply the CFI to a security-constrained unit commitment example and demonstrate that the CFI can improve scheduling quality by incorporating temporal information.

