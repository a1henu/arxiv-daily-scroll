---
layout: default
title: OxEnsemble: Fair Ensembles for Low-Data Classification
---

# OxEnsemble: Fair Ensembles for Low-Data Classification
**arXiv**：[2512.09665v1](https://arxiv.org/abs/2512.09665) · [PDF](https://arxiv.org/pdf/2512.09665.pdf)  
**作者**：Jonathan Rystrøm, Zihao Fu, Chris Russell  

**一句话要点**：提出OxEnsemble方法，解决数据稀缺且不平衡场景下的公平分类问题

**关键词**：公平分类, 低数据学习, 集成学习, 医疗影像, 群体不平衡

## 3 点简述
- 核心问题：医疗影像等低数据场景中，数据稀缺且群体不平衡，假阴性可能致命
- 方法要点：通过集成多个满足公平约束的模型，高效聚合预测，兼顾数据与计算效率
- 实验效果：在多个医疗影像数据集上，比现有方法获得更一致的公平-准确性权衡

## 摘要（原文）

> We address the problem of fair classification in settings where data is scarce and unbalanced across demographic groups. Such low-data regimes are common in domains like medical imaging, where false negatives can have fatal consequences.
>   We propose a novel approach \emph{OxEnsemble} for efficiently training ensembles and enforcing fairness in these low-data regimes. Unlike other approaches, we aggregate predictions across ensemble members, each trained to satisfy fairness constraints. By construction, \emph{OxEnsemble} is both data-efficient, carefully reusing held-out data to enforce fairness reliably, and compute-efficient, requiring little more compute than used to fine-tune or evaluate an existing model. We validate this approach with new theoretical guarantees. Experimentally, our approach yields more consistent outcomes and stronger fairness-accuracy trade-offs than existing methods across multiple challenging medical imaging classification datasets.

