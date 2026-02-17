---
layout: default
title: Multi-dimensional Persistent Sheaf Laplacians for Image Analysis
---

# Multi-dimensional Persistent Sheaf Laplacians for Image Analysis
**arXiv**：[2602.14846v1](https://arxiv.org/abs/2602.14846) · [PDF](https://arxiv.org/pdf/2602.14846.pdf)  
**作者**：Xiang Xiang Wang, Guo-Wei Wei  

**一句话要点**：提出多维持续层拉普拉斯框架以提升图像分析稳定性

**关键词**：图像分析, 拓扑数据分析, 持续同调, 降维方法, 单纯复形, 分类任务

## 3 点简述
- 核心问题：传统降维方法对降维维度选择敏感，影响性能稳定性。
- 方法要点：利用多维度互补优势，基于单纯复形构建持续层拉普拉斯提取多尺度局部拓扑谱表示。
- 实验或效果：在COIL20和ETH80数据集上验证，性能更稳定且优于PCA基线。

## 摘要（原文）

> We propose a multi-dimensional persistent sheaf Laplacian (MPSL) framework on simplicial complexes for image analysis. The proposed method is motivated by the strong sensitivity of commonly used dimensionality reduction techniques, such as principal component analysis (PCA), to the choice of reduced dimension. Rather than selecting a single reduced dimension or averaging results across dimensions, we exploit complementary advantages of multiple reduced dimensions. At a given dimension, image samples are regarded as simplicial complexes, and persistent sheaf Laplacians are utilized to extract a multiscale localized topological spectral representation for individual image samples. Statistical summaries of the resulting spectra are then aggregated across scales and dimensions to form multiscale multi-dimensional image representations. We evaluate the proposed framework on the COIL20 and ETH80 image datasets using standard classification protocols. Experimental results show that the proposed method provides more stable performance across a wide range of reduced dimensions and achieves consistent improvements to PCA-based baselines in moderate dimensional regimes.

