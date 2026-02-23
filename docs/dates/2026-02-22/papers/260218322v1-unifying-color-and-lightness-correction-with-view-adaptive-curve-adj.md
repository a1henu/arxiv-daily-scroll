---
layout: default
title: Unifying Color and Lightness Correction with View-Adaptive Curve Adjustment for Robust 3D Novel View Synthesis
---

# Unifying Color and Lightness Correction with View-Adaptive Curve Adjustment for Robust 3D Novel View Synthesis
**arXiv**：[2602.18322v1](https://arxiv.org/abs/2602.18322) · [PDF](https://arxiv.org/pdf/2602.18322.pdf)  
**作者**：Ziteng Cui, Shuhong Liu, Xiaoyu Dong, Xuangeng Chu, Lin Gu, Ming-Hsuan Yang, Tatsuya Harada  

**一句话要点**：提出Luminance-GS++框架，通过统一颜色与亮度校正解决复杂光照下3D新视角合成的鲁棒性问题。

**关键词**：3D新视角合成, 颜色校正, 亮度调整, 3D高斯泼溅, 多视角一致性, 无监督学习

## 3 点简述
- 核心问题：多视角捕获中光照、传感器和ISP差异导致光度不一致，降低NeRF和3DGS等方法的合成质量。
- 方法要点：结合全局视角自适应亮度调整与局部像素级残差细化，设计无监督目标联合优化校正与一致性。
- 实验或效果：在低光、过曝和复杂光照场景中实现先进性能，保持3DGS显式表示和实时渲染效率。

## 摘要（原文）

> High-quality image acquisition in real-world environments remains challenging due to complex illumination variations and inherent limitations of camera imaging pipelines. These issues are exacerbated in multi-view capture, where differences in lighting, sensor responses, and image signal processor (ISP) configurations introduce photometric and chromatic inconsistencies that violate the assumptions of photometric consistency underlying modern 3D novel view synthesis (NVS) methods, including Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS), leading to degraded reconstruction and rendering quality. We propose Luminance-GS++, a 3DGS-based framework for robust NVS under diverse illumination conditions. Our method combines a globally view-adaptive lightness adjustment with a local pixel-wise residual refinement for precise color correction. We further design unsupervised objectives that jointly enforce lightness correction and multi-view geometric and photometric consistency. Extensive experiments demonstrate state-of-the-art performance across challenging scenarios, including low-light, overexposure, and complex luminance and chromatic variations. Unlike prior approaches that modify the underlying representation, our method preserves the explicit 3DGS formulation, improving reconstruction fidelity while maintaining real-time rendering efficiency.

