---
layout: default
title: V-DPM: 4D Video Reconstruction with Dynamic Point Maps
---

# V-DPM: 4D Video Reconstruction with Dynamic Point Maps
**arXiv**：[2601.09499v1](https://arxiv.org/abs/2601.09499) · [PDF](https://arxiv.org/pdf/2601.09499.pdf)  
**作者**：Edgar Sucar, Eldar Insafutdinov, Zihang Lai, Andrea Vedaldi  

**一句话要点**：提出V-DPM以从视频中重建动态3D场景，扩展动态点地图至多视图输入。

**关键词**：动态点地图, 4D视频重建, VGGT架构, 合成数据适应, 多视图处理

## 3 点简述
- 核心问题：现有动态点地图仅支持图像对，视频应用受限且需后处理优化。
- 方法要点：基于VGGT架构，通过合成数据适应，实现神经预测动态点地图。
- 实验或效果：在动态场景3D和4D重建中达到先进性能，恢复全点3D运动。

## 摘要（原文）

> Powerful 3D representations such as DUSt3R invariant point maps, which encode 3D shape and camera parameters, have significantly advanced feed forward 3D reconstruction. While point maps assume static scenes, Dynamic Point Maps (DPMs) extend this concept to dynamic 3D content by additionally representing scene motion. However, existing DPMs are limited to image pairs and, like DUSt3R, require post processing via optimization when more than two views are involved. We argue that DPMs are more useful when applied to videos and introduce V-DPM to demonstrate this. First, we show how to formulate DPMs for video input in a way that maximizes representational power, facilitates neural prediction, and enables reuse of pretrained models. Second, we implement these ideas on top of VGGT, a recent and powerful 3D reconstructor. Although VGGT was trained on static scenes, we show that a modest amount of synthetic data is sufficient to adapt it into an effective V-DPM predictor. Our approach achieves state of the art performance in 3D and 4D reconstruction for dynamic scenes. In particular, unlike recent dynamic extensions of VGGT such as P3, DPMs recover not only dynamic depth but also the full 3D motion of every point in the scene.

