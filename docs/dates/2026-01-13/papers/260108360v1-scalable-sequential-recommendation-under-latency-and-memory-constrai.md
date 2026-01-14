---
layout: default
title: Scalable Sequential Recommendation under Latency and Memory Constraints
---

# Scalable Sequential Recommendation under Latency and Memory Constraints
**arXiv**：[2601.08360v1](https://arxiv.org/abs/2601.08360) · [PDF](https://arxiv.org/pdf/2601.08360.pdf)  
**作者**：Adithya Parthasarathy, Aswathnarayan Muthukrishnan Kirubakaran, Vinoth Punniyamoorthy, Nachiappan Chockalingam, Lokesh Butra, Kabilan Kannan, Abhirup Mazumder, Sumit Saha  

**一句话要点**：提出HoloMambaRec以解决序列推荐中长程建模与资源约束的平衡问题

**关键词**：序列推荐, 长程建模, 资源约束, 全息降维表示, 选择性状态空间编码, 线性时间处理

## 3 点简述
- 核心问题：Transformer方法因二次注意力复杂度，需截断用户历史，限制长程建模实用性
- 方法要点：结合全息降维表示与选择性状态空间编码，实现线性时间处理与属性感知嵌入
- 实验或效果：在Amazon Beauty和MovieLens-1M上优于SASRec，与GRU4Rec竞争，内存复杂度更低

## 摘要（原文）

> Sequential recommender systems must model long-range user behavior while operating under strict memory and latency constraints. Transformer-based approaches achieve strong accuracy but suffer from quadratic attention complexity, forcing aggressive truncation of user histories and limiting their practicality for long-horizon modeling. This paper presents HoloMambaRec, a lightweight sequential recommendation architecture that combines holographic reduced representations for attribute-aware embedding with a selective state space encoder for linear-time sequence processing. Item and attribute information are bound using circular convolution, preserving embedding dimensionality while encoding structured metadata. A shallow selective state space backbone, inspired by recent Mamba-style models, enables efficient training and constant-time recurrent inference. Experiments on Amazon Beauty and MovieLens-1M datasets demonstrate that HoloMambaRec consistently outperforms SASRec and achieves competitive performance with GRU4Rec under a constrained 10-epoch training budget, while maintaining substantially lower memory complexity. The design further incorporates forward-compatible mechanisms for temporal bundling and inference-time compression, positioning HoloMambaRec as a practical and extensible alternative for scalable, metadata-aware sequential recommendation.

