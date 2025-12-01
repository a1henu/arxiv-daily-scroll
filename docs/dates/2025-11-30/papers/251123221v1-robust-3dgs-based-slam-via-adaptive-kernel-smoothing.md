---
layout: default
title: Robust 3DGS-based SLAM via Adaptive Kernel Smoothing
---

# Robust 3DGS-based SLAM via Adaptive Kernel Smoothing
**arXiv**：[2511.23221v1](https://arxiv.org/abs/2511.23221) · [PDF](https://arxiv.org/pdf/2511.23221.pdf)  
**作者**：Shouhe Zhang, Dayong Ren, Sensen Song, Wenjie Li, Piaopiao Yu, Yurong Qian  

**一句话要点**：提出自适应核平滑方法以增强3DGS-SLAM的跟踪鲁棒性

**关键词**：3D高斯溅射, SLAM, 鲁棒性增强, 自适应核平滑, 相机姿态跟踪

## 3 点简述
- 核心问题：传统3DGS-SLAM过度依赖渲染质量，对参数误差敏感，导致相机姿态跟踪不稳定。
- 方法要点：通过CB-KNN自适应调整局部高斯分布，引入可控模糊作为正则化，提升光栅化过程的鲁棒性。
- 实验或效果：在保持场景重建质量的同时，显著提高了相机姿态跟踪的鲁棒性和准确性。

## 摘要（原文）

> In this paper, we challenge the conventional notion in 3DGS-SLAM that rendering quality is the primary determinant of tracking accuracy. We argue that, compared to solely pursuing a perfect scene representation, it is more critical to enhance the robustness of the rasterization process against parameter errors to ensure stable camera pose tracking. To address this challenge, we propose a novel approach that leverages a smooth kernel strategy to enhance the robustness of 3DGS-based SLAM. Unlike conventional methods that focus solely on minimizing rendering error, our core insight is to make the rasterization process more resilient to imperfections in the 3DGS parameters. We hypothesize that by allowing each Gaussian to influence a smoother, wider distribution of pixels during rendering, we can mitigate the detrimental effects of parameter noise from outlier Gaussians. This approach intentionally introduces a controlled blur to the rendered image, which acts as a regularization term, stabilizing the subsequent pose optimization. While a complete redesign of the rasterization pipeline is an ideal solution, we propose a practical and effective alternative that is readily integrated into existing 3DGS frameworks. Our method, termed Corrective Blurry KNN (CB-KNN), adaptively modifies the RGB values and locations of the K-nearest neighboring Gaussians within a local region. This dynamic adjustment generates a smoother local rendering, reducing the impact of erroneous GS parameters on the overall image. Experimental results demonstrate that our approach, while maintaining the overall quality of the scene reconstruction (mapping), significantly improves the robustness and accuracy of camera pose tracking.

