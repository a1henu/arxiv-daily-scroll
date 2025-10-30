---
layout: default
title: $D^2GS$: Dense Depth Regularization for LiDAR-free Urban Scene Reconstruction
---

# $D^2GS$: Dense Depth Regularization for LiDAR-free Urban Scene Reconstruction
**arXiv**：[2510.25173v1](https://arxiv.org/abs/2510.25173) · [PDF](https://arxiv.org/pdf/2510.25173.pdf)  
**作者**：Kejing Xia, Jidong Jia, Ke Jin, Yucai Bai, Li Sun, Dacheng Tao, Youjian Zhang  

**一句话要点**：提出D^2GS框架，用于无LiDAR城市场景重建，通过密集深度正则化提升几何精度

**关键词**：城市场景重建, 高斯泼溅, 深度正则化, 无LiDAR重建, 扩散模型, 几何优化

## 3 点简述
- 核心问题：现有城市重建方法依赖LiDAR，但获取准确LiDAR数据存在校准和空间对齐困难
- 方法要点：使用多视角深度预测初始化点云，结合扩散先验增强深度，优化高斯几何
- 实验效果：在Waymo数据集上优于现有方法，几何精度高，甚至超越使用真实LiDAR的方法

## 摘要（原文）

> Recently, Gaussian Splatting (GS) has shown great potential for urban scene
> reconstruction in the field of autonomous driving. However, current urban scene
> reconstruction methods often depend on multimodal sensors as inputs,
> \textit{i.e.} LiDAR and images. Though the geometry prior provided by LiDAR
> point clouds can largely mitigate ill-posedness in reconstruction, acquiring
> such accurate LiDAR data is still challenging in practice: i) precise
> spatiotemporal calibration between LiDAR and other sensors is required, as they
> may not capture data simultaneously; ii) reprojection errors arise from spatial
> misalignment when LiDAR and cameras are mounted at different locations. To
> avoid the difficulty of acquiring accurate LiDAR depth, we propose $D^2GS$, a
> LiDAR-free urban scene reconstruction framework. In this work, we obtain
> geometry priors that are as effective as LiDAR while being denser and more
> accurate. $\textbf{First}$, we initialize a dense point cloud by
> back-projecting multi-view metric depth predictions. This point cloud is then
> optimized by a Progressive Pruning strategy to improve the global consistency.
> $\textbf{Second}$, we jointly refine Gaussian geometry and predicted dense
> metric depth via a Depth Enhancer. Specifically, we leverage diffusion priors
> from a depth foundation model to enhance the depth maps rendered by Gaussians.
> In turn, the enhanced depths provide stronger geometric constraints during
> Gaussian training. $\textbf{Finally}$, we improve the accuracy of ground
> geometry by constraining the shape and normal attributes of Gaussians within
> road regions. Extensive experiments on the Waymo dataset demonstrate that our
> method consistently outperforms state-of-the-art methods, producing more
> accurate geometry even when compared with those using ground-truth LiDAR data.

