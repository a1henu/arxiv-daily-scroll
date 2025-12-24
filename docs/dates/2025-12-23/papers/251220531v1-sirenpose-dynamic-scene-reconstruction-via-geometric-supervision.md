---
layout: default
title: SirenPose: Dynamic Scene Reconstruction via Geometric Supervision
---

# SirenPose: Dynamic Scene Reconstruction via Geometric Supervision
**arXiv**：[2512.20531v1](https://arxiv.org/abs/2512.20531) · [PDF](https://arxiv.org/pdf/2512.20531.pdf)  
**作者**：Kaitong Cai, Jensen Zhang, Jing Yang, Keze Wang  

**一句话要点**：提出SirenPose，通过几何监督实现动态场景的准确重建

**关键词**：动态场景重建, 几何监督, 正弦表示网络, 关键点预测, 时空一致性, 单目视频

## 3 点简述
- 核心问题：现有方法在快速运动、遮挡等挑战性场景中难以保持运动保真度和时空一致性
- 方法要点：结合正弦表示网络的周期性激活与关键点几何监督，引入物理约束提升时空一致性
- 实验或效果：在多个基准测试中优于先进方法，显著降低FVD、FID，提升LPIPS和运动平滑度

## 摘要（原文）

> We introduce SirenPose, a geometry-aware loss formulation that integrates the periodic activation properties of sinusoidal representation networks with keypoint-based geometric supervision, enabling accurate and temporally consistent reconstruction of dynamic 3D scenes from monocular videos. Existing approaches often struggle with motion fidelity and spatiotemporal coherence in challenging settings involving fast motion, multi-object interaction, occlusion, and rapid scene changes. SirenPose incorporates physics inspired constraints to enforce coherent keypoint predictions across both spatial and temporal dimensions, while leveraging high frequency signal modeling to capture fine grained geometric details. We further expand the UniKPT dataset to 600,000 annotated instances and integrate graph neural networks to model keypoint relationships and structural correlations. Extensive experiments on benchmarks including Sintel, Bonn, and DAVIS demonstrate that SirenPose consistently outperforms state-of-the-art methods. On DAVIS, SirenPose achieves a 17.8 percent reduction in FVD, a 28.7 percent reduction in FID, and a 6.0 percent improvement in LPIPS compared to MoSCA. It also improves temporal consistency, geometric accuracy, user score, and motion smoothness. In pose estimation, SirenPose outperforms Monst3R with lower absolute trajectory error as well as reduced translational and rotational relative pose error, highlighting its effectiveness in handling rapid motion, complex dynamics, and physically plausible reconstruction.

