---
layout: default
title: Mosaic Learning: A Framework for Decentralized Learning with Model Fragmentation
---

# Mosaic Learning: A Framework for Decentralized Learning with Model Fragmentation
**arXiv**：[2602.04352v1](https://arxiv.org/abs/2602.04352) · [PDF](https://arxiv.org/pdf/2602.04352.pdf)  
**作者**：Sayan Biswas, Davide Frey, Romaric Gaudel, Nirupam Gupta, Anne-Marie Kermarrec, Dimitri Lerévérend, Rafael Pires, Rishi Sharma, François Taïani, Martijn de Vos  

**一句话要点**：提出Mosaic Learning框架，通过模型分片实现去中心化学习，提升性能而不增加通信成本。

**关键词**：去中心化学习, 模型分片, 参数相关性, 收敛分析, 通信优化, 分布式机器学习

## 3 点简述
- 核心问题：去中心化学习中数据无法集中处理，传统方法通信冗余且信息传播受限。
- 方法要点：将模型分解为片段独立传播，利用参数相关性减少通信，理论证明收敛率最优。
- 实验或效果：在四个学习任务上评估，节点级测试准确率比基线提升高达12个百分点。

## 摘要（原文）

> Decentralized learning (DL) enables collaborative machine learning (ML) without a central server, making it suitable for settings where training data cannot be centrally hosted. We introduce Mosaic Learning, a DL framework that decomposes models into fragments and disseminates them independently across the network. Fragmentation reduces redundant communication across correlated parameters and enables more diverse information propagation without increasing communication cost. We theoretically show that Mosaic Learning (i) shows state-of-the-art worst-case convergence rate, and (ii) leverages parameter correlation in an ML model, improving contraction by reducing the highest eigenvalue of a simplified system. We empirically evaluate Mosaic Learning on four learning tasks and observe up to 12 percentage points higher node-level test accuracy compared to epidemic learning (EL), a state-of-the-art baseline. In summary, Mosaic Learning improves DL performance without sacrificing its utility or efficiency, and positions itself as a new DL standard.

