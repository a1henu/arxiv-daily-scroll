---
layout: default
title: HELMLAB: An Analytical, Data-Driven Color Space for Perceptual Distance in UI Design Systems
---

# HELMLAB: An Analytical, Data-Driven Color Space for Perceptual Distance in UI Design Systems
**arXiv**：[2602.23010v1](https://arxiv.org/abs/2602.23010) · [PDF](https://arxiv.org/pdf/2602.23010.pdf)  
**作者**：Gorkem Yildiz  

**一句话要点**：提出HELMLAB颜色空间以提升UI设计系统中的感知距离度量精度

**关键词**：颜色空间, 感知距离, UI设计系统, 数据驱动, 可逆变换, 跨数据集验证

## 3 点简述
- 核心问题：现有颜色空间在UI设计中感知距离度量不精确，影响设计系统一致性
- 方法要点：通过72参数分析变换，结合学习矩阵、功率压缩和傅里叶校正，优化感知组织
- 实验或效果：在COMBVD数据集上STRESS降低20.4%，跨数据集验证显示竞争性能，变换可逆且误差低

## 摘要（原文）

> We present HELMLAB, a 72-parameter analytical color space for UI design systems. The forward transform maps CIE XYZ to a perceptually-organized Lab representation through learned matrices, per-channel power compression, Fourier hue correction, and embedded Helmholtz-Kohlrausch lightness adjustment. A post-pipeline neutral correction guarantees that achromatic colors map to a=b=0 (chroma < 10^-6), and a rigid rotation of the chromatic plane improves hue-angle alignment without affecting the distance metric, which is invariant under isometries. On the COMBVD dataset (3,813 color pairs), HELMLAB achieves a STRESS of 23.22, a 20.4% reduction from CIEDE2000 (29.18). Cross-validation on He et al. 2022 and MacAdam 1974 shows competitive cross-dataset performance. The transform is invertible with round-trip errors below 10^-14. Gamut mapping, design-token export, and dark/light mode adaptation utilities are included for use in web and mobile design systems.

