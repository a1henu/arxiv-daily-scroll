---
layout: default
title: Federated Distillation Assisted Vehicle Edge Caching Scheme Based on Lightweight DDPM
---

# Federated Distillation Assisted Vehicle Edge Caching Scheme Based on Lightweight DDPM
**arXiv**：[2512.09378v1](https://arxiv.org/abs/2512.09378) · [PDF](https://arxiv.org/pdf/2512.09378.pdf)  
**作者**：Xun Li, Qiong Wu, Pingyi Fan, Kezhi Wang, Wen Chen, Khaled B. Letaief  

**一句话要点**：提出基于轻量DDPM的联邦蒸馏辅助车辆边缘缓存方案，以降低通信开销并提升缓存命中率。

**关键词**：车辆边缘缓存, 联邦蒸馏, 轻量去噪扩散概率模型, 通信开销优化, 隐私保护

## 3 点简述
- 核心问题：传统联邦学习在车辆边缘缓存中通信开销大且易因车辆移动导致训练失败。
- 方法要点：结合联邦蒸馏与轻量去噪扩散概率模型，保护隐私并减少模型传输。
- 实验或效果：仿真显示方案对车速变化鲁棒，显著降低通信开销并提高缓存命中百分比。

## 摘要（原文）

> Vehicle edge caching is a promising technology that can significantly reduce the latency for vehicle users (VUs) to access content by pre-caching user-interested content at edge nodes. It is crucial to accurately predict the content that VUs are interested in without exposing their privacy. Traditional federated learning (FL) can protect user privacy by sharing models rather than raw data. However, the training of FL requires frequent model transmission, which can result in significant communication overhead. Additionally, vehicles may leave the road side unit (RSU) coverage area before training is completed, leading to training failures. To address these issues, in this letter, we propose a federated distillation-assisted vehicle edge caching scheme based on lightweight denoising diffusion probabilistic model (LDPM). The simulation results demonstrate that the proposed vehicle edge caching scheme has good robustness to variations in vehicle speed, significantly reducing communication overhead and improving cache hit percentage.

