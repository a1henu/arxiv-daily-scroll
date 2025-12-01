---
layout: default
title: HMR3D: Hierarchical Multimodal Representation for 3D Scene Understanding with Large Vision-Language Model
---

# HMR3D: Hierarchical Multimodal Representation for 3D Scene Understanding with Large Vision-Language Model
**arXiv**：[2511.22961v1](https://arxiv.org/abs/2511.22961) · [PDF](https://arxiv.org/pdf/2511.22961.pdf)  
**作者**：Chen Li, Eric Peh, Basura Fernando  

**一句话要点**：提出HMR3D：基于大视觉语言模型的分层多模态表示，用于3D场景理解

**关键词**：3D场景理解, 大视觉语言模型, 多模态表示, 分层特征, 显式对齐, 多视角图像

## 3 点简述
- 核心问题：现有VLM方法隐式对齐3D特征导致性能不佳，因数据稀缺和空间关系复杂。
- 方法要点：利用多视角图像和文本描述在输入空间显式对齐，文本引用3D坐标捕获空间关系，图像覆盖全面视角。
- 实验或效果：在3D问答基准上验证有效性，提升场景理解性能。

## 摘要（原文）

> Recent advances in large vision-language models (VLMs) have shown significant promise for 3D scene understanding. Existing VLM-based approaches typically align 3D scene features with the VLM's embedding space. However, this implicit alignment often yields suboptimal performance due to the scarcity of 3D data and the inherent complexity of spatial relationships in 3D environments. To address these limitations, we propose a novel hierarchical multimodal representation for 3D scene reasoning that explicitly aligns with VLMs at the input space by leveraging both multi-view images and text descriptions. The text descriptions capture spatial relationships by referencing the 3D coordinates of detected objects, while the multi-view images include a top-down perspective and four directional views (forward, left, right, and backward), ensuring comprehensive scene coverage. Additionally, we introduce a hierarchical feature representation that aggregates patch-level image features into view-level and scene-level representations, enabling the model to reason over both local and global scene context. Experimental results on both situated 3D Q&A and general 3D Q&A benchmarks demonstrate the effectiveness of our approach.

