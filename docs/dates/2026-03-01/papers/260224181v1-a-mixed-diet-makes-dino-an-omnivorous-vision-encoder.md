---
layout: default
title: A Mixed Diet Makes DINO An Omnivorous Vision Encoder
---

# A Mixed Diet Makes DINO An Omnivorous Vision Encoder
**arXiv**：[2602.24181v1](https://arxiv.org/abs/2602.24181) · [PDF](https://arxiv.org/pdf/2602.24181.pdf)  
**作者**：Rishabh Kabra, Maks Ovsjanikov, Drew A. Hudson, Ye Xia, Skanda Koppula, Andre Araujo, Joao Carreira, Niloy J. Mitra  

**一句话要点**：提出Omnivorous Vision Encoder以解决多模态特征对齐问题，实现场景无关输入的统一嵌入。

**关键词**：多模态对齐, 视觉编码器, 特征蒸馏, 模态无关表示, 跨模态理解

## 3 点简述
- 核心问题：预训练视觉编码器如DINOv2在多模态任务中特征对齐差，如RGB与深度图相似度接近随机图像。
- 方法要点：通过双目标训练学习模态无关特征空间，包括最大化同场景多模态对齐和蒸馏冻结教师模型输出。
- 实验或效果：学生编码器成为'杂食性'，为任意输入模态生成一致且强大的嵌入，保持基础模型判别语义。

## 摘要（原文）

> Pre-trained vision encoders like DINOv2 have demonstrated exceptional performance on unimodal tasks. However, we observe that their feature representations are poorly aligned across different modalities. For instance, the feature embedding for an RGB image and its corresponding depth map of the same scene exhibit a cosine similarity that is nearly identical to that of two random, unrelated images. To address this, we propose the Omnivorous Vision Encoder, a novel framework that learns a modality-agnostic feature space. We train the encoder with a dual objective: first, to maximize the feature alignment between different modalities of the same scene; and second, a distillation objective that anchors the learned representations to the output of a fully frozen teacher such as DINOv2. The resulting student encoder becomes "omnivorous" by producing a consistent, powerful embedding for a given scene, regardless of the input modality (RGB, Depth, Segmentation, etc.). This approach enables robust cross-modal understanding while retaining the discriminative semantics of the original foundation model.

