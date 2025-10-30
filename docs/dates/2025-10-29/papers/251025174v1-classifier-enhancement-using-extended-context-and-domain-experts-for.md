---
layout: default
title: Classifier Enhancement Using Extended Context and Domain Experts for Semantic Segmentation
---

# Classifier Enhancement Using Extended Context and Domain Experts for Semantic Segmentation
**arXiv**：[2510.25174v1](https://arxiv.org/abs/2510.25174) · [PDF](https://arxiv.org/pdf/2510.25174.pdf)  
**作者**：Huadong Tang, Youpeng Zhao, Min Xu, Jun Wang, Qiang Wu  

**一句话要点**：提出扩展上下文感知分类器以解决语义分割中类分布差异和类不平衡问题

**关键词**：语义分割, 上下文感知分类器, 师生网络, 类不平衡, 记忆库

## 3 点简述
- 核心问题：固定参数分类器无法适应图像间类分布差异，类不平衡导致分割偏向多数类
- 方法要点：动态调整分类器，结合数据集级和图像级上下文信息，采用师生网络范式
- 实验或效果：在ADE20K、COCO-Stuff10K和Pascal-Context数据集上达到先进性能

## 摘要（原文）

> Prevalent semantic segmentation methods generally adopt a vanilla classifier
> to categorize each pixel into specific classes.
>   Although such a classifier learns global information from the training data,
> this information is represented by a set of fixed parameters (weights and
> biases).
>   However, each image has a different class distribution, which prevents the
> classifier from addressing the unique characteristics of individual images.
>   At the dataset level, class imbalance leads to segmentation results being
> biased towards majority classes, limiting the model's effectiveness in
> identifying and segmenting minority class regions.
>   In this paper, we propose an Extended Context-Aware Classifier (ECAC) that
> dynamically adjusts the classifier using global (dataset-level) and local
> (image-level) contextual information.
>   Specifically, we leverage a memory bank to learn dataset-level contextual
> information of each class, incorporating the class-specific contextual
> information from the current image to improve the classifier for precise pixel
> labeling.
>   Additionally, a teacher-student network paradigm is adopted, where the domain
> expert (teacher network) dynamically adjusts contextual information with ground
> truth and transfers knowledge to the student network.
>   Comprehensive experiments illustrate that the proposed ECAC can achieve
> state-of-the-art performance across several datasets, including ADE20K,
> COCO-Stuff10K, and Pascal-Context.

