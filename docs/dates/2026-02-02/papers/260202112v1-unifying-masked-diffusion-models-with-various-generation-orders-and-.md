---
layout: default
title: Unifying Masked Diffusion Models with Various Generation Orders and Beyond
---

# Unifying Masked Diffusion Models with Various Generation Orders and Beyond
**arXiv**：[2602.02112v1](https://arxiv.org/abs/2602.02112) · [PDF](https://arxiv.org/pdf/2602.02112.pdf)  
**作者**：Chunsan Hong, Sanghyun Lee, Jong Chul Ye  

**一句话要点**：提出可表达顺序的掩码扩散模型，统一多种生成顺序并联合学习顺序与扩散主干。

**关键词**：掩码扩散模型, 生成顺序学习, 语言生成, 扩散生成过程, 联合优化

## 3 点简述
- 掩码扩散模型生成质量依赖顺序，现有方法多阶段优化成本高且次优。
- 提出OeMDM统一多种生成顺序，LoMDM联合学习顺序与扩散主干。
- 实验显示LoMDM在多个语言建模基准上优于现有离散扩散模型。

## 摘要（原文）

> Masked diffusion models (MDMs) are a potential alternative to autoregressive models (ARMs) for language generation, but generation quality depends critically on the generation order. Prior work either hard-codes an ordering (e.g., blockwise left-to-right) or learns an ordering policy for a pretrained MDM, which incurs extra cost and can yield suboptimal solutions due to the two-stage optimization. Motivated by this, we propose order-expressive masked diffusion model (OeMDM) for a broad class of diffusion generative processes with various generation orders, enabling the interpretation of MDM, ARM, and block diffusion in a single framework. Furthermore, building on OeMDM, we introduce learnable-order masked diffusion model (LoMDM), which jointly learns the generation ordering and diffusion backbone through a single objective from scratch, enabling the diffusion model to generate text in context-dependent ordering. Empirically, we confirm that LoMDM outperforms various discrete diffusion models across multiple language modeling benchmarks.

