---
layout: default
title: From Global to Local: Cluster-Aware Learning for Wi-Fi Fingerprinting Indoor Localisation
---

# From Global to Local: Cluster-Aware Learning for Wi-Fi Fingerprinting Indoor Localisation
**arXiv**：[2601.05650v1](https://arxiv.org/abs/2601.05650) · [PDF](https://arxiv.org/pdf/2601.05650.pdf)  
**作者**：Miguel Matey-Sanz, Joaquín Torres-Sospedra, Joaquín Huerta, Sergio Trilles  

**一句话要点**：提出基于聚类的Wi-Fi指纹室内定位方法，通过结构化数据集提升定位精度

**关键词**：Wi-Fi指纹定位, 聚类学习, 室内定位, 数据集结构化, 机器学习模型

## 3 点简述
- 核心问题：Wi-Fi指纹定位受数据集大小、异质性和信号波动影响，全局模型在大型多楼层环境中精度下降
- 方法要点：使用空间或无线电特征对指纹聚类，定位时基于最强接入点分配至相关集群，在子集上执行定位
- 实验或效果：在三个公共数据集上评估，显示定位误差一致减少，但楼层检测精度可能降低

## 摘要（原文）

> Wi-Fi fingerprinting remains one of the most practical solutions for indoor positioning, however, its performance is often limited by the size and heterogeneity of fingerprint datasets, strong Received Signal Strength Indicator variability, and the ambiguity introduced in large and multi-floor environments. These factors significantly degrade localisation accuracy, particularly when global models are applied without considering structural constraints. This paper introduces a clustering-based method that structures the fingerprint dataset prior to localisation. Fingerprints are grouped using either spatial or radio features, and clustering can be applied at the building or floor level. In the localisation phase, a clustering estimation procedure based on the strongest access points assigns unseen fingerprints to the most relevant cluster. Localisation is then performed only within the selected clusters, allowing learning models to operate on reduced and more coherent subsets of data. The effectiveness of the method is evaluated on three public datasets and several machine learning models. Results show a consistent reduction in localisation errors, particularly under building-level strategies, but at the cost of reducing the floor detection accuracy. These results demonstrate that explicitly structuring datasets through clustering is an effective and flexible approach for scalable indoor positioning.

