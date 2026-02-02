---
layout: default
title: RPWithPrior: Label Differential Privacy in Regression
---

# RPWithPrior: Label Differential Privacy in Regression
**arXiv**：[2601.22625v1](https://arxiv.org/abs/2601.22625) · [PDF](https://arxiv.org/pdf/2601.22625.pdf)  
**作者**：Haixia Liu, Ruifan Huang  

**一句话要点**：提出RPWithPrior方法，在回归任务中实现ε-标签差分隐私，避免离散化并利用先验知识提升性能。

**关键词**：标签差分隐私, 回归分析, 连续随机变量, 先验知识, 隐私保护算法

## 3 点简述
- 核心问题：现有回归方法在ε-标签差分隐私下需离散化输出空间，与现实场景不符，导致性能受限。
- 方法要点：将原始和随机响应建模为连续随机变量，估计最优随机响应区间，设计已知和未知先验的算法。
- 实验或效果：在多个数据集上优于高斯、拉普拉斯、阶梯、RRonBins和无偏机制，验证了方法的有效性。

## 摘要（原文）

> With the wide application of machine learning techniques in practice, privacy preservation has gained increasing attention. Protecting user privacy with minimal accuracy loss is a fundamental task in the data analysis and mining community. In this paper, we focus on regression tasks under $ε$-label differential privacy guarantees. Some existing methods for regression with $ε$-label differential privacy, such as the RR-On-Bins mechanism, discretized the output space into finite bins and then applied RR algorithm. To efficiently determine these finite bins, the authors rounded the original responses down to integer values. However, such operations does not align well with real-world scenarios. To overcome these limitations, we model both original and randomized responses as continuous random variables, avoiding discretization entirely. Our novel approach estimates an optimal interval for randomized responses and introduces new algorithms designed for scenarios where a prior is either known or unknown. Additionally, we prove that our algorithm, RPWithPrior, guarantees $ε$-label differential privacy. Numerical results demonstrate that our approach gets better performance compared with the Gaussian, Laplace, Staircase, and RRonBins, Unbiased mechanisms on the Communities and Crime, Criteo Sponsored Search Conversion Log, California Housing datasets.

