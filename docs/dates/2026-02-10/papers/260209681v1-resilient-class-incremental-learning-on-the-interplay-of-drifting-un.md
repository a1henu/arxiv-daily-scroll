---
layout: default
title: Resilient Class-Incremental Learning: on the Interplay of Drifting, Unlabelled and Imbalanced Data Streams
---

# Resilient Class-Incremental Learning: on the Interplay of Drifting, Unlabelled and Imbalanced Data Streams
**arXiv**：[2602.09681v1](https://arxiv.org/abs/2602.09681) · [PDF](https://arxiv.org/pdf/2602.09681.pdf)  
**作者**：Jin Li, Kleanthis Malialis, Marios Polycarpou  

**一句话要点**：提出SCIL框架以解决概念漂移、类别不平衡和标签稀缺下的流式类增量学习问题

**关键词**：流式学习, 类增量学习, 概念漂移, 类别不平衡, 伪标签学习, 自编码器

## 3 点简述
- 核心问题：数据流中概念漂移、类别不平衡、标签稀缺和新类出现共同导致表示不稳定和检测可靠性下降
- 方法要点：集成自编码器与多层感知器，采用双损失策略、修正伪标签、队列管理和过采样处理不平衡
- 实验或效果：在真实和合成数据集上评估，SCIL优于强基线和先进方法，代码和数据集已开源

## 摘要（原文）

> In today's connected world, the generation of massive streaming data across diverse domains has become commonplace. In the presence of concept drift, class imbalance, label scarcity, and new class emergence, they jointly degrade representation stability, bias learning toward outdated distributions, and reduce the resilience and reliability of detection in dynamic environments. This paper proposes SCIL (Streaming Class-Incremental Learning) to address these challenges. The SCIL framework integrates an autoencoder (AE) with a multi-layer perceptron for multi-class prediction, uses a dual-loss strategy (classification and reconstruction) for prediction and new class detection, employs corrected pseudo-labels for online training, manages classes with queues, and applies oversampling to handle imbalance. The rationale behind the method's structure is elucidated through ablation studies and a comprehensive experimental evaluation is performed using both real-world and synthetic datasets that feature class imbalance, incremental classes, and concept drifts. Our results demonstrate that SCIL outperforms strong baselines and state-of-the-art methods. Based on our commitment to Open Science, we make our code and datasets available to the community.

