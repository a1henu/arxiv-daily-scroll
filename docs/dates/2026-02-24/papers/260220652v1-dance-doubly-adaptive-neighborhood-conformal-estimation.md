---
layout: default
title: DANCE: Doubly Adaptive Neighborhood Conformal Estimation
---

# DANCE: Doubly Adaptive Neighborhood Conformal Estimation
**arXiv**：[2602.20652v1](https://arxiv.org/abs/2602.20652) · [PDF](https://arxiv.org/pdf/2602.20652.pdf)  
**作者**：Brandon R. Feng, Brian J. Reich, Daniel Beaglehole, Xihaier Luo, David Keetae Park, Shinjae Yoo, Zhechao Huang, Xueyu Mao, Olcay Boz, Jungeum Kim  

**一句话要点**：提出DANCE算法，结合双重自适应非共形分数，提升预训练模型分类任务的不确定性量化效率。

**关键词**：共形预测, 不确定性量化, 深度学习, 分类任务, 嵌入表示, 自适应算法

## 3 点简述
- 核心问题：预训练模型在分类任务中，基于logit分数的共形预测可能导致预测集过大且保守。
- 方法要点：DANCE使用嵌入表示，结合任务自适应核回归和最近邻非共形分数，实现双重局部自适应。
- 实验或效果：在多个数据集上优于现有基线，在预测集大小效率和鲁棒性方面表现优越。

## 摘要（原文）

> The recent developments of complex deep learning models have led to unprecedented ability to accurately predict across multiple data representation types. Conformal prediction for uncertainty quantification of these models has risen in popularity, providing adaptive, statistically-valid prediction sets. For classification tasks, conformal methods have typically focused on utilizing logit scores. For pre-trained models, however, this can result in inefficient, overly conservative set sizes when not calibrated towards the target task. We propose DANCE, a doubly locally adaptive nearest-neighbor based conformal algorithm combining two novel nonconformity scores directly using the data's embedded representation. DANCE first fits a task-adaptive kernel regression model from the embedding layer before using the learned kernel space to produce the final prediction sets for uncertainty quantification. We test against state-of-the-art local, task-adapted and zero-shot conformal baselines, demonstrating DANCE's superior blend of set size efficiency and robustness across various datasets.

