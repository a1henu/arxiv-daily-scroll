---
layout: default
title: GenDet: Painting Colored Bounding Boxes on Images via Diffusion Model for Object Detection
---

# GenDet: Painting Colored Bounding Boxes on Images via Diffusion Model for Object Detection
**arXiv**：[2601.07273v1](https://arxiv.org/abs/2601.07273) · [PDF](https://arxiv.org/pdf/2601.07273.pdf)  
**作者**：Chen Min, Chengyang Li, Fanjie Kong, Qi Zhu, Dawei Zhao, Liang Xiao  

**一句话要点**：提出GenDet，通过扩散模型在图像上生成带语义标注的边界框以解决目标检测问题。

**关键词**：目标检测, 扩散模型, 生成式建模, 语义约束, 统一视觉理解

## 3 点简述
- 核心问题：将目标检测重新定义为图像生成任务，以弥合生成模型与判别任务之间的差距。
- 方法要点：基于预训练Stable Diffusion构建条件生成架构，在潜在空间中施加语义约束以控制边界框位置和类别。
- 实验或效果：系统实验显示GenDet在保持生成模型灵活性的同时，达到与判别检测器竞争的准确度。

## 摘要（原文）

> This paper presents GenDet, a novel framework that redefines object detection as an image generation task. In contrast to traditional approaches, GenDet adopts a pioneering approach by leveraging generative modeling: it conditions on the input image and directly generates bounding boxes with semantic annotations in the original image space. GenDet establishes a conditional generation architecture built upon the large-scale pre-trained Stable Diffusion model, formulating the detection task as semantic constraints within the latent space. It enables precise control over bounding box positions and category attributes, while preserving the flexibility of the generative model. This novel methodology effectively bridges the gap between generative models and discriminative tasks, providing a fresh perspective for constructing unified visual understanding systems. Systematic experiments demonstrate that GenDet achieves competitive accuracy compared to discriminative detectors, while retaining the flexibility characteristic of generative methods.

