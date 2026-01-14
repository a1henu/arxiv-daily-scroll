---
layout: default
title: MLPlatt: Simple Calibration Framework for Ranking Models
---

# MLPlatt: Simple Calibration Framework for Ranking Models
**arXiv**：[2601.08345v1](https://arxiv.org/abs/2601.08345) · [PDF](https://arxiv.org/pdf/2601.08345.pdf)  
**作者**：Piotr Bajger, Roman Dusek, Krzysztof Galias, Paweł Młyniec, Aleksander Wawer, Paweł Zawistowski  

**一句话要点**：提出MLPlatt方法以解决排序模型的后验校准问题，保持排序质量并输出可解释点击率概率。

**关键词**：排序模型校准, 后验校准, 点击率预测, 上下文感知, 电子商务应用

## 3 点简述
- 排序模型常因使用典型排序损失函数而缺乏可解释性和尺度校准，影响下游任务应用。
- MLPlatt是一种简单有效的后验校准方法，设计为上下文感知，能保持项目排序并转换为点击率概率。
- 在两个数据集上验证，MLPlatt在F-ECE指标上优于现有方法超10%，且不损害排序质量。

## 摘要（原文）

> Ranking models are extensively used in e-commerce for relevance estimation. These models often suffer from poor interpretability and no scale calibration, particularly when trained with typical ranking loss functions. This paper addresses the problem of post-hoc calibration of ranking models. We introduce MLPlatt: a simple yet effective ranking model calibration method that preserves the item ordering and converts ranker outputs to interpretable click-through rate (CTR) probabilities usable in downstream tasks. The method is context-aware by design and achieves good calibration metrics globally, and within strata corresponding to different values of a selected categorical field (such as user country or device), which is often important from a business perspective of an E-commerce platform. We demonstrate the superiority of MLPlatt over existing approaches on two datasets, achieving an improvement of over 10\% in F-ECE (Field Expected Calibration Error) compared to other methods. Most importantly, we show that high-quality calibration can be achieved without compromising the ranking quality.

