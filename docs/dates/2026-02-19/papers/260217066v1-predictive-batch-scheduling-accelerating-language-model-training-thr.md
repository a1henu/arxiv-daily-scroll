---
layout: default
title: Predictive Batch Scheduling: Accelerating Language Model Training Through Loss-Aware Sample Prioritization
---

# Predictive Batch Scheduling: Accelerating Language Model Training Through Loss-Aware Sample Prioritization
**arXiv**：[2602.17066v1](https://arxiv.org/abs/2602.17066) · [PDF](https://arxiv.org/pdf/2602.17066.pdf)  
**作者**：Sumedh Rasal  

**一句话要点**：提出预测性批次调度以加速语言模型训练，通过动态优先高损失样本构建批次。

**关键词**：语言模型训练, 批次调度, 课程学习, 样本优先级, 损失预测, 计算优化

## 3 点简述
- 核心问题：传统课程学习需预定义难度指标，硬样本挖掘需昂贵逐样本损失跟踪，计算开销大。
- 方法要点：使用轻量级线性预测器在线训练，从静态词元级特征估计样本难度，仅需四个简单特征。
- 实验或效果：在130M参数变压器上，PBS实现评估损失收敛加速6-13%，预测器相关性从0.14提升至0.44。

## 摘要（原文）

> We introduce Predictive Batch Scheduling (PBS), a novel training optimization technique that accelerates language model convergence by dynamically prioritizing high-loss samples during batch construction. Unlike curriculum learning approaches that require predefined difficulty metrics or hard example mining methods that demand expensive per-sample loss tracking, PBS employs a lightweight linear predictor trained online to estimate sample difficulty from static token-level features. Our predictor achieves 0.44 correlation with actual loss using only four simple features: token frequency, sequence length, vocabulary diversity, and rare token ratio. Experiments on a 130M parameter transformer demonstrate that PBS achieves 6-13\% faster convergence measured by evaluation loss across training checkpoints, with the predictor's correlation improving from 0.14 to 0.44 over 10,000 training steps. These results validate that token frequency statistics encode meaningful information about sample difficulty, enabling effective curriculum learning with negligible computational overhead.

