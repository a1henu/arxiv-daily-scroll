---
layout: default
title: CylinderSplat: 3D Gaussian Splatting with Cylindrical Triplanes for Panoramic Novel View Synthesis
---

# CylinderSplat: 3D Gaussian Splatting with Cylindrical Triplanes for Panoramic Novel View Synthesis
**arXiv**：[2603.05882v1](https://arxiv.org/abs/2603.05882) · [PDF](https://arxiv.org/pdf/2603.05882.pdf)  
**作者**：Qiwei Wang, Xianghui Ze, Jingyi Yu, Yujiao Shi  

**一句话要点**：提出圆柱三平面表示法以解决全景新视图合成中的几何失真与遮挡问题

**关键词**：全景新视图合成, 3D高斯溅射, 圆柱三平面表示, 稀疏视图重建, 曼哈顿世界假设, 双分支架构

## 3 点简述
- 现有方法在稀疏视图下难以处理遮挡，且笛卡尔三平面表示不适用于360度场景几何。
- 采用圆柱三平面表示，结合像素与体积分支，灵活处理单视图到多视图输入。
- 实验表明，在单视图和多视图全景合成中，重建质量和几何精度均优于先前方法。

## 摘要（原文）

> Feed-forward 3D Gaussian Splatting (3DGS) has shown great promise for real-time novel view synthesis, but its application to panoramic imagery remains challenging. Existing methods often rely on multi-view cost volumes for geometric refinement, which struggle to resolve occlusions in sparse-view scenarios. Furthermore, standard volumetric representations like Cartesian Triplanes are poor in capturing the inherent geometry of $360^\circ$ scenes, leading to distortion and aliasing.
>   In this work, we introduce CylinderSplat, a feed-forward framework for panoramic 3DGS that addresses these limitations. The core of our method is a new {cylindrical Triplane} representation, which is better aligned with panoramic data and real-world structures adhering to the Manhattan-world assumption. We use a dual-branch architecture: a pixel-based branch reconstructs well-observed regions, while a volume-based branch leverages the cylindrical Triplane to complete occluded or sparsely-viewed areas. Our framework is designed to flexibly handle a variable number of input views, from single to multiple panoramas. Extensive experiments demonstrate that CylinderSplat achieves state-of-the-art results in both single-view and multi-view panoramic novel view synthesis, outperforming previous methods in both reconstruction quality and geometric accuracy.

