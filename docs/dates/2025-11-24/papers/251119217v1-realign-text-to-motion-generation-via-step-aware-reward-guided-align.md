---
layout: default
title: ReAlign: Text-to-Motion Generation via Step-Aware Reward-Guided Alignment
---

# ReAlign: Text-to-Motion Generation via Step-Aware Reward-Guided Alignment
**arXiv**：[2511.19217v1](https://arxiv.org/abs/2511.19217) · [PDF](https://arxiv.org/pdf/2511.19217.pdf)  
**作者**：Wanjiang Weng, Xiaofeng Tan, Junbo Wang, Guo-Sen Xie, Pan Zhou, Hongsong Wang  

**一句话要点**：提出ReAlign方法，通过奖励引导对齐解决文本到运动生成中的语义不一致问题

**关键词**：文本到运动生成, 扩散模型, 奖励引导对齐, 步感知奖励, 语义一致性, 运动质量优化

## 3 点简述
- 核心问题：扩散模型中文本与运动分布不匹配，导致语义不一致或低质量运动
- 方法要点：引入步感知奖励模型和奖励引导策略，优化去噪过程以提升对齐
- 实验或效果：在生成和检索任务中显著改进文本-运动对齐和运动质量

## 摘要（原文）

> Text-to-motion generation, which synthesizes 3D human motions from text inputs, holds immense potential for applications in gaming, film, and robotics. Recently, diffusion-based methods have been shown to generate more diversity and realistic motion. However, there exists a misalignment between text and motion distributions in diffusion models, which leads to semantically inconsistent or low-quality motions. To address this limitation, we propose Reward-guided sampling Alignment (ReAlign), comprising a step-aware reward model to assess alignment quality during the denoising sampling and a reward-guided strategy that directs the diffusion process toward an optimally aligned distribution. This reward model integrates step-aware tokens and combines a text-aligned module for semantic consistency and a motion-aligned module for realism, refining noisy motions at each timestep to balance probability density and alignment. Extensive experiments of both motion generation and retrieval tasks demonstrate that our approach significantly improves text-motion alignment and motion quality compared to existing state-of-the-art methods.

