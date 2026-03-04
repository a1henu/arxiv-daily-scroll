---
layout: default
title: Spatial Autoregressive Modeling of DINOv3 Embeddings for Unsupervised Anomaly Detection
---

# Spatial Autoregressive Modeling of DINOv3 Embeddings for Unsupervised Anomaly Detection
**arXiv**：[2603.02974v1](https://arxiv.org/abs/2603.02974) · [PDF](https://arxiv.org/pdf/2603.02974.pdf)  
**作者**：Ertunc Erdil, Nico Schulthess, Guney Tombak, Ender Konukoglu  

**一句话要点**：提出基于DINOv3嵌入的空间自回归模型，用于无监督异常检测

**关键词**：无监督异常检测, DINOv3嵌入, 空间自回归模型, 医学图像分析, 参数化建模

## 3 点简述
- 现有方法忽略补丁间的空间关系，假设自注意力已编码上下文信息
- 使用2D自回归CNN建模补丁嵌入的空间依赖，学习紧凑参数化正态分布
- 在BMAD基准测试中，实现竞争性性能，显著降低推理时间和内存需求

## 摘要（原文）

> DINO models provide rich patch-level representations that have recently enabled strong performance in unsupervised anomaly detection (UAD). Most existing methods extract patch embeddings from ``normal'' images and model them independently, ignoring spatial and neighborhood relationships between patches. This implicitly assumes that self-attention and positional encodings sufficiently encode contextual information within each patch embedding. In addition, the normative distribution is often modeled as memory banks or prototype-based representations, which require storing large numbers of features and performing costly comparisons at inference time, leading to substantial memory and computational overhead. In this work, we address both limitations by proposing a simple and efficient framework that explicitly models spatial and contextual dependencies between patch embeddings using a 2D autoregressive (AR) model. Instead of storing embeddings or clustering prototypes, our approach learns a compact parametric model of the normative distribution via an AR convolutional neural network (CNN). At test time, anomaly detection reduces to a single forward pass through the network and enables fast and memory-efficient inference. We evaluate our method on the BMAD benchmark, which comprises three medical imaging datasets, and compare it against existing work including recent DINO-based methods. Experimental results demonstrate that explicitly modeling spatial dependencies achieves competitive anomaly detection performance while substantially reducing inference time and memory requirements. Code is available at the project page: https://eerdil.github.io/spatial-ar-dinov3-uad/.

