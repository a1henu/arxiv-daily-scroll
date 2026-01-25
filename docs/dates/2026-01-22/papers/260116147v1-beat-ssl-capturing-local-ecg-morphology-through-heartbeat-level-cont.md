---
layout: default
title: Beat-ssl: Capturing Local ECG Morphology through Heartbeat-level Contrastive Learning with Soft Targets
---

# Beat-ssl: Capturing Local ECG Morphology through Heartbeat-level Contrastive Learning with Soft Targets
**arXiv**：[2601.16147v1](https://arxiv.org/abs/2601.16147) · [PDF](https://arxiv.org/pdf/2601.16147.pdf)  
**作者**：Muhammad Ilham Rizqyawan, Peter Macfarlane, Stathis Hadjidemetriou, Fani Deligianni  

**一句话要点**：提出Beat-SSL，通过心跳级对比学习与软目标捕获ECG局部形态，以解决标注数据稀缺问题。

**关键词**：心电图分析, 对比学习, 软目标, 双上下文学习, 迁移学习

## 3 点简述
- 核心问题：ECG标注数据获取困难，现有对比学习框架未充分利用ECG特性或依赖硬目标。
- 方法要点：采用双上下文学习，结合节律级和心跳级对比，并引入软目标以捕捉特征相似性。
- 实验或效果：在节律分类任务中达到基础模型93%性能，分割任务超越其他方法4%。

## 摘要（原文）

> Obtaining labelled ECG data for developing supervised models is challenging. Contrastive learning (CL) has emerged as a promising pretraining approach that enables effective transfer learning with limited labelled data. However, existing CL frameworks either focus solely on global context or fail to exploit ECG-specific characteristics. Furthermore, these methods rely on hard contrastive targets, which may not adequately capture the continuous nature of feature similarity in ECG signals. In this paper, we propose Beat-SSL, a contrastive learning framework that performs dual-context learning through both rhythm-level and heartbeat-level contrasting with soft targets. We evaluated our pretrained model on two downstream tasks: 1) multilabel classification for global rhythm assessment, and 2) ECG segmentation to assess its capacity to learn representations across both contexts. We conducted an ablation study and compared the best configuration with three other methods, including one ECG foundation model. Despite the foundation model's broader pretraining, Beat-SSL reached 93% of its performance in multilabel classification task and surpassed all other methods in the segmentation task by 4%.

