---
layout: default
title: OCCAM: Class-Agnostic, Training-Free, Prior-Free and Multi-Class Object Counting
---

# OCCAM: Class-Agnostic, Training-Free, Prior-Free and Multi-Class Object Counting
**arXiv**：[2601.13871v1](https://arxiv.org/abs/2601.13871) · [PDF](https://arxiv.org/pdf/2601.13871.pdf)  
**作者**：Michail Spanakis, Iason Oikonomidis, Antonis Argyros  

**一句话要点**：提出OCCAM方法，实现无需训练、先验信息和多类别的类无关物体计数。

**关键词**：类无关物体计数, 训练自由方法, 多类别计数, Segment Anything Model 2, FINCH算法, 合成数据集

## 3 点简述
- 核心问题：解决类无关物体计数，无需假设单类别或依赖额外信息如视觉示例或文本提示。
- 方法要点：基于Segment Anything Model 2和自定义FINCH算法，实现训练自由和多类别计数。
- 实验或效果：在FSC-147和CARPK数据集上表现竞争性，提出合成多类数据集和F1分数作为评估指标。

## 摘要（原文）

> Class-Agnostic object Counting (CAC) involves counting instances of objects from arbitrary classes within an image. Due to its practical importance, CAC has received increasing attention in recent years. Most existing methods assume a single object class per image, rely on extensive training of large deep learning models and address the problem by incorporating additional information, such as visual exemplars or text prompts. In this paper, we present OCCAM, the first training-free approach to CAC that operates without the need of any supplementary information. Moreover, our approach addresses the multi-class variant of the problem, as it is capable of counting the object instances in each and every class among arbitrary object classes within an image. We leverage Segment Anything Model 2 (SAM2), a foundation model, and a custom threshold-based variant of the First Integer Neighbor Clustering Hierarchy (FINCH) algorithm to achieve competitive performance on widely used benchmark datasets, FSC-147 and CARPK. We propose a synthetic multi-class dataset and F1 score as a more suitable evaluation metric. The code for our method and the proposed synthetic dataset will be made publicly available at https://mikespanak.github.io/OCCAM_counter.

