---
layout: default
title: Closing the gap in multimodal medical representation alignment
---

# Closing the gap in multimodal medical representation alignment
**arXiv**：[2602.20046v1](https://arxiv.org/abs/2602.20046) · [PDF](https://arxiv.org/pdf/2602.20046.pdf)  
**作者**：Eleonora Grassucci, Giordano Cicchetti, Danilo Comminiello  

**一句话要点**：提出模态无关框架以解决医学多模态表示对齐中的模态间隙问题

**关键词**：多模态学习, 医学表示对齐, 模态间隙, 跨模态检索, 图像描述生成

## 3 点简述
- 核心问题：CLIP对比损失在医学多模态对齐中导致模态间隙，影响语义对齐和潜在空间结构。
- 方法要点：设计模态无关框架，增强放射学图像与临床文本的语义对齐，减少模态间隙。
- 实验或效果：提升跨模态检索和图像描述生成性能，验证了方法在医学领域的有效性。

## 摘要（原文）

> In multimodal learning, CLIP has emerged as the de-facto approach for mapping different modalities into a shared latent space by bringing semantically similar representations closer while pushing apart dissimilar ones. However, CLIP-based contrastive losses exhibit unintended behaviors that negatively impact true semantic alignment, leading to sparse and fragmented latent spaces. This phenomenon, known as the modality gap, has been partially mitigated for standard text and image pairs but remains unknown and unresolved in more complex multimodal settings, such as the medical domain. In this work, we study this phenomenon in the latter case, revealing that the modality gap is present also in medical alignment, and we propose a modality-agnostic framework that closes this gap, ensuring that semantically related representations are more aligned, regardless of their source modality. Our method enhances alignment between radiology images and clinical text, improving cross-modal retrieval and image captioning.

