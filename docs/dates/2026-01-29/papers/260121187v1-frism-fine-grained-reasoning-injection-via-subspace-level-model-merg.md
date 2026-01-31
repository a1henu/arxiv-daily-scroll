---
layout: default
title: FRISM: Fine-Grained Reasoning Injection via Subspace-Level Model Merging for Vision-Language Models
---

# FRISM: Fine-Grained Reasoning Injection via Subspace-Level Model Merging for Vision-Language Models
**arXiv**：[2601.21187v1](https://arxiv.org/abs/2601.21187) · [PDF](https://arxiv.org/pdf/2601.21187.pdf)  
**作者**：Chenyu Huang, Peng Ye, Xudong Tan, Jinhan Mu, Shenghe Zheng, Li Shen, Tao Chen  

**一句话要点**：提出FRISM框架，通过子空间级模型合并实现细粒度推理注入，以解决视觉语言模型中推理与视觉能力权衡问题。

**关键词**：视觉语言模型, 模型合并, 推理能力注入, 子空间分解, 自蒸馏学习, 视觉推理

## 3 点简述
- 现有方法在粗粒度层级别合并模型，导致推理能力注入与视觉能力保持之间的权衡问题。
- FRISM基于子空间级模型合并，通过SVD分解推理模型任务向量并自适应调整子空间缩放系数，实现细粒度推理注入。
- 实验表明，FRISM在多种视觉推理基准上保持视觉能力的同时，有效提升推理性能，达到先进水平。

## 摘要（原文）

> Efficiently enhancing the reasoning capabilities of Vision-Language Models (VLMs) by merging them with Large Reasoning Models (LRMs) has emerged as a promising direction. However, existing methods typically operate at a coarse-grained layer level, which often leads to a trade-off between injecting reasoning capabilities and preserving visual capabilities. To address this limitation, we propose {FRISM} (Fine-grained Reasoning Injection via Subspace-level model Merging), a fine-grained reasoning injection framework based on subspace-level model merging. Observing that reasoning capabilities are encoded in distinct subspaces, FRISM decomposes LRM task vectors via Singular Value Decomposition (SVD) and adaptively tunes the scaling coefficients of each subspace through learning to realize fine-grained reasoning injection. Furthermore, we introduce a label-free self-distillation learning strategy with a dual-objective optimization using common vision-language perception datasets. Extensive experiments demonstrate that FRISM effectively improves reasoning capabilities without compromising the model's original visual capabilities by consistently achieving state-of-the-art performance across diverse visual reasoning benchmarks.

