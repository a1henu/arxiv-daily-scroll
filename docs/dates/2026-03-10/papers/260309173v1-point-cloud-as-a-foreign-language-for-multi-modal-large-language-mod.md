---
layout: default
title: Point Cloud as a Foreign Language for Multi-modal Large Language Model
---

# Point Cloud as a Foreign Language for Multi-modal Large Language Model
**arXiv**：[2603.09173v1](https://arxiv.org/abs/2603.09173) · [PDF](https://arxiv.org/pdf/2603.09173.pdf)  
**作者**：Sneha Paul, Zachary Patterson, Nizar Bouguila  

**一句话要点**：提出SAGE端到端3D多模态大语言模型，直接处理原始点云以解决语义对齐和计算效率问题。

**关键词**：点云处理, 多模态大语言模型, 端到端学习, 3D理解, 语义对齐, 偏好优化

## 3 点简述
- 核心问题：现有基于编码器的3D MLLMs存在语义对齐差、分辨率敏感和计算开销大。
- 方法要点：引入轻量级3D分词器，将点云转换为离散令牌，并采用偏好优化训练策略增强推理。
- 实验或效果：在多个3D理解基准上优于现有方法，计算效率高、泛化性强且对分辨率变化鲁棒。

## 摘要（原文）

> Multi-modal large language models (MLLMs) have shown remarkable progress in integrating visual and linguistic understanding. Recent efforts have extended these capabilities to 3D understanding through encoder-based architectures that rely on pre-trained 3D encoders to extract geometric features. However, such approaches suffer from semantic misalignment between geometric and linguistic spaces, resolution sensitivity, and substantial computational overhead. In this work, we present SAGE, the first end-to-end 3D MLLM that directly processes raw point clouds without relying on a pre-trained 3D encoder. Our approach introduces a lightweight 3D tokenizer that combines geometric sampling and neighbourhood aggregation with vector quantization to convert point clouds into discrete tokens--treating 3D data as a foreign language that naturally extends the LLM's vocabulary. Furthermore, to enhance the model's reasoning capability on complex 3D tasks, we propose a preference optimization training strategy with a semantic alignment-based reward, specifically designed for open-ended 3D question answering where responses are descriptive. Extensive experiments across diverse 3D understanding benchmarks demonstrate that our end-to-end approach outperforms existing encoder-based methods while offering significant advantages in computational efficiency, generalization across LLM backbones, and robustness to input resolution variations. Code is available at: github.com/snehaputul/SAGE3D.

