---
layout: default
title: Seeing and Knowing in the Wild: Open-domain Visual Entity Recognition with Large-scale Knowledge Graphs via Contrastive Learning
---

# Seeing and Knowing in the Wild: Open-domain Visual Entity Recognition with Large-scale Knowledge Graphs via Contrastive Learning
**arXiv**：[2510.13675v1](https://arxiv.org/abs/2510.13675) · [PDF](https://arxiv.org/pdf/2510.13675.pdf)  
**作者**：Hongkuan Zhou, Lavdim Halilaj, Sebastian Monka, Stefan Schmid, Yuqicheng Zhu, Jingcheng Wu, Nadeem Nazer, Steffen Staab  

**一句话要点**：提出知识引导对比学习框架，解决开放域视觉实体识别中的零样本和长尾问题。

**关键词**：开放域视觉实体识别, 对比学习, 知识图谱, 零样本学习, 长尾分布

## 3 点简述
- 核心问题：开放域视觉实体识别面临零样本、长尾分布和语义歧义挑战。
- 方法要点：结合图像、文本和知识图谱，在共享语义空间进行对比学习。
- 实验或效果：在OVEN基准上，小模型对未见实体准确率提升10.5%。

## 摘要（原文）

> Open-domain visual entity recognition aims to identify and link entities
> depicted in images to a vast and evolving set of real-world concepts, such as
> those found in Wikidata. Unlike conventional classification tasks with fixed
> label sets, it operates under open-set conditions, where most target entities
> are unseen during training and exhibit long-tail distributions. This makes the
> task inherently challenging due to limited supervision, high visual ambiguity,
> and the need for semantic disambiguation. In this work, we propose a
> Knowledge-guided Contrastive Learning (KnowCoL) framework that combines both
> images and text descriptions into a shared semantic space grounded by
> structured information from Wikidata. By abstracting visual and textual inputs
> to a conceptual level, the model leverages entity descriptions, type
> hierarchies, and relational context to support zero-shot entity recognition. We
> evaluate our approach on the OVEN benchmark, a large-scale open-domain visual
> recognition dataset with Wikidata IDs as the label space. Our experiments show
> that using visual, textual, and structured knowledge greatly improves accuracy,
> especially for rare and unseen entities. Our smallest model improves the
> accuracy on unseen entities by 10.5% compared to the state-of-the-art, despite
> being 35 times smaller.

