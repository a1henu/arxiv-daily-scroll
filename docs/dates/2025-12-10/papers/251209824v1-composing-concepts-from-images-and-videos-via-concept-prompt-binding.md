---
layout: default
title: Composing Concepts from Images and Videos via Concept-prompt Binding
---

# Composing Concepts from Images and Videos via Concept-prompt Binding
**arXiv**：[2512.09824v1](https://arxiv.org/abs/2512.09824) · [PDF](https://arxiv.org/pdf/2512.09824.pdf)  
**作者**：Xianghao Kong, Zeyu Zhang, Yuwei Guo, Zhuoran Zhao, Songchun Zhang, Anyi Rao  

**一句话要点**：提出Bind & Compose方法，通过概念-提示绑定实现图像与视频的灵活视觉概念组合。

**关键词**：视觉概念组合, 扩散变换器, 概念-提示绑定, 时间解耦, 多样化吸收机制

## 3 点简述
- 核心问题：视觉概念组合在准确提取复杂概念和灵活结合图像与视频概念方面存在不足。
- 方法要点：采用分层绑定结构和多样化吸收机制，结合时间解耦策略，提升概念绑定准确性和兼容性。
- 实验或效果：评估显示在概念一致性、提示保真度和运动质量上优于现有方法，拓展视觉创意可能性。

## 摘要（原文）

> Visual concept composition, which aims to integrate different elements from images and videos into a single, coherent visual output, still falls short in accurately extracting complex concepts from visual inputs and flexibly combining concepts from both images and videos. We introduce Bind & Compose, a one-shot method that enables flexible visual concept composition by binding visual concepts with corresponding prompt tokens and composing the target prompt with bound tokens from various sources. It adopts a hierarchical binder structure for cross-attention conditioning in Diffusion Transformers to encode visual concepts into corresponding prompt tokens for accurate decomposition of complex visual concepts. To improve concept-token binding accuracy, we design a Diversify-and-Absorb Mechanism that uses an extra absorbent token to eliminate the impact of concept-irrelevant details when training with diversified prompts. To enhance the compatibility between image and video concepts, we present a Temporal Disentanglement Strategy that decouples the training process of video concepts into two stages with a dual-branch binder structure for temporal modeling. Evaluations demonstrate that our method achieves superior concept consistency, prompt fidelity, and motion quality over existing approaches, opening up new possibilities for visual creativity.

