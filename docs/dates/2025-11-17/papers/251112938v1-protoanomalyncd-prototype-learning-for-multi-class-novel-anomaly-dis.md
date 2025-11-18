---
layout: default
title: ProtoAnomalyNCD: Prototype Learning for Multi-class Novel Anomaly Discovery in Industrial Scenarios
---

# ProtoAnomalyNCD: Prototype Learning for Multi-class Novel Anomaly Discovery in Industrial Scenarios
**arXiv**：[2511.12938v1](https://arxiv.org/abs/2511.12938) · [PDF](https://arxiv.org/pdf/2511.12938.pdf)  
**作者**：Botong Zhao, Qijun Shi, Shujing Lyu, Yue Lu  

**一句话要点**：提出ProtoAnomalyNCD以解决工业场景中多类未知异常发现与分类问题

**关键词**：工业异常检测, 原型学习, 多类异常发现, 注意力机制, 异常图引导, 未知异常分类

## 3 点简述
- 核心问题：现有方法仅检测异常存在，无法发现和分类多类未知异常类型。
- 方法要点：结合Grounded SAM定位对象区域，并设计异常图引导注意力模块增强特征。
- 实验或效果：在MVTec AD等数据集上优于现有方法，实现任务级统一。

## 摘要（原文）

> Existing industrial anomaly detection methods mainly determine whether an anomaly is present. However, real-world applications also require discovering and classifying multiple anomaly types. Since industrial anomalies are semantically subtle and current methods do not sufficiently exploit image priors, direct clustering approaches often perform poorly. To address these challenges, we propose ProtoAnomalyNCD, a prototype-learning-based framework for discovering unseen anomaly classes of multiple types that can be integrated with various anomaly detection methods. First, to suppress background clutter, we leverage Grounded SAM with text prompts to localize object regions as priors for the anomaly classification network. Next, because anomalies usually appear as subtle and fine-grained patterns on the product, we introduce an Anomaly-Map-Guided Attention block. Within this block, we design a Region Guidance Factor that helps the attention module distinguish among background, object regions, and anomalous regions. By using both localized product regions and anomaly maps as priors, the module enhances anomalous features while suppressing background noise and preserving normal features for contrastive learning. Finally, under a unified prototype-learning framework, ProtoAnomalyNCD discovers and clusters unseen anomaly classes while simultaneously enabling multi-type anomaly classification. We further extend our method to detect unseen outliers, achieving task-level unification. Our method outperforms state-of-the-art approaches on the MVTec AD, MTD, and Real-IAD datasets.

