---
layout: default
title: Pip-Stereo: Progressive Iterations Pruner for Iterative Optimization based Stereo Matching
---

# Pip-Stereo: Progressive Iterations Pruner for Iterative Optimization based Stereo Matching
**arXiv**：[2602.20496v1](https://arxiv.org/abs/2602.20496) · [PDF](https://arxiv.org/pdf/2602.20496.pdf)  
**作者**：Jintu Zheng, Qizhe Liu, HuangXin Xu, Zhuojie Chen  

**一句话要点**：提出Pip-Stereo以解决迭代立体匹配在边缘部署中的效率问题

**关键词**：立体匹配, 迭代优化, 边缘计算, 硬件加速, 实时处理, 稀疏更新

## 3 点简述
- 核心问题：迭代立体匹配依赖RNN导致边缘部署困难，更新存在时空冗余
- 方法要点：引入渐进迭代剪枝策略和协作单目先验转移框架，无需专用编码器
- 实验或效果：在边缘硬件上实现实时高精度，如Jetson Orin NX上75ms处理320×640帧

## 摘要（原文）

> While iterative stereo matching achieves high accuracy, its dependence on Recurrent Neural Networks (RNN) hinders edge deployment, a challenge underexplored in existing researches. We analyze iterative refinement and reveal that disparity updates are spatially sparse and temporally redundant. First, we introduce a progressive iteration pruning strategy that suppresses redundant update steps, effectively collapsing the recursive computation into a near-single-pass inference. Second, we propose a collaborative monocular prior transfer framework that implicitly embeds depth priors without requiring a dedicated monocular encoder, thereby eliminating its associated computational burden. Third, we develop FlashGRU, a hardware-aware RNN operator leveraging structured sparsity and I/O-conscious design, achieving a 7.28$\times$ speedup, 76.6\% memory peak reduction and 80.9\% global memory requests reduction over natvie ConvGRUs under 2K resolution. Our PipStereo enables real-time, high-fidelity stereo matching on edge hardware: it processes 320$\times$640 frames in just 75ms on an NVIDIA Jetson Orin NX (FP16) and 19ms on RTX 4090, matching the accuracy of large iterative based models, and our generalization ability and accuracy far exceeds that of existing real-time methods. Our embedded AI projects will be updated at: https://github.com/XPENG-Aridge-AI.

