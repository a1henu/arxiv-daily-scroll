---
layout: default
title: MonarchRT: Efficient Attention for Real-Time Video Generation
---

# MonarchRT: Efficient Attention for Real-Time Video Generation
**arXiv**：[2602.12271v1](https://arxiv.org/abs/2602.12271) · [PDF](https://arxiv.org/pdf/2602.12271.pdf)  
**作者**：Krish Agarwal, Zhuoming Chen, Cheng Luo, Yongqi Chen, Haizhong Zheng, Xun Huang, Atri Rudra, Beidi Chen  

**一句话要点**：提出Monarch-RT结构化注意力参数化方法，以解决实时视频生成中3D自注意力的计算瓶颈。

**关键词**：实时视频生成, 注意力机制, 结构化参数化, 计算效率, 扩散变换器, 稀疏注意力

## 3 点简述
- 核心问题：实时视频生成中，3D自注意力的二次计算成本成为瓶颈，尤其在少步和自回归场景下，误差随时间累积。
- 方法要点：基于Monarch矩阵因子化注意力，通过块结构对齐和扩展的平铺参数化，实现高表达力与计算效率。
- 实验或效果：在Self-Forcing模型上达到95%注意力稀疏性且无质量损失，优化实现比FlashAttention内核快1.4-11.8倍，单RTX 5090实现16 FPS实时生成。

## 摘要（原文）

> Real-time video generation with Diffusion Transformers is bottlenecked by the quadratic cost of 3D self-attention, especially in real-time regimes that are both few-step and autoregressive, where errors compound across time and each denoising step must carry substantially more information. In this setting, we find that prior sparse-attention approximations break down, despite showing strong results for bidirectional, many-step diffusion. Specifically, we observe that video attention is not reliably sparse, but instead combines pronounced periodic structure driven by spatiotemporal position with dynamic, sparse semantic correspondences and dense mixing, exceeding the representational capacity of even oracle top-k attention. Building on this insight, we propose Monarch-RT, a structured attention parameterization for video diffusion models that factorizes attention using Monarch matrices. Through appropriately aligned block structure and our extended tiled Monarch parameterization, we achieve high expressivity while preserving computational efficiency. We further overcome the overhead of parameterization through finetuning, with custom Triton kernels. We first validate the high efficacy of Monarch-RT over existing sparse baselines designed only for bidirectional models. We further observe that Monarch-RT attains up to 95% attention sparsity with no loss in quality when applied to the state-of-the-art model Self-Forcing, making Monarch-RT a pioneering work on highly-capable sparse attention parameterization for real-time video generation. Our optimized implementation outperforms FlashAttention-2, FlashAttention-3, and FlashAttention-4 kernels on Nvidia RTX 5090, H100, and B200 GPUs respectively, providing kernel speedups in the range of 1.4-11.8X. This enables us, for the first time, to achieve true real-time video generation with Self-Forcing at 16 FPS on a single RTX 5090.

