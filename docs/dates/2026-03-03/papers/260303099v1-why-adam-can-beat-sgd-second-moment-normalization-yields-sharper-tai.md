---
layout: default
title: Why Adam Can Beat SGD: Second-Moment Normalization Yields Sharper Tails
---

# Why Adam Can Beat SGD: Second-Moment Normalization Yields Sharper Tails
**arXiv**：[2603.03099v1](https://arxiv.org/abs/2603.03099) · [PDF](https://arxiv.org/pdf/2603.03099.pdf)  
**作者**：Ruinan Jin, Yingbin Liang, Shaofeng Zou  

**一句话要点**：揭示Adam二阶矩归一化机制，理论区分其与SGD的高概率收敛行为

**关键词**：Adam优化器, SGD优化器, 二阶矩归一化, 高概率收敛, 停时分析, 有界方差模型

## 3 点简述
- 核心问题：现有理论未能充分解释Adam相比SGD的实证性能优势
- 方法要点：基于二阶矩归一化，采用停时/鞅分析，在经典有界方差模型下证明理论分离
- 实验或效果：Adam对置信参数δ的依赖为δ^{-1/2}，优于SGD的至少δ^{-1}依赖

## 摘要（原文）

> Despite Adam demonstrating faster empirical convergence than SGD in many applications, much of the existing theory yields guarantees essentially comparable to those of SGD, leaving the empirical performance gap insufficiently explained. In this paper, we uncover a key second-moment normalization in Adam and develop a stopping-time/martingale analysis that provably distinguishes Adam from SGD under the classical bounded variance model (a second moment assumption). In particular, we establish the first theoretical separation between the high-probability convergence behaviors of the two methods: Adam achieves a $δ^{-1/2}$ dependence on the confidence parameter $δ$, whereas corresponding high-probability guarantee for SGD necessarily incurs at least a $δ^{-1}$ dependence.

