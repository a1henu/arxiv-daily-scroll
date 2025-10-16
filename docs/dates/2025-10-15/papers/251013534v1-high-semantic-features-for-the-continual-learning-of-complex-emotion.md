---
layout: default
title: High Semantic Features for the Continual Learning of Complex Emotions: a Lightweight Solution
---

# High Semantic Features for the Continual Learning of Complex Emotions: a Lightweight Solution
**arXiv**：[2510.13534v1](https://arxiv.org/abs/2510.13534) · [PDF](https://arxiv.org/pdf/2510.13534.pdf)  
**作者**：Thibault Geoffroy, gauthier Gerspacher, Lionel Prevost  

**一句话要点**：提出基于动作单元的高语义特征方法，以轻量模型解决复杂情感识别的持续学习问题。

**关键词**：持续学习, 情感识别, 动作单元, 轻量模型, 特征提取

## 3 点简述
- 核心问题：持续学习中旧任务易被遗忘，源于任务间特征不匹配。
- 方法要点：使用动作单元作为非瞬态高语义特征，优于浅层和深度卷积网络。
- 实验或效果：在CFEE数据集上，增量学习复杂情感准确率达0.75，模型轻量。

## 摘要（原文）

> Incremental learning is a complex process due to potential catastrophic
> forgetting of old tasks when learning new ones. This is mainly due to transient
> features that do not fit from task to task. In this paper, we focus on complex
> emotion recognition. First, we learn basic emotions and then, incrementally,
> like humans, complex emotions. We show that Action Units, describing facial
> muscle movements, are non-transient, highly semantical features that outperform
> those extracted by both shallow and deep convolutional neural networks. Thanks
> to this ability, our approach achieves interesting results when learning
> incrementally complex, compound emotions with an accuracy of 0.75 on the CFEE
> dataset and can be favorably compared to state-of-the-art results. Moreover, it
> results in a lightweight model with a small memory footprint.

