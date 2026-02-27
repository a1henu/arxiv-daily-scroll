---
layout: default
title: HELMLAB: An Analytical, Data-Driven Color Space for Perceptual Distance in UI Design Systems
---

# HELMLAB: An Analytical, Data-Driven Color Space for Perceptual Distance in UI Design Systems
**arXiv**：[2602.23010v1](https://arxiv.org/abs/2602.23010) · [PDF](https://arxiv.org/pdf/2602.23010.pdf)  
**作者**：Gorkem Yildiz  

**一句话要点**：提出HELMLAB颜色空间以提升UI设计系统中颜色感知距离的准确性

**关键词**：颜色空间, 感知距离, UI设计系统, 颜色校正, 数据驱动模型

## 3 点简述
- 核心问题：UI设计系统需要更精确的颜色感知距离度量，以改进颜色选择和对比度评估。
- 方法要点：通过72参数分析模型，结合学习矩阵、功率压缩、傅里叶色调校正和Helmholtz-Kohlrausch调整，实现从CIE XYZ到感知Lab的映射。
- 实验或效果：在COMBVD数据集上，STRESS为23.22，比CIEDE2000降低20.4%，并展示跨数据集竞争性能。

## 摘要（原文）

> We present HELMLAB, a 72-parameter analytical color space for UI design systems. The forward transform maps CIE XYZ to a perceptually-organized Lab representation through learned matrices, per-channel power compression, Fourier hue correction, and embedded Helmholtz-Kohlrausch lightness adjustment. A post-pipeline neutral correction guarantees that achromatic colors map to a=b=0 (chroma < 10^-6), and a rigid rotation of the chromatic plane improves hue-angle alignment without affecting the distance metric, which is invariant under isometries. On the COMBVD dataset (3,813 color pairs), HELMLAB achieves a STRESS of 23.22, a 20.4% reduction from CIEDE2000 (29.18). Cross-validation on He et al. 2022 and MacAdam 1974 shows competitive cross-dataset performance. The transform is invertible with round-trip errors below 10^-14. Gamut mapping, design-token export, and dark/light mode adaptation utilities are included for use in web and mobile design systems.

