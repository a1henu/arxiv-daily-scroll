---
layout: default
title: Object-Centric Data Synthesis for Category-level Object Detection
---

# Object-Centric Data Synthesis for Category-level Object Detection
**arXiv**：[2511.23450v1](https://arxiv.org/abs/2511.23450) · [PDF](https://arxiv.org/pdf/2511.23450.pdf)  
**作者**：Vikhyat Agarwal, Jiayi Cora Guo, Declan Hoban, Sissi Zhang, Nicholas Moran, Peter Cho, Srilakshmi Pattabiraman, Shantanu Joshi  

**一句话要点**：提出基于物体中心数据合成方法，以在数据受限场景下提升类别级物体检测性能

**关键词**：物体中心数据合成, 类别级物体检测, 数据增强, 3D渲染, 图像扩散模型, 长尾类别

## 3 点简述
- 核心问题：新物体类别检测需大量标注数据，但长尾类别数据获取成本高
- 方法要点：利用物体中心数据（多视图图像或3D模型），通过图像处理、3D渲染和扩散模型合成真实杂乱图像
- 实验或效果：在数据受限设置中评估四种合成方法，显著提升模型在真实世界数据的类别级泛化能力

## 摘要（原文）

> Deep learning approaches to object detection have achieved reliable detection of specific object classes in images. However, extending a model's detection capability to new object classes requires large amounts of annotated training data, which is costly and time-consuming to acquire, especially for long-tailed classes with insufficient representation in existing datasets. Here, we introduce the object-centric data setting, when limited data is available in the form of object-centric data (multi-view images or 3D models), and systematically evaluate the performance of four different data synthesis methods to finetune object detection models on novel object categories in this setting. The approaches are based on simple image processing techniques, 3D rendering, and image diffusion models, and use object-centric data to synthesize realistic, cluttered images with varying contextual coherence and complexity. We assess how these methods enable models to achieve category-level generalization in real-world data, and demonstrate significant performance boosts within this data-constrained experimental setting.

