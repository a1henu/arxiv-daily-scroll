---
layout: default
title: MVGSR: Multi-View Consistent 3D Gaussian Super-Resolution via Epipolar Guidance
---

# MVGSR: Multi-View Consistent 3D Gaussian Super-Resolution via Epipolar Guidance
**arXiv**：[2512.15048v1](https://arxiv.org/abs/2512.15048) · [PDF](https://arxiv.org/pdf/2512.15048.pdf)  
**作者**：Kaizhe Zhang, Shinan Chen, Qian Zhao, Weizhan Zhang, Caixia Yan, Yudeng Xin  

**一句话要点**：提出MVGSR框架，通过极线引导实现多视图一致的3D高斯超分辨率，提升渲染细节与一致性。

**关键词**：3D高斯超分辨率, 多视图一致性, 极线约束, 注意力机制, 相机姿态选择, 高分辨率渲染

## 3 点简述
- 核心问题：基于低分辨率图像的3D高斯重建无法直接用于高分辨率渲染，现有方法缺乏跨视图一致性。
- 方法要点：引入基于相机姿态的辅助视图选择，并设计极线约束的多视图注意力机制，选择性聚合多视图信息。
- 实验或效果：在物体中心和场景级基准测试中达到先进性能，验证了方法的有效性和适应性。

## 摘要（原文）

> Scenes reconstructed by 3D Gaussian Splatting (3DGS) trained on low-resolution (LR) images are unsuitable for high-resolution (HR) rendering. Consequently, a 3DGS super-resolution (SR) method is needed to bridge LR inputs and HR rendering. Early 3DGS SR methods rely on single-image SR networks, which lack cross-view consistency and fail to fuse complementary information across views. More recent video-based SR approaches attempt to address this limitation but require strictly sequential frames, limiting their applicability to unstructured multi-view datasets. In this work, we introduce Multi-View Consistent 3D Gaussian Splatting Super-Resolution (MVGSR), a framework that focuses on integrating multi-view information for 3DGS rendering with high-frequency details and enhanced consistency. We first propose an Auxiliary View Selection Method based on camera poses, making our method adaptable for arbitrarily organized multi-view datasets without the need of temporal continuity or data reordering. Furthermore, we introduce, for the first time, an epipolar-constrained multi-view attention mechanism into 3DGS SR, which serves as the core of our proposed multi-view SR network. This design enables the model to selectively aggregate consistent information from auxiliary views, enhancing the geometric consistency and detail fidelity of 3DGS representations. Extensive experiments demonstrate that our method achieves state-of-the-art performance on both object-centric and scene-level 3DGS SR benchmarks.

