---
layout: default
title: CLIP4VI-ReID: Learning Modality-shared Representations via CLIP Semantic Bridge for Visible-Infrared Person Re-identification
---

# CLIP4VI-ReID: Learning Modality-shared Representations via CLIP Semantic Bridge for Visible-Infrared Person Re-identification
**arXiv**：[2511.10309v1](https://arxiv.org/abs/2511.10309) · [PDF](https://arxiv.org/pdf/2511.10309.pdf)  
**作者**：Xiaomei Yang, Xizhan Gao, Sijie Niu, Fa Zhu, Guang Feng, Xiaofeng Qu, David Camacho  

**一句话要点**：提出CLIP4VI-ReID网络，通过CLIP语义桥学习模态共享表示以解决可见光-红外行人重识别问题

**关键词**：可见光-红外行人重识别, 模态共享表示学习, CLIP语义桥, 跨模态对齐, 文本语义生成

## 3 点简述
- 核心问题：可见光与红外图像物理特性差异大，导致跨模态对齐困难。
- 方法要点：设计文本语义生成、红外特征嵌入和高层语义对齐模块，利用文本桥接模态。
- 实验或效果：在多个VI-ReID数据集上优于现有方法，提升模态共享表示的判别性。

## 摘要（原文）

> This paper proposes a novel CLIP-driven modality-shared representation learning network named CLIP4VI-ReID for VI-ReID task, which consists of Text Semantic Generation (TSG), Infrared Feature Embedding (IFE), and High-level Semantic Alignment (HSA). Specifically, considering the huge gap in the physical characteristics between natural images and infrared images, the TSG is designed to generate text semantics only for visible images, thereby enabling preliminary visible-text modality alignment. Then, the IFE is proposed to rectify the feature embeddings of infrared images using the generated text semantics. This process injects id-related semantics into the shared image encoder, enhancing its adaptability to the infrared modality. Besides, with text serving as a bridge, it enables indirect visible-infrared modality alignment. Finally, the HSA is established to refine the high-level semantic alignment. This process ensures that the fine-tuned text semantics only contain id-related information, thereby achieving more accurate cross-modal alignment and enhancing the discriminability of the learned modal-shared representations. Extensive experimental results demonstrate that the proposed CLIP4VI-ReID achieves superior performance than other state-of-the-art methods on some widely used VI-ReID datasets.

