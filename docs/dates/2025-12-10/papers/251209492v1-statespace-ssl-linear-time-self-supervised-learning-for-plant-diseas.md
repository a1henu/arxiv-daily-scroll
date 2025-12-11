---
layout: default
title: StateSpace-SSL: Linear-Time Self-supervised Learning for Plant Disease Detectio
---

# StateSpace-SSL: Linear-Time Self-supervised Learning for Plant Disease Detectio
**arXiv**：[2512.09492v1](https://arxiv.org/abs/2512.09492) · [PDF](https://arxiv.org/pdf/2512.09492.pdf)  
**作者**：Abdullah Al Mamun, Miaohua Zhang, David Ahmedt-Aristizabal, Zeeshan Hayder, Mohammad Awrangjeb  

**一句话要点**：提出StateSpace-SSL线性时间自监督学习框架，用于植物病害检测

**关键词**：植物病害检测, 自监督学习, 状态空间模型, 线性时间计算, 特征表示学习

## 3 点简述
- 现有CNN和Transformer自监督方法难以捕捉叶片病害连续模式或计算成本高
- 采用Vision Mamba状态空间编码器，通过定向扫描建模长程病变连续性
- 在三个公开数据集上优于基线，学习到紧凑、病变聚焦的特征图

## 摘要（原文）

> Self-supervised learning (SSL) is attractive for plant disease detection as it can exploit large collections of unlabeled leaf images, yet most existing SSL methods are built on CNNs or vision transformers that are poorly matched to agricultural imagery. CNN-based SSL struggles to capture disease patterns that evolve continuously along leaf structures, while transformer-based SSL introduces quadratic attention cost from high-resolution patches. To address these limitations, we propose StateSpace-SSL, a linear-time SSL framework that employs a Vision Mamba state-space encoder to model long-range lesion continuity through directional scanning across the leaf surface. A prototype-driven teacher-student objective aligns representations across multiple views, encouraging stable and lesion-aware features from labelled data. Experiments on three publicly available plant disease datasets show that StateSpace-SSL consistently outperforms the CNN- and transformer-based SSL baselines in various evaluation metrics. Qualitative analyses further confirm that it learns compact, lesion-focused feature maps, highlighting the advantage of linear state-space modelling for self-supervised plant disease representation learning.

