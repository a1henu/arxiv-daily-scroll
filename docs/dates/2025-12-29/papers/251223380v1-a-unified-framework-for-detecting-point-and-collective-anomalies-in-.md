---
layout: default
title: A unified framework for detecting point and collective anomalies in operating system logs via collaborative transformers
---

# A unified framework for detecting point and collective anomalies in operating system logs via collaborative transformers
**arXiv**：[2512.23380v1](https://arxiv.org/abs/2512.23380) · [PDF](https://arxiv.org/pdf/2512.23380.pdf)  
**作者**：Mohammad Nasirzadeh, Jafar Tahmoresnezhad, Parviz Rashidi-Khazaee  

**一句话要点**：提出CoLog框架，通过协作Transformer检测操作系统日志中的点异常和集体异常。

**关键词**：日志异常检测, 多模态学习, 协作Transformer, 操作系统安全, 点异常检测, 集体异常检测

## 3 点简述
- 核心问题：单模态方法忽略日志多模态性，多模态方法未处理模态间交互。
- 方法要点：利用协作Transformer和多头注意力学习模态交互，结合模态适应层处理异质性。
- 实验或效果：在七个基准数据集上平均精确率99.63%，召回率99.59%，F1分数99.61%。

## 摘要（原文）

> Log anomaly detection is crucial for preserving the security of operating systems. Depending on the source of log data collection, various information is recorded in logs that can be considered log modalities. In light of this intuition, unimodal methods often struggle by ignoring the different modalities of log data. Meanwhile, multimodal methods fail to handle the interactions between these modalities. Applying multimodal sentiment analysis to log anomaly detection, we propose CoLog, a framework that collaboratively encodes logs utilizing various modalities. CoLog utilizes collaborative transformers and multi-head impressed attention to learn interactions among several modalities, ensuring comprehensive anomaly detection. To handle the heterogeneity caused by these interactions, CoLog incorporates a modality adaptation layer, which adapts the representations from different log modalities. This methodology enables CoLog to learn nuanced patterns and dependencies within the data, enhancing its anomaly detection capabilities. Extensive experiments demonstrate CoLog's superiority over existing state-of-the-art methods. Furthermore, in detecting both point and collective anomalies, CoLog achieves a mean precision of 99.63%, a mean recall of 99.59%, and a mean F1 score of 99.61% across seven benchmark datasets for log-based anomaly detection. The comprehensive detection capabilities of CoLog make it highly suitable for cybersecurity, system monitoring, and operational efficiency. CoLog represents a significant advancement in log anomaly detection, providing a sophisticated and effective solution to point and collective anomaly detection through a unified framework and a solution to the complex challenges automatic log data analysis poses. We also provide the implementation of CoLog at https://github.com/NasirzadehMoh/CoLog.

