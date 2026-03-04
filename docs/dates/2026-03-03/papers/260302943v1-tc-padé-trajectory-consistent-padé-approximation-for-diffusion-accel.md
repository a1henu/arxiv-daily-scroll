---
layout: default
title: TC-Padé: Trajectory-Consistent Padé Approximation for Diffusion Acceleration
---

# TC-Padé: Trajectory-Consistent Padé Approximation for Diffusion Acceleration
**arXiv**：[2603.02943v1](https://arxiv.org/abs/2603.02943) · [PDF](https://arxiv.org/pdf/2603.02943.pdf)  
**作者**：Benlei Cui, Shaoxuan He, Bukun Huang, Zhizeng Ye, Yunyun Sun, Longtao Huang, Hui Xue, Yang Yang, Jingqun Tang, Zhou Zhao, Haiwen Hong  

**一句话要点**：提出轨迹一致Padé近似以加速扩散模型采样，解决低步数下特征缓存误差累积问题。

**关键词**：扩散模型加速, 特征缓存, Padé近似, 轨迹一致性, 采样优化, 图像视频生成

## 3 点简述
- 核心问题：扩散模型迭代采样计算负担重，现有特征缓存在20-30步低步数下因误差累积导致轨迹漂移。
- 方法要点：基于Padé近似建模特征演化，结合自适应系数调制和阶段感知预测策略，提升轨迹一致性。
- 实验或效果：在DiT-XL/2、FLUX.1-dev和Wan2.1上验证，实现最高2.88倍加速，质量指标优于现有方法。

## 摘要（原文）

> Despite achieving state-of-the-art generation quality, diffusion models are hindered by the substantial computational burden of their iterative sampling process. While feature caching techniques achieve effective acceleration at higher step counts (e.g., 50 steps), they exhibit critical limitations in the practical low-step regime of 20-30 steps. As the interval between steps increases, polynomial-based extrapolators like TaylorSeer suffer from error accumulation and trajectory drift. Meanwhile, conventional caching strategies often overlook the distinct dynamical properties of different denoising phases. To address these challenges, we propose Trajectory-Consistent Padé approximation, a feature prediction framework grounded in Padé approximation. By modeling feature evolution through rational functions, our approach captures asymptotic and transitional behaviors more accurately than Taylor-based methods. To enable stable and trajectory-consistent sampling under reduced step counts, TC-Padé incorporates (1) adaptive coefficient modulation that leverages historical cached residuals to detect subtle trajectory transitions, and (2) step-aware prediction strategies tailored to the distinct dynamics of early, mid, and late sampling stages. Extensive experiments on DiT-XL/2, FLUX.1-dev, and Wan2.1 across both image and video generation demonstrate the effectiveness of TC-Padé. For instance, TC-Padé achieves 2.88x acceleration on FLUX.1-dev and 1.72x on Wan2.1 while maintaining high quality across FID, CLIP, Aesthetic, and VBench-2.0 metrics, substantially outperforming existing feature caching methods.

