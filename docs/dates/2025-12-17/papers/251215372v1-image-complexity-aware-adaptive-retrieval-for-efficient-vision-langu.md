---
layout: default
title: Image Complexity-Aware Adaptive Retrieval for Efficient Vision-Language Models
---

# Image Complexity-Aware Adaptive Retrieval for Efficient Vision-Language Models
**arXiv**：[2512.15372v1](https://arxiv.org/abs/2512.15372) · [PDF](https://arxiv.org/pdf/2512.15372.pdf)  
**作者**：Mikel Williams-Lekuona, Georgina Cosma  

**一句话要点**：提出ICAR方法，通过图像复杂度感知自适应检索，在保持视觉-语言模型性能的同时提升计算效率。

**关键词**：图像复杂度评估, 自适应计算, 视觉-语言检索, 双路径训练, 计算效率优化

## 3 点简述
- 视觉-语言模型中视觉变换器对所有图像采用统一计算，浪费资源于简单图像。
- ICAR通过双路径训练生成兼容嵌入，使简单图像提前退出，复杂图像全深度处理，保持跨模态对齐。
- 实验显示ICAR在标准基准上实现20%速度提升，保持类别级性能及95%实例级性能。

## 摘要（原文）

> Vision transformers in vision-language models apply uniform computational effort across all images, expending 175.33 GFLOPs (ViT-L/14) whether analysing a straightforward product photograph or a complex street scene. We propose ICAR (Image Complexity-Aware Retrieval), which enables vision transformers to use less compute for simple images whilst processing complex images through their full network depth. The key challenge is maintaining cross-modal alignment: embeddings from different processing depths must remain compatible for text matching. ICAR solves this through dual-path training that produces compatible embeddings from both reduced-compute and full-compute processing. This maintains compatibility between image representations and text embeddings in the same semantic space, whether an image exits early or processes fully. Unlike existing two-stage approaches that require expensive reranking, ICAR enables direct image-text matching without additional overhead. To determine how much compute to use, we develop ConvNeXt-IC, which treats image complexity assessment as a classification task. By applying modern classifier backbones rather than specialised architectures, ConvNeXt-IC achieves state-of-the-art performance with 0.959 correlation with human judgement (Pearson) and 4.4x speedup. Evaluated on standard benchmarks augmented with real-world web data, ICAR achieves 20% practical speedup while maintaining category-level performance and 95% of instance-level performance, enabling sustainable scaling of vision-language systems.

