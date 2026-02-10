---
layout: default
title: Shifting the Breaking Point of Flow Matching for Multi-Instance Editing
---

# Shifting the Breaking Point of Flow Matching for Multi-Instance Editing
**arXiv**：[2602.08749v1](https://arxiv.org/abs/2602.08749) · [PDF](https://arxiv.org/pdf/2602.08749.pdf)  
**作者**：Carmine Zaccagnino, Fabio Quattrini, Enis Simsar, Marta Tintoré Gazulla, Rita Cucchiara, Alessio Tonioni, Silvia Cascianelli  

**一句话要点**：提出实例解耦注意力机制，以解决流匹配模型在多实例编辑中的语义干扰问题。

**关键词**：流匹配模型, 多实例编辑, 注意力机制, 图像编辑, 语义解耦

## 3 点简述
- 核心问题：流匹配模型在多实例编辑时，全局条件速度场和联合注意力机制导致语义干扰。
- 方法要点：引入实例解耦注意力，分区联合注意力操作，绑定实例特定文本指令与空间区域。
- 实验或效果：在自然图像和文本密集信息图编辑中，促进编辑解耦与局部性，保持全局一致性。

## 摘要（原文）

> Flow matching models have recently emerged as an efficient alternative to diffusion, especially for text-guided image generation and editing, offering faster inference through continuous-time dynamics. However, existing flow-based editors predominantly support global or single-instruction edits and struggle with multi-instance scenarios, where multiple parts of a reference input must be edited independently without semantic interference. We identify this limitation as a consequence of globally conditioned velocity fields and joint attention mechanisms, which entangle concurrent edits. To address this issue, we introduce Instance-Disentangled Attention, a mechanism that partitions joint attention operations, enforcing binding between instance-specific textual instructions and spatial regions during velocity field estimation. We evaluate our approach on both natural image editing and a newly introduced benchmark of text-dense infographics with region-level editing instructions. Experimental results demonstrate that our approach promotes edit disentanglement and locality while preserving global output coherence, enabling single-pass, instance-level editing.

