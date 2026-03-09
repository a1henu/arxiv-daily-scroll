---
layout: default
title: RAC: Rectified Flow Auto Coder
---

# RAC: Rectified Flow Auto Coder
**arXiv**：[2603.05925v1](https://arxiv.org/abs/2603.05925) · [PDF](https://arxiv.org/pdf/2603.05925.pdf)  
**作者**：Sen Fang, Yalin Feng, Yanxin Zhang, Dimitris N. Metaxas  

**一句话要点**：提出Rectified Flow Auto Coder以替代传统VAE，提升生成质量并降低计算成本。

**关键词**：Rectified Flow, 自编码器, 生成模型, 多步解码, 双向推理, 计算效率

## 3 点简述
- 核心问题：传统VAE存在重建与生成差距，解码路径可能弯曲，计算成本高。
- 方法要点：基于Rectified Flow设计多步解码，路径直且可校正，支持双向推理减少参数。
- 实验或效果：在重建和生成上超越SOTA VAE，计算成本降低约70%，参数减少近41%。

## 摘要（原文）

> In this paper, we propose a Rectified Flow Auto Coder (RAC) inspired by Rectified Flow to replace the traditional VAE: 1. It achieves multi-step decoding by applying the decoder to flow timesteps. Its decoding path is straight and correctable, enabling step-by-step refinement. 2. The model inherently supports bidirectional inference, where the decoder serves as the encoder through time reversal (hence Coder rather than encoder or decoder), reducing parameter count by nearly 41%. 3. This generative decoding method improves generation quality since the model can correct latent variables along the path, partially addressing the reconstruction--generation gap. Experiments show that RAC surpasses SOTA VAEs in both reconstruction and generation with approximately 70% lower computational cost.

