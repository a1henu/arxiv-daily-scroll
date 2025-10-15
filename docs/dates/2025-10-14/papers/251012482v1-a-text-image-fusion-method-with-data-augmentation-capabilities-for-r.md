---
layout: default
title: A Text-Image Fusion Method with Data Augmentation Capabilities for Referring Medical Image Segmentation
---

# A Text-Image Fusion Method with Data Augmentation Capabilities for Referring Medical Image Segmentation
**arXiv**：[2510.12482v1](https://arxiv.org/abs/2510.12482) · [PDF](https://arxiv.org/pdf/2510.12482.pdf)  
**作者**：Shurong Chai, Rahul Kumar JAIN, Rui Xu, Shaocong Mo, Ruibo Hou, Shiyu Teng, Jiaqing Liu, Lanfen Lin, Yen-Wei Chen  

**一句话要点**：提出早期融合框架以解决医学图像分割中文本-图像空间对齐问题

**关键词**：医学图像分割, 文本引导分割, 早期融合, 数据增强, 多模态学习

## 3 点简述
- 核心问题：传统数据增强破坏文本与图像空间对齐，影响分割性能
- 方法要点：早期融合文本与视觉特征，设计轻量生成器投影文本嵌入
- 实验或效果：在三个医学任务和四个框架上实现最优结果，代码开源

## 摘要（原文）

> Deep learning relies heavily on data augmentation to mitigate limited data,
> especially in medical imaging. Recent multimodal learning integrates text and
> images for segmentation, known as referring or text-guided image segmentation.
> However, common augmentations like rotation and flipping disrupt spatial
> alignment between image and text, weakening performance. To address this, we
> propose an early fusion framework that combines text and visual features before
> augmentation, preserving spatial consistency. We also design a lightweight
> generator that projects text embeddings into visual space, bridging semantic
> gaps. Visualization of generated pseudo-images shows accurate region
> localization. Our method is evaluated on three medical imaging tasks and four
> segmentation frameworks, achieving state-of-the-art results. Code is publicly
> available on GitHub: https://github.com/11yxk/MedSeg_EarlyFusion.

