---
layout: default
title: Breaking the Data Barrier: Robust Few-Shot 3D Vessel Segmentation using Foundation Models
---

# Breaking the Data Barrier: Robust Few-Shot 3D Vessel Segmentation using Foundation Models
**arXiv**：[2602.23782v1](https://arxiv.org/abs/2602.23782) · [PDF](https://arxiv.org/pdf/2602.23782.pdf)  
**作者**：Kirato Yoshihara, Yohei Sugawara, Yuta Tokuoka, Lihang Hong  

**一句话要点**：提出基于基础模型的轻量3D适配框架，以解决少样本和域偏移下的血管分割问题。

**关键词**：血管分割, 少样本学习, 域适应, 基础模型, 3D医学图像, 轻量适配

## 3 点简述
- 核心问题：现有血管分割方法依赖大规模标注数据，在少样本和域偏移时性能下降严重。
- 方法要点：利用预训练视觉基础模型DINOv3，通过3D适配器、多尺度聚合器和Z通道嵌入实现2D到3D的迁移。
- 实验或效果：在5样本少样本和域外数据上，Dice分数显著超越nnU-Net等基线，提升达30-50%。

## 摘要（原文）

> State-of-the-art vessel segmentation methods typically require large-scale annotated datasets and suffer from severe performance degradation under domain shifts. In clinical practice, however, acquiring extensive annotations for every new scanner or protocol is unfeasible. To address this, we propose a novel framework leveraging a pre-trained Vision Foundation Model (DINOv3) adapted for volumetric vessel segmentation. We introduce a lightweight 3D Adapter for volumetric consistency, a multi-scale 3D Aggregator for hierarchical feature fusion, and Z-channel embedding to effectively bridge the gap between 2D pre-training and 3D medical modalities, enabling the model to capture continuous vascular structures from limited data. We validated our method on the TopCoW (in-domain) and Lausanne (out-of-distribution) datasets. In the extreme few-shot regime with 5 training samples, our method achieved a Dice score of 43.42%, marking a 30% relative improvement over the state-of-the-art nnU-Net (33.41%) and outperforming other Transformer-based baselines, such as SwinUNETR and UNETR, by up to 45%. Furthermore, in the out-of-distribution setting, our model demonstrated superior robustness, achieving a 50% relative improvement over nnU-Net (21.37% vs. 14.22%), which suffered from severe domain overfitting. Ablation studies confirmed that our 3D adaptation mechanism and multi-scale aggregation strategy are critical for vascular continuity and robustness. Our results suggest foundation models offer a viable cold-start solution, improving clinical reliability under data scarcity or domain shifts.

