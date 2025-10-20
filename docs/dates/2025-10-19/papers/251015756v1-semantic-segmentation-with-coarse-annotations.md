---
layout: default
title: Semantic segmentation with coarse annotations
---

# Semantic segmentation with coarse annotations
**arXiv**：[2510.15756v1](https://arxiv.org/abs/2510.15756) · [PDF](https://arxiv.org/pdf/2510.15756.pdf)  
**作者**：Jort de Jong, Mike Holenderski  

**一句话要点**：提出基于超像素正则化方法，以提升粗标注下的语义分割边界对齐效果

**关键词**：语义分割, 粗标注, 超像素正则化, 边界对齐, 编码器-解码器架构

## 3 点简述
- 核心问题：粗标注语义分割中边界对齐困难，因部分像素未标注
- 方法要点：在编码器-解码器架构中，引入SLIC超像素正则化，鼓励分割结果与颜色位置一致
- 实验或效果：在SUIM等数据集上，边界召回率显著优于现有方法

## 摘要（原文）

> Semantic segmentation is the task of classifying each pixel in an image.
> Training a segmentation model achieves best results using annotated images,
> where each pixel is annotated with the corresponding class. When obtaining fine
> annotations is difficult or expensive, it may be possible to acquire coarse
> annotations, e.g. by roughly annotating pixels in an images leaving some pixels
> around the boundaries between classes unlabeled. Segmentation with coarse
> annotations is difficult, in particular when the objective is to optimize the
> alignment of boundaries between classes. This paper proposes a regularization
> method for models with an encoder-decoder architecture with superpixel based
> upsampling. It encourages the segmented pixels in the decoded image to be
> SLIC-superpixels, which are based on pixel color and position, independent of
> the segmentation annotation. The method is applied to FCN-16 fully
> convolutional network architecture and evaluated on the SUIM, Cityscapes, and
> PanNuke data sets. It is shown that the boundary recall improves significantly
> compared to state-of-the-art models when trained on coarse annotations.

