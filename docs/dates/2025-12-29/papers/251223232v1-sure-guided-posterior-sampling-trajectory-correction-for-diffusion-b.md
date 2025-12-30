---
layout: default
title: SURE Guided Posterior Sampling: Trajectory Correction for Diffusion-Based Inverse Problems
---

# SURE Guided Posterior Sampling: Trajectory Correction for Diffusion-Based Inverse Problems
**arXiv**：[2512.23232v1](https://arxiv.org/abs/2512.23232) · [PDF](https://arxiv.org/pdf/2512.23232.pdf)  
**作者**：Minwoo Kim, Hongki Lim  

**一句话要点**：提出SURE引导后验采样以解决扩散模型逆问题中的误差累积问题

**关键词**：扩散模型, 逆问题求解, 后验采样, 误差校正, 低计算成本

## 3 点简述
- 扩散模型用于逆问题求解时，迭代方法因误差累积需大量步骤
- SGPS利用SURE梯度更新和PCA噪声估计校正采样轨迹偏差
- 在少于100次NFE下保持高质量重建，优于现有方法

## 摘要（原文）

> Diffusion models have emerged as powerful learned priors for solving inverse problems. However, current iterative solving approaches which alternate between diffusion sampling and data consistency steps typically require hundreds or thousands of steps to achieve high quality reconstruction due to accumulated errors. We address this challenge with SURE Guided Posterior Sampling (SGPS), a method that corrects sampling trajectory deviations using Stein's Unbiased Risk Estimate (SURE) gradient updates and PCA based noise estimation. By mitigating noise induced errors during the critical early and middle sampling stages, SGPS enables more accurate posterior sampling and reduces error accumulation. This allows our method to maintain high reconstruction quality with fewer than 100 Neural Function Evaluations (NFEs). Our extensive evaluation across diverse inverse problems demonstrates that SGPS consistently outperforms existing methods at low NFE counts.

