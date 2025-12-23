---
layout: default
title: Faster Distributed Inference-Only Recommender Systems via Bounded Lag Synchronous Collectives
---

# Faster Distributed Inference-Only Recommender Systems via Bounded Lag Synchronous Collectives
**arXiv**：[2512.19342v1](https://arxiv.org/abs/2512.19342) · [PDF](https://arxiv.org/pdf/2512.19342.pdf)  
**作者**：Kiril Dichev, Filip Pawlowski, Albert-Jan Yzelman  

**一句话要点**：提出有界滞后同步集体操作以加速分布式推理推荐系统

**关键词**：分布式推荐系统, 深度学习推荐模型, 稀疏特征查找, 有界滞后同步, 推理优化

## 3 点简述
- 核心问题：分布式推荐系统推理中，稀疏特征查找的异步通信是主要瓶颈
- 方法要点：设计有界滞后同步alltoallv操作，允许进程在限定滞后内异步执行
- 实验或效果：在不平衡场景下，显著提升推理延迟和吞吐量，掩盖进程延迟

## 摘要（原文）

> Recommender systems are enablers of personalized content delivery, and therefore revenue, for many large companies. In the last decade, deep learning recommender models (DLRMs) are the de-facto standard in this field. The main bottleneck in DLRM inference is the lookup of sparse features across huge embedding tables, which are usually partitioned across the aggregate RAM of many nodes. In state-of-the-art recommender systems, the distributed lookup is implemented via irregular all-to-all (alltoallv) communication, and often presents the main bottleneck. Today, most related work sees this operation as a given; in addition, every collective is synchronous in nature. In this work, we propose a novel bounded lag synchronous (BLS) version of the alltoallv operation. The bound can be a parameter allowing slower processes to lag behind entire iterations before the fastest processes block. In special applications such as inference-only DLRM, the accuracy of the application is fully preserved. We implement BLS alltoallv in a new PyTorch Distributed backend and evaluate it with a BLS version of the reference DLRM code. We show that for well balanced, homogeneous-access DLRM runs our BLS technique does not offer notable advantages. But for unbalanced runs, e.g. runs with strongly irregular embedding table accesses or with delays across different processes, our BLS technique improves both the latency and throughput of inference-only DLRM. In the best-case scenario, the proposed reduced synchronisation can mask the delays across processes altogether.

