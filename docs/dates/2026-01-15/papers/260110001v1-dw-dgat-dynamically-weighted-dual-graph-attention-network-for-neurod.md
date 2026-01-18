---
layout: default
title: DW-DGAT: Dynamically Weighted Dual Graph Attention Network for Neurodegenerative Disease Diagnosis
---

# DW-DGAT: Dynamically Weighted Dual Graph Attention Network for Neurodegenerative Disease Diagnosis
**arXiv**：[2601.10001v1](https://arxiv.org/abs/2601.10001) · [PDF](https://arxiv.org/pdf/2601.10001.pdf)  
**作者**：Chengjia Liang, Zhenjiong Wang, Chao Chen, Ruizhi Zhang, Songxi Liang, Hai Xie, Haijun Lei, Zhongwei Huang  

**一句话要点**：提出动态加权双图注意力网络，用于神经退行性疾病早期诊断。

**关键词**：神经退行性疾病诊断, 图注意力网络, 多模态数据融合, 类别不平衡处理, 脑影像分析

## 3 点简述
- 核心问题：多模态数据高维异构与类别不平衡，阻碍帕金森病和阿尔茨海默病早期诊断。
- 方法要点：融合多结构数据，基于脑区和样本关系构建双图注意力，动态生成类别权重。
- 实验或效果：在PPMI和ADNI数据集上验证，性能达到先进水平。

## 摘要（原文）

> Parkinson's disease (PD) and Alzheimer's disease (AD) are the two most prevalent and incurable neurodegenerative diseases (NDs) worldwide, for which early diagnosis is critical to delay their progression. However, the high dimensionality of multi-metric data with diverse structural forms, the heterogeneity of neuroimaging and phenotypic data, and class imbalance collectively pose significant challenges to early ND diagnosis. To address these challenges, we propose a dynamically weighted dual graph attention network (DW-DGAT) that integrates: (1) a general-purpose data fusion strategy to merge three structural forms of multi-metric data; (2) a dual graph attention architecture based on brain regions and inter-sample relationships to extract both micro- and macro-level features; and (3) a class weight generation mechanism combined with two stable and effective loss functions to mitigate class imbalance. Rigorous experiments, based on the Parkinson Progression Marker Initiative (PPMI) and Alzhermer's Disease Neuroimaging Initiative (ADNI) studies, demonstrate the state-of-the-art performance of our approach.

