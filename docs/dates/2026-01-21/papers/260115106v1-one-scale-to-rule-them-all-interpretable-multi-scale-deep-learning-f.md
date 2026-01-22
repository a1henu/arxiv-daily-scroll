---
layout: default
title: One scale to rule them all: interpretable multi-scale Deep Learning for predicting cell survival after proton and carbon ion irradiation
---

# One scale to rule them all: interpretable multi-scale Deep Learning for predicting cell survival after proton and carbon ion irradiation
**arXiv**：[2601.15106v1](https://arxiv.org/abs/2601.15106) · [PDF](https://arxiv.org/pdf/2601.15106.pdf)  
**作者**：Giulio Bordieri, Giorgio Cartechini, Anna Bianchi, Anna Selva, Valeria Conte, Marta Missiaggia, Francesco G. Cordoni  

**一句话要点**：提出可解释多尺度深度学习模型，预测质子与碳离子辐照后细胞存活率。

**关键词**：细胞存活预测, 多尺度深度学习, 可解释性模型, 质子碳离子辐照, 剂量学特征

## 3 点简述
- 核心问题：能量沉积空间尺度与生物效应关联未完全阐明，影响放疗与辐射防护。
- 方法要点：结合LET、纳米与微剂量学量，利用序列注意力实现多尺度特征分析与决策透明。
- 实验或效果：在PIDE数据集上训练测试，预测RBE准确度高，较小空间尺度量影响更大。

## 摘要（原文）

> The relationship between the physical characteristics of the radiation field and biological damage is central to both radiotherapy and radioprotection, yet the link between spatial scales of energy deposition and biological effects remains not entirely understood. To address this, we developed an interpretable deep learning model that predicts cell survival after proton and carbon ion irradiation, leveraging sequential attention to highlight relevant features and provide insight into the contribution of different energy deposition scales. Trained and tested on the PIDE dataset, our model incorporates, beside LET, nanodosimetric and microdosimetric quantities simulated with MC-Startrack and Open-TOPAS, enabling multi-scale characterization. While achieving high predictive accuracy, our approach also emphasizes transparency in decision-making. We demonstrate high accuracy in predicting RBE for in vitro experiments. Multiple scales are utilized concurrently, with no single spatial scale being predominant. Quantities defined at smaller spatial domains generally have a greater influence, whereas the LET plays a lesser role.

