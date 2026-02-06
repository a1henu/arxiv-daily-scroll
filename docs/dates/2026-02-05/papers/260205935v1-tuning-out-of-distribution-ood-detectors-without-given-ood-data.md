---
layout: default
title: Tuning Out-of-Distribution (OOD) Detectors Without Given OOD Data
---

# Tuning Out-of-Distribution (OOD) Detectors Without Given OOD Data
**arXiv**：[2602.05935v1](https://arxiv.org/abs/2602.05935) · [PDF](https://arxiv.org/pdf/2602.05935.pdf)  
**作者**：Sudeepta Mondal, Xinyi Mary Xie, Ruxiao Duan, Alex Wong, Ganesh Sundaramoorthi  

**一句话要点**：提出无需给定OOD数据的OOD检测器调优方法，以解决现有方法依赖特定OOD数据集的问题。

**关键词**：OOD检测, 神经网络调优, 无监督学习, 分布外检测, 模型泛化

## 3 点简述
- 核心问题：现有OOD检测器调优依赖特定OOD数据集，导致性能不稳定且数据获取困难。
- 方法要点：提出通用调优方法，仅使用神经网络训练数据，无需额外OOD数据集。
- 实验或效果：在参数较多的OOD检测器家族中，方法优于基线，参数较少时表现相当。

## 摘要（原文）

> Existing out-of-distribution (OOD) detectors are often tuned by a separate dataset deemed OOD with respect to the training distribution of a neural network (NN). OOD detectors process the activations of NN layers and score the output, where parameters of the detectors are determined by fitting to an in-distribution (training) set and the aforementioned dataset chosen adhocly. At detector training time, this adhoc dataset may not be available or difficult to obtain, and even when it's available, it may not be representative of actual OOD data, which is often ''unknown unknowns." Current benchmarks may specify some left-out set from test OOD sets. We show that there can be significant variance in performance of detectors based on the adhoc dataset chosen in current literature, and thus even if such a dataset can be collected, the performance of the detector may be highly dependent on the choice. In this paper, we introduce and formalize the often neglected problem of tuning OOD detectors without a given ``OOD'' dataset. To this end, we present strong baselines as an attempt to approach this problem. Furthermore, we propose a new generic approach to OOD detector tuning that does not require any extra data other than those used to train the NN. We show that our approach improves over baseline methods consistently across higher-parameter OOD detector families, while being comparable across lower-parameter families.

