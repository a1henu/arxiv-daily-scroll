---
layout: default
title: Optimizing Decoding Paths in Masked Diffusion Models by Quantifying Uncertainty
---

# Optimizing Decoding Paths in Masked Diffusion Models by Quantifying Uncertainty
**arXiv**：[2512.21336v1](https://arxiv.org/abs/2512.21336) · [PDF](https://arxiv.org/pdf/2512.21336.pdf)  
**作者**：Ziyu Chen, Xinbei Jiang, Peng Sun, Tao Lin  

**一句话要点**：提出去噪熵以量化不确定性，优化掩码扩散模型的解码路径

**关键词**：掩码扩散模型, 解码路径优化, 不确定性量化, 去噪熵, 生成质量提升

## 3 点简述
- 核心问题：掩码扩散模型解码顺序敏感，导致输出质量不稳定。
- 方法要点：引入去噪熵度量不确定性，提出后验选择和实时指导算法优化路径。
- 实验或效果：在推理、规划和代码基准上显著提升生成准确性和质量。

## 摘要（原文）

> Masked Diffusion Models (MDMs) offer flexible, non-autoregressive generation, but this freedom introduces a challenge: final output quality is highly sensitive to the decoding order. We are the first to formalize this issue, attributing the variability in output quality to the cumulative predictive uncertainty along a generative path. To quantify this uncertainty, we introduce Denoising Entropy, a computable metric that serves as an internal signal for evaluating generative process. Leveraging this metric, we propose two algorithms designed to optimize the decoding path: a post-hoc selection method and a real-time guidance strategy. Experiments demonstrate that our entropy-guided methods significantly improve generation quality, consistently boosting accuracy on challenging reasoning, planning, and code benchmarks. Our work establishes Denoising Entropy as a principled tool for understanding and controlling generation, effectively turning the uncertainty in MDMs from a liability into a key advantage for discovering high-quality solutions.

