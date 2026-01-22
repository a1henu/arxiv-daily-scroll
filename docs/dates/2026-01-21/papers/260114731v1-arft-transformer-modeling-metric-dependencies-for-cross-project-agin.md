---
layout: default
title: ARFT-Transformer: Modeling Metric Dependencies for Cross-Project Aging-Related Bug Prediction
---

# ARFT-Transformer: Modeling Metric Dependencies for Cross-Project Aging-Related Bug Prediction
**arXiv**：[2601.14731v1](https://arxiv.org/abs/2601.14731) · [PDF](https://arxiv.org/pdf/2601.14731.pdf)  
**作者**：Shuning Ge, Fangyun Qin, Xiaohui Wan, Yang Liu, Qian Dai, Zheng Zheng  

**一句话要点**：提出ARFT-Transformer以解决跨项目老化相关缺陷预测中的度量依赖和类别不平衡问题

**关键词**：跨项目缺陷预测, 老化相关缺陷, Transformer模型, 度量依赖建模, 类别不平衡处理, 软件老化

## 3 点简述
- 核心问题：跨项目老化相关缺陷预测面临度量独立处理导致信息重叠和类别不平衡的挑战
- 方法要点：引入度量级多头注意力机制捕获度量交互，并采用Focal Loss函数处理类别不平衡
- 实验或效果：在三个开源项目上验证，在单源和多源情况下平均优于现有方法，平衡指标提升最高达29.54%和19.92%

## 摘要（原文）

> Software systems that run for long periods often suffer from software aging, which is typically caused by Aging-Related Bugs (ARBs). To mitigate the risk of ARBs early in the development phase, ARB prediction has been introduced into software aging research. However, due to the difficulty of collecting ARBs, within-project ARB prediction faces the challenge of data scarcity, leading to the proposal of cross-project ARB prediction. This task faces two major challenges: 1) domain adaptation issue caused by distribution difference between source and target projects; and 2) severe class imbalance between ARB-prone and ARB-free samples. Although various methods have been proposed for cross-project ARB prediction, existing approaches treat the input metrics independently and often neglect the rich inter-metric dependencies, which can lead to overlapping information and misjudgment of metric importance, potentially affecting the model's performance. Moreover, they typically use cross-entropy as the loss function during training, which cannot distinguish the difficulty of sample classification. To overcome these limitations, we propose ARFT-Transformer, a transformer-based cross-project ARB prediction framework that introduces a metric-level multi-head attention mechanism to capture metric interactions and incorporates Focal Loss function to effectively handle class imbalance. Experiments conducted on three large-scale open-source projects demonstrate that ARFT-Transformer on average outperforms state-of-the-art cross-project ARB prediction methods in both single-source and multi-source cases, achieving up to a 29.54% and 19.92% improvement in Balance metric.

