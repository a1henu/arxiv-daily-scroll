---
layout: default
title: Relational In-Context Learning via Synthetic Pre-training with Structural Prior
---

# Relational In-Context Learning via Synthetic Pre-training with Structural Prior
**arXiv**：[2603.03805v1](https://arxiv.org/abs/2603.03805) · [PDF](https://arxiv.org/pdf/2603.03805.pdf)  
**作者**：Yanbo Wang, Jiaxuan You, Chuan Shi, Muhan Zhang  

**一句话要点**：提出RDB-PFN，首个基于合成数据的关系型基础模型，通过结构先验实现关系数据库的上下文学习。

**关键词**：关系数据库, 合成数据预训练, 上下文学习, 基础模型, 少样本学习

## 3 点简述
- 核心问题：关系数据库缺乏高质量公开数据，导致基础模型训练困难。
- 方法要点：设计关系先验生成器，从零生成多样合成数据库进行预训练。
- 实验或效果：在19个真实关系预测任务中，实现强少样本性能，超越基线模型。

## 摘要（原文）

> Relational Databases (RDBs) are the backbone of modern business, yet they lack foundation models comparable to those in text or vision. A key obstacle is that high-quality RDBs are private, scarce and structurally heterogeneous, making internet-scale pre-training infeasible. To overcome this data scarcity, We introduce $\textbf{RDB-PFN}$, the first relational foundation model trained purely via $\textbf{synthetic data}$. Inspired by Prior-Data Fitted Networks (PFNs) where synthetic data generated from Structural Causal Models (SCMs) enables reasoning on single tables, we design a $\textbf{Relational Prior Generator}$ to create an infinite stream of diverse RDBs from scratch. Pre-training on $\textbf{over 2 million}$ synthetic single-table and relational tasks, RDB-PFN learns to adapt to any new database instantly via genuine $\textbf{in-context learning}$. Experiments verify RDB-PFN achieves strong few-shot performance on 19 real-world relational prediction tasks, outperforming graph-based and single-table foundation-model baselines (given the same DFS-linearized inputs), while using a lightweight architecture and fast inference. The code is available at https://github.com/MuLabPKU/RDBPFN

