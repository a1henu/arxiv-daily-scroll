---
layout: default
title: IDT: A Physically Grounded Transformer for Feed-Forward Multi-View Intrinsic Decomposition
---

# IDT: A Physically Grounded Transformer for Feed-Forward Multi-View Intrinsic Decomposition
**arXiv**：[2512.23667v1](https://arxiv.org/abs/2512.23667) · [PDF](https://arxiv.org/pdf/2512.23667.pdf)  
**作者**：Kang Du, Yirui Guan, Zeyu Wang  

**一句话要点**：提出IDT前馈Transformer框架，以解决多视角本征图像分解中的视角不一致问题。

**关键词**：多视角本征图像分解, Transformer模型, 物理图像形成模型, 视角一致性, 前馈框架

## 3 点简述
- 核心问题：RGB图像混合材质、光照和视角效应，多视角分解易产生视角不一致。
- 方法要点：基于物理图像形成模型，使用Transformer联合推理多图，分解为漫反射、漫反射着色和镜面着色。
- 实验或效果：在合成和真实数据集上，IDT提升分解质量和多视角一致性，优于先前方法。

## 摘要（原文）

> Intrinsic image decomposition is fundamental for visual understanding, as RGB images entangle material properties, illumination, and view-dependent effects. Recent diffusion-based methods have achieved strong results for single-view intrinsic decomposition; however, extending these approaches to multi-view settings remains challenging, often leading to severe view inconsistency. We propose \textbf{Intrinsic Decomposition Transformer (IDT)}, a feed-forward framework for multi-view intrinsic image decomposition. By leveraging transformer-based attention to jointly reason over multiple input images, IDT produces view-consistent intrinsic factors in a single forward pass, without iterative generative sampling. IDT adopts a physically grounded image formation model that explicitly decomposes images into diffuse reflectance, diffuse shading, and specular shading. This structured factorization separates Lambertian and non-Lambertian light transport, enabling interpretable and controllable decomposition of material and illumination effects across views. Experiments on both synthetic and real-world datasets demonstrate that IDT achieves cleaner diffuse reflectance, more coherent diffuse shading, and better-isolated specular components, while substantially improving multi-view consistency compared to prior intrinsic decomposition methods.

