---
layout: default
title: Early Warning of Intraoperative Adverse Events via Transformer-Driven Multi-Label Learning
---

# Early Warning of Intraoperative Adverse Events via Transformer-Driven Multi-Label Learning
**arXiv**：[2603.05212v1](https://arxiv.org/abs/2603.05212) · [PDF](https://arxiv.org/pdf/2603.05212.pdf)  
**作者**：Xueyao Wang, Xiuding Cai, Honglin Shang, Yaoyao Zhu, Yu Yao  

**一句话要点**：提出IAENet框架，通过Transformer多标签学习预测术中不良事件，提升早期预警性能。

**关键词**：术中不良事件预测, 多标签学习, Transformer模型, 时间序列分析, 类别不平衡处理

## 3 点简述
- 核心问题：术中不良事件预测存在事件依赖忽略、异构数据利用不足和类别不平衡挑战。
- 方法要点：结合TAFiLM模块融合静态与动态数据，并引入LCRLoss正则化处理事件共现与不平衡。
- 实验或效果：在5、10、15分钟预警任务中，平均F1分数分别提升5.05%、2.82%和7.57%。

## 摘要（原文）

> Early warning of intraoperative adverse events plays a vital role in reducing surgical risk and improving patient safety. While deep learning has shown promise in predicting the single adverse event, several key challenges remain: overlooking adverse event dependencies, underutilizing heterogeneous clinical data, and suffering from the class imbalance inherent in medical datasets. To address these issues, we construct the first Multi-label Adverse Events dataset (MuAE) for intraoperative adverse events prediction, covering six critical events. Next, we propose a novel Transformerbased multi-label learning framework (IAENet) that combines an improved Time-Aware Feature-wise Linear Modulation (TAFiLM) module for static covariates and dynamic variables robust fusion and complex temporal dependencies modeling. Furthermore, we introduce a Label-Constrained Reweighting Loss (LCRLoss) with co-occurrence regularization to effectively mitigate intra-event imbalance and enforce structured consistency among frequently co-occurring events. Extensive experiments demonstrate that IAENet consistently outperforms strong baselines on 5, 10, and 15-minute early warning tasks, achieving improvements of +5.05%, +2.82%, and +7.57% on average F1 score. These results highlight the potential of IAENet for supporting intelligent intraoperative decision-making in clinical practice.

