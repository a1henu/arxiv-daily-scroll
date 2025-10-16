---
layout: default
title: Sample-Centric Multi-Task Learning for Detection and Segmentation of Industrial Surface Defects
---

# Sample-Centric Multi-Task Learning for Detection and Segmentation of Industrial Surface Defects
**arXiv**：[2510.13226v1](https://arxiv.org/abs/2510.13226) · [PDF](https://arxiv.org/pdf/2510.13226.pdf)  
**作者**：Hang-Cheng Dong, Yibo Jiao, Fupeng Wei, Guodong Liu, Dong Ye, Bingguo Liu  

**一句话要点**：提出样本中心多任务学习框架以解决工业表面缺陷检测中的样本级决策不稳定问题

**关键词**：工业缺陷检测, 多任务学习, 样本级决策, 分割评估指标, 缺陷稀疏性

## 3 点简述
- 核心问题：像素中心训练易受大均匀区域主导，导致小或低对比度缺陷检测不稳定
- 方法要点：联合学习样本级缺陷分类和像素级掩码定位，通过样本级监督提升召回率
- 实验或效果：在基准数据集上显著提高样本级决策可靠性和缺陷定位完整性

## 摘要（原文）

> Industrial surface defect inspection for sample-wise quality control (QC)
> must simultaneously decide whether a given sample contains defects and localize
> those defects spatially. In real production lines, extreme
> foreground-background imbalance, defect sparsity with a long-tailed scale
> distribution, and low contrast are common. As a result, pixel-centric training
> and evaluation are easily dominated by large homogeneous regions, making it
> difficult to drive models to attend to small or low-contrast defects-one of the
> main bottlenecks for deployment. Empirically, existing models achieve strong
> pixel-overlap metrics (e.g., mIoU) but exhibit insufficient stability at the
> sample level, especially for sparse or slender defects. The root cause is a
> mismatch between the optimization objective and the granularity of QC
> decisions. To address this, we propose a sample-centric multi-task learning
> framework and evaluation suite. Built on a shared-encoder architecture, the
> method jointly learns sample-level defect classification and pixel-level mask
> localization. Sample-level supervision modulates the feature distribution and,
> at the gradient level, continually boosts recall for small and low-contrast
> defects, while the segmentation branch preserves boundary and shape details to
> enhance per-sample decision stability and reduce misses. For evaluation, we
> propose decision-linked metrics, Seg_mIoU and Seg_Recall, which remove the bias
> of classical mIoU caused by empty or true-negative samples and tightly couple
> localization quality with sample-level decisions. Experiments on two benchmark
> datasets demonstrate that our approach substantially improves the reliability
> of sample-level decisions and the completeness of defect localization.

