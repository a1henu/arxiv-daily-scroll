---
layout: default
title: SPyCer: Semi-Supervised Physics-Guided Contextual Attention for Near-Surface Air Temperature Estimation from Satellite Imagery
---

# SPyCer: Semi-Supervised Physics-Guided Contextual Attention for Near-Surface Air Temperature Estimation from Satellite Imagery
**arXiv**：[2603.05219v1](https://arxiv.org/abs/2603.05219) · [PDF](https://arxiv.org/pdf/2603.05219.pdf)  
**作者**：Sofiane Bouaziz, Adel Hafiane, Raphael Canals, Rachid Nedjai  

**一句话要点**：提出SPyCer半监督物理引导网络，利用卫星图像连续估计近地表气温

**关键词**：近地表气温估计, 半监督学习, 物理引导网络, 卫星图像分析, 注意力机制, 表面能量平衡

## 3 点简述
- 问题：近地表气温传感器稀疏，难以提供连续空间测量。
- 方法：结合像素监督与物理约束，通过注意力机制捕获邻域物理影响。
- 效果：在真实数据集上优于基线，实现空间一致且物理一致的估计。

## 摘要（原文）

> Modern Earth observation relies on satellites to capture detailed surface properties. Yet, many phenomena that affect humans and ecosystems unfold in the atmosphere close to the surface. Near-ground sensors provide accurate measurements of certain environmental characteristics, such as near-surface air temperature (NSAT). However, they remain sparse and unevenly distributed, limiting their ability to provide continuous spatial measurements. To bridge this gap, we introduce SPyCer, a semi-supervised physics-guided network that can leverage pixel information and physical modeling to guide the learning process through meaningful physical properties. It is designed for continuous estimation of NSAT by proxy using satellite imagery. SPyCer frames NSAT prediction as a pixel-wise vision problem, where each near-ground sensor is projected onto satellite image coordinates and positioned at the center of a local image patch. The corresponding sensor pixel is supervised using both observed NSAT and physics-based constraints, while surrounding pixels contribute through physics-guided regularization derived from the surface energy balance and advection-diffusion-reaction partial differential equations. To capture the physical influence of neighboring pixels, SPyCer employs a multi-head attention guided by land cover characteristics and modulated with Gaussian distance weighting. Experiments on real-world datasets demonstrate that SPyCer produces spatially coherent and physically consistent NSAT estimates, outperforming existing baselines in terms of accuracy, generalization, and alignment with underlying physical processes.

