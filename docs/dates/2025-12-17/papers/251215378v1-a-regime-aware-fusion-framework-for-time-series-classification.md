---
layout: default
title: A Regime-Aware Fusion Framework for Time Series Classification
---

# A Regime-Aware Fusion Framework for Time Series Classification
**arXiv**：[2512.15378v1](https://arxiv.org/abs/2512.15378) · [PDF](https://arxiv.org/pdf/2512.15378.pdf)  
**作者**：Honey Singh Chauhan, Zahraa S. Abdallah  

**一句话要点**：提出Fusion-3框架，通过自适应融合多种表示以提升特定数据集上的时间序列分类性能。

**关键词**：时间序列分类, 表示融合, 元特征聚类, 自适应框架, 核方法

## 3 点简述
- 核心问题：Rocket等核方法在时间序列分类中表现不一致，需针对性改进。
- 方法要点：基于元特征聚类数据集，自适应融合Rocket、Sax和Sfa表示。
- 实验或效果：在UCR数据集上，F3在结构化变异性或丰富频率内容的数据集中表现更优。

## 摘要（原文）

> Kernel-based methods such as Rocket are among the most effective default approaches for univariate time series classification (TSC), yet they do not perform equally well across all datasets. We revisit the long-standing intuition that different representations capture complementary structure and show that selectively fusing them can yield consistent improvements over Rocket on specific, systematically identifiable kinds of datasets. We introduce Fusion-3 (F3), a lightweight framework that adaptively fuses Rocket, Sax, and Sfa representations. To understand when fusion helps, we cluster UCR datasets into six groups using meta-features capturing series length, spectral structure, roughness, and class imbalance, and treat these clusters as interpretable data-structure regimes. Our analysis shows that fusion typically outperforms strong baselines in regimes with structured variability or rich frequency content, while offering diminishing returns in highly irregular or outlier-heavy settings. To support these findings, we combine three complementary analyses: non-parametric paired statistics across datasets, ablation studies isolating the roles of individual representations, and attribution via SHAP to identify which dataset properties predict fusion gains. Sample-level case studies further reveal the underlying mechanism: fusion primarily improves performance by rescuing specific errors, with adaptive increases in frequency-domain weighting precisely where corrections occur. Using 5-fold cross-validation on the 113 UCR datasets, F3 yields small but consistent average improvements over Rocket, supported by frequentist and Bayesian evidence and accompanied by clearly identifiable failure cases. Our results show that selectively applied fusion provides dependable and interpretable extension to strong kernel-based methods, correcting their weaknesses precisely where the data support it.

