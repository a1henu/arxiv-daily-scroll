---
layout: default
title: FSampler: Training Free Acceleration of Diffusion Sampling via Epsilon Extrapolation
---

# FSampler: Training Free Acceleration of Diffusion Sampling via Epsilon Extrapolation
**arXiv**：[2511.09180v1](https://arxiv.org/abs/2511.09180) · [PDF](https://arxiv.org/pdf/2511.09180.pdf)  
**作者**：Michael A. Vladimir  

**一句话要点**：提出FSampler以加速扩散采样，无需训练且兼容多种采样器。

**关键词**：扩散模型, 采样加速, 训练自由方法, 函数评估优化, 外推预测

## 3 点简述
- 核心问题：扩散采样函数评估次数多，导致计算成本高。
- 方法要点：基于历史去噪信号外推预测，减少模型调用。
- 实验效果：在多个模型上减少15-50%模型调用，保持高保真度。

## 摘要（原文）

> FSampler is a training free, sampler agnostic execution layer that accelerates diffusion sampling by reducing the number of function evaluations (NFE). FSampler maintains a short history of denoising signals (epsilon) from recent real model calls and extrapolates the next epsilon using finite difference predictors at second order, third order, or fourth order, falling back to lower order when history is insufficient. On selected steps the predicted epsilon substitutes the model call while keeping each sampler's update rule unchanged. Predicted epsilons are validated for finiteness and magnitude; a learning stabilizer rescales predictions on skipped steps to correct drift, and an optional gradient estimation stabilizer compensates local curvature. Protected windows, periodic anchors, and a cap on consecutive skips bound deviation over the trajectory. Operating at the sampler level, FSampler integrates with Euler/DDIM, DPM++ 2M/2S, LMS/AB2, and RES family exponential multistep methods and drops into standard workflows. FLUX.1 dev, Qwen Image, and Wan 2.2, FSampler reduces time by 8 to 22% and model calls by 15 to 25% at high fidelity (Structural Similarity Index (SSIM) 0.95 to 0.99), without altering sampler formulas. With an aggressive adaptive gate, reductions can reach 45 to 50% fewer model calls at lower fidelity (SSIM 0.73 to 0.74).

