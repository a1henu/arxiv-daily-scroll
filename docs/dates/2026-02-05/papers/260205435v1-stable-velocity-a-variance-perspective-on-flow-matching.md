---
layout: default
title: Stable Velocity: A Variance Perspective on Flow Matching
---

# Stable Velocity: A Variance Perspective on Flow Matching
**arXiv**：[2602.05435v1](https://arxiv.org/abs/2602.05435) · [PDF](https://arxiv.org/pdf/2602.05435.pdf)  
**作者**：Donglin Yang, Yongxing Zhang, Xin Yu, Liang Hou, Xin Tao, Pengfei Wan, Xiaojuan Qi, Renjie Liao  

**一句话要点**：提出Stable Velocity框架，通过方差视角改进流匹配的训练稳定性和采样效率。

**关键词**：流匹配, 方差减少, 训练稳定性, 采样加速, 生成模型, 条件速度

## 3 点简述
- 核心问题：流匹配依赖单样本条件速度导致高方差训练目标，优化不稳定且收敛慢。
- 方法要点：提出StableVM方差减少目标和VA-REPA自适应监督，并在低方差区域实现闭式采样加速。
- 实验或效果：在ImageNet和大模型上提升训练效率，采样速度超2倍且质量不降。

## 摘要（原文）

> While flow matching is elegant, its reliance on single-sample conditional velocities leads to high-variance training targets that destabilize optimization and slow convergence. By explicitly characterizing this variance, we identify 1) a high-variance regime near the prior, where optimization is challenging, and 2) a low-variance regime near the data distribution, where conditional and marginal velocities nearly coincide. Leveraging this insight, we propose Stable Velocity, a unified framework that improves both training and sampling. For training, we introduce Stable Velocity Matching (StableVM), an unbiased variance-reduction objective, along with Variance-Aware Representation Alignment (VA-REPA), which adaptively strengthen auxiliary supervision in the low-variance regime. For inference, we show that dynamics in the low-variance regime admit closed-form simplifications, enabling Stable Velocity Sampling (StableVS), a finetuning-free acceleration. Extensive experiments on ImageNet $256\times256$ and large pretrained text-to-image and text-to-video models, including SD3.5, Flux, Qwen-Image, and Wan2.2, demonstrate consistent improvements in training efficiency and more than $2\times$ faster sampling within the low-variance regime without degrading sample quality. Our code is available at https://github.com/linYDTHU/StableVelocity.

