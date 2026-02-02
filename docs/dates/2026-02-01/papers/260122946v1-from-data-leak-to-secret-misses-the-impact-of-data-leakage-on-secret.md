---
layout: default
title: From Data Leak to Secret Misses: The Impact of Data Leakage on Secret Detection Models
---

# From Data Leak to Secret Misses: The Impact of Data Leakage on Secret Detection Models
**arXiv**：[2601.22946v1](https://arxiv.org/abs/2601.22946) · [PDF](https://arxiv.org/pdf/2601.22946.pdf)  
**作者**：Farnaz Soltaniani, Mohammad Ghafari  

**一句话要点**：揭示数据泄露对基于AI的秘密检测模型性能的夸大影响

**关键词**：数据泄露, 秘密检测, 机器学习评估, 基准数据集, 模型泛化

## 3 点简述
- 核心问题：训练与测试集数据重复导致模型记忆而非泛化，误导性能评估
- 方法要点：分析广泛使用的硬编码秘密基准数据集中的重复样本
- 实验或效果：展示数据泄露如何显著提升报告性能，影响真实世界有效性

## 摘要（原文）

> Machine learning models are increasingly used for software security tasks. These models are commonly trained and evaluated on large Internet-derived datasets, which often contain duplicated or highly similar samples. When such samples are split across training and test sets, data leakage may occur, allowing models to memorize patterns instead of learning to generalize. We investigate duplication in a widely used benchmark dataset of hard coded secrets and show how data leakage can substantially inflate the reported performance of AI-based secret detectors, resulting in a misleading picture of their real-world effectiveness.

