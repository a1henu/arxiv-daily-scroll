---
layout: default
title: SplitFlux: Learning to Decouple Content and Style from a Single Image
---

# SplitFlux: Learning to Decouple Content and Style from a Single Image
**arXiv**：[2511.15258v1](https://arxiv.org/abs/2511.15258) · [PDF](https://arxiv.org/pdf/2511.15258.pdf)  
**作者**：Yitong Yang, Yinglin Wang, Changshuo Wang, Yongjun Zhang, Ziyang Chen, Shuting He  

**一句话要点**：提出SplitFlux以解决单图像内容与风格解耦问题

**关键词**：内容风格解耦, 图像生成, LoRA微调, 单图像学习, 视觉门控

## 3 点简述
- 核心问题：现有方法如Flux难以有效分离图像内容与风格，影响定制生成质量。
- 方法要点：基于Flux模型，通过LoRA微调单Dream块，实现内容与风格解耦。
- 实验或效果：在多样场景中优于先进方法，提升内容保持和风格化质量。

## 摘要（原文）

> Disentangling image content and style is essential for customized image generation. Existing SDXL-based methods struggle to achieve high-quality results, while the recently proposed Flux model fails to achieve effective content-style separation due to its underexplored characteristics. To address these challenges, we conduct a systematic analysis of Flux and make two key observations: (1) Single Dream Blocks are essential for image generation; and (2) Early single stream blocks mainly control content, whereas later blocks govern style. Based on these insights, we propose SplitFlux, which disentangles content and style by fine-tuning the single dream blocks via LoRA, enabling the disentangled content to be re-embedded into new contexts. It includes two key components: (1) Rank-Constrained Adaptation. To preserve content identity and structure, we compress the rank and amplify the magnitude of updates within specific blocks, preventing content leakage into style blocks. (2) Visual-Gated LoRA. We split the content LoRA into two branches with different ranks, guided by image saliency. The high-rank branch preserves primary subject information, while the low-rank branch encodes residual details, mitigating content overfitting and enabling seamless re-embedding. Extensive experiments demonstrate that SplitFlux consistently outperforms state-of-the-art methods, achieving superior content preservation and stylization quality across diverse scenarios.

