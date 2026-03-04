---
layout: default
title: SemanticDialect: Semantic-Aware Mixed-Format Quantization for Video Diffusion Transformers
---

# SemanticDialect: Semantic-Aware Mixed-Format Quantization for Video Diffusion Transformers
**arXiv**：[2603.02883v1](https://arxiv.org/abs/2603.02883) · [PDF](https://arxiv.org/pdf/2603.02883.pdf)  
**作者**：Wonsuk Jang, Thierry Tambe  

**一句话要点**：提出SemanticDialect，通过语义感知混合格式量化降低视频扩散变换器的部署成本。

**关键词**：视频扩散变换器, 混合格式量化, 语义感知, 激活分解, 块级优化

## 3 点简述
- 核心问题：视频扩散变换器量化时，高激活变化和语义/时序一致性保持导致质量下降。
- 方法要点：基于块级混合格式量化，引入激活分解和语义感知方言分配以提升量化精度。
- 实验效果：在视频扩散变换器模型上优于现有量化方法，接近FP16质量。

## 摘要（原文）

> Diffusion Transformers (DiT) achieve strong video generation quality, but their memory and compute costs hinder edge deployment. Quantization can reduce these costs, yet existing methods often degrade video quality under high activation variation and the need to preserve semantic/temporal coherence. We propose SemanticDialect, which advances recent block-wise mixed-format quantization-selecting a per-block optimal format (a dialect) from multiple candidates (a formatbook)-by scaling the formatbook with lookup tables for quantization error and quantized values, enabling efficient per-block format selection and quantization at low online cost. We also introduce activation decomposition that reduces quantization error by re-quantizing and adding back residual errors, with attention-guided salient token selection. We further propose semantic-aware dialect assignment (SeDA) to improve quantized value consistency by sharing a sub-formatbook among semantically correlated tokens. Experiments on video DiT (VDiT) models show that SemanticDialect outperforms prior VDiT quantization methods and fine-grained block-wise format baselines, while approaching FP16 quality on Open-Sora 2.0.

