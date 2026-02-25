---
layout: default
title: Event-Aided Sharp Radiance Field Reconstruction for Fast-Flying Drones
---

# Event-Aided Sharp Radiance Field Reconstruction for Fast-Flying Drones
**arXiv**：[2602.21101v1](https://arxiv.org/abs/2602.21101) · [PDF](https://arxiv.org/pdf/2602.21101.pdf)  
**作者**：Rong Zou, Marco Cannici, Davide Scaramuzza  

**一句话要点**：提出事件辅助的锐利辐射场重建框架，以解决快速飞行无人机图像模糊和位姿噪声问题。

**关键词**：事件相机, 神经辐射场, 运动模糊, 无人机重建, 视觉惯性里程计, 多模态融合

## 3 点简述
- 核心问题：高速无人机飞行导致图像严重运动模糊和位姿估计漂移，影响NeRF重建质量。
- 方法要点：融合异步事件流与模糊图像，嵌入NeRF优化，联合精炼事件视觉惯性里程计先验。
- 实验或效果：在合成和真实数据上验证，重建高保真辐射场，性能提升超50%，无需地面真值监督。

## 摘要（原文）

> Fast-flying aerial robots promise rapid inspection under limited battery constraints, with direct applications in infrastructure inspection, terrain exploration, and search and rescue. However, high speeds lead to severe motion blur in images and induce significant drift and noise in pose estimates, making dense 3D reconstruction with Neural Radiance Fields (NeRFs) particularly challenging due to their high sensitivity to such degradations. In this work, we present a unified framework that leverages asynchronous event streams alongside motion-blurred frames to reconstruct high-fidelity radiance fields from agile drone flights. By embedding event-image fusion into NeRF optimization and jointly refining event-based visual-inertial odometry priors using both event and frame modalities, our method recovers sharp radiance fields and accurate camera trajectories without ground-truth supervision. We validate our approach on both synthetic data and real-world sequences captured by a fast-flying drone. Despite highly dynamic drone flights, where RGB frames are severely degraded by motion blur and pose priors become unreliable, our method reconstructs high-fidelity radiance fields and preserves fine scene details, delivering a performance gain of over 50% on real-world data compared to state-of-the-art methods.

