---
layout: default
title: UFO-4D: Unposed Feedforward 4D Reconstruction from Two Images
---

# UFO-4D: Unposed Feedforward 4D Reconstruction from Two Images
**arXiv**：[2602.24290v1](https://arxiv.org/abs/2602.24290) · [PDF](https://arxiv.org/pdf/2602.24290.pdf)  
**作者**：Junhwa Hur, Charles Herrmann, Songyou Peng, Philipp Henzler, Zeyu Ma, Todd Zickler, Deqing Sun  

**一句话要点**：提出UFO-4D框架，从无位姿图像对中前馈重建密集4D表示

**关键词**：4D重建, 动态3D高斯, 前馈框架, 无位姿图像, 联合估计, 可微分渲染

## 3 点简述
- 核心问题：无位姿图像密集4D重建依赖慢速优化或任务特定模型，缺乏统一前馈方法
- 方法要点：使用动态3D高斯表示，通过可微分渲染联合估计几何、运动和相机位姿
- 实验或效果：在几何、运动和位姿联合估计上优于先前工作，支持高保真4D插值

## 摘要（原文）

> Dense 4D reconstruction from unposed images remains a critical challenge, with current methods relying on slow test-time optimization or fragmented, task-specific feedforward models. We introduce UFO-4D, a unified feedforward framework to reconstruct a dense, explicit 4D representation from just a pair of unposed images. UFO-4D directly estimates dynamic 3D Gaussian Splats, enabling the joint and consistent estimation of 3D geometry, 3D motion, and camera pose in a feedforward manner. Our core insight is that differentiably rendering multiple signals from a single Dynamic 3D Gaussian representation offers major training advantages. This approach enables a self-supervised image synthesis loss while tightly coupling appearance, depth, and motion. Since all modalities share the same geometric primitives, supervising one inherently regularizes and improves the others. This synergy overcomes data scarcity, allowing UFO-4D to outperform prior work by up to 3 times in joint geometry, motion, and camera pose estimation. Our representation also enables high-fidelity 4D interpolation across novel views and time. Please visit our project page for visual results: https://ufo-4d.github.io/

