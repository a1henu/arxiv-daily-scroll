---
layout: default
title: Qute: Towards Quantum-Native Database
---

# Qute: Towards Quantum-Native Database
**arXiv**：[2602.14699v1](https://arxiv.org/abs/2602.14699) · [PDF](https://arxiv.org/pdf/2602.14699.pdf)  
**作者**：Muzhi Chen, Xuanhe Zhou, Wei Zhou, Bangrui Xu, Surui Tang, Guoliang Li, Bingsheng He, Yeye He, Yitong Song, Fan Wu  

**一句话要点**：提出量子原生数据库Qute，将量子计算作为一等执行选项以提升数据库性能。

**关键词**：量子数据库, SQL编译, 混合优化器, 量子索引, 保真度存储, 量子原生系统

## 3 点简述
- 核心问题：现有方法在经典机器上模拟量子算法或适配数据库，未充分利用量子计算潜力。
- 方法要点：编译扩展SQL为门高效量子电路，采用混合优化器动态选择量子或经典执行计划。
- 实验或效果：在真实量子处理器上部署，显示在大规模下优于经典基线，并开源原型。

## 摘要（原文）

> This paper envisions a quantum database (Qute) that treats quantum computation as a first-class execution option. Unlike prior simulation-based methods that either run quantum algorithms on classical machines or adapt existing databases for quantum simulation, Qute instead (i) compiles an extended form of SQL into gate-efficient quantum circuits, (ii) employs a hybrid optimizer to dynamically select between quantum and classical execution plans, (iii) introduces selective quantum indexing, and (iv) designs fidelity-preserving storage to mitigate current qubit constraints. We also present a three-stage evolution roadmap toward quantum-native database. Finally, by deploying Qute on a real quantum processor (origin_wukong), we show that it outperforms a classical baseline at scale, and we release an open-source prototype at https://github.com/weAIDB/Qute.

