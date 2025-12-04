---
layout: default
title: Hierarchical Attention for Sparse Volumetric Anomaly Detection in Subclinical Keratoconus
---

# Hierarchical Attention for Sparse Volumetric Anomaly Detection in Subclinical Keratoconus
**arXiv**：[2512.03346v1](https://arxiv.org/abs/2512.03346) · [PDF](https://arxiv.org/pdf/2512.03346.pdf)  
**作者**：Lynn Kandakji, William Woof, Nikolas Pontikos  

**一句话要点**：提出分层注意力模型以解决亚临床圆锥角膜三维医学影像中稀疏异常检测的挑战

**关键词**：分层注意力, 稀疏异常检测, 三维医学影像, 亚临床圆锥角膜, 空间尺度对齐, 参数效率

## 3 点简述
- 核心问题：现有2D/3D CNN和ViT在检测稀疏、非相邻的早期疾病信号时，因局部性或全局注意力扩散导致性能不足。
- 方法要点：通过分层注意力模型，实现空间尺度对齐，匹配亚临床异常的多切片范围，避免过度局部或全局关注。
- 实验或效果：在亚临床圆锥角膜检测中，分层注意力模型比传统方法灵敏度与特异性提高21-23%，参数效率更高。

## 摘要（原文）

> The detection of weak, spatially distributed anomalies in volumetric medical imaging remains a major challenge. The subtle, non-adjacent nature of early disease signals is often lost due to suboptimal architectural inductive biases: 2D/3D CNNs impose strong locality, while ViTs diffuse unconstrained global attention. This conflict leaves the optimal inductive structure for robust, sparse volumetric pattern recognition unresolved. This study presents a controlled comparison of sixteen modern deep learning architectures spanning 2D/3D convolutional, hybrid, and volumetric transformer families for subclinical keratoconus (SKC) detection from 3D anterior segment OCT volumes. We demonstrate that hierarchical attention models offer a superior and more parameter-efficient inductive bias, surpassing the performance of both 2D and 3D CNNs and ViTs. Our results show 21-23% higher sensitivity and specificity in the sparse anomaly (subclinical) regime. Mechanistic analyses reveal that this advantage stems from precise spatial scale alignment: hierarchical windowing produces effective receptive fields matched to the intermediate, multi-slice extent of subclinical abnormalities. This avoids excessive CNN locality and diffuse global attention. Attention-distance measurements confirm a key insight into architectural adaptation: the required spatial integration length shifts significantly based on the signal strength, with subclinical cases necessitating longer integration compared to both healthy and manifest disease states. Representational similarity and auxiliary age/sex prediction tasks further support the generalizability of these inductive principles. The findings provide design guidance for future volumetric anomaly detection systems, establishing hierarchical attention as a principled and effective approach for early pathological change analysis in 3D medical imaging.

