---
layout: default
title: DCMIL: A Progressive Representation Learning Model of Whole Slide Images for Cancer Prognosis Analysis
---

# DCMIL: A Progressive Representation Learning Model of Whole Slide Images for Cancer Prognosis Analysis
**arXiv**：[2510.14403v1](https://arxiv.org/abs/2510.14403) · [PDF](https://arxiv.org/pdf/2510.14403.pdf)  
**作者**：Chao Tu, Kun Huang, Jie Zhang, Qianjin Feng, Yu Zhang, Zhenyuan Ning  

**一句话要点**：提出DCMIL模型以解决全切片图像癌症预后分析中的计算瓶颈和标注稀缺问题

**关键词**：全切片图像分析, 多实例学习, 癌症预后, 对比学习, 计算病理学

## 3 点简述
- 核心问题：全切片图像尺寸巨大且缺乏密集标注，阻碍癌症预后模型发展
- 方法要点：采用双课程对比多实例学习，无需密集标注，渐进学习多放大级别特征
- 实验或效果：在12种癌症类型上验证，性能优于标准模型，识别预后关键区域

## 摘要（原文）

> The burgeoning discipline of computational pathology shows promise in
> harnessing whole slide images (WSIs) to quantify morphological heterogeneity
> and develop objective prognostic modes for human cancers. However, progress is
> impeded by the computational bottleneck of gigapixel-size inputs and the
> scarcity of dense manual annotations. Current methods often overlook
> fine-grained information across multi-magnification WSIs and variations in
> tumor microenvironments. Here, we propose an easy-to-hard progressive
> representation learning model, termed dual-curriculum contrastive
> multi-instance learning (DCMIL), to efficiently process WSIs for cancer
> prognosis. The model does not rely on dense annotations and enables the direct
> transformation of gigapixel-size WSIs into outcome predictions. Extensive
> experiments on twelve cancer types (5,954 patients, 12.54 million tiles)
> demonstrate that DCMIL outperforms standard WSI-based prognostic models.
> Additionally, DCMIL identifies fine-grained prognosis-salient regions, provides
> robust instance uncertainty estimation, and captures morphological differences
> between normal and tumor tissues, with the potential to generate new biological
> insights. All codes have been made publicly accessible at
> https://github.com/tuuuc/DCMIL.

