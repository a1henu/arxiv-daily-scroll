---
layout: default
title: No Data? No Problem: Robust Vision-Tabular Learning with Missing Values
---

# No Data? No Problem: Robust Vision-Tabular Learning with Missing Values
**arXiv**：[2512.19602v1](https://arxiv.org/abs/2512.19602) · [PDF](https://arxiv.org/pdf/2512.19602.pdf)  
**作者**：Marta Hasny, Laura Daza, Keno Bressem, Maxime Di Folco, Julia Schnabel  

**一句话要点**：提出RoVTL框架以解决医学影像与表格数据融合中缺失值鲁棒性问题

**关键词**：多模态学习, 缺失值鲁棒性, 医学影像分析, 对比学习, 表格数据融合

## 3 点简述
- 核心问题：真实世界医学数据集表格属性常缺失，需训练时利用完整数据、推理时鲁棒处理缺失值。
- 方法要点：通过对比预训练引入缺失增强，下游任务使用门控交叉注意力融合与Tabular More vs. Fewer损失。
- 实验或效果：在UK Biobank心脏MRI上优于现有方法，并泛化至外部数据集和自然图像领域。

## 摘要（原文）

> Large-scale medical biobanks provide imaging data complemented by extensive tabular information, such as demographics or clinical measurements. However, this abundance of tabular attributes does not reflect real-world datasets, where only a subset of attributes may be available. This discrepancy calls for methods that can leverage all the tabular data during training while remaining robust to missing values at inference. To address this challenge, we propose RoVTL (Robust Vision-Tabular Learning), a framework designed to handle any level of tabular data availability, from 0% to 100%. RoVTL comprises two key stages: contrastive pretraining, where we introduce tabular attribute missingness as data augmentation to promote robustness, and downstream task tuning using a gated cross-attention module for multimodal fusion. During fine-tuning, we employ a novel Tabular More vs. Fewer loss that ranks performance based on the amount of available tabular data. Combined with disentangled gradient learning, this enables consistent performance across all tabular data completeness scenarios. We evaluate RoVTL on cardiac MRI scans from the UK Biobank, demonstrating superior robustness to missing tabular data compared to prior methods. Furthermore, RoVTL successfully generalizes to an external cardiac MRI dataset for multimodal disease classification, and extends to the natural images domain, achieving robust performance on a car advertisements dataset. The code is available at https://github.com/marteczkah/RoVTL.

