---
layout: default
title: Specific Emitter Identification via Active Learning
---

# Specific Emitter Identification via Active Learning
**arXiv**：[2601.04502v1](https://arxiv.org/abs/2601.04502) · [PDF](https://arxiv.org/pdf/2601.04502.pdf)  
**作者**：Jingyi Wang, Fanggang Wang  

**一句话要点**：提出基于主动学习的特定辐射源识别方法，以解决无线通信中标注数据稀缺问题。

**关键词**：特定辐射源识别, 主动学习, 半监督学习, 对比学习, 无线通信安全

## 3 点简述
- 核心问题：特定辐射源识别依赖大规模标注数据，获取成本高且耗时。
- 方法要点：采用三阶段半监督训练，结合自监督对比学习、联合损失优化和主动学习样本选择。
- 实验或效果：在ADS-B和WiFi数据集上，有限标注下显著优于传统方法，提高识别精度并降低标注成本。

## 摘要（原文）

> With the rapid growth of wireless communications, specific emitter identification (SEI) is significant for communication security. However, its model training relies heavily on the large-scale labeled data, which are costly and time-consuming to obtain. To address this challenge, we propose an SEI approach enhanced by active learning (AL), which follows a three-stage semi-supervised training scheme. In the first stage, self-supervised contrastive learning is employed with a dynamic dictionary update mechanism to extract robust representations from large amounts of the unlabeled data. In the second stage, supervised training on a small labeled dataset is performed, where the contrastive and cross-entropy losses are jointly optimized to improve the feature separability and strengthen the classification boundaries. In the third stage, an AL module selects the most valuable samples from the unlabeled data for annotation based on the uncertainty and representativeness criteria, further enhancing generalization under limited labeling budgets. Experimental results on the ADS-B and WiFi datasets demonstrate that the proposed SEI approach significantly outperforms the conventional supervised and semi-supervised methods under limited annotation conditions, achieving higher recognition accuracy with lower labeling cost.

