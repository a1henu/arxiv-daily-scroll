---
layout: default
title: TauFlow: Dynamic Causal Constraint for Complexity-Adaptive Lightweight Segmentation
---

# TauFlow: Dynamic Causal Constraint for Complexity-Adaptive Lightweight Segmentation
**arXiv**：[2511.07057v1](https://arxiv.org/abs/2511.07057) · [PDF](https://arxiv.org/pdf/2511.07057.pdf)  
**作者**：Zidong Chen, Fadratul Hafinaz Hassan  

**一句话要点**：提出TauFlow模型以解决边缘设备上轻量级医学图像分割的精度下降和边界处理问题

**关键词**：轻量级分割, 动态特征响应, 医学图像处理, 边缘计算, 脑启发机制

## 3 点简述
- 核心问题：轻量模型在边缘设备部署时，处理病变边界与背景对比及参数减少导致的精度下降
- 方法要点：引入动态特征响应策略，包括ConvLTC调节特征更新率和STDP模块减少编码器-解码器冲突
- 实验或效果：STDP模块将特征冲突率从约35%-40%降低至8%-10%，提升模型性能

## 摘要（原文）

> Deploying lightweight medical image segmentation models on edge devices
> presents two major challenges: 1) efficiently handling the stark contrast
> between lesion boundaries and background regions, and 2) the sharp drop in
> accuracy that occurs when pursuing extremely lightweight designs (e.g., <0.5M
> parameters). To address these problems, this paper proposes TauFlow, a novel
> lightweight segmentation model. The core of TauFlow is a dynamic feature
> response strategy inspired by brain-like mechanisms. This is achieved through
> two key innovations: the Convolutional Long-Time Constant Cell (ConvLTC), which
> dynamically regulates the feature update rate to "slowly" process low-frequency
> backgrounds and "quickly" respond to high-frequency boundaries; and the STDP
> Self-Organizing Module, which significantly mitigates feature conflicts between
> the encoder and decoder, reducing the conflict rate from approximately 35%-40%
> to 8%-10%.

