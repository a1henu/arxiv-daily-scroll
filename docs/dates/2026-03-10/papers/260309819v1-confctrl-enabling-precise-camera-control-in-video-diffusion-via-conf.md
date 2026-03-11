---
layout: default
title: ConfCtrl: Enabling Precise Camera Control in Video Diffusion via Confidence-Aware Interpolation
---

# ConfCtrl: Enabling Precise Camera Control in Video Diffusion via Confidence-Aware Interpolation
**arXiv**：[2603.09819v1](https://arxiv.org/abs/2603.09819) · [PDF](https://arxiv.org/pdf/2603.09819.pdf)  
**作者**：Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Yang Bai, Chi Zhang, Ziyuan Liu, Abhinav Valada  

**一句话要点**：提出ConfCtrl框架，通过置信度感知插值实现视频扩散模型中的精确相机控制，以解决大视角变化下的新视角合成问题。

**关键词**：新视角合成, 视频扩散模型, 相机控制, 置信度感知, 几何重建, 大视角变化

## 3 点简述
- 核心问题：现有方法在大视角变化下难以合成新视角，回归方法无法重建未见区域，相机引导扩散模型易偏离轨迹。
- 方法要点：结合置信度加权的点云潜变量初始化扩散过程，采用卡尔曼滤波启发的预测-更新机制平衡相机姿态预测与几何观测。
- 实验或效果：在多个数据集上验证，ConfCtrl能生成几何一致、视觉合理的新视角，有效重建遮挡区域。

## 摘要（原文）

> We address the challenge of novel view synthesis from only two input images under large viewpoint changes. Existing regression-based methods lack the capacity to reconstruct unseen regions, while camera-guided diffusion models often deviate from intended trajectories due to noisy point cloud projections or insufficient conditioning from camera poses. To address these issues, we propose ConfCtrl, a confidence-aware video interpolation framework that enables diffusion models to follow prescribed camera poses while completing unseen regions. ConfCtrl initializes the diffusion process by combining a confidence-weighted projected point cloud latent with noise as the conditioning input. It then applies a Kalman-inspired predict-update mechanism, treating the projected point cloud as a noisy measurement and using learned residual corrections to balance pose-driven predictions with noisy geometric observations. This allows the model to rely on reliable projections while down-weighting uncertain regions, yielding stable, geometry-aware generation. Experiments on multiple datasets show that ConfCtrl produces geometrically consistent and visually plausible novel views, effectively reconstructing occluded regions under large viewpoint changes.

