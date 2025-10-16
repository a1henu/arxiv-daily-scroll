---
layout: default
title: Language as a Label: Zero-Shot Multimodal Classification of Everyday Postures under Data Scarcity
---

# Language as a Label: Zero-Shot Multimodal Classification of Everyday Postures under Data Scarcity
**arXiv**：[2510.13364v1](https://arxiv.org/abs/2510.13364) · [PDF](https://arxiv.org/pdf/2510.13364.pdf)  
**作者**：MingZe Tang, Jubal Chandy Jacob  

**一句话要点**：研究提示设计对零样本多模态分类的影响，发现简单提示在数据稀缺下表现更优。

**关键词**：零样本分类, 视觉语言模型, 提示设计, 数据稀缺, 人体姿态识别

## 3 点简述
- 核心问题：提示设计如何影响视觉相似类别的零样本分类，如坐、站、走/跑。
- 方法要点：使用三层提示设计，评估OpenCLIP、MetaCLIP 2和SigLip等模型。
- 实验或效果：简单提示在MetaCLIP 2和OpenCLIP中准确率最高，详细提示导致性能下降。

## 摘要（原文）

> Recent Vision-Language Models (VLMs) enable zero-shot classification by
> aligning images and text in a shared space, a promising approach for
> data-scarce conditions. However, the influence of prompt design on recognizing
> visually similar categories, such as human postures, is not well understood.
> This study investigates how prompt specificity affects the zero-shot
> classification of sitting, standing, and walking/running on a small, 285-image
> COCO-derived dataset. A suite of modern VLMs, including OpenCLIP, MetaCLIP 2,
> and SigLip, were evaluated using a three-tiered prompt design that
> systematically increases linguistic detail. Our findings reveal a compelling,
> counter-intuitive trend: for the highest-performing models (MetaCLIP 2 and
> OpenCLIP), the simplest, most basic prompts consistently achieve the best
> results. Adding descriptive detail significantly degrades performance for
> instance, MetaCLIP 2's multi-class accuracy drops from 68.8\% to 55.1\% a
> phenomenon we term "prompt overfitting". Conversely, the lower-performing
> SigLip model shows improved classification on ambiguous classes when given more
> descriptive, body-cue-based prompts.

