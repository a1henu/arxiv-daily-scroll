---
layout: default
title: Inspiration Seeds: Learning Non-Literal Visual Combinations for Generative Exploration
---

# Inspiration Seeds: Learning Non-Literal Visual Combinations for Generative Exploration
**arXiv**：[2602.08615v1](https://arxiv.org/abs/2602.08615) · [PDF](https://arxiv.org/pdf/2602.08615.pdf)  
**作者**：Kfir Goldberg, Elad Richardson, Yael Vinker  

**一句话要点**：提出Inspiration Seeds框架，通过非语言视觉组合支持创意探索中的早期构思

**关键词**：视觉生成, 创意探索, 非语言组合, CLIP自编码器, 图像合成

## 3 点简述
- 核心问题：生成模型依赖文本提示，难以支持开放式的视觉探索和灵感激发。
- 方法要点：基于CLIP稀疏自编码器提取视觉编辑方向，实现无文本输入的图像组合生成。
- 实验或效果：模型能快速生成多样且视觉连贯的构图，揭示输入图像间的潜在关系。

## 摘要（原文）

> While generative models have become powerful tools for image synthesis, they are typically optimized for executing carefully crafted textual prompts, offering limited support for the open-ended visual exploration that often precedes idea formation. In contrast, designers frequently draw inspiration from loosely connected visual references, seeking emergent connections that spark new ideas. We propose Inspiration Seeds, a generative framework that shifts image generation from final execution to exploratory ideation. Given two input images, our model produces diverse, visually coherent compositions that reveal latent relationships between inputs, without relying on user-specified text prompts. Our approach is feed-forward, trained on synthetic triplets of decomposed visual aspects derived entirely through visual means: we use CLIP Sparse Autoencoders to extract editing directions in CLIP latent space and isolate concept pairs. By removing the reliance on language and enabling fast, intuitive recombination, our method supports visual ideation at the early and ambiguous stages of creative work.

