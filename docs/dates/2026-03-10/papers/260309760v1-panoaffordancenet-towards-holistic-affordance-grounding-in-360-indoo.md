---
layout: default
title: PanoAffordanceNet: Towards Holistic Affordance Grounding in 360° Indoor Environments
---

# PanoAffordanceNet: Towards Holistic Affordance Grounding in 360° Indoor Environments
**arXiv**：[2603.09760v1](https://arxiv.org/abs/2603.09760) · [PDF](https://arxiv.org/pdf/2603.09760.pdf)  
**作者**：Guoliang Zhu, Wanjun Jia, Caoyang Shao, Yuheng Zhang, Zhiyong Li, Kailun Yang  

**一句话要点**：提出PanoAffordanceNet以解决360°室内环境中整体可供性定位的挑战

**关键词**：全景可供性定位, 失真感知调制, 球形密集化头, 多级约束学习, 具身智能感知, 360°室内环境

## 3 点简述
- 核心问题：360°全景图因ERP投影导致几何失真、语义分散和跨尺度对齐困难，现有方法局限于对象中心视角。
- 方法要点：采用DASM进行纬度相关校准和OSDH恢复拓扑连续性，结合像素级、分布和区域-文本对比约束抑制语义漂移。
- 实验或效果：构建首个高质量全景数据集360-AGD，实验显示PanoAffordanceNet显著优于现有方法，为具身智能场景级感知奠定基础。

## 摘要（原文）

> Global perception is essential for embodied agents in 360° spaces, yet current affordance grounding remains largely object-centric and restricted to perspective views. To bridge this gap, we introduce a novel task: Holistic Affordance Grounding in 360° Indoor Environments. This task faces unique challenges, including severe geometric distortions from Equirectangular Projection (ERP), semantic dispersion, and cross-scale alignment difficulties. We propose PanoAffordanceNet, an end-to-end framework featuring a Distortion-Aware Spectral Modulator (DASM) for latitude-dependent calibration and an Omni-Spherical Densification Head (OSDH) to restore topological continuity from sparse activations. By integrating multi-level constraints comprising pixel-wise, distributional, and region-text contrastive objectives, our framework effectively suppresses semantic drift under low supervision. Furthermore, we construct 360-AGD, the first high-quality panoramic affordance grounding dataset. Extensive experiments demonstrate that PanoAffordanceNet significantly outperforms existing methods, establishing a solid baseline for scene-level perception in embodied intelligence. The source code and benchmark dataset will be made publicly available at https://github.com/GL-ZHU925/PanoAffordanceNet.

