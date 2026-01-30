---
layout: default
title: Embracing Aleatoric Uncertainty in Medical Multimodal Learning with Missing Modalities
---

# Embracing Aleatoric Uncertainty in Medical Multimodal Learning with Missing Modalities
**arXiv**：[2601.21950v1](https://arxiv.org/abs/2601.21950) · [PDF](https://arxiv.org/pdf/2601.21950.pdf)  
**作者**：Linxiao Gong, Yang Liu, Lianlong Sun, Yulai Bi, Jing Liu, Xiaoguang Zhu  

**一句话要点**：提出Aleatoric Uncertainty Modeling以解决医学多模态学习中缺失模态的问题

**关键词**：医学多模态学习, 缺失模态处理, 偶然不确定性建模, 动态消息传递, 不确定性感知聚合

## 3 点简述
- 核心问题：医学多模态学习面临缺失模态挑战，现有方法忽略数据采集的固有不确定性。
- 方法要点：通过建模单模态表示为多元高斯分布，量化偶然不确定性，并基于不确定性动态聚合信息。
- 实验或效果：在MIMIC-IV和eICU数据集上，AUC-ROC分别提升2.26%和2.17%，优于现有方法。

## 摘要（原文）

> Medical multimodal learning faces significant challenges with missing modalities prevalent in clinical practice. Existing approaches assume equal contribution of modality and random missing patterns, neglecting inherent uncertainty in medical data acquisition. In this regard, we propose the Aleatoric Uncertainty Modeling (AUM) that explicitly quantifies unimodal aleatoric uncertainty to address missing modalities. Specifically, AUM models each unimodal representation as a multivariate Gaussian distribution to capture aleatoric uncertainty and enable principled modality reliability quantification. To adaptively aggregate captured information, we develop a dynamic message-passing mechanism within a bipartite patient-modality graph using uncertainty-aware aggregation mechanism. Through this process, missing modalities are naturally accommodated, while more reliable information from available modalities is dynamically emphasized to guide representation generation. Our AUM framework achieves an improvement of 2.26% AUC-ROC on MIMIC-IV mortality prediction and 2.17% gain on eICU, outperforming existing state-of-the-art approaches.

