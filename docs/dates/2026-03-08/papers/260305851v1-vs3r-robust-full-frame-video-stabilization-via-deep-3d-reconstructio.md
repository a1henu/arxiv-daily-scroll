---
layout: default
title: VS3R: Robust Full-frame Video Stabilization via Deep 3D Reconstruction
---

# VS3R: Robust Full-frame Video Stabilization via Deep 3D Reconstruction
**arXiv**：[2603.05851v1](https://arxiv.org/abs/2603.05851) · [PDF](https://arxiv.org/pdf/2603.05851.pdf)  
**作者**：Muhua Zhu, Xinhao Jin, Yu Zhang, Yifei Xue, Tie Ji, Yizhen Lao  

**一句话要点**：提出VS3R框架，通过深度3D重建与生成视频扩散实现鲁棒全帧视频稳定

**关键词**：视频稳定, 3D重建, 生成视频扩散, 全帧处理, 鲁棒性优化

## 3 点简述
- 核心问题：视频稳定面临几何鲁棒性与全帧一致性的权衡，2D方法裁剪严重，3D方法在极端运动下易失效。
- 方法要点：结合前馈3D重建与生成视频扩散，联合估计相机参数、深度和掩码，并引入混合稳定渲染模块融合语义与几何线索。
- 实验或效果：在多种相机模型下实现高保真全帧稳定，在鲁棒性和视觉质量上显著优于现有方法。

## 摘要（原文）

> Video stabilization aims to mitigate camera shake but faces a fundamental trade-off between geometric robustness and full-frame consistency. While 2D methods suffer from aggressive cropping, 3D techniques are often undermined by fragile optimization pipelines that fail under extreme motions. To bridge this gap, we propose VS3R, a framework that synergizes feed-forward 3D reconstruction with generative video diffusion. Our pipeline jointly estimates camera parameters, depth, and masks to ensure all-scenario reliability, and introduces a Hybrid Stabilized Rendering module that fuses semantic and geometric cues for dynamic consistency. Finally, a Dual-Stream Video Diffusion Model restores disoccluded regions and rectifies artifacts by synergizing structural guidance with semantic anchors. Collectively, VS3R achieves high-fidelity, full-frame stabilization across diverse camera models and significantly outperforms state-of-the-art methods in robustness and visual quality.

