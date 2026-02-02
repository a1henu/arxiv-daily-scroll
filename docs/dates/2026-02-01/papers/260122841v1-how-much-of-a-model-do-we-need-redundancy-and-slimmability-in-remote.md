---
layout: default
title: How Much of a Model Do We Need? Redundancy and Slimmability in Remote Sensing Foundation Models
---

# How Much of a Model Do We Need? Redundancy and Slimmability in Remote Sensing Foundation Models
**arXiv**：[2601.22841v1](https://arxiv.org/abs/2601.22841) · [PDF](https://arxiv.org/pdf/2601.22841.pdf)  
**作者**：Leonard Hackel, Tom Burgert, Begüm Demir  

**一句话要点**：提出后剪枝可瘦身性作为遥感基础模型冗余度诊断与部署策略

**关键词**：遥感基础模型, 模型冗余, 后剪枝, 可瘦身性, 表示分析, 资源受限部署

## 3 点简述
- 核心问题：遥感基础模型在较小规模即进入过参数化，参数增加主要导致冗余而非新抽象
- 方法要点：使用后剪枝均匀缩减预训练编码器宽度，测量六个先进模型在四个分类任务上的表示冗余
- 实验或效果：遥感模型在1%计算量下保持超71%相对准确率，与计算机视觉模型形成七倍差异

## 摘要（原文）

> Large-scale foundation models (FMs) in remote sensing (RS) are developed based on the paradigms established in computer vision (CV) and have shown promise for various Earth observation applications. However, the direct transfer of scaling assumptions from CV to RS has not been adequately examined. We hypothesize that RS FMs enter an overparameterized regime at substantially smaller scales than their CV counterparts, where increasing parameter count primarily induces redundant representations rather than qualitatively new abstractions. To test this hypothesis, we use post-hoc slimming, where we uniformly reduce the width of pretrained encoder, as a tool to measure representational redundancy across six state-of-the-art RS FMs on four downstream classification tasks. Our findings reveal a significant contrast with those in the CV domain: while a post-hoc slimmed masked autoencoder (MAE) trained on ImageNet retains less than 10% accuracy at 1% FLOPs, RS FMs maintain over 71% relative accuracy at the same budget. This sevenfold difference provides strong empirical support for our hypothesis. We further demonstrate that learned slimmable training can improve both Momentum Contrast (MoCo)- and MAE- based models. In addition, through the explained variance ratio and the feature correlation analysis, we provide mechanistic explanations showing that RS FMs distribute task-relevant information with high redundancy. Our findings establish post-hoc slimmability as both a practical deployment strategy for resource-constrained environments and a diagnostic tool that challenges the prevailing scaling paradigm in RS. Upon acceptance, we will publish all code.

