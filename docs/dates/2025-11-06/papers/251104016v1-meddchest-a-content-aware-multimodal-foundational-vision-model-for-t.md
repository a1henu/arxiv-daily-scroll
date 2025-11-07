---
layout: default
title: MedDChest: A Content-Aware Multimodal Foundational Vision Model for Thoracic Imaging
---

# MedDChest: A Content-Aware Multimodal Foundational Vision Model for Thoracic Imaging
**arXiv**：[2511.04016v1](https://arxiv.org/abs/2511.04016) · [PDF](https://arxiv.org/pdf/2511.04016.pdf)  
**作者**：Mahmoud Soliman, Islam Osman, Mohamed S. Shehata, Rasika Rajapakshe  

**一句话要点**：提出MedDChest基础视觉模型，通过领域特定预训练解决胸部影像诊断中的领域差距问题。

**关键词**：胸部影像, 基础视觉模型, 领域特定预训练, 内容感知数据增强, Vision Transformer, 医学诊断

## 3 点简述
- 核心问题：医学影像模型性能受限于基于自然图像预训练骨干网络的领域差距。
- 方法要点：从零预训练ViT模型，使用内容感知数据增强策略优化解剖相关区域采样。
- 实验或效果：在多样化下游诊断任务中，显著优于ImageNet预训练模型。

## 摘要（原文）

> The performance of vision models in medical imaging is often hindered by the
> prevailing paradigm of fine-tuning backbones pre-trained on out-of-domain
> natural images. To address this fundamental domain gap, we propose MedDChest, a
> new foundational Vision Transformer (ViT) model optimized specifically for
> thoracic imaging. We pre-trained MedDChest from scratch on a massive, curated,
> multimodal dataset of over 1.2 million images, encompassing different
> modalities including Chest X-ray and Computed Tomography (CT) compiled from 10
> public sources. A core technical contribution of our work is Guided Random
> Resized Crops, a novel content-aware data augmentation strategy that biases
> sampling towards anatomically relevant regions, overcoming the inefficiency of
> standard cropping techniques on medical scans. We validate our model's
> effectiveness by fine-tuning it on a diverse set of downstream diagnostic
> tasks. Comprehensive experiments empirically demonstrate that MedDChest
> significantly outperforms strong, publicly available ImageNet-pretrained
> models. By establishing the superiority of large-scale, in-domain pre-training
> combined with domain-specific data augmentation, MedDChest provides a powerful
> and robust feature extractor that serves as a significantly better starting
> point for a wide array of thoracic diagnostic tasks. The model weights will be
> made publicly available to foster future research and applications.

