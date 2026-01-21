---
layout: default
title: Unsupervised Video Class-Incremental Learning via Deep Embedded Clustering Management
---

# Unsupervised Video Class-Incremental Learning via Deep Embedded Clustering Management
**arXiv**：[2601.14069v1](https://arxiv.org/abs/2601.14069) · [PDF](https://arxiv.org/pdf/2601.14069.pdf)  
**作者**：Nattapong Kurpukdee, Adrian G. Bors  

**一句话要点**：提出基于深度嵌入聚类管理的无监督视频类增量学习方法，以解决无标签视频学习中的遗忘问题。

**关键词**：无监督学习, 视频类增量学习, 深度聚类, 特征提取, 知识迁移, 动作识别

## 3 点简述
- 核心问题：无监督视频类增量学习（uVCIL）旨在无标签条件下学习视频信息而不遗忘，现有方法依赖监督标签和任务边界，成本高或不现实。
- 方法要点：使用深度特征提取器获取视频特征，逐步构建深度聚类，通过模型初始化实现任务间知识迁移，无需类别或任务信息。
- 实验或效果：在UCF101、HMDB51和Something-to-Something V2数据集上忽略标签进行评估，显著优于基线方法。

## 摘要（原文）

> Unsupervised video class incremental learning (uVCIL) represents an important learning paradigm for learning video information without forgetting, and without considering any data labels. Prior approaches have focused on supervised class-incremental learning, relying on using the knowledge of labels and task boundaries, which is costly, requires human annotation, or is simply not a realistic option. In this paper, we propose a simple yet effective approach to address the uVCIL. We first consider a deep feature extractor network, providing a set of representative video features during each task without assuming any class or task information. We then progressively build a series of deep clusters from the extracted features. During the successive task learning, the model updated from the previous task is used as an initial state in order to transfer knowledge to the current learning task. We perform in-depth evaluations on three standard video action recognition datasets, including UCF101, HMDB51, and Something-to-Something V2, by ignoring the labels from the supervised setting. Our approach significantly outperforms other baselines on all datasets.

