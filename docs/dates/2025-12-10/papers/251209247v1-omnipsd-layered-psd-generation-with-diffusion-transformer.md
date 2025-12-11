---
layout: default
title: OmniPSD: Layered PSD Generation with Diffusion Transformer
---

# OmniPSD: Layered PSD Generation with Diffusion Transformer
**arXiv**：[2512.09247v1](https://arxiv.org/abs/2512.09247) · [PDF](https://arxiv.org/pdf/2512.09247.pdf)  
**作者**：Cheng Liu, Yiren Song, Haofan Wang, Mike Zheng Shou  

**一句话要点**：提出OmniPSD扩散框架，实现文本生成和图像分解PSD文件，支持透明通道和层级结构。

**关键词**：扩散模型, PSD生成, 图像分解, 透明通道, 上下文学习, 层级结构

## 3 点简述
- 核心问题：现有扩散模型难以生成或重建带透明alpha通道的分层PSD文件。
- 方法要点：基于Flux生态系统，通过空间注意力和上下文学习统一处理文本生成和图像分解。
- 实验或效果：在新RGBA分层数据集上验证高保真生成、结构一致性和透明度感知。

## 摘要（原文）

> Recent advances in diffusion models have greatly improved image generation and editing, yet generating or reconstructing layered PSD files with transparent alpha channels remains highly challenging. We propose OmniPSD, a unified diffusion framework built upon the Flux ecosystem that enables both text-to-PSD generation and image-to-PSD decomposition through in-context learning. For text-to-PSD generation, OmniPSD arranges multiple target layers spatially into a single canvas and learns their compositional relationships through spatial attention, producing semantically coherent and hierarchically structured layers. For image-to-PSD decomposition, it performs iterative in-context editing, progressively extracting and erasing textual and foreground components to reconstruct editable PSD layers from a single flattened image. An RGBA-VAE is employed as an auxiliary representation module to preserve transparency without affecting structure learning. Extensive experiments on our new RGBA-layered dataset demonstrate that OmniPSD achieves high-fidelity generation, structural consistency, and transparency awareness, offering a new paradigm for layered design generation and decomposition with diffusion transformers.

