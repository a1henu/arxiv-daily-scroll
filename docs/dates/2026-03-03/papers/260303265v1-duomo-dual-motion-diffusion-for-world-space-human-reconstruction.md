---
layout: default
title: DuoMo: Dual Motion Diffusion for World-Space Human Reconstruction
---

# DuoMo: Dual Motion Diffusion for World-Space Human Reconstruction
**arXiv**：[2603.03265v1](https://arxiv.org/abs/2603.03265) · [PDF](https://arxiv.org/pdf/2603.03265.pdf)  
**作者**：Yufu Wang, Evonne Ng, Soyong Shin, Rawal Khirodkar, Yuan Dong, Zhaoen Su, Jinhyung Park, Kris Kitani, Alexander Richard, Fabian Prada, Michael Zollhofer  

**一句话要点**：提出DuoMo双运动扩散方法，从无约束视频中恢复世界坐标下的人体运动

**关键词**：世界坐标人体重建, 运动扩散模型, 无约束视频分析, 全局运动一致性, 非参数化网格生成

## 3 点简述
- 核心问题：从噪声或不完整视频中重建全局一致的世界坐标人体运动，需平衡泛化性与一致性
- 方法要点：通过相机空间和世界空间两个扩散模型分解运动学习，先估计相机坐标运动再提升至世界坐标并优化
- 实验或效果：在EMDB和RICH数据集上实现世界空间重建误差显著降低，保持低脚滑移，性能达到最先进水平

## 摘要（原文）

> We present DuoMo, a generative method that recovers human motion in world-space coordinates from unconstrained videos with noisy or incomplete observations. Reconstructing such motion requires solving a fundamental trade-off: generalizing from diverse and noisy video inputs while maintaining global motion consistency. Our approach addresses this problem by factorizing motion learning into two diffusion models. The camera-space model first estimates motion from videos in camera coordinates. The world-space model then lifts this initial estimate into world coordinates and refines it to be globally consistent. Together, the two models can reconstruct motion across diverse scenes and trajectories, even from highly noisy or incomplete observations. Moreover, our formulation is general, generating the motion of mesh vertices directly and bypassing parametric models. DuoMo achieves state-of-the-art performance. On EMDB, our method obtains a 16% reduction in world-space reconstruction error while maintaining low foot skating. On RICH, it obtains a 30% reduction in world-space error. Project page: https://yufu-wang.github.io/duomo/

