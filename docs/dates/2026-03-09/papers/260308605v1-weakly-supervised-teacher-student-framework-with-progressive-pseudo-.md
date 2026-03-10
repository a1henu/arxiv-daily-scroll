---
layout: default
title: Weakly Supervised Teacher-Student Framework with Progressive Pseudo-mask Refinement for Gland Segmentation
---

# Weakly Supervised Teacher-Student Framework with Progressive Pseudo-mask Refinement for Gland Segmentation
**arXiv**：[2603.08605v1](https://arxiv.org/abs/2603.08605) · [PDF](https://arxiv.org/pdf/2603.08605.pdf)  
**作者**：Hikmat Khan, Wei Chen, Muhammad Khalid Khan Niazi  

**一句话要点**：提出弱监督师生框架，通过渐进伪掩码优化实现结直肠癌腺体分割

**关键词**：弱监督分割, 师生框架, 伪掩码优化, 腺体分割, 结直肠癌病理

## 3 点简述
- 问题：腺体分割依赖像素级标注，获取成本高，弱监督方法易产生不完整伪掩码。
- 方法：结合稀疏标注与指数移动平均教师网络，通过置信度过滤和自适应融合渐进优化伪掩码。
- 效果：在Gland Segmentation数据集上平均IoU达80.10，跨数据集评估显示良好泛化性。

## 摘要（原文）

> Background and objectives: Colorectal cancer histopathological grading depends on accurate segmentation of glandular structures. Current deep learning approaches rely on large scale pixel level annotations that are labor intensive and difficult to obtain in routine clinical practice. Weakly supervised semantic segmentation offers a promising alternative. However, class activation map based methods often produce incomplete pseudo masks that emphasize highly discriminative regions and fail to supervise unannotated glandular structures. We propose a weakly supervised teacher student framework that leverages sparse pathologist annotations and an Exponential Moving Average stabilized teacher network to generate refined pseudo masks.
>   Methods: The framework integrates confidence based filtering, adaptive fusion of teacher predictions with limited ground truth, and curriculum guided refinement to progressively segment unannotated glandular regions. The method was evaluated on an institutional colorectal cancer cohort from The Ohio State University Wexner Medical Center consisting of 60 hematoxylin and eosin stained whole slide images and on public datasets including the Gland Segmentation dataset, TCGA COAD, TCGA READ, and SPIDER.
>   Results: On the Gland Segmentation dataset the framework achieved a mean Intersection over Union of 80.10 and a mean Dice coefficient of 89.10. Cross cohort evaluation demonstrated robust generalization on TCGA COAD and TCGA READ without additional annotations, while reduced performance on SPIDER reflected domain shift.
>   Conclusions: The proposed framework provides an annotation efficient and generalizable approach for gland segmentation in colorectal histopathology.

