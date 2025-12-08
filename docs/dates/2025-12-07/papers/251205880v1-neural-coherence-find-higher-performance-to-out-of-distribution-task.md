---
layout: default
title: Neural Coherence : Find higher performance to out-of-distribution tasks from few samples
---

# Neural Coherence : Find higher performance to out-of-distribution tasks from few samples
**arXiv**：[2512.05880v1](https://arxiv.org/abs/2512.05880) · [PDF](https://arxiv.org/pdf/2512.05880.pdf)  
**作者**：Simon Guiroy, Mats Richter, Sarath Chandar, Christopher Pal  

**一句话要点**：提出神经一致性方法，以少量无标注样本解决分布外任务中的模型选择问题

**关键词**：模型选择, 分布外泛化, 神经一致性, 无标注学习, 数据高效学习

## 3 点简述
- 核心问题：在数据稀缺、无标注且分布外的任务中，如何从大规模预训练中选择最佳模型检查点
- 方法要点：基于神经一致性，通过分析源域和目标域的激活统计特征，实现高效数据利用的模型选择
- 实验或效果：在ImageNet1K预训练模型上，于Food-101等目标域和元学习设置中显著提升泛化性能

## 摘要（原文）

> To create state-of-the-art models for many downstream tasks, it has become common practice to fine-tune a pre-trained large vision model. However, it remains an open question of how to best determine which of the many possible model checkpoints resulting from a large training run to use as the starting point. This becomes especially important when data for the target task of interest is scarce, unlabeled and out-of-distribution. In such scenarios, common methods relying on in-distribution validation data become unreliable or inapplicable. This work proposes a novel approach for model selection that operates reliably on just a few unlabeled examples from the target task. Our approach is based on a novel concept: Neural Coherence, which entails characterizing a model's activation statistics for source and target domains, allowing one to define model selection methods with high data-efficiency. We provide experiments where models are pre-trained on ImageNet1K and examine target domains consisting of Food-101, PlantNet-300K and iNaturalist. We also evaluate it in many meta-learning settings. Our approach significantly improves generalization across these different target domains compared to established baselines. We further demonstrate the versatility of Neural Coherence as a powerful principle by showing its effectiveness in training data selection.

