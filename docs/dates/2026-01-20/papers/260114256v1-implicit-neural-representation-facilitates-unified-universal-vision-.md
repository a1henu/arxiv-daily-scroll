---
layout: default
title: Implicit Neural Representation Facilitates Unified Universal Vision Encoding
---

# Implicit Neural Representation Facilitates Unified Universal Vision Encoding
**arXiv**：[2601.14256v1](https://arxiv.org/abs/2601.14256) · [PDF](https://arxiv.org/pdf/2601.14256.pdf)  
**作者**：Matthew Gwilliam, Xiao Wang, Xuefeng Hu, Zhenheng Yang  

**一句话要点**：提出基于隐式神经表示的通用视觉编码模型，统一识别与生成任务

**关键词**：隐式神经表示, 超网络, 知识蒸馏, 视觉编码, 统一表示, 图像生成

## 3 点简述
- 核心问题：现有模型通常专用于识别或生成，缺乏统一表示
- 方法要点：训练超网络映射图像到模型权重，结合知识蒸馏提升泛化
- 实验或效果：在视觉任务中竞争SOTA，同时支持高质量图像生成

## 摘要（原文）

> Models for image representation learning are typically designed for either recognition or generation. Various forms of contrastive learning help models learn to convert images to embeddings that are useful for classification, detection, and segmentation. On the other hand, models can be trained to reconstruct images with pixel-wise, perceptual, and adversarial losses in order to learn a latent space that is useful for image generation. We seek to unify these two directions with a first-of-its-kind model that learns representations which are simultaneously useful for recognition and generation. We train our model as a hyper-network for implicit neural representation, which learns to map images to model weights for fast, accurate reconstruction. We further integrate our INR hyper-network with knowledge distillation to improve its generalization and performance. Beyond the novel training design, the model also learns an unprecedented compressed embedding space with outstanding performance for various visual tasks. The complete model competes with state-of-the-art results for image representation learning, while also enabling generative capabilities with its high-quality tiny embeddings. The code is available at https://github.com/tiktok/huvr.

