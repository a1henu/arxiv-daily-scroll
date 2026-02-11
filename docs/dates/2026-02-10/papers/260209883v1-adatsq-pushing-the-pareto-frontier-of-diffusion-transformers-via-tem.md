---
layout: default
title: AdaTSQ: Pushing the Pareto Frontier of Diffusion Transformers via Temporal-Sensitivity Quantization
---

# AdaTSQ: Pushing the Pareto Frontier of Diffusion Transformers via Temporal-Sensitivity Quantization
**arXiv**：[2602.09883v1](https://arxiv.org/abs/2602.09883) · [PDF](https://arxiv.org/pdf/2602.09883.pdf)  
**作者**：Shaoqiu Zhang, Zizhong Ding, Kaicheng Yang, Junyi Wu, Xianglong Yan, Xi Li, Bingnan Duan, Jianping Fang, Yulun Zhang  

**一句话要点**：提出AdaTSQ框架，通过时间敏感量化提升扩散变换器的效率与质量平衡

**关键词**：扩散变换器, 后训练量化, 时间敏感量化, 帕累托优化, Fisher信息, 边缘部署

## 3 点简述
- 核心问题：扩散变换器计算成本高，现有量化方法忽视其时间动态特性，导致效果不佳
- 方法要点：采用帕累托感知的时间步动态位宽分配和Fisher引导的时间校准机制，优化量化策略
- 实验或效果：在多个先进扩散变换器上验证，AdaTSQ显著优于SVDQuant和ViDiT-Q等现有方法

## 摘要（原文）

> Diffusion Transformers (DiTs) have emerged as the state-of-the-art backbone for high-fidelity image and video generation. However, their massive computational cost and memory footprint hinder deployment on edge devices. While post-training quantization (PTQ) has proven effective for large language models (LLMs), directly applying existing methods to DiTs yields suboptimal results due to the neglect of the unique temporal dynamics inherent in diffusion processes. In this paper, we propose AdaTSQ, a novel PTQ framework that pushes the Pareto frontier of efficiency and quality by exploiting the temporal sensitivity of DiTs. First, we propose a Pareto-aware timestep-dynamic bit-width allocation strategy. We model the quantization policy search as a constrained pathfinding problem. We utilize a beam search algorithm guided by end-to-end reconstruction error to dynamically assign layer-wise bit-widths across different timesteps. Second, we propose a Fisher-guided temporal calibration mechanism. It leverages temporal Fisher information to prioritize calibration data from highly sensitive timesteps, seamlessly integrating with Hessian-based weight optimization. Extensive experiments on four advanced DiTs (e.g., Flux-Dev, Flux-Schnell, Z-Image, and Wan2.1) demonstrate that AdaTSQ significantly outperforms state-of-the-art methods like SVDQuant and ViDiT-Q. Our code will be released at https://github.com/Qiushao-E/AdaTSQ.

