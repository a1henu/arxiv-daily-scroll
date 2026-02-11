---
layout: default
title: Measuring Dataset Diversity from a Geometric Perspective
---

# Measuring Dataset Diversity from a Geometric Perspective
**arXiv**：[2602.09340v1](https://arxiv.org/abs/2602.09340) · [PDF](https://arxiv.org/pdf/2602.09340.pdf)  
**作者**：Yang Ba, Mohammad Sadeq Abolhasani, Michelle V Mancenido, Rong Pan  

**一句话要点**：提出基于拓扑数据分析的几何多样性度量框架，以量化数据集的结构丰富性

**关键词**：数据集多样性, 拓扑数据分析, 持久性景观, 几何结构, 度量框架, 数据集评估

## 3 点简述
- 现有多样性度量主要关注统计变异，忽略几何结构，导致评估不全面
- 引入持久性景观从拓扑数据中提取几何特征，提供理论基础的多样性度量
- 通过多模态实验验证PLDiv的可靠性、可解释性，适用于数据集构建与评估

## 摘要（原文）

> Diversity can be broadly defined as the presence of meaningful variation across elements, which can be viewed from multiple perspectives, including statistical variation and geometric structural richness in the dataset. Existing diversity metrics, such as feature-space dispersion and metric-space magnitude, primarily capture distributional variation or entropy, while largely neglecting the geometric structure of datasets. To address this gap, we introduce a framework based on topological data analysis (TDA) and persistence landscapes (PLs) to extract and quantify geometric features from data. This approach provides a theoretically grounded means of measuring diversity beyond entropy, capturing the rich geometric and structural properties of datasets. Through extensive experiments across diverse modalities, we demonstrate that our proposed PLs-based diversity metric (PLDiv) is powerful, reliable, and interpretable, directly linking data diversity to its underlying geometry and offering a foundational tool for dataset construction, augmentation, and evaluation.

