---
layout: default
title: Word-Anchored Temporal Forgery Localization
---

# Word-Anchored Temporal Forgery Localization
**arXiv**：[2603.06220v1](https://arxiv.org/abs/2603.06220) · [PDF](https://arxiv.org/pdf/2603.06220.pdf)  
**作者**：Tianyi Wang, Xi Shao, Harry Cheng, Yinglong Wang, Mohan Kankanhalli  

**一句话要点**：提出词锚定时序伪造定位方法，通过词级分类解决特征粒度错位与计算成本问题。

**关键词**：时序伪造定位, 词级分类, 特征重对齐, 不对称损失, 伪造检测, 计算效率

## 3 点简述
- 核心问题：现有时序伪造定位方法存在特征粒度错位和高计算成本。
- 方法要点：将任务转为词级二分类，引入特征重对齐模块和不对称损失函数。
- 实验或效果：在数据集内和跨数据集设置下显著优于先进方法，参数少且效率高。

## 摘要（原文）

> Current temporal forgery localization (TFL) approaches typically rely on temporal boundary regression or continuous frame-level anomaly detection paradigms to derive candidate forgery proposals. However, they suffer not only from feature granularity misalignment but also from costly computation. To address these issues, we propose word-anchored temporal forgery localization (WAFL), a novel paradigm that shifts the TFL task from temporal regression and continuous localization to discrete word-level binary classification. Specifically, we first analyze the essence of temporal forgeries and identify the minimum meaningful forgery units, word tokens, and then align data preprocessing with the natural linguistic boundaries of speech. To adapt powerful pre-trained foundation backbones for feature extraction, we introduce the forensic feature realignment (FFR) module, mapping representations from the pre-trained semantic space to a discriminative forensic manifold. This allows subsequent lightweight linear classifiers to efficiently perform binary classification and accomplish the TFL task. Furthermore, to overcome the extreme class imbalance inherent to forgery detection, we design the artifact-centric asymmetric (ACA) loss, which breaks the standard precision-recall trade-off by dynamically suppressing overwhelming authentic gradients while asymmetrically prioritizing subtle forensic artifacts. Extensive experiments demonstrate that WAFL significantly outperforms state-of-the-art approaches in localization performance under both in- and cross-dataset settings, while requiring substantially fewer learnable parameters and operating at high computational efficiency.

