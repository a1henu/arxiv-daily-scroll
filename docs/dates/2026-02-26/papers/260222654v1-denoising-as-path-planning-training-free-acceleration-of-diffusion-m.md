---
layout: default
title: Denoising as Path Planning: Training-Free Acceleration of Diffusion Models with DPCache
---

# Denoising as Path Planning: Training-Free Acceleration of Diffusion Models with DPCache
**arXiv**：[2602.22654v1](https://arxiv.org/abs/2602.22654) · [PDF](https://arxiv.org/pdf/2602.22654.pdf)  
**作者**：Bowen Cui, Yuanbin Wang, Huajiang Xu, Biaolong Chen, Aixi Zhang, Hao Jiang, Zhengzheng Jin, Xu Liu, Pipei Huang  

**一句话要点**：提出DPCache框架，将扩散模型去噪加速建模为全局路径规划问题，实现免训练高效采样。

**关键词**：扩散模型加速, 免训练采样, 路径规划, 缓存优化, 动态规划, 图像生成

## 3 点简述
- 核心问题：扩散模型多步迭代采样计算开销大，现有缓存方法忽略去噪轨迹全局结构，易导致误差累积和视觉伪影。
- 方法要点：构建路径感知成本张量量化跳步误差，利用动态规划选择关键时间步序列以最小化总路径成本，保持轨迹保真度。
- 实验或效果：在DiT、FLUX和HunyuanVideo上验证，DPCache在加速同时质量损失小，优于先前方法，部分场景甚至超越全步基线。

## 摘要（原文）

> Diffusion models have demonstrated remarkable success in image and video generation, yet their practical deployment remains hindered by the substantial computational overhead of multi-step iterative sampling. Among acceleration strategies, caching-based methods offer a training-free and effective solution by reusing or predicting features across timesteps. However, existing approaches rely on fixed or locally adaptive schedules without considering the global structure of the denoising trajectory, often leading to error accumulation and visual artifacts. To overcome this limitation, we propose DPCache, a novel training-free acceleration framework that formulates diffusion sampling acceleration as a global path planning problem. DPCache constructs a Path-Aware Cost Tensor from a small calibration set to quantify the path-dependent error of skipping timesteps conditioned on the preceding key timestep. Leveraging this tensor, DPCache employs dynamic programming to select an optimal sequence of key timesteps that minimizes the total path cost while preserving trajectory fidelity. During inference, the model performs full computations only at these key timesteps, while intermediate outputs are efficiently predicted using cached features. Extensive experiments on DiT, FLUX, and HunyuanVideo demonstrate that DPCache achieves strong acceleration with minimal quality loss, outperforming prior acceleration methods by $+$0.031 ImageReward at 4.87$\times$ speedup and even surpassing the full-step baseline by $+$0.028 ImageReward at 3.54$\times$ speedup on FLUX, validating the effectiveness of our path-aware global scheduling framework. Code will be released at https://github.com/argsss/DPCache.

