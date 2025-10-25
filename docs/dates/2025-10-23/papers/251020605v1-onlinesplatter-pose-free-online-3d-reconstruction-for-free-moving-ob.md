---
layout: default
title: OnlineSplatter: Pose-Free Online 3D Reconstruction for Free-Moving Objects
---

# OnlineSplatter: Pose-Free Online 3D Reconstruction for Free-Moving Objects
**arXiv**：[2510.20605v1](https://arxiv.org/abs/2510.20605) · [PDF](https://arxiv.org/pdf/2510.20605.pdf)  
**作者**：Mark He Huang, Lin Geng Foo, Christian Theobalt, Ying Sun, De Wen Soh  

**一句话要点**：提出OnlineSplatter以解决无姿态自由移动物体的在线3D重建问题

**关键词**：在线3D重建, 自由移动物体, 高斯表示, 无姿态重建, 记忆模块, 前馈框架

## 3 点简述
- 核心问题：单目视频中自由移动物体的3D重建，缺乏可靠姿态或深度线索。
- 方法要点：使用双键记忆模块融合特征，实现前馈在线重建，计算成本恒定。
- 实验或效果：在真实数据集上优于先进基线，性能随观察增加而提升。

## 摘要（原文）

> Free-moving object reconstruction from monocular video remains challenging,
> particularly without reliable pose or depth cues and under arbitrary object
> motion. We introduce OnlineSplatter, a novel online feed-forward framework
> generating high-quality, object-centric 3D Gaussians directly from RGB frames
> without requiring camera pose, depth priors, or bundle optimization. Our
> approach anchors reconstruction using the first frame and progressively refines
> the object representation through a dense Gaussian primitive field, maintaining
> constant computational cost regardless of video sequence length. Our core
> contribution is a dual-key memory module combining latent appearance-geometry
> keys with explicit directional keys, robustly fusing current frame features
> with temporally aggregated object states. This design enables effective
> handling of free-moving objects via spatial-guided memory readout and an
> efficient sparsification mechanism, ensuring comprehensive yet compact object
> coverage. Evaluations on real-world datasets demonstrate that OnlineSplatter
> significantly outperforms state-of-the-art pose-free reconstruction baselines,
> consistently improving with more observations while maintaining constant memory
> and runtime.

