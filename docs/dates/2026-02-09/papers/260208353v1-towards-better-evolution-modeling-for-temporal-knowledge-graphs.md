---
layout: default
title: Towards Better Evolution Modeling for Temporal Knowledge Graphs
---

# Towards Better Evolution Modeling for Temporal Knowledge Graphs
**arXiv**：[2602.08353v1](https://arxiv.org/abs/2602.08353) · [PDF](https://arxiv.org/pdf/2602.08353.pdf)  
**作者**：Zhang Jiasheng, Li Zhangpin, Wang Mingzhe, Shao Jie, Cui Jiangtao, Li Hui  

**一句话要点**：提出TKG演化基准以解决现有基准中的偏差和简化问题

**关键词**：时序知识图谱, 演化建模, 基准评估, 数据集偏差, 时间信息利用, 知识过时学习

## 3 点简述
- 发现现有TKG基准存在捷径，如仅依赖共现计数即可达到高性能，无需时间信息
- 分析偏差根源，包括数据集固有偏差、评估任务简化及时间间隔知识格式不合理
- 引入包含四个偏差校正数据集和两个新任务的基准，促进更准确的TKG演化建模评估

## 摘要（原文）

> Temporal knowledge graphs (TKGs) structurally preserve evolving human knowledge. Recent research has focused on designing models to learn the evolutionary nature of TKGs to predict future facts, achieving impressive results. For instance, Hits@10 scores over 0.9 on YAGO dataset. However, we find that existing benchmarks inadvertently introduce a shortcut. Near state-of-the-art performance can be simply achieved by counting co-occurrences, without using any temporal information. In this work, we examine the root cause of this issue, identifying inherent biases in current datasets and over simplified form of evaluation task that can be exploited by these biases. Through this analysis, we further uncover additional limitations of existing benchmarks, including unreasonable formatting of time-interval knowledge, ignorance of learning knowledge obsolescence, and insufficient information for precise evolution understanding, all of which can amplify the shortcut and hinder a fair assessment. Therefore, we introduce the TKG evolution benchmark. It includes four bias-corrected datasets and two novel tasks closely aligned with the evolution process, promoting a more accurate understanding of the challenges in TKG evolution modeling. Benchmark is available at: https://github.com/zjs123/TKG-Benchmark.

