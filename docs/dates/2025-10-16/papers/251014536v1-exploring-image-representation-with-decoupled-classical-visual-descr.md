---
layout: default
title: Exploring Image Representation with Decoupled Classical Visual Descriptors
---

# Exploring Image Representation with Decoupled Classical Visual Descriptors
**arXiv**：[2510.14536v1](https://arxiv.org/abs/2510.14536) · [PDF](https://arxiv.org/pdf/2510.14536.pdf)  
**作者**：Chenyuan Qu, Hao Chen, Jianbo Jiao  

**一句话要点**：提出VisualSplit框架，通过解耦经典视觉描述符提升图像表示的可解释性和控制能力。

**关键词**：图像表示学习, 经典视觉描述符, 可解释AI, 图像生成, 属性控制

## 3 点简述
- 核心问题：深度学习图像表示不透明，难以解释视觉信息处理过程。
- 方法要点：将图像分解为独立经典描述符，采用重建预训练学习可解释表示。
- 实验或效果：在图像生成和编辑等任务中实现有效属性控制，超越传统分类和分割。

## 摘要（原文）

> Exploring and understanding efficient image representations is a
> long-standing challenge in computer vision. While deep learning has achieved
> remarkable progress across image understanding tasks, its internal
> representations are often opaque, making it difficult to interpret how visual
> information is processed. In contrast, classical visual descriptors (e.g. edge,
> colour, and intensity distribution) have long been fundamental to image
> analysis and remain intuitively understandable to humans. Motivated by this
> gap, we ask a central question: Can modern learning benefit from these
> classical cues? In this paper, we answer it with VisualSplit, a framework that
> explicitly decomposes images into decoupled classical descriptors, treating
> each as an independent but complementary component of visual knowledge. Through
> a reconstruction-driven pre-training scheme, VisualSplit learns to capture the
> essence of each visual descriptor while preserving their interpretability. By
> explicitly decomposing visual attributes, our method inherently facilitates
> effective attribute control in various advanced visual tasks, including image
> generation and editing, extending beyond conventional classification and
> segmentation, suggesting the effectiveness of this new learning approach for
> visual understanding. Project page: https://chenyuanqu.com/VisualSplit/.

