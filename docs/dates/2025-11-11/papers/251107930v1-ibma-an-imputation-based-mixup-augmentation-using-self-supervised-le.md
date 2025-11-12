---
layout: default
title: IBMA: An Imputation-Based Mixup Augmentation Using Self-Supervised Learning for Time Series Data
---

# IBMA: An Imputation-Based Mixup Augmentation Using Self-Supervised Learning for Time Series Data
**arXiv**：[2511.07930v1](https://arxiv.org/abs/2511.07930) · [PDF](https://arxiv.org/pdf/2511.07930.pdf)  
**作者**：Dang Nha Nguyen, Hai Dang Nguyen, Khoa Tho Anh Nguyen  

**一句话要点**：提出基于插值的混合增强方法，用于提升时间序列预测性能。

**关键词**：时间序列预测, 数据增强, 混合增强, 插值方法, 自监督学习

## 3 点简述
- 时间序列数据增强策略较少，混合增强等先进技术应用不足。
- 结合插值增强与混合增强，提高模型泛化能力。
- 在多个数据集和模型上测试，IBMA在24个实例中22次提升性能。

## 摘要（原文）

> Data augmentation in time series forecasting plays a crucial role in enhancing model performance by introducing variability while maintaining the underlying temporal patterns. However, time series data offers fewer augmentation strategies compared to fields such as image or text, with advanced techniques like Mixup rarely being used. In this work, we propose a novel approach, Imputation-Based Mixup Augmentation (IBMA), which combines Imputation-Augmented data with Mixup augmentation to bolster model generalization and improve forecasting performance. We evaluate the effectiveness of this method across several forecasting models, including DLinear (MLP), TimesNet (CNN), and iTrainformer (Transformer), these models represent some of the most recent advances in time series forecasting. Our experiments, conducted on four datasets (ETTh1, ETTh2, ETTm1, ETTm2) and compared against eight other augmentation techniques, demonstrate that IBMA consistently enhances performance, achieving 22 improvements out of 24 instances, with 10 of those being the best performances, particularly with iTrainformer imputation.

