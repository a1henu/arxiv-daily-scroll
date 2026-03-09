---
layout: default
title: WorldCache: Accelerating World Models for Free via Heterogeneous Token Caching
---

# WorldCache: Accelerating World Models for Free via Heterogeneous Token Caching
**arXiv**：[2603.06331v1](https://arxiv.org/abs/2603.06331) · [PDF](https://arxiv.org/pdf/2603.06331.pdf)  
**作者**：Weilun Feng, Guoxin Fan, Haotong Qin, Chuanguang Yang, Mingqiang Wu, Yuqi Li, Xiangqi Li, Zhulin An, Libo Huang, Dingrui Wang, Longlong Liao, Michele Magno, Yongjun Xu  

**一句话要点**：提出WorldCache框架，通过异构令牌缓存加速扩散世界模型推理

**关键词**：扩散世界模型, 推理加速, 令牌缓存, 异构令牌预测, 自适应跳过, 资源受限计算

## 3 点简述
- 扩散世界模型推理成本高，特征缓存面临令牌异构性和非均匀时间动态性挑战
- 引入曲率引导异构令牌预测和混沌优先自适应跳过，针对性处理令牌异质性和动态变化
- 实验显示WorldCache实现最高3.7倍加速，保持98%推演质量，适用于资源受限场景

## 摘要（原文）

> Diffusion-based world models have shown strong potential for unified world simulation, but the iterative denoising remains too costly for interactive use and long-horizon rollouts. While feature caching can accelerate inference without training, we find that policies designed for single-modal diffusion transfer poorly to world models due to two world-model-specific obstacles: \emph{token heterogeneity} from multi-modal coupling and spatial variation, and \emph{non-uniform temporal dynamics} where a small set of hard tokens drives error growth, making uniform skipping either unstable or overly conservative. We propose \textbf{WorldCache}, a caching framework tailored to diffusion world models. We introduce \textit{Curvature-guided Heterogeneous Token Prediction}, which uses a physics-grounded curvature score to estimate token predictability and applies a Hermite-guided damped predictor for chaotic tokens with abrupt direction changes. We also design \textit{Chaotic-prioritized Adaptive Skipping}, which accumulates a curvature-normalized, dimensionless drift signal and recomputes only when bottleneck tokens begin to drift. Experiments on diffusion world models show that WorldCache delivers up to \textbf{3.7$\times$} end-to-end speedups while maintaining \textbf{98\%} rollout quality, demonstrating the vast advantages and practicality of WorldCache in resource-constrained scenarios. Our code is released in https://github.com/FofGofx/WorldCache.

