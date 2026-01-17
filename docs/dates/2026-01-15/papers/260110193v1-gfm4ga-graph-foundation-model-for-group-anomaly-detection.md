---
layout: default
title: GFM4GA: Graph Foundation Model for Group Anomaly Detection
---

# GFM4GA: Graph Foundation Model for Group Anomaly Detection
**arXiv**：[2601.10193v1](https://arxiv.org/abs/2601.10193) · [PDF](https://arxiv.org/pdf/2601.10193.pdf)  
**作者**：Jiujiu Chen, Weijun Zeng, Shaofeng Hu, Sihong Xie, Hui Xiong  

**一句话要点**：提出GFM4GA图基础模型以解决网络应用中群体异常检测的挑战

**关键词**：群体异常检测, 图基础模型, 对比学习, 少样本学习, 网络应用

## 3 点简述
- 核心问题：群体异常检测面临模式多样且个体在异常群体中可能表现正常，现有图基础模型无法泛化。
- 方法要点：通过基于特征估计和群体提取的双层对比学习预训练，捕获潜在群体异常结构和特征不一致性。
- 实验或效果：在参数约束和群体异常比例加权的少样本设置下微调，实验显示AUROC和AUPRC平均提升2.85%和2.55%。

## 摘要（原文）

> Group anomaly detection is crucial in many network applications, but faces challenges due to diverse anomaly patterns. Motivated by the success of large language models (LLMs) in natural language processing, graph foundation models (GFMs) is proposed to handle few-shot learning task with fewer labeling efforts. GFMs have been successfully applied to detection of individual anomalies but cannot be generalized to group anomalies, as group anomaly patterns must be detected as a whole and individuals in an abnormal group can look rather normal. Therefore, we propose GFM4GA, a novel graph foundation model for group anomaly detection. The pipeline is pretrained via dual-level contrastive learning based on feature-based estimation and group extraction, to capture potential group anomaly structure and feature inconsistencies. In the downstream tasks, the pipeline is finetuned in parameter-constrained and group-anomaly-proportion weighted few-shot settings, and its adaptive ability to unseen group anomalies expanded via group contexts determined by labeled anomaly neighbors. Experiments show that GFM4GA surpasses group anomaly detectors and GFMs for individual anomalies, achieving average improvements of 2.85% in AUROC and 2.55% in AUPRC.

