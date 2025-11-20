---
layout: default
title: ShelfOcc: Native 3D Supervision beyond LiDAR for Vision-Based Occupancy Estimation
---

# ShelfOcc: Native 3D Supervision beyond LiDAR for Vision-Based Occupancy Estimation
**arXiv**：[2511.15396v1](https://arxiv.org/abs/2511.15396) · [PDF](https://arxiv.org/pdf/2511.15396.pdf)  
**作者**：Simon Boeder, Fabian Gigengack, Simon Roesler, Holger Caesar, Benjamin Risse  

**一句话要点**：提出ShelfOcc方法，通过视频生成3D语义体素标签，实现无LiDAR的视觉占用估计。

**关键词**：3D占用估计, 弱监督学习, 视觉几何, 体素表示, 自动驾驶场景

## 3 点简述
- 核心问题：现有方法依赖2D投影监督，存在几何不一致和深度渗漏问题。
- 方法要点：过滤和累积静态几何，处理动态内容，传播语义到稳定体素表示。
- 实验或效果：在Occ3D-nuScenes基准上，相对改进达34%，优于先前弱监督方法。

## 摘要（原文）

> Recent progress in self- and weakly supervised occupancy estimation has largely relied on 2D projection or rendering-based supervision, which suffers from geometric inconsistencies and severe depth bleeding. We thus introduce ShelfOcc, a vision-only method that overcomes these limitations without relying on LiDAR. ShelfOcc brings supervision into native 3D space by generating metrically consistent semantic voxel labels from video, enabling true 3D supervision without any additional sensors or manual 3D annotations. While recent vision-based 3D geometry foundation models provide a promising source of prior knowledge, they do not work out of the box as a prediction due to sparse or noisy and inconsistent geometry, especially in dynamic driving scenes. Our method introduces a dedicated framework that mitigates these issues by filtering and accumulating static geometry consistently across frames, handling dynamic content and propagating semantic information into a stable voxel representation. This data-centric shift in supervision for weakly/shelf-supervised occupancy estimation allows the use of essentially any SOTA occupancy model architecture without relying on LiDAR data. We argue that such high-quality supervision is essential for robust occupancy learning and constitutes an important complementary avenue to architectural innovation. On the Occ3D-nuScenes benchmark, ShelfOcc substantially outperforms all previous weakly/shelf-supervised methods (up to a 34% relative improvement), establishing a new data-driven direction for LiDAR-free 3D scene understanding.

