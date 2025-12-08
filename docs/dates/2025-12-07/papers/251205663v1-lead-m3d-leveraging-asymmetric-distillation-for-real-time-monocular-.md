---
layout: default
title: LeAD-M3D: Leveraging Asymmetric Distillation for Real-time Monocular 3D Detection
---

# LeAD-M3D: Leveraging Asymmetric Distillation for Real-time Monocular 3D Detection
**arXiv**：[2512.05663v1](https://arxiv.org/abs/2512.05663) · [PDF](https://arxiv.org/pdf/2512.05663.pdf)  
**作者**：Johannes Meier, Jonathan Michel, Oussema Dhaouadi, Yung-Hsu Yang, Christoph Reich, Zuria Bauer, Stefan Roth, Marc Pollefeys, Jacques Kaiser, Daniel Cremers  

**一句话要点**：提出LeAD-M3D，通过非对称蒸馏实现实时单目3D检测，无需额外模态。

**关键词**：单目3D检测, 知识蒸馏, 实时推理, 深度估计, 非对称训练, 3D匹配

## 3 点简述
- 核心问题：单目3D检测面临深度模糊、视角变化和高计算成本挑战。
- 方法要点：采用A2D2蒸馏几何知识、CM3D改进匹配、CGI3D加速推理。
- 实验或效果：在KITTI、Waymo和Rope3D上达到SOTA精度，速度提升最高3.6倍。

## 摘要（原文）

> Real-time monocular 3D object detection remains challenging due to severe depth ambiguity, viewpoint shifts, and the high computational cost of 3D reasoning. Existing approaches either rely on LiDAR or geometric priors to compensate for missing depth, or sacrifice efficiency to achieve competitive accuracy. We introduce LeAD-M3D, a monocular 3D detector that achieves state-of-the-art accuracy and real-time inference without extra modalities. Our method is powered by three key components. Asymmetric Augmentation Denoising Distillation (A2D2) transfers geometric knowledge from a clean-image teacher to a mixup-noised student via a quality- and importance-weighted depth-feature loss, enabling stronger depth reasoning without LiDAR supervision. 3D-aware Consistent Matching (CM3D) improves prediction-to-ground truth assignment by integrating 3D MGIoU into the matching score, yielding more stable and precise supervision. Finally, Confidence-Gated 3D Inference (CGI3D) accelerates detection by restricting expensive 3D regression to top-confidence regions. Together, these components set a new Pareto frontier for monocular 3D detection: LeAD-M3D achieves state-of-the-art accuracy on KITTI and Waymo, and the best reported car AP on Rope3D, while running up to 3.6x faster than prior high-accuracy methods. Our results demonstrate that high fidelity and real-time efficiency in monocular 3D detection are simultaneously attainable - without LiDAR, stereo, or geometric assumptions.

