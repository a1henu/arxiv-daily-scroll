---
layout: default
title: Instance-Level Composed Image Retrieval
---

# Instance-Level Composed Image Retrieval
**arXiv**：[2510.25387v1](https://arxiv.org/abs/2510.25387) · [PDF](https://arxiv.org/pdf/2510.25387.pdf)  
**作者**：Bill Psomas, George Retsinas, Nikos Efthymiadis, Panagiotis Filntisis, Yannis Avrithis, Petros Maragos, Ondrej Chum, Giorgos Tolias  

**一句话要点**：提出i-CIR数据集和BASIC方法以解决实例级组合图像检索的数据与方法挑战

**关键词**：组合图像检索, 实例级检索, 视觉语言模型, 训练无关方法, 数据集构建, 后期融合

## 3 点简述
- 核心问题：组合图像检索缺乏高质量训练和评估数据，尤其实例级定义。
- 方法要点：使用预训练VLM进行训练无关检索，通过后期融合优化图像相似度。
- 实验或效果：在i-CIR和现有数据集上达到新SOTA，支持硬负样本选择。

## 摘要（原文）

> The progress of composed image retrieval (CIR), a popular research direction
> in image retrieval, where a combined visual and textual query is used, is held
> back by the absence of high-quality training and evaluation data. We introduce
> a new evaluation dataset, i-CIR, which, unlike existing datasets, focuses on an
> instance-level class definition. The goal is to retrieve images that contain
> the same particular object as the visual query, presented under a variety of
> modifications defined by textual queries. Its design and curation process keep
> the dataset compact to facilitate future research, while maintaining its
> challenge-comparable to retrieval among more than 40M random
> distractors-through a semi-automated selection of hard negatives.
>   To overcome the challenge of obtaining clean, diverse, and suitable training
> data, we leverage pre-trained vision-and-language models (VLMs) in a
> training-free approach called BASIC. The method separately estimates
> query-image-to-image and query-text-to-image similarities, performing late
> fusion to upweight images that satisfy both queries, while down-weighting those
> that exhibit high similarity with only one of the two. Each individual
> similarity is further improved by a set of components that are simple and
> intuitive. BASIC sets a new state of the art on i-CIR but also on existing CIR
> datasets that follow a semantic-level class definition. Project page:
> https://vrg.fel.cvut.cz/icir/.

