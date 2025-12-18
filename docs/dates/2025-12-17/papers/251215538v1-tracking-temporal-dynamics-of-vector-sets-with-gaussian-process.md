---
layout: default
title: Tracking Temporal Dynamics of Vector Sets with Gaussian Process
---

# Tracking Temporal Dynamics of Vector Sets with Gaussian Process
**arXiv**：[2512.15538v1](https://arxiv.org/abs/2512.15538) · [PDF](https://arxiv.org/pdf/2512.15538.pdf)  
**作者**：Taichi Aida, Mamoru Komachi, Toshinobu Ogiso, Hiroya Takamura, Daichi Mochihashi  

**一句话要点**：提出基于高斯过程的向量集时序动态建模方法，用于生态、犯罪和语言等领域分析。

**关键词**：高斯过程建模, 时序向量分析, 随机傅里叶特征, 犯罪分布分析, 词嵌入演化

## 3 点简述
- 核心问题：分析随时间演变的向量集，如生态系统结构、犯罪分布和词嵌入，面临复杂结构变化的挑战。
- 方法要点：使用无限维高斯过程建模向量集分布，通过随机傅里叶特征近似潜在函数，获得紧凑可比的时序向量表示。
- 实验或效果：在犯罪分布和词嵌入数据上验证，方法能捕捉时序动态，提供可解释和稳健的低维可视化表示。

## 摘要（原文）

> Understanding the temporal evolution of sets of vectors is a fundamental challenge across various domains, including ecology, crime analysis, and linguistics. For instance, ecosystem structures evolve due to interactions among plants, herbivores, and carnivores; the spatial distribution of crimes shifts in response to societal changes; and word embedding vectors reflect cultural and semantic trends over time. However, analyzing such time-varying sets of vectors is challenging due to their complicated structures, which also evolve over time. In this work, we propose a novel method for modeling the distribution underlying each set of vectors using infinite-dimensional Gaussian processes. By approximating the latent function in the Gaussian process with Random Fourier Features, we obtain compact and comparable vector representations over time. This enables us to track and visualize temporal transitions of vector sets in a low-dimensional space. We apply our method to both sociological data (crime distributions) and linguistic data (word embeddings), demonstrating its effectiveness in capturing temporal dynamics. Our results show that the proposed approach provides interpretable and robust representations, offering a powerful framework for analyzing structural changes in temporally indexed vector sets across diverse domains.

