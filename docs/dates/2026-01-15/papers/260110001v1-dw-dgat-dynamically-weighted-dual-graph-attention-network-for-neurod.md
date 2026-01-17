---
layout: default
title: DW-DGAT: Dynamically Weighted Dual Graph Attention Network for Neurodegenerative Disease Diagnosis
---

# DW-DGAT: Dynamically Weighted Dual Graph Attention Network for Neurodegenerative Disease Diagnosis
**arXiv**：[2601.10001v1](https://arxiv.org/abs/2601.10001) · [PDF](https://arxiv.org/pdf/2601.10001.pdf)  
**作者**：Chengjia Liang, Zhenjiong Wang, Chao Chen, Ruizhi Zhang, Songxi Liang, Hai Xie, Haijun Lei, Zhongwei Huang  

**一句话要点**：提出动态加权双图注意力网络以解决神经退行性疾病早期诊断中的多模态数据融合与类别不平衡问题。

**关键词**：神经退行性疾病诊断, 多模态数据融合, 图注意力网络, 类别不平衡处理, 脑影像分析

## 3 点简述
- 核心问题：帕金森病和阿尔茨海默病的早期诊断面临多模态数据高维异构和类别不平衡的挑战。
- 方法要点：采用通用数据融合策略、基于脑区和样本关系的双图注意力架构，以及类别权重生成机制。
- 实验或效果：在PPMI和ADNI数据集上验证了方法的先进性能，实现了状态-of-the-art的诊断效果。

## 摘要（原文）

> Parkinson's disease (PD) and Alzheimer's disease (AD) are the two most prevalent and incurable neurodegenerative diseases (NDs) worldwide, for which early diagnosis is critical to delay their progression. However, the high dimensionality of multi-metric data with diverse structural forms, the heterogeneity of neuroimaging and phenotypic data, and class imbalance collectively pose significant challenges to early ND diagnosis. To address these challenges, we propose a dynamically weighted dual graph attention network (DW-DGAT) that integrates: (1) a general-purpose data fusion strategy to merge three structural forms of multi-metric data; (2) a dual graph attention architecture based on brain regions and inter-sample relationships to extract both micro- and macro-level features; and (3) a class weight generation mechanism combined with two stable and effective loss functions to mitigate class imbalance. Rigorous experiments, based on the Parkinson Progression Marker Initiative (PPMI) and Alzhermer's Disease Neuroimaging Initiative (ADNI) studies, demonstrate the state-of-the-art performance of our approach.

