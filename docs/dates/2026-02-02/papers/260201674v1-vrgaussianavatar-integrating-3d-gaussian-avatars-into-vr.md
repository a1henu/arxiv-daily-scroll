---
layout: default
title: VRGaussianAvatar: Integrating 3D Gaussian Avatars into VR
---

# VRGaussianAvatar: Integrating 3D Gaussian Avatars into VR
**arXiv**：[2602.01674v1](https://arxiv.org/abs/2602.01674) · [PDF](https://arxiv.org/pdf/2602.01674.pdf)  
**作者**：Hail Song, Boram Yoon, Seokhwan Yang, Seoyoung Kang, Hyunjeong Kim, Henning Metzmacher, Woontack Woo  

**一句话要点**：提出VRGaussianAvatar系统，实现基于头戴显示器跟踪信号的实时全身3D高斯泼溅化身虚拟现实。

**关键词**：虚拟现实化身, 3D高斯泼溅, 实时渲染, 双目批处理, 逆运动学, 用户研究

## 3 点简述
- 核心问题：仅用HMD跟踪信号实现实时全身3D高斯泼溅化身在VR中的高效渲染。
- 方法要点：采用并行流水线，前端通过逆运动学估计全身姿态，后端引入双目批处理优化立体渲染效率。
- 实验或效果：系统保持交互式VR性能，在用户研究中获得更高外观相似性、体现感和合理性评分。

## 摘要（原文）

> We present VRGaussianAvatar, an integrated system that enables real-time full-body 3D Gaussian Splatting (3DGS) avatars in virtual reality using only head-mounted display (HMD) tracking signals. The system adopts a parallel pipeline with a VR Frontend and a GA Backend. The VR Frontend uses inverse kinematics to estimate full-body pose and streams the resulting pose along with stereo camera parameters to the backend. The GA Backend stereoscopically renders a 3DGS avatar reconstructed from a single image. To improve stereo rendering efficiency, we introduce Binocular Batching, which jointly processes left and right eye views in a single batched pass to reduce redundant computation and support high-resolution VR displays. We evaluate VRGaussianAvatar with quantitative performance tests and a within-subject user study against image- and video-based mesh avatar baselines. Results show that VRGaussianAvatar sustains interactive VR performance and yields higher perceived appearance similarity, embodiment, and plausibility. Project page and source code are available at https://vrgaussianavatar.github.io.

