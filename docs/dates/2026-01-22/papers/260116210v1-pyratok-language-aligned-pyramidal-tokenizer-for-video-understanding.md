---
layout: default
title: PyraTok: Language-Aligned Pyramidal Tokenizer for Video Understanding and Generation
---

# PyraTok: Language-Aligned Pyramidal Tokenizer for Video Understanding and Generation
**arXiv**：[2601.16210v1](https://arxiv.org/abs/2601.16210) · [PDF](https://arxiv.org/pdf/2601.16210.pdf)  
**作者**：Onkar Susladkar, Tushar Prakash, Adheesh Juvekar, Kiet A. Nguyen, Dong-Hwan Jang, Inderjit S Dhillon, Ismini Lourentzou  

**一句话要点**：提出PyraTok语言对齐金字塔分词器，以增强视频理解与生成的跨模态对齐和零样本迁移能力。

**关键词**：视频理解, 文本到视频生成, 跨模态对齐, 零样本迁移, 金字塔分词器, 语言对齐量化

## 3 点简述
- 现有视频分词器存在单尺度、词汇有限和语言监督浅的问题，导致跨模态对齐差和零样本迁移弱。
- PyraTok通过语言对齐金字塔量化模块，在多个时空分辨率上学习语义结构化的离散潜在表示。
- 在十个基准测试中，PyraTok实现了最先进的视频重建、文本到视频质量提升和零样本性能。

## 摘要（原文）

> Discrete video VAEs underpin modern text-to-video generation and video understanding systems, yet existing tokenizers typically learn visual codebooks at a single scale with limited vocabularies and shallow language supervision, leading to poor cross-modal alignment and zero-shot transfer. We introduce PyraTok, a language-aligned pyramidal tokenizer that learns semantically structured discrete latents across multiple spatiotemporal resolutions. PyraTok builds on a pretrained video VAE and a novel Language aligned Pyramidal Quantization (LaPQ) module that discretizes encoder features at several depths using a shared large binary codebook, yielding compact yet expressive video token sequences. To tightly couple visual tokens with language, PyraTok jointly optimizes multi-scale text-guided quantization and a global autoregressive objective over the token hierarchy. Across ten benchmarks, PyraTok delivers state-of-the-art (SOTA) video reconstruction, consistently improves text-to-video quality, and sets new SOTA zero-shot performance on video segmentation, temporal action localization, and video understanding, scaling robustly to up to 4K/8K resolutions.

