---
layout: default
title: Geometric Disentanglement of Text Embeddings for Subject-Consistent Text-to-Image Generation using A Single Prompt
---

# Geometric Disentanglement of Text Embeddings for Subject-Consistent Text-to-Image Generation using A Single Prompt
**arXiv**：[2512.16443v1](https://arxiv.org/abs/2512.16443) · [PDF](https://arxiv.org/pdf/2512.16443.pdf)  
**作者**：Shangxun Li, Youngjung Uh  

**一句话要点**：提出几何解缠方法以提升单提示下文本到图像生成的主体一致性

**关键词**：文本到图像生成, 主体一致性, 几何解缠, 文本嵌入优化, 训练免费方法

## 3 点简述
- 核心问题：文本嵌入在跨帧生成中语义纠缠，导致主体不一致和文本对齐差。
- 方法要点：从几何角度精炼文本嵌入，抑制不需要的语义，无需训练或微调。
- 实验或效果：在主体一致性和文本对齐上显著优于现有基线方法。

## 摘要（原文）

> Text-to-image diffusion models excel at generating high-quality images from natural language descriptions but often fail to preserve subject consistency across multiple outputs, limiting their use in visual storytelling. Existing approaches rely on model fine-tuning or image conditioning, which are computationally expensive and require per-subject optimization. 1Prompt1Story, a training-free approach, concatenates all scene descriptions into a single prompt and rescales token embeddings, but it suffers from semantic leakage, where embeddings across frames become entangled, causing text misalignment. In this paper, we propose a simple yet effective training-free approach that addresses semantic entanglement from a geometric perspective by refining text embeddings to suppress unwanted semantics. Extensive experiments prove that our approach significantly improves both subject consistency and text alignment over existing baselines.

