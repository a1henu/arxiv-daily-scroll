---
layout: default
title: SIRR-LMM: Single-image Reflection Removal via Large Multimodal Model
---

# SIRR-LMM: Single-image Reflection Removal via Large Multimodal Model
**arXiv**：[2601.07209v1](https://arxiv.org/abs/2601.07209) · [PDF](https://arxiv.org/pdf/2601.07209.pdf)  
**作者**：Yu Guo, Zhiqiang Lao, Xiyun Song, Yubin Zhou, Heather Yu  

**一句话要点**：提出SIRR-LMM方法，利用大型多模态模型解决单图像反射去除问题。

**关键词**：单图像反射去除, 大型多模态模型, 合成数据集, 路径追踪, LoRA微调

## 3 点简述
- 核心问题：玻璃表面反射导致单图像反射去除困难，现有数据集物理真实性或规模不足。
- 方法要点：通过路径追踪合成数据集，并采用LoRA微调大型多模态模型进行反射去除。
- 实验或效果：相比先进方法，提升了反射去除和分离性能。

## 摘要（原文）

> Glass surfaces create complex interactions of reflected and transmitted light, making single-image reflection removal (SIRR) challenging. Existing datasets suffer from limited physical realism in synthetic data or insufficient scale in real captures. We introduce a synthetic dataset generation framework that path-traces 3D glass models over real background imagery to create physically accurate reflection scenarios with varied glass properties, camera settings, and post-processing effects. To leverage the capabilities of Large Multimodal Model (LMM), we concatenate the image layers into a single composite input, apply joint captioning, and fine-tune the model using task-specific LoRA rather than full-parameter training. This enables our approach to achieve improved reflection removal and separation performance compared to state-of-the-art methods.

