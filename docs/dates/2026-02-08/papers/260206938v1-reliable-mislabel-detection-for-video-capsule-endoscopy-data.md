---
layout: default
title: Reliable Mislabel Detection for Video Capsule Endoscopy Data
---

# Reliable Mislabel Detection for Video Capsule Endoscopy Data
**arXiv**：[2602.06938v1](https://arxiv.org/abs/2602.06938) · [PDF](https://arxiv.org/pdf/2602.06938.pdf)  
**作者**：Julia Werner, Julius Oexle, Oliver Bause, Maxime Le Floch, Franz Brinkmann, Hannah Tolle, Jochen Hampe, Oliver Bringmann  

**一句话要点**：提出医疗数据集误标检测框架，提升视频胶囊内镜数据分类性能

**关键词**：误标检测, 医疗影像, 视频胶囊内镜, 深度学习, 数据清洗, 异常检测

## 3 点简述
- 核心问题：医疗影像标注依赖专家，数据有限且类边界模糊，影响深度学习分类准确性。
- 方法要点：开发误标检测框架，识别并清理数据集中的错误标签，基于公开视频胶囊内镜数据集验证。
- 实验或效果：框架成功检测误标样本，经专家复审后，清洗数据集提升了异常检测性能，优于现有基线。

## 摘要（原文）

> The classification performance of deep neural networks relies strongly on access to large, accurately annotated datasets. In medical imaging, however, obtaining such datasets is particularly challenging since annotations must be provided by specialized physicians, which severely limits the pool of annotators. Furthermore, class boundaries can often be ambiguous or difficult to define which further complicates machine learning-based classification. In this paper, we want to address this problem and introduce a framework for mislabel detection in medical datasets. This is validated on the two largest, publicly available datasets for Video Capsule Endoscopy, an important imaging procedure for examining the gastrointestinal tract based on a video stream of lowresolution images. In addition, potentially mislabeled samples identified by our pipeline were reviewed and re-annotated by three experienced gastroenterologists. Our results show that the proposed framework successfully detects incorrectly labeled data and results in an improved anomaly detection performance after cleaning the datasets compared to current baselines.

