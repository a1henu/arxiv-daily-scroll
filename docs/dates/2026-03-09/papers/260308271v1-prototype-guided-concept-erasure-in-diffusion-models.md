---
layout: default
title: Prototype-Guided Concept Erasure in Diffusion Models
---

# Prototype-Guided Concept Erasure in Diffusion Models
**arXiv**：[2603.08271v1](https://arxiv.org/abs/2603.08271) · [PDF](https://arxiv.org/pdf/2603.08271.pdf)  
**作者**：Yuze Cai, Jiahao Lu, Hongxiang Shi, Yichao Zhou, Hong Lu  

**一句话要点**：提出原型引导的概念擦除方法，以解决扩散模型中宽泛概念难以可靠移除的问题。

**关键词**：概念擦除, 扩散模型, 原型引导, 负条件, 图像生成安全, 嵌入聚类

## 3 点简述
- 现有方法在擦除具体概念（如Pikachu）时有效，但对宽泛概念（如“性”或“暴力”）性能下降。
- 利用模型嵌入几何识别概念编码，通过聚类生成概念原型，作为负条件信号实现精确擦除。
- 多基准实验显示，该方法能更可靠移除宽泛概念，同时保持图像质量，提升生成安全性。

## 摘要（原文）

> Concept erasure is extensively utilized in image generation to prevent text-to-image models from generating undesired content. Existing methods can effectively erase narrow concepts that are specific and concrete, such as distinct intellectual properties (e.g. Pikachu) or recognizable characters (e.g. Elon Musk). However, their performance degrades on broad concepts such as ``sexual'' or ``violent'', whose wide scope and multi-faceted nature make them difficult to erase reliably. To overcome this limitation, we exploit the model's intrinsic embedding geometry to identify latent embeddings that encode a given concept. By clustering these embeddings, we derive a set of concept prototypes that summarize the model's internal representations of the concept, and employ them as negative conditioning signals during inference to achieve precise and reliable erasure. Extensive experiments across multiple benchmarks show that our approach achieves substantially more reliable removal of broad concepts while preserving overall image quality, marking a step towards safer and more controllable image generation.

