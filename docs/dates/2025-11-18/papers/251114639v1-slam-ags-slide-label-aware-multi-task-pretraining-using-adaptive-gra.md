---
layout: default
title: SLAM-AGS: Slide-Label Aware Multi-Task Pretraining Using Adaptive Gradient Surgery in Computational Cytology
---

# SLAM-AGS: Slide-Label Aware Multi-Task Pretraining Using Adaptive Gradient Surgery in Computational Cytology
**arXiv**：[2511.14639v1](https://arxiv.org/abs/2511.14639) · [PDF](https://arxiv.org/pdf/2511.14639.pdf)  
**作者**：Marco Acerbis, Swarnadip Chatterjee, Christophe Avenel, Joakim Lindblad  

**一句话要点**：提出SLAM-AGS多任务预训练框架，解决计算细胞学中标签不可靠和见证率低的问题。

**关键词**：计算细胞学, 多任务学习, 自适应梯度手术, 弱监督学习, 自监督学习, 袋级预测

## 3 点简述
- 核心问题：实例级标签不可靠且成本高，见证率极低。
- 方法要点：联合优化弱监督相似性和自监督对比目标，应用自适应梯度手术。
- 实验或效果：在低见证率下提升袋级F1分数和阳性细胞检索性能。

## 摘要（原文）

> Computational cytology faces two major challenges: i) instance-level labels are unreliable and prohibitively costly to obtain, ii) witness rates are extremely low. We propose SLAM-AGS, a Slide-Label-Aware Multitask pretraining framework that jointly optimizes (i) a weakly supervised similarity objective on slide-negative patches and (ii) a self-supervised contrastive objective on slide-positive patches, yielding stronger performance on downstream tasks. To stabilize learning, we apply Adaptive Gradient Surgery to tackle conflicting task gradients and prevent model collapse. We integrate the pretrained encoder into an attention-based Multiple Instance Learning aggregator for bag-level prediction and attention-guided retrieval of the most abnormal instances in a bag. On a publicly available bone-marrow cytology dataset, with simulated witness rates from 10% down to 0.5%, SLAM-AGS improves bag-level F1-Score and Top 400 positive cell retrieval over other pretraining methods, with the largest gains at low witness rates, showing that resolving gradient interference enables stable pretraining and better performance on downstream tasks. To facilitate reproducibility, we share our complete implementation and evaluation framework as open source: https://github.com/Ace95/SLAM-AGS.

