---
layout: default
title: CompSplat: Compression-aware 3D Gaussian Splatting for Real-world Video
---

# CompSplat: Compression-aware 3D Gaussian Splatting for Real-world Video
**arXiv**：[2602.09816v1](https://arxiv.org/abs/2602.09816) · [PDF](https://arxiv.org/pdf/2602.09816.pdf)  
**作者**：Hojun Song, Heejung Choi, Aro Kim, Chae-yeong Song, Gahyeon Kim, Soo Ye Kim, Jaehyup Lee, Sang-hyo Park  

**一句话要点**：提出CompSplat框架，通过建模压缩特性解决长视频压缩下的三维重建与渲染问题

**关键词**：三维高斯泼溅, 压缩感知训练, 长视频新视角合成, 几何一致性, 自适应剪枝, 真实世界视频

## 3 点简述
- 核心问题：真实世界长视频的压缩导致帧间不一致和几何误差累积，影响新视角合成质量
- 方法要点：引入压缩感知的帧加权和自适应剪枝策略，增强鲁棒性和几何一致性
- 实验或效果：在多个基准测试中，在严重压缩条件下实现最先进的渲染质量和姿态精度

## 摘要（原文）

> High-quality novel view synthesis (NVS) from real-world videos is crucial for applications such as cultural heritage preservation, digital twins, and immersive media. However, real-world videos typically contain long sequences with irregular camera trajectories and unknown poses, leading to pose drift, feature misalignment, and geometric distortion during reconstruction. Moreover, lossy compression amplifies these issues by introducing inconsistencies that gradually degrade geometry and rendering quality. While recent studies have addressed either long-sequence NVS or unposed reconstruction, compression-aware approaches still focus on specific artifacts or limited scenarios, leaving diverse compression patterns in long videos insufficiently explored. In this paper, we propose CompSplat, a compression-aware training framework that explicitly models frame-wise compression characteristics to mitigate inter-frame inconsistency and accumulated geometric errors. CompSplat incorporates compression-aware frame weighting and an adaptive pruning strategy to enhance robustness and geometric consistency, particularly under heavy compression. Extensive experiments on challenging benchmarks, including Tanks and Temples, Free, and Hike, demonstrate that CompSplat achieves state-of-the-art rendering quality and pose accuracy, significantly surpassing most recent state-of-the-art NVS approaches under severe compression conditions.

