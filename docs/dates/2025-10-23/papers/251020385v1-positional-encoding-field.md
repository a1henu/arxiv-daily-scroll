---
layout: default
title: Positional Encoding Field
---

# Positional Encoding Field
**arXiv**：[2510.20385v1](https://arxiv.org/abs/2510.20385) · [PDF](https://arxiv.org/pdf/2510.20385.pdf)  
**作者**：Yunpeng Bai, Haoxiang Li, Qixing Huang  

**一句话要点**：提出位置编码场以增强扩散变换器在3D空间建模和图像生成中的性能

**关键词**：扩散变换器, 位置编码, 3D建模, 新视角合成, 图像编辑

## 3 点简述
- 核心问题：扩散变换器中位置编码对空间一致性的主导作用未被充分探索，影响3D几何建模。
- 方法要点：扩展位置编码至3D场，引入深度感知和分层编码，支持体积推理和细粒度控制。
- 实验或效果：在单图像新视角合成中达到最优，并推广至可控空间图像编辑。

## 摘要（原文）

> Diffusion Transformers (DiTs) have emerged as the dominant architecture for
> visual generation, powering state-of-the-art image and video models. By
> representing images as patch tokens with positional encodings (PEs), DiTs
> combine Transformer scalability with spatial and temporal inductive biases. In
> this work, we revisit how DiTs organize visual content and discover that patch
> tokens exhibit a surprising degree of independence: even when PEs are
> perturbed, DiTs still produce globally coherent outputs, indicating that
> spatial coherence is primarily governed by PEs. Motivated by this finding, we
> introduce the Positional Encoding Field (PE-Field), which extends positional
> encodings from the 2D plane to a structured 3D field. PE-Field incorporates
> depth-aware encodings for volumetric reasoning and hierarchical encodings for
> fine-grained sub-patch control, enabling DiTs to model geometry directly in 3D
> space. Our PE-Field-augmented DiT achieves state-of-the-art performance on
> single-image novel view synthesis and generalizes to controllable spatial image
> editing.

