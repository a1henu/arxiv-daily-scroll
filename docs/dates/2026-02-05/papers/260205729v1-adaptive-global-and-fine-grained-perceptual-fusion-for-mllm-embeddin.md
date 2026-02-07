---
layout: default
title: Adaptive Global and Fine-Grained Perceptual Fusion for MLLM Embeddings Compatible with Hard Negative Amplification
---

# Adaptive Global and Fine-Grained Perceptual Fusion for MLLM Embeddings Compatible with Hard Negative Amplification
**arXiv**：[2602.05729v1](https://arxiv.org/abs/2602.05729) · [PDF](https://arxiv.org/pdf/2602.05729.pdf)  
**作者**：Lexiang Hu, Youze Xue, Dian Li, Gang Liu, Zhouchen Lin  

**一句话要点**：提出AGFF-Embed方法，通过自适应融合全局与细粒度感知，增强MLLM嵌入在复杂场景下的理解能力。

**关键词**：多模态嵌入, 全局与细粒度融合, MLLM嵌入, 硬负样本增强, 自适应聚合

## 3 点简述
- 核心问题：现有MLLM嵌入仅捕获全局语义，难以处理混合全局与细粒度元素的复杂场景。
- 方法要点：提示MLLM生成多维度嵌入，并自适应平滑聚合，结合EGA技术增强硬负样本。
- 实验或效果：在MMEB和MMVP-VLM基准上实现全面最优性能，提升通用与细粒度理解。

## 摘要（原文）

> Multimodal embeddings serve as a bridge for aligning vision and language, with the two primary implementations -- CLIP-based and MLLM-based embedding models -- both limited to capturing only global semantic information. Although numerous studies have focused on fine-grained understanding, we observe that complex scenarios currently targeted by MLLM embeddings often involve a hybrid perceptual pattern of both global and fine-grained elements, thus necessitating a compatible fusion mechanism. In this paper, we propose Adaptive Global and Fine-grained perceptual Fusion for MLLM Embeddings (AGFF-Embed), a method that prompts the MLLM to generate multiple embeddings focusing on different dimensions of semantic information, which are then adaptively and smoothly aggregated. Furthermore, we adapt AGFF-Embed with the Explicit Gradient Amplification (EGA) technique to achieve in-batch hard negatives enhancement without requiring fine-grained editing of the dataset. Evaluation on the MMEB and MMVP-VLM benchmarks shows that AGFF-Embed comprehensively achieves state-of-the-art performance in both general and fine-grained understanding compared to other multimodal embedding models.

