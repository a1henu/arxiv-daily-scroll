---
layout: default
title: Degradation-based augmented training for robust individual animal re-identification
---

# Degradation-based augmented training for robust individual animal re-identification
**arXiv**：[2603.04163v1](https://arxiv.org/abs/2603.04163) · [PDF](https://arxiv.org/pdf/2603.04163.pdf)  
**作者**：Thanos Polychronou, Lukáš Adam, Viktor Penchev, Kostas Papafitsoros  

**一句话要点**：提出基于退化的增强训练框架，提升野生动物个体重识别在图像退化下的鲁棒性

**关键词**：野生动物重识别, 图像退化, 增强训练, 深度度量学习, 鲁棒性提升

## 3 点简述
- 核心问题：图像退化因素降低野生动物个体重识别性能，影响生态研究。
- 方法要点：在训练中应用人工多样化退化，增强深度特征提取器的鲁棒性。
- 实验或效果：在真实退化图像数据集上，Rank-1准确率提升高达8.5%。

## 摘要（原文）

> Wildlife re-identification aims to recognise individual animals by matching query images to a database of previously identified individuals, based on their fine-scale unique morphological characteristics. Current state-of-the-art models for multispecies re- identification are based on deep metric learning representing individual identities by fea- ture vectors in an embedding space, the similarity of which forms the basis for a fast automated identity retrieval. Yet very often, the discriminative information of individual wild animals gets significantly reduced due to the presence of several degradation factors in images, leading to reduced retrieval performance and limiting the downstream eco- logical studies. Here, starting by showing that the extent of this performance reduction greatly varies depending on the animal species (18 wild animal datasets), we introduce an augmented training framework for deep feature extractors, where we apply artificial but diverse degradations in images in the training set. We show that applying this augmented training only to a subset of individuals, leads to an overall increased re-identification performance, under the same type of degradations, even for individuals not seen during training. The introduction of diverse degradations during training leads to a gain of up to 8.5% Rank-1 accuracy to a dataset of real-world degraded animal images, selected using human re-ID expert annotations provided here for the first time. Our work is the first to systematically study image degradation in wildlife re-identification, while introducing all the necessary benchmarks, publicly available code and data, enabling further research on this topic.

