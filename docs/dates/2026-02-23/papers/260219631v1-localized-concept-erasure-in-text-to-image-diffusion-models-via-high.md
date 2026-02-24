---
layout: default
title: Localized Concept Erasure in Text-to-Image Diffusion Models via High-Level Representation Misdirection
---

# Localized Concept Erasure in Text-to-Image Diffusion Models via High-Level Representation Misdirection
**arXiv**：[2602.19631v1](https://arxiv.org/abs/2602.19631) · [PDF](https://arxiv.org/pdf/2602.19631.pdf)  
**作者**：Uichan Lee, Jeonghyeon Kim, Sangheum Hwang  

**一句话要点**：提出HiRM方法，通过误导文本编码器高层表示实现局部概念擦除，以解决扩散模型生成有害内容的问题。

**关键词**：概念擦除, 文本到图像扩散模型, 高层表示误导, 文本编码器, 局部更新, 生成安全

## 3 点简述
- 核心问题：文本到图像扩散模型可能生成有害或侵权内容，现有概念擦除方法易影响非目标概念生成质量。
- 方法要点：HiRM误导文本编码器早期层中目标概念的高层语义表示至指定向量，仅更新包含视觉属性因果状态的层。
- 实验或效果：在UnlearnCanvas和NSFW基准上表现优异，能精确移除概念且对无关概念影响小，训练成本低且可迁移至新架构。

## 摘要（原文）

> Recent advances in text-to-image (T2I) diffusion models have seen rapid and widespread adoption. However, their powerful generative capabilities raise concerns about potential misuse for synthesizing harmful, private, or copyrighted content. To mitigate such risks, concept erasure techniques have emerged as a promising solution. Prior works have primarily focused on fine-tuning the denoising component (e.g., the U-Net backbone). However, recent causal tracing studies suggest that visual attribute information is localized in the early self-attention layers of the text encoder, indicating a potential alternative for concept erasing. Building on this insight, we conduct preliminary experiments and find that directly fine-tuning early layers can suppress target concepts but often degrades the generation quality of non-target concepts. To overcome this limitation, we propose High-Level Representation Misdirection (HiRM), which misdirects high-level semantic representations of target concepts in the text encoder toward designated vectors such as random directions or semantically defined directions (e.g., supercategories), while updating only early layers that contain causal states of visual attributes. Our decoupling strategy enables precise concept removal with minimal impact on unrelated concepts, as demonstrated by strong results on UnlearnCanvas and NSFW benchmarks across diverse targets (e.g., objects, styles, nudity). HiRM also preserves generative utility at low training cost, transfers to state-of-the-art architectures such as Flux without additional training, and shows synergistic effects with denoiser-based concept erasing methods.

