---
layout: default
title: GHR-VQA: Graph-guided Hierarchical Relational Reasoning for Video Question Answering
---

# GHR-VQA: Graph-guided Hierarchical Relational Reasoning for Video Question Answering
**arXiv**：[2511.20201v1](https://arxiv.org/abs/2511.20201) · [PDF](https://arxiv.org/pdf/2511.20201.pdf)  
**作者**：Dionysia Danai Brilli, Dimitrios Mallis, Vassilis Pitsikalis, Petros Maragos  

**一句话要点**：提出GHR-VQA框架，利用场景图增强视频问答中的人-物交互推理。

**关键词**：视频问答, 场景图, 图神经网络, 人-物交互, 时空推理

## 3 点简述
- 核心问题：视频问答中如何有效建模人-物交互和时空动态。
- 方法要点：构建帧级场景图并链接到全局根节点，使用图神经网络处理。
- 实验或效果：在AGQA数据集上实现对象关系推理性能提升7.3%。

## 摘要（原文）

> We propose GHR-VQA, Graph-guided Hierarchical Relational Reasoning for Video Question Answering (Video QA), a novel human-centric framework that incorporates scene graphs to capture intricate human-object interactions within video sequences. Unlike traditional pixel-based methods, each frame is represented as a scene graph and human nodes across frames are linked to a global root, forming the video-level graph and enabling cross-frame reasoning centered on human actors. The video-level graphs are then processed by Graph Neural Networks (GNNs), transforming them into rich, context-aware embeddings for efficient processing. Finally, these embeddings are integrated with question features in a hierarchical network operating across different abstraction levels, enhancing both local and global understanding of video content. This explicit human-rooted structure enhances interpretability by decomposing actions into human-object interactions and enables a more profound understanding of spatiotemporal dynamics. We validate our approach on the Action Genome Question Answering (AGQA) dataset, achieving significant performance improvements, including a 7.3% improvement in object-relation reasoning over the state of the art.

