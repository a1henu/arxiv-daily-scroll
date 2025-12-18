---
layout: default
title: MMMamba: A Versatile Cross-Modal In Context Fusion Framework for Pan-Sharpening and Zero-Shot Image Enhancement
---

# MMMamba: A Versatile Cross-Modal In Context Fusion Framework for Pan-Sharpening and Zero-Shot Image Enhancement
**arXiv**：[2512.15261v1](https://arxiv.org/abs/2512.15261) · [PDF](https://arxiv.org/pdf/2512.15261.pdf)  
**作者**：Yingying Wang, Xuanhua He, Chen Wu, Jialing Huang, Suiyun Zhang, Rui Liu, Xinghao Ding, Haoxuan Che  

**一句话要点**：提出MMMamba框架，通过跨模态上下文融合解决全色锐化和零样本图像增强问题。

**关键词**：全色锐化, 跨模态融合, 上下文学习, Mamba架构, 零样本增强, 图像超分辨率

## 3 点简述
- 核心问题：传统CNN方法在融合高分辨率全色与低分辨率多光谱图像时，适应性受限且计算效率低。
- 方法要点：基于Mamba架构，引入多模态交错扫描机制，实现线性计算复杂度的跨模态信息交换。
- 实验或效果：在多个任务和基准测试中，性能优于现有最先进技术，支持零样本超分辨率。

## 摘要（原文）

> Pan-sharpening aims to generate high-resolution multispectral (HRMS) images by integrating a high-resolution panchromatic (PAN) image with its corresponding low-resolution multispectral (MS) image. To achieve effective fusion, it is crucial to fully exploit the complementary information between the two modalities. Traditional CNN-based methods typically rely on channel-wise concatenation with fixed convolutional operators, which limits their adaptability to diverse spatial and spectral variations. While cross-attention mechanisms enable global interactions, they are computationally inefficient and may dilute fine-grained correspondences, making it difficult to capture complex semantic relationships. Recent advances in the Multimodal Diffusion Transformer (MMDiT) architecture have demonstrated impressive success in image generation and editing tasks. Unlike cross-attention, MMDiT employs in-context conditioning to facilitate more direct and efficient cross-modal information exchange. In this paper, we propose MMMamba, a cross-modal in-context fusion framework for pan-sharpening, with the flexibility to support image super-resolution in a zero-shot manner. Built upon the Mamba architecture, our design ensures linear computational complexity while maintaining strong cross-modal interaction capacity. Furthermore, we introduce a novel multimodal interleaved (MI) scanning mechanism that facilitates effective information exchange between the PAN and MS modalities. Extensive experiments demonstrate the superior performance of our method compared to existing state-of-the-art (SOTA) techniques across multiple tasks and benchmarks.

