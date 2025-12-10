---
layout: default
title: Siamese-Driven Optimization for Low-Resolution Image Latent Embedding in Image Captioning
---

# Siamese-Driven Optimization for Low-Resolution Image Latent Embedding in Image Captioning
**arXiv**：[2512.08873v1](https://arxiv.org/abs/2512.08873) · [PDF](https://arxiv.org/pdf/2512.08873.pdf)  
**作者**：Jing Jie Tan, Anissa Mokraoui, Ban-Hoe Kwan, Danny Wee-Kiat Ng, Yan-Chai Hum  

**一句话要点**：提出SOLI方法以解决轻量级低分辨率图像描述中的计算效率问题

**关键词**：低分辨率图像描述, 孪生网络, 潜在嵌入优化, 轻量级模型, 计算效率

## 3 点简述
- 核心问题：低分辨率图像描述任务中，大型模型计算资源需求高，重训练困难。
- 方法要点：采用孪生网络架构优化潜在嵌入，通过双路径结构减少计算开销。
- 实验或效果：在资源受限场景下，保持性能的同时提升效率和准确性。

## 摘要（原文）

> Image captioning is essential in many fields including assisting visually impaired individuals, improving content management systems, and enhancing human-computer interaction. However, a recent challenge in this domain is dealing with low-resolution image (LRI). While performance can be improved by using larger models like transformers for encoding, these models are typically heavyweight, demanding significant computational resources and memory, leading to challenges in retraining. To address this, the proposed SOLI (Siamese-Driven Optimization for Low-Resolution Image Latent Embedding in Image Captioning) approach presents a solution specifically designed for lightweight, low-resolution images captioning. It employs a Siamese network architecture to optimize latent embeddings, enhancing the efficiency and accuracy of the image-to-text translation process. By focusing on a dual-pathway neural network structure, SOLI minimizes computational overhead without sacrificing performance, making it an ideal choice for training on resource-constrained scenarios.

