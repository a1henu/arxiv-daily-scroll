---
layout: default
title: Affine Correspondences in Stereo Vision: Theory, Practice, and Limitations
---

# Affine Correspondences in Stereo Vision: Theory, Practice, and Limitations
**arXiv**：[2603.01836v1](https://arxiv.org/abs/2603.01836) · [PDF](https://arxiv.org/pdf/2603.01836.pdf)  
**作者**：Levente Hajder  

**一句话要点**：提出基于仿射对应的立体视觉方法，用于三维重建和几何估计，评估其精度与局限性。

**关键词**：仿射对应, 立体视觉, 三维重建, 表面法线估计, 基础矩阵, 精度评估

## 3 点简述
- 核心问题：仿射变换在立体视觉中的应用，如表面法线、基础矩阵估计，但精度影响重建质量。
- 方法要点：提出从对应图像方向估计局部仿射变换的新技术，并利用基础矩阵优化处理。
- 实验或效果：通过合成和真实数据评估，重建表面法线精度在几度内，详细分析特殊姿态和平面方向。

## 摘要（原文）

> Affine transformations have been recently used for stereo vision. They can be exploited in various computer vision application, e.g., when estimating surface normals, homographies, fundamental and essential matrices. Even full 3D reconstruction can be obtained by using affine correspondences. First, this paper overviews the fundamental statements for affine transformations and epipolar geometry. Then it is investigated how the transformation accuracy influences the quality of the 3D reconstruction. Besides, we propose novel techniques for estimating the local affine transformation from corresponding image directions; moreover, the fundamental matrix, related to the processed image pair, can also be exploited. Both synthetic and real quantitative evaluations are implemented based on the accuracy of the reconstructed surface normals. For the latter one, a special object, containing three perpendicular planes with chessboard patterns, is constructed. The quantitative evaluations are based on the accuracy of the reconstructed surface normals and it is concluded that the estimation accuracy is around a few degrees for realistic test cases. Special stereo poses and plane orientations are also evaluated in detail.

