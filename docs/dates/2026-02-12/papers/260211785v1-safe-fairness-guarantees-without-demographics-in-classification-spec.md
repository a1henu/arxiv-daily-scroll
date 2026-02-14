---
layout: default
title: Safe Fairness Guarantees Without Demographics in Classification: Spectral Uncertainty Set Perspective
---

# Safe Fairness Guarantees Without Demographics in Classification: Spectral Uncertainty Set Perspective
**arXiv**：[2602.11785v1](https://arxiv.org/abs/2602.11785) · [PDF](https://arxiv.org/pdf/2602.11785.pdf)  
**作者**：Ainhize Barrainkua, Santiago Mazuelas, Novi Quadrianto, Jose A. Lozano  

**一句话要点**：提出SPECTRE方法，通过谱调整优化无人口统计信息分类的公平性保证

**关键词**：公平机器学习, 无人口统计公平性, 鲁棒优化, 谱调整, 极小极大方法, 分类系统

## 3 点简述
- 核心问题：现有公平性方法依赖人口统计信息，实践中难以获取，且鲁棒优化易受异常值影响
- 方法要点：SPECTRE采用极小极大公平策略，调整傅里叶特征映射谱，约束最坏分布与经验分布的偏差
- 实验或效果：在ACS数据集上验证，SPECTRE提供最高平均公平保证和最小四分位距，优于现有方法

## 摘要（原文）

> As automated classification systems become increasingly prevalent, concerns have emerged over their potential to reinforce and amplify existing societal biases. In the light of this issue, many methods have been proposed to enhance the fairness guarantees of classifiers. Most of the existing interventions assume access to group information for all instances, a requirement rarely met in practice. Fairness without access to demographic information has often been approached through robust optimization techniques,which target worst-case outcomes over a set of plausible distributions known as the uncertainty set. However, their effectiveness is strongly influenced by the chosen uncertainty set. In fact, existing approaches often overemphasize outliers or overly pessimistic scenarios, compromising both overall performance and fairness. To overcome these limitations, we introduce SPECTRE, a minimax-fair method that adjusts the spectrum of a simple Fourier feature mapping and constrains the extent to which the worst-case distribution can deviate from the empirical distribution. We perform extensive experiments on the American Community Survey datasets involving 20 states. The safeness of SPECTRE comes as it provides the highest average values on fairness guarantees together with the smallest interquartile range in comparison to state-of-the-art approaches, even compared to those with access to demographic group information. In addition, we provide a theoretical analysis that derives computable bounds on the worst-case error for both individual groups and the overall population, as well as characterizes the worst-case distributions responsible for these extremal performances

