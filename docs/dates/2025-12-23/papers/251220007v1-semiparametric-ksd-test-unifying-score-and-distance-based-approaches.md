---
layout: default
title: Semiparametric KSD test: unifying score and distance-based approaches for goodness-of-fit testing
---

# Semiparametric KSD test: unifying score and distance-based approaches for goodness-of-fit testing
**arXiv**：[2512.20007v1](https://arxiv.org/abs/2512.20007) · [PDF](https://arxiv.org/pdf/2512.20007.pdf)  
**作者**：Zhihan Huang, Ziang Niu  

**一句话要点**：提出半参数核化Stein差异检验，统一基于分数和距离的拟合优度测试方法。

**关键词**：拟合优度测试, 分数方法, 积分概率度量, 核化Stein差异, 非参数检验, 模型评估

## 3 点简述
- 核心问题：拟合优度测试中，基于分数的方法难以扩展到非参数替代，因缺乏合适分数函数。
- 方法要点：通过指数倾斜模型，将分数测试与积分概率度量统一，提出基于核化Stein函数类的半参数检验。
- 实验或效果：SKSD检验计算高效，支持通用参数估计，在通用非参数替代下具有一致性和Pitman效率。

## 摘要（原文）

> Goodness-of-fit (GoF) tests are fundamental for assessing model adequacy. Score-based tests are appealing because they require fitting the model only once under the null. However, extending them to powerful nonparametric alternatives is difficult due to the lack of suitable score functions. Through a class of exponentially tilted models, we show that the resulting score-based GoF tests are equivalent to the tests based on integral probability metrics (IPMs) indexed by a function class. When the class is rich, the test is universally consistent. This simple yet insightful perspective enables reinterpretation of classical distance-based testing procedures-including those based on Kolmogorov-Smirnov distance, Wasserstein-1 distance, and maximum mean discrepancy-as arising from score-based constructions. Building on this insight, we propose a new nonparametric score-based GoF test through a special class of IPM induced by kernelized Stein's function class, called semiparametric kernelized Stein discrepancy (SKSD) test. Compared with other nonparametric score-based tests, the SKSD test is computationally efficient and accommodates general nuisance-parameter estimators, supported by a generic parametric bootstrap procedure. The SKSD test is universally consistent and attains Pitman efficiency. Moreover, SKSD test provides simple GoF tests for models with intractable likelihoods but tractable scores with the help of Stein's identity and we use two popular models, kernel exponential family and conditional Gaussian models, to illustrate the power of our method. Our method achieves power comparable to task-specific normality tests such as Anderson-Darling and Lilliefors, despite being designed for general nonparametric alternatives.

