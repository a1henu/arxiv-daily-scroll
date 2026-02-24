---
layout: default
title: Multimodal Dataset Distillation Made Simple by Prototype-Guided Data Synthesis
---

# Multimodal Dataset Distillation Made Simple by Prototype-Guided Data Synthesis
**arXiv**：[2602.19756v1](https://arxiv.org/abs/2602.19756) · [PDF](https://arxiv.org/pdf/2602.19756.pdf)  
**作者**：Junhyeok Choi, Sangwoo Mo, Minwoo Chae  

**一句话要点**：提出原型引导数据合成的免学习多模态数据集蒸馏框架，以解决大规模训练和架构依赖问题。

**关键词**：多模态学习, 数据集蒸馏, 原型引导, 免学习框架, 跨架构泛化, 图像合成

## 3 点简述
- 核心问题：多模态学习依赖大规模数据集，现有蒸馏方法需全数据集训练和联合优化，导致成本高且架构依赖。
- 方法要点：使用CLIP提取对齐嵌入，获取原型，通过unCLIP解码器合成图像，实现免学习蒸馏。
- 实验或效果：在实验中优于基于优化的蒸馏和子集选择方法，实现跨架构泛化的最先进性能。

## 摘要（原文）

> Recent advances in multimodal learning have achieved remarkable success across diverse vision-language tasks. However, such progress heavily relies on large-scale image-text datasets, making training costly and inefficient. Prior efforts in dataset filtering and pruning attempt to mitigate this issue, but still require relatively large subsets to maintain performance and fail under very small subsets. Dataset distillation offers a promising alternative, yet existing multimodal dataset distillation methods require full-dataset training and joint optimization of image pixels and text features, making them architecture-dependent and limiting cross-architecture generalization. To overcome this, we propose a learning-free dataset distillation framework that eliminates the need for large-scale training and optimization while enhancing generalization across architectures. Our method uses CLIP to extract aligned image-text embeddings, obtains prototypes, and employs an unCLIP decoder to synthesize images, enabling efficient and scalable multimodal dataset distillation. Extensive experiments demonstrate that our approach consistently outperforms optimization-based dataset distillation and subset selection methods, achieving state-of-the-art cross-architecture generalization.

