---
layout: default
title: Semi-Supervised Few-Shot Adaptation of Vision-Language Models
---

# Semi-Supervised Few-Shot Adaptation of Vision-Language Models
**arXiv**：[2603.02959v1](https://arxiv.org/abs/2603.02959) · [PDF](https://arxiv.org/pdf/2603.02959.pdf)  
**作者**：Julio Silva-Rodríguez, Ender Konukoglu  

**一句话要点**：提出半监督少样本适应方法，利用未标注数据提升医学视觉语言模型在低样本场景下的性能。

**关键词**：视觉语言模型, 少样本适应, 半监督学习, 医学图像分类, 伪标签传播

## 3 点简述
- 核心问题：医学图像分类中，少样本适应因类别不平衡导致性能下降，标注成本高。
- 方法要点：引入半监督求解器，在少样本适应过程中传播文本引导的伪标签，利用未标注数据。
- 实验或效果：在低样本场景下，减少标注工作量超过50%，实现更经济的标注流程。

## 摘要（原文）

> Vision-language models (VLMs) pre-trained on large, heterogeneous data sources are becoming increasingly popular, providing rich multi-modal embeddings that enable efficient transfer to new tasks. A particularly relevant application is few-shot adaptation, where only a handful of annotated examples are available to adapt the model through multi-modal linear probes. In medical imaging, specialized VLMs have shown promising performance in zero- and few-shot image classification, which is valuable for mitigating the high cost of expert annotations. However, challenges remain in extremely low-shot regimes: the inherent class imbalances in medical tasks often lead to underrepresented categories, penalizing overall model performance. To address this limitation, we propose leveraging unlabeled data by introducing an efficient semi-supervised solver that propagates text-informed pseudo-labels during few-shot adaptation. The proposed method enables lower-budget annotation pipelines for adapting VLMs, reducing labeling effort by >50% in low-shot regimes.

