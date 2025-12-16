---
layout: default
title: DePT3R: Joint Dense Point Tracking and 3D Reconstruction of Dynamic Scenes in a Single Forward Pass
---

# DePT3R: Joint Dense Point Tracking and 3D Reconstruction of Dynamic Scenes in a Single Forward Pass
**arXiv**：[2512.13122v1](https://arxiv.org/abs/2512.13122) · [PDF](https://arxiv.org/pdf/2512.13122.pdf)  
**作者**：Vivek Alumootil, Tuan-Anh Vu, M. Khalid Jawed  

**一句话要点**：提出DePT3R框架，在单次前向传播中联合实现动态场景的密集点跟踪与3D重建。

**关键词**：动态场景理解, 密集点跟踪, 3D重建, 多任务学习, 无相机位姿, 单次前向传播

## 3 点简述
- 核心问题：现有动态场景密集点跟踪方法依赖成对处理、已知相机位姿或时序假设，限制灵活性。
- 方法要点：通过强大骨干网络提取时空特征，使用密集预测头回归像素级映射，无需相机位姿。
- 实验或效果：在动态场景基准测试中表现优异，内存效率显著提升，代码开源。

## 摘要（原文）

> Current methods for dense 3D point tracking in dynamic scenes typically rely on pairwise processing, require known camera poses, or assume a temporal ordering to input frames, constraining their flexibility and applicability. Additionally, recent advances have successfully enabled efficient 3D reconstruction from large-scale, unposed image collections, underscoring opportunities for unified approaches to dynamic scene understanding. Motivated by this, we propose DePT3R, a novel framework that simultaneously performs dense point tracking and 3D reconstruction of dynamic scenes from multiple images in a single forward pass. This multi-task learning is achieved by extracting deep spatio-temporal features with a powerful backbone and regressing pixel-wise maps with dense prediction heads. Crucially, DePT3R operates without requiring camera poses, substantially enhancing its adaptability and efficiency-especially important in dynamic environments with rapid changes. We validate DePT3R on several challenging benchmarks involving dynamic scenes, demonstrating strong performance and significant improvements in memory efficiency over existing state-of-the-art methods. Data and codes are available via the open repository: https://github.com/StructuresComp/DePT3R

