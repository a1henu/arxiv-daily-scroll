---
layout: default
title: TurboDiffusion: Accelerating Video Diffusion Models by 100-200 Times
---

# TurboDiffusion: Accelerating Video Diffusion Models by 100-200 Times
**arXiv**：[2512.16093v1](https://arxiv.org/abs/2512.16093) · [PDF](https://arxiv.org/pdf/2512.16093.pdf)  
**作者**：Jintao Zhang, Kaiwen Zheng, Kai Jiang, Haoxu Wang, Ion Stoica, Joseph E. Gonzalez, Jianfei Chen, Jun Zhu  

**一句话要点**：提出TurboDiffusion框架，加速视频扩散模型100-200倍，保持视频质量。

**关键词**：视频生成加速, 注意力优化, 步数蒸馏, 模型量化, 扩散模型

## 3 点简述
- 核心问题：视频扩散模型生成速度慢，需加速以提升实用性。
- 方法要点：采用注意力加速、步数蒸馏和W8A8量化等技术优化计算。
- 实验效果：在多个模型上实现100-200倍加速，单GPU运行，质量可比。

## 摘要（原文）

> We introduce TurboDiffusion, a video generation acceleration framework that can speed up end-to-end diffusion generation by 100-200x while maintaining video quality. TurboDiffusion mainly relies on several components for acceleration: (1) Attention acceleration: TurboDiffusion uses low-bit SageAttention and trainable Sparse-Linear Attention (SLA) to speed up attention computation. (2) Step distillation: TurboDiffusion adopts rCM for efficient step distillation. (3) W8A8 quantization: TurboDiffusion quantizes model parameters and activations to 8 bits to accelerate linear layers and compress the model. In addition, TurboDiffusion incorporates several other engineering optimizations.
>   We conduct experiments on the Wan2.2-I2V-14B-720P, Wan2.1-T2V-1.3B-480P, Wan2.1-T2V-14B-720P, and Wan2.1-T2V-14B-480P models. Experimental results show that TurboDiffusion achieves 100-200x speedup for video generation even on a single RTX 5090 GPU, while maintaining comparable video quality. The GitHub repository, which includes model checkpoints and easy-to-use code, is available at https://github.com/thu-ml/TurboDiffusion.

