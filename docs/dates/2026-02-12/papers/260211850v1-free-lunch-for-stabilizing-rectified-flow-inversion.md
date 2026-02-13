---
layout: default
title: Free Lunch for Stabilizing Rectified Flow Inversion
---

# Free Lunch for Stabilizing Rectified Flow Inversion
**arXiv**：[2602.11850v1](https://arxiv.org/abs/2602.11850) · [PDF](https://arxiv.org/pdf/2602.11850.pdf)  
**作者**：Chenru Wang, Beier Zhu, Chi Zhang  

**一句话要点**：提出Proximal-Mean Inversion以稳定Rectified Flow反演，提升重建与编辑质量

**关键词**：Rectified Flow反演, 速度场稳定, 训练自由方法, 图像重建, 图像编辑, PIE-Bench

## 3 点简述
- Rectified Flow反演存在近似误差累积，导致速度场不稳定和重建编辑质量下降
- 提出PMI方法，通过梯度校正引导速度场向历史平均移动，并引入mimic-CFG平衡编辑效果与结构一致性
- 在PIE-Bench上实验显示，方法显著提升反演稳定性、重建质量和编辑保真度，同时减少计算开销

## 摘要（原文）

> Rectified-Flow (RF)-based generative models have recently emerged as strong alternatives to traditional diffusion models, demonstrating state-of-the-art performance across various tasks. By learning a continuous velocity field that transforms simple noise into complex data, RF-based models not only enable high-quality generation, but also support training-free inversion, which facilitates downstream tasks such as reconstruction and editing. However, existing inversion methods, such as vanilla RF-based inversion, suffer from approximation errors that accumulate across timesteps, leading to unstable velocity fields and degraded reconstruction and editing quality. To address this challenge, we propose Proximal-Mean Inversion (PMI), a training-free gradient correction method that stabilizes the velocity field by guiding it toward a running average of past velocities, constrained within a theoretically derived spherical Gaussian. Furthermore, we introduce mimic-CFG, a lightweight velocity correction scheme for editing tasks, which interpolates between the current velocity and its projection onto the historical average, balancing editing effectiveness and structural consistency. Extensive experiments on PIE-Bench demonstrate that our methods significantly improve inversion stability, image reconstruction quality, and editing fidelity, while reducing the required number of neural function evaluations. Our approach achieves state-of-the-art performance on the PIE-Bench with enhanced efficiency and theoretical soundness.

