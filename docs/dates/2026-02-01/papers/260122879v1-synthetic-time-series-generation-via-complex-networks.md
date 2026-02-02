---
layout: default
title: Synthetic Time Series Generation via Complex Networks
---

# Synthetic Time Series Generation via Complex Networks
**arXiv**：[2601.22879v1](https://arxiv.org/abs/2601.22879) · [PDF](https://arxiv.org/pdf/2601.22879.pdf)  
**作者**：Jaime Vale, Vanessa Freitas Silva, Maria Eduarda Silva, Fernando Silva  

**一句话要点**：提出基于分位数图映射的框架，以生成保留统计与结构特性的合成时间序列数据。

**关键词**：合成时间序列生成, 分位数图, 复杂网络映射, 数据增强, 机器学习应用

## 3 点简述
- 核心问题：高质量时间序列数据获取受限，需合成数据以支持机器学习应用。
- 方法要点：将时间序列映射为分位数图，再通过逆映射重构，以生成合成数据。
- 实验或效果：在模拟和真实数据集上评估，与GAN方法相比，提供竞争性且可解释的替代方案。

## 摘要（原文）

> Time series data are essential for a wide range of applications, particularly in developing robust machine learning models. However, access to high-quality datasets is often limited due to privacy concerns, acquisition costs, and labeling challenges. Synthetic time series generation has emerged as a promising solution to address these constraints. In this work, we present a framework for generating synthetic time series by leveraging complex networks mappings. Specifically, we investigate whether time series transformed into Quantile Graphs (QG) -- and then reconstructed via inverse mapping -- can produce synthetic data that preserve the statistical and structural properties of the original. We evaluate the fidelity and utility of the generated data using both simulated and real-world datasets, and compare our approach against state-of-the-art Generative Adversarial Network (GAN) methods. Results indicate that our quantile graph-based methodology offers a competitive and interpretable alternative for synthetic time series generation.

