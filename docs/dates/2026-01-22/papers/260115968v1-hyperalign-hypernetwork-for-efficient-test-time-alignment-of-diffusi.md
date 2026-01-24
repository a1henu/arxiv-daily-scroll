---
layout: default
title: HyperAlign: Hypernetwork for Efficient Test-Time Alignment of Diffusion Models
---

# HyperAlign: Hypernetwork for Efficient Test-Time Alignment of Diffusion Models
**arXiv**：[2601.15968v1](https://arxiv.org/abs/2601.15968) · [PDF](https://arxiv.org/pdf/2601.15968.pdf)  
**作者**：Xin Xie, Jiaxian Guo, Dong Gong  

**一句话要点**：提出HyperAlign超网络框架，以高效测试时对齐扩散模型，提升生成图像与人类偏好的一致性。

**关键词**：扩散模型对齐, 超网络训练, 测试时优化, 低秩适配, 奖励条件生成, 图像生成质量

## 3 点简述
- 核心问题：扩散模型生成图像常与人类偏好不一致，现有对齐方法在多样性与计算开销间难以权衡。
- 方法要点：训练超网络动态生成低秩适配权重，基于输入隐变量、时间步和提示调整去噪轨迹，实现奖励条件对齐。
- 实验或效果：在Stable Diffusion和FLUX等模型上评估，显著优于微调和测试时缩放基线，增强语义一致性和视觉吸引力。

## 摘要（原文）

> Diffusion models achieve state-of-the-art performance but often fail to generate outputs that align with human preferences and intentions, resulting in images with poor aesthetic quality and semantic inconsistencies. Existing alignment methods present a difficult trade-off: fine-tuning approaches suffer from loss of diversity with reward over-optimization, while test-time scaling methods introduce significant computational overhead and tend to under-optimize. To address these limitations, we propose HyperAlign, a novel framework that trains a hypernetwork for efficient and effective test-time alignment. Instead of modifying latent states, HyperAlign dynamically generates low-rank adaptation weights to modulate the diffusion model's generation operators. This allows the denoising trajectory to be adaptively adjusted based on input latents, timesteps and prompts for reward-conditioned alignment. We introduce multiple variants of HyperAlign that differ in how frequently the hypernetwork is applied, balancing between performance and efficiency. Furthermore, we optimize the hypernetwork using a reward score objective regularized with preference data to reduce reward hacking. We evaluate HyperAlign on multiple extended generative paradigms, including Stable Diffusion and FLUX. It significantly outperforms existing fine-tuning and test-time scaling baselines in enhancing semantic consistency and visual appeal.

