---
layout: default
title: Image-Intrinsic Priors for Integrated Circuit Defect Detection and Novel Class Discovery via Self-Supervised Learning
---

# Image-Intrinsic Priors for Integrated Circuit Defect Detection and Novel Class Discovery via Self-Supervised Learning
**arXiv**：[2511.03120v1](https://arxiv.org/abs/2511.03120) · [PDF](https://arxiv.org/pdf/2511.03120.pdf)  
**作者**：Botong. Zhao, Xubin. Wang, Shujing. Lyu, Yue. Lu  

**一句话要点**：提出IC DefectNCD框架，利用图像内在先验进行集成电路缺陷检测与未知类别发现。

**关键词**：集成电路缺陷检测, 自监督学习, 图像内在先验, 未知类别发现, 注意力机制

## 3 点简述
- 集成电路制造缺陷检测面临标注成本高、新类别和罕见缺陷难以处理的问题。
- 方法包括自监督学习、自适应二值化和软掩码注意力机制，提升缺陷区域敏感度。
- 在真实数据集上验证，覆盖15种缺陷类型，表现出稳健的检测和分类性能。

## 摘要（原文）

> Integrated circuit manufacturing is highly complex, comprising hundreds of
> process steps. Defects can arise at any stage, causing yield loss and
> ultimately degrading product reliability. Supervised methods require extensive
> human annotation and struggle with emergent categories and rare, data scarce
> defects. Clustering-based unsupervised methods often exhibit unstable
> performance due to missing priors. We propose IC DefectNCD, a support set free
> framework that leverages Image Intrinsic Priors in IC SEM images for defect
> detection and novel class discovery. We first develop Self Normal Information
> Guided IC Defect Detection, aggregating representative normal features via a
> learnable normal information extractor and using reconstruction residuals to
> coarsely localize defect regions. To handle saliency variations across defects,
> we introduce an adaptive binarization strategy that produces stable subimages
> focused on core defective areas. Finally, we design Self Defect Information
> Guided IC Defect Classification, which incorporates a soft mask guided
> attention mechanism to inject spatial defect priors into the teacher student
> model. This enhances sensitivity to defective regions, suppresses background
> interference, and enables recognition and classification of unseen defects. We
> validate the approach on a real world dataset spanning three key fabrication
> stages and covering 15 defect types. Experiments demonstrate robust performance
> on both defect detection and unseen defect classification.

