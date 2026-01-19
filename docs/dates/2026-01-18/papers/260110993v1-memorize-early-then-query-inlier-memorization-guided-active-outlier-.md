---
layout: default
title: Memorize Early, Then Query: Inlier-Memorization-Guided Active Outlier Detection
---

# Memorize Early, Then Query: Inlier-Memorization-Guided Active Outlier Detection
**arXiv**：[2601.10993v1](https://arxiv.org/abs/2601.10993) · [PDF](https://arxiv.org/pdf/2601.10993.pdf)  
**作者**：Minseo Kang, Seunghwan Park, Dongha Kim  

**一句话要点**：提出IMBoost框架，结合记忆效应与主动学习以提升异常检测性能

**关键词**：异常检测, 记忆效应, 主动学习, 深度学习, 无监督学习, 生成模型

## 3 点简述
- 核心问题：无监督异常检测在数据重叠或密集异常时效果不佳，依赖记忆效应仍有限制
- 方法要点：采用两阶段框架，先诱导记忆效应，后通过主动查询极化异常与正常样本的分数差异
- 实验或效果：在多个基准数据集上显著优于现有方法，且计算成本更低，理论分析支持分离效果增强

## 摘要（原文）

> Outlier detection (OD) aims to identify abnormal instances, known as outliers or anomalies, by learning typical patterns of normal data, or inliers. Performing OD under an unsupervised regime-without any information about anomalous instances in the training data-is challenging. A recently observed phenomenon, known as the inlier-memorization (IM) effect, where deep generative models (DGMs) tend to memorize inlier patterns during early training, provides a promising signal for distinguishing outliers. However, existing unsupervised approaches that rely solely on the IM effect still struggle when inliers and outliers are not well-separated or when outliers form dense clusters. To address these limitations, we incorporate active learning to selectively acquire informative labels, and propose IMBoost, a novel framework that explicitly reinforces the IM effect to improve outlier detection. Our method consists of two stages: 1) a warm-up phase that induces and promotes the IM effect, and 2) a polarization phase in which actively queried samples are used to maximize the discrepancy between inlier and outlier scores. In particular, we propose a novel query strategy and tailored loss function in the polarization phase to effectively identify informative samples and fully leverage the limited labeling budget. We provide a theoretical analysis showing that the IMBoost consistently decreases inlier risk while increasing outlier risk throughout training, thereby amplifying their separation. Extensive experiments on diverse benchmark datasets demonstrate that IMBoost not only significantly outperforms state-of-the-art active OD methods but also requires substantially less computational cost.

