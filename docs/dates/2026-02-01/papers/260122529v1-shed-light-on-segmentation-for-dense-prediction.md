---
layout: default
title: SHED Light on Segmentation for Dense Prediction
---

# SHED Light on Segmentation for Dense Prediction
**arXiv**：[2601.22529v1](https://arxiv.org/abs/2601.22529) · [PDF](https://arxiv.org/pdf/2601.22529.pdf)  
**作者**：Seung Hyun Lee, Sangwoo Mo, Stella X. Yu  

**一句话要点**：提出SHED架构，通过融入分割增强密集预测的几何先验，以解决结构不一致问题。

**关键词**：密集预测, 分割层次, 几何先验, 编码器-解码器, 跨域泛化, 3D感知

## 3 点简述
- 核心问题：密集预测方法常忽略场景结构，导致像素级预测的结构不一致。
- 方法要点：采用编码器-解码器架构，通过双向分层推理，无监督地学习分割层次。
- 实验或效果：提升深度边界锐度和分割一致性，并展示从合成到真实场景的强泛化能力。

## 摘要（原文）

> Dense prediction infers per-pixel values from a single image and is fundamental to 3D perception and robotics. Although real-world scenes exhibit strong structure, existing methods treat it as an independent pixel-wise prediction, often resulting in structural inconsistencies. We propose SHED, a novel encoder-decoder architecture that enforces geometric prior explicitly by incorporating segmentation into dense prediction. By bidirectional hierarchical reasoning, segment tokens are hierarchically pooled in the encoder and unpooled in the decoder to reverse the hierarchy. The model is supervised only at the final output, allowing the segment hierarchy to emerge without explicit segmentation supervision. SHED improves depth boundary sharpness and segment coherence, while demonstrating strong cross-domain generalization from synthetic to the real-world environments. Its hierarchy-aware decoder better captures global 3D scene layouts, leading to improved semantic segmentation performance. Moreover, SHED enhances 3D reconstruction quality and reveals interpretable part-level structures that are often missed by conventional pixel-wise methods.

