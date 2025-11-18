---
layout: default
title: MGCA-Net: Multi-Grained Category-Aware Network for Open-Vocabulary Temporal Action Localization
---

# MGCA-Net: Multi-Grained Category-Aware Network for Open-Vocabulary Temporal Action Localization
**arXiv**：[2511.13039v1](https://arxiv.org/abs/2511.13039) · [PDF](https://arxiv.org/pdf/2511.13039.pdf)  
**作者**：Zhenying Fang, Richang Hong  

**一句话要点**：提出多粒度类别感知网络以解决开放词汇时序动作定位中单粒度识别精度低的问题

**关键词**：开放词汇时序动作定位, 多粒度类别感知, 动作识别, 视频理解, 零样本学习

## 3 点简述
- 核心问题：现有方法在单粒度识别动作类别，导致基础和新增类别识别精度下降
- 方法要点：结合定位器、动作存在预测器、常规分类器和粗到细分类器实现多粒度类别感知
- 实验或效果：在THUMOS'14和ActivityNet-1.3基准上达到最先进性能，零样本设置表现优异

## 摘要（原文）

> Open-Vocabulary Temporal Action Localization (OV-TAL) aims to recognize and localize instances of any desired action categories in videos without explicitly curating training data for all categories. Existing methods mostly recognize action categories at a single granularity, which degrades the recognition accuracy of both base and novel action categories. To address these issues, we propose a Multi-Grained Category-Aware Network (MGCA-Net) comprising a localizer, an action presence predictor, a conventional classifier, and a coarse-to-fine classifier. Specifically, the localizer localizes category-agnostic action proposals. For these action proposals, the action presence predictor estimates the probability that they belong to an action instance. At the same time, the conventional classifier predicts the probability of each action proposal over base action categories at the snippet granularity. Novel action categories are recognized by the coarse-to-fine classifier, which first identifies action presence at the video granularity. Finally, it assigns each action proposal to one category from the coarse categories at the proposal granularity. Through coarse-to-fine category awareness for novel actions and the conventional classifier's awareness of base actions, multi-grained category awareness is achieved, effectively enhancing localization performance. Comprehensive evaluations on the THUMOS'14 and ActivityNet-1.3 benchmarks demonstrate that our method achieves state-of-the-art performance. Furthermore, our MGCA-Net achieves state-of-the-art results under the Zero-Shot Temporal Action Localization setting.

