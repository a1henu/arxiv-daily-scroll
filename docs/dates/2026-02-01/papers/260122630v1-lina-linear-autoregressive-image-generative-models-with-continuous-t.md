---
layout: default
title: LINA: Linear Autoregressive Image Generative Models with Continuous Tokens
---

# LINA: Linear Autoregressive Image Generative Models with Continuous Tokens
**arXiv**：[2601.22630v1](https://arxiv.org/abs/2601.22630) · [PDF](https://arxiv.org/pdf/2601.22630.pdf)  
**作者**：Jiahao Wang, Ting Pan, Haoge Deng, Dongchen Han, Taiqiang Wu, Xinlong Wang, Ping Luo  

**一句话要点**：提出LINA线性自回归图像生成模型，通过优化线性注意力设计解决计算成本高的问题，用于文本到图像合成。

**关键词**：线性注意力, 自回归模型, 文本到图像合成, 计算效率, 连续令牌, KV门机制

## 3 点简述
- 核心问题：连续令牌自回归模型在视觉生成中计算成本高，影响效率。
- 方法要点：系统分析线性注意力缩放行为，优化归一化范式与卷积增强，引入KV门机制。
- 实验或效果：LINA在ImageNet和GenEval基准上表现竞争性，线性注意力模块减少约61% FLOPs。

## 摘要（原文）

> Autoregressive models with continuous tokens form a promising paradigm for visual generation, especially for text-to-image (T2I) synthesis, but they suffer from high computational cost. We study how to design compute-efficient linear attention within this framework. Specifically, we conduct a systematic empirical analysis of scaling behavior with respect to parameter counts under different design choices, focusing on (1) normalization paradigms in linear attention (division-based vs. subtraction-based) and (2) depthwise convolution for locality augmentation.
>   Our results show that although subtraction-based normalization is effective for image classification, division-based normalization scales better for linear generative transformers. In addition, incorporating convolution for locality modeling plays a crucial role in autoregressive generation, consistent with findings in diffusion models.
>   We further extend gating mechanisms, commonly used in causal linear attention, to the bidirectional setting and propose a KV gate. By introducing data-independent learnable parameters to the key and value states, the KV gate assigns token-wise memory weights, enabling flexible memory management similar to forget gates in language models.
>   Based on these findings, we present LINA, a simple and compute-efficient T2I model built entirely on linear attention, capable of generating high-fidelity 1024x1024 images from user instructions. LINA achieves competitive performance on both class-conditional and T2I benchmarks, obtaining 2.18 FID on ImageNet (about 1.4B parameters) and 0.74 on GenEval (about 1.5B parameters). A single linear attention module reduces FLOPs by about 61 percent compared to softmax attention. Code and models are available at: https://github.com/techmonsterwang/LINA.

