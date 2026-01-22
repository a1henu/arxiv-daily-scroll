---
layout: default
title: READ-Net: Clarifying Emotional Ambiguity via Adaptive Feature Recalibration for Audio-Visual Depression Detection
---

# READ-Net: Clarifying Emotional Ambiguity via Adaptive Feature Recalibration for Audio-Visual Depression Detection
**arXiv**：[2601.14651v1](https://arxiv.org/abs/2601.14651) · [PDF](https://arxiv.org/pdf/2601.14651.pdf)  
**作者**：Chenglizhao Chen, Boze Li, Mengke Song, Dehao Feng, Xinyu Liu, Shanchen Pang, Jufeng Yang, Hui Yu  

**一句话要点**：提出READ-Net通过自适应特征重校准解决视听抑郁检测中的情感模糊问题

**关键词**：视听抑郁检测, 情感模糊, 自适应特征重校准, 特征表示, 心理健康分析

## 3 点简述
- 核心问题：情感模糊导致抑郁信号与瞬时情感表达混淆，影响检测准确性。
- 方法要点：自适应特征重校准动态调整情感特征权重，增强抑郁相关信号并过滤情感噪声。
- 实验或效果：在三个公开数据集上优于现有方法，平均准确率提升4.55%，F1分数提升1.26%。

## 摘要（原文）

> Depression is a severe global mental health issue that impairs daily functioning and overall quality of life. Although recent audio-visual approaches have improved automatic depression detection, methods that ignore emotional cues often fail to capture subtle depressive signals hidden within emotional expressions. Conversely, those incorporating emotions frequently confuse transient emotional expressions with stable depressive symptoms in feature representations, a phenomenon termed \emph{Emotional Ambiguity}, thereby leading to detection errors. To address this critical issue, we propose READ-Net, the first audio-visual depression detection framework explicitly designed to resolve Emotional Ambiguity through Adaptive Feature Recalibration (AFR). The core insight of AFR is to dynamically adjust the weights of emotional features to enhance depression-related signals. Rather than merely overlooking or naively combining emotional information, READ-Net innovatively identifies and preserves depressive-relevant cues within emotional features, while adaptively filtering out irrelevant emotional noise. This recalibration strategy significantly clarifies feature representations, and effectively mitigates the persistent challenge of emotional interference. Additionally, READ-Net can be easily integrated into existing frameworks for improved performance. Extensive evaluations on three publicly available datasets show that READ-Net outperforms state-of-the-art methods, with average gains of 4.55\% in accuracy and 1.26\% in F1-score, demonstrating its robustness to emotional disturbances and improving audio-visual depression detection.

