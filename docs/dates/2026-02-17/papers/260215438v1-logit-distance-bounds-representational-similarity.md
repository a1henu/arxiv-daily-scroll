---
layout: default
title: Logit Distance Bounds Representational Similarity
---

# Logit Distance Bounds Representational Similarity
**arXiv**：[2602.15438v1](https://arxiv.org/abs/2602.15438) · [PDF](https://arxiv.org/pdf/2602.15438.pdf)  
**作者**：Beatrix M. B. Nielsen, Emanuele Marconato, Luigi Gresele, Andrea Dittadi, Simon Buchholz  

**一句话要点**：提出基于logit距离的表示相似性保证，以解决KL散度在蒸馏中无法保持线性表示的问题。

**关键词**：表示相似性, logit距离, 模型蒸馏, 线性表示, KL散度, 概念可恢复性

## 3 点简述
- 核心问题：KL散度相近时，模型内部表示可能缺乏线性相似性，影响蒸馏效果。
- 方法要点：定义logit距离，证明其能上界表示差异，确保线性表示相似性。
- 实验或效果：在合成和图像数据集上，logit距离蒸馏提升表示相似性和概念可恢复性。

## 摘要（原文）

> For a broad family of discriminative models that includes autoregressive language models, identifiability results imply that if two models induce the same conditional distributions, then their internal representations agree up to an invertible linear transformation. We ask whether an analogous conclusion holds approximately when the distributions are close instead of equal. Building on the observation of Nielsen et al. (2025) that closeness in KL divergence need not imply high linear representational similarity, we study a distributional distance based on logit differences and show that closeness in this distance does yield linear similarity guarantees. Specifically, we define a representational dissimilarity measure based on the models' identifiability class and prove that it is bounded by the logit distance. We further show that, when model probabilities are bounded away from zero, KL divergence upper-bounds logit distance; yet the resulting bound fails to provide nontrivial control in practice. As a consequence, KL-based distillation can match a teacher's predictions while failing to preserve linear representational properties, such as linear-probe recoverability of human-interpretable concepts. In distillation experiments on synthetic and image datasets, logit-distance distillation yields students with higher linear representational similarity and better preservation of the teacher's linearly recoverable concepts.

