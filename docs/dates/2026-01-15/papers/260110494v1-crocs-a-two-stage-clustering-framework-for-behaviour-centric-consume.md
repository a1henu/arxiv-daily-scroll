---
layout: default
title: CROCS: A Two-Stage Clustering Framework for Behaviour-Centric Consumer Segmentation with Smart Meter Data
---

# CROCS: A Two-Stage Clustering Framework for Behaviour-Centric Consumer Segmentation with Smart Meter Data
**arXiv**：[2601.10494v1](https://arxiv.org/abs/2601.10494) · [PDF](https://arxiv.org/pdf/2601.10494.pdf)  
**作者**：Luke W. Yerbury, Ricardo J. G. B. Campello, G. C. Livingston, Mark Goldsworthy, Lachlan O'Neil  

**一句话要点**：提出CROCS两阶段聚类框架，基于智能电表数据实现行为中心消费者细分以支持需求侧管理。

**关键词**：智能电表数据, 消费者细分, 两阶段聚类, 需求侧管理, 行为分析, 鲁棒聚类

## 3 点简述
- 核心问题：现有聚类方法难以处理消费者行为多样性、数据异常和大规模部署。
- 方法要点：第一阶段独立聚类日负荷曲线形成代表性负荷集，第二阶段使用加权最小距离和比较集合并聚类。
- 实验或效果：在合成和真实数据集上验证，能捕捉行为变异性、发现同步异步相似性，且鲁棒高效。

## 摘要（原文）

> With grid operators confronting rising uncertainty from renewable integration and a broader push toward electrification, Demand-Side Management (DSM) -- particularly Demand Response (DR) -- has attracted significant attention as a cost-effective mechanism for balancing modern electricity systems. Unprecedented volumes of consumption data from a continuing global deployment of smart meters enable consumer segmentation based on real usage behaviours, promising to inform the design of more effective DSM and DR programs. However, existing clustering-based segmentation methods insufficiently reflect the behavioural diversity of consumers, often relying on rigid temporal alignment, and faltering in the presence of anomalies, missing data, or large-scale deployments.
>   To address these challenges, we propose a novel two-stage clustering framework -- Clustered Representations Optimising Consumer Segmentation (CROCS). In the first stage, each consumer's daily load profiles are clustered independently to form a Representative Load Set (RLS), providing a compact summary of their typical diurnal consumption behaviours. In the second stage, consumers are clustered using the Weighted Sum of Minimum Distances (WSMD), a novel set-to-set measure that compares RLSs by accounting for both the prevalence and similarity of those behaviours. Finally, community detection on the WSMD-induced graph reveals higher-order prototypes that embody the shared diurnal behaviours defining consumer groups, enhancing the interpretability of the resulting clusters.
>   Extensive experiments on both synthetic and real Australian smart meter datasets demonstrate that CROCS captures intra-consumer variability, uncovers both synchronous and asynchronous behavioural similarities, and remains robust to anomalies and missing data, while scaling efficiently through natural parallelisation. These results...

