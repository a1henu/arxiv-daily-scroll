---
layout: default
title: ETC: training-free diffusion models acceleration with Error-aware Trend Consistency
---

# ETC: training-free diffusion models acceleration with Error-aware Trend Consistency
**arXiv**：[2510.24129v1](https://arxiv.org/abs/2510.24129) · [PDF](https://arxiv.org/pdf/2510.24129.pdf)  
**作者**：Jiajian Xie, Hubery Yin, Chen Li, Zhou Zhao, Shengyu Zhang  

**一句话要点**：提出误差感知趋势一致性框架以加速扩散模型采样

**关键词**：扩散模型加速, 训练免费方法, 趋势一致性, 误差容忍, 采样优化

## 3 点简述
- 核心问题：训练免费扩散模型加速方法忽略去噪趋势和误差控制，导致轨迹偏差
- 方法要点：引入一致趋势预测器和模型特定误差容忍搜索机制，稳定加速采样
- 实验或效果：在FLUX上实现2.65倍加速，一致性退化可忽略（SSIM下降0.074）

## 摘要（原文）

> Diffusion models have achieved remarkable generative quality but remain
> bottlenecked by costly iterative sampling. Recent training-free methods
> accelerate diffusion process by reusing model outputs. However, these methods
> ignore denoising trends and lack error control for model-specific tolerance,
> leading to trajectory deviations under multi-step reuse and exacerbating
> inconsistencies in the generated results. To address these issues, we introduce
> Error-aware Trend Consistency (ETC), a framework that (1) introduces a
> consistent trend predictor that leverages the smooth continuity of diffusion
> trajectories, projecting historical denoising patterns into stable future
> directions and progressively distributing them across multiple approximation
> steps to achieve acceleration without deviating; (2) proposes a model-specific
> error tolerance search mechanism that derives corrective thresholds by
> identifying transition points from volatile semantic planning to stable quality
> refinement. Experiments show that ETC achieves a 2.65x acceleration over FLUX
> with negligible (-0.074 SSIM score) degradation of consistency.

