---
layout: default
title: Memorization Control in Diffusion Models from Denoising-centric Perspective
---

# Memorization Control in Diffusion Models from Denoising-centric Perspective
**arXiv**：[2601.21348v1](https://arxiv.org/abs/2601.21348) · [PDF](https://arxiv.org/pdf/2601.21348.pdf)  
**作者**：Thuy Phuong Vu, Mai Viet Hoang Do, Minhhuy Le, Dinh-Cuong Hoang, Phan Xuan Tan  

**一句话要点**：提出基于去噪视角的时间步采样策略以控制扩散模型中的记忆化问题

**关键词**：扩散模型, 记忆化控制, 去噪过程, 时间步采样, 分布对齐

## 3 点简述
- 核心问题：均匀时间步采样导致去噪步骤学习贡献不均，偏向记忆化训练数据
- 方法要点：调整时间步采样策略，通过置信区间宽度控制学习位置，平衡记忆化与泛化
- 实验效果：在图像和1D信号生成任务中，后移学习重点减少记忆化，改善与训练分布对齐

## 摘要（原文）

> Controlling memorization in diffusion models is critical for applications that require generated data to closely match the training distribution. Existing approaches mainly focus on data centric or model centric modifications, treating the diffusion model as an isolated predictor. In this paper, we study memorization in diffusion models from a denoising centric perspective. We show that uniform timestep sampling leads to unequal learning contributions across denoising steps due to differences in signal to noise ratio, which biases training toward memorization. To address this, we propose a timestep sampling strategy that explicitly controls where learning occurs along the denoising trajectory. By adjusting the width of the confidence interval, our method provides direct control over the memorization generalization trade off. Experiments on image and 1D signal generation tasks demonstrate that shifting learning emphasis toward later denoising steps consistently reduces memorization and improves distributional alignment with training data, validating the generality and effectiveness of our approach.

