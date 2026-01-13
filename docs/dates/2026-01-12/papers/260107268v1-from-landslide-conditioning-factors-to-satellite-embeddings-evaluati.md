---
layout: default
title: From Landslide Conditioning Factors to Satellite Embeddings: Evaluating the Utilisation of Google AlphaEarth for Landslide Susceptibility Mapping using Deep Learning
---

# From Landslide Conditioning Factors to Satellite Embeddings: Evaluating the Utilisation of Google AlphaEarth for Landslide Susceptibility Mapping using Deep Learning
**arXiv**：[2601.07268v1](https://arxiv.org/abs/2601.07268) · [PDF](https://arxiv.org/pdf/2601.07268.pdf)  
**作者**：Yusen Cheng, Qinfeng Zhu, Lei Fan  

**一句话要点**：评估Google AlphaEarth嵌入作为滑坡敏感性制图替代预测因子的潜力

**关键词**：滑坡敏感性制图, Google AlphaEarth嵌入, 深度学习, 遥感数据, 地理空间分析

## 3 点简述
- 核心问题：传统滑坡条件因子在可用性、异质性和预处理不确定性方面限制制图可靠性。
- 方法要点：使用Google AlphaEarth嵌入作为统一地表条件表示，与滑坡条件因子对比，采用深度学习模型评估。
- 实验或效果：AE嵌入模型在所有区域和模型中表现更优，F1分数和AUC值提升，空间模式更清晰。

## 摘要（原文）

> Data-driven landslide susceptibility mapping (LSM) typically relies on landslide conditioning factors (LCFs), whose availability, heterogeneity, and preprocessing-related uncertainties can constrain mapping reliability. Recently, Google AlphaEarth (AE) embeddings, derived from multi-source geospatial observations, have emerged as a unified representation of Earth surface conditions. This study evaluated the potential of AE embeddings as alternative predictors for LSM. Two AE representations, including retained principal components and the full set of 64 embedding bands, were systematically compared with conventional LCFs across three study areas (Nantou County, Taiwan; Hong Kong; and part of Emilia-Romagna, Italy) using three deep learning models (CNN1D, CNN2D, and Vision Transformer). Performance was assessed using multiple evaluation metrics, ROC-AUC analysis, error statistics, and spatial pattern assessment. Results showed that AE-based models consistently outperformed LCFs across all regions and models, yielding higher F1-scores, AUC values, and more stable error distributions. Such improvement was most pronounced when using the full 64-band AE representation, with F1-score improvements of approximately 4% to 15% and AUC increased ranging from 0.04 to 0.11, depending on the study area and model. AE-based susceptibility maps also exhibited clearer spatial correspondence with observed landslide occurrences and enhanced sensitivity to localised landslide-prone conditions. Performance improvements were more evident in Nantou and Emilia than in Hong Kong, revealing that closer temporal alignment between AE embeddings and landslide inventories may lead to more effective LSM outcomes. These findings highlight the strong potential of AE embeddings as a standardised and information-rich alternative to conventional LCFs for LSM.

