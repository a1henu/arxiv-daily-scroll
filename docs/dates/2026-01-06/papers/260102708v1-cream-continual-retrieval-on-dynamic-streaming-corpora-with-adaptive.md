---
layout: default
title: CREAM: Continual Retrieval on Dynamic Streaming Corpora with Adaptive Soft Memory
---

# CREAM: Continual Retrieval on Dynamic Streaming Corpora with Adaptive Soft Memory
**arXiv**：[2601.02708v1](https://arxiv.org/abs/2601.02708) · [PDF](https://arxiv.org/pdf/2601.02708.pdf)  
**作者**：HuiJeong Son, Hyeongu Kang, Sunho Kim, Subeen Ho, SeongKu Kang, Dongha Lee, Susik Yoon  

**一句话要点**：提出CREAM框架以解决动态流数据中无监督持续检索的分布偏移问题

**关键词**：持续检索, 动态流数据, 自适应软内存, 无监督学习, 分布偏移, 语义演化

## 3 点简述
- 核心问题：动态数据流中分布偏移导致检索性能下降，现有方法依赖固定查询和标注文档，泛化能力有限
- 方法要点：通过细粒度相似性估计、正则化聚类原型和分层核心集采样，构建自适应软内存以捕获流数据语义
- 实验或效果：在无标注设置下，平均在Success@5和Recall@10指标上分别超越最强方法27.79%和44.5%，性能接近或超过监督方法

## 摘要（原文）

> Information retrieval (IR) in dynamic data streams is emerging as a challenging task, as shifts in data distribution degrade the performance of AI-powered IR systems. To mitigate this issue, memory-based continual learning has been widely adopted for IR. However, existing methods rely on a fixed set of queries with ground-truth relevant documents, which limits generalization to unseen queries and documents, making them impractical for real-world applications. To enable more effective learning with unseen topics of a new corpus without ground-truth labels, we propose CREAM, a self-supervised framework for memory-based continual retrieval. CREAM captures the evolving semantics of streaming queries and documents into dynamically structured soft memory and leverages it to adapt to both seen and unseen topics in an unsupervised setting. We realize this through three key techniques: fine-grained similarity estimation, regularized cluster prototyping, and stratified coreset sampling. Experiments on two benchmark datasets demonstrate that CREAM exhibits superior adaptability and retrieval accuracy, outperforming the strongest method in a label-free setting by 27.79\% in Success@5 and 44.5\% in Recall@10 on average, and achieving performance comparable to or even exceeding that of supervised methods.

