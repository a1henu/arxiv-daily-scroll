---
layout: default
title: FrameDiT: Diffusion Transformer with Frame-Level Matrix Attention for Efficient Video Generation
---

# FrameDiT: Diffusion Transformer with Frame-Level Matrix Attention for Efficient Video Generation
**arXiv**：[2603.09721v1](https://arxiv.org/abs/2603.09721) · [PDF](https://arxiv.org/pdf/2603.09721.pdf)  
**作者**：Minh Khoa Le, Kien Do, Duc Thanh Nguyen, Truyen Tran  

**一句话要点**：提出FrameDiT，基于帧级矩阵注意力解决视频扩散模型中时空建模效率与效果权衡问题。

**关键词**：视频生成, 扩散变换器, 矩阵注意力, 时空建模, 高效计算

## 3 点简述
- 核心问题：视频扩散模型在高效建模复杂时空动态时面临全局注意力昂贵与局部注意力受限的权衡。
- 方法要点：引入矩阵注意力，以帧为矩阵处理，通过矩阵原生操作实现跨帧全局时空结构保持。
- 实验或效果：FrameDiT-H在多个基准上达到最先进结果，提升时间一致性和视频质量，同时保持高效。

## 摘要（原文）

> High-fidelity video generation remains challenging for diffusion models due to the difficulty of modeling complex spatio-temporal dynamics efficiently. Recent video diffusion methods typically represent a video as a sequence of spatio-temporal tokens which can be modeled using Diffusion Transformers (DiTs). However, this approach faces a trade-off between the strong but expensive Full 3D Attention and the efficient but temporally limited Local Factorized Attention. To resolve this trade-off, we propose Matrix Attention, a frame-level temporal attention mechanism that processes an entire frame as a matrix and generates query, key, and value matrices via matrix-native operations. By attending across frames rather than tokens, Matrix Attention effectively preserves global spatio-temporal structure and adapts to significant motion. We build FrameDiT-G, a DiT architecture based on MatrixAttention, and further introduce FrameDiT-H, which integrates Matrix Attention with Local Factorized Attention to capture both large and small motion. Extensive experiments show that FrameDiT-H achieves state-of-the-art results across multiple video generation benchmarks, offering improved temporal coherence and video quality while maintaining efficiency comparable to Local Factorized Attention.

