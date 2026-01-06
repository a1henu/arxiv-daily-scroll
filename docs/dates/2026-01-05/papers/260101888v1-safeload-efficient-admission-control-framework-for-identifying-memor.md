---
layout: default
title: SafeLoad: Efficient Admission Control Framework for Identifying Memory-Overloading Queries in Cloud Data Warehouses
---

# SafeLoad: Efficient Admission Control Framework for Identifying Memory-Overloading Queries in Cloud Data Warehouses
**arXiv**：[2601.01888v1](https://arxiv.org/abs/2601.01888) · [PDF](https://arxiv.org/pdf/2601.01888.pdf)  
**作者**：Yifan Wu, Yuhan Li, Zhenhua Wang, Zhongle Xie, Dingyu Yang, Ke Chen, Lidan Shou, Bo Tang, Liang Lin, Huan Li, Gang Chen  

**一句话要点**：提出SafeLoad框架以解决云数据仓库中内存过载查询的识别问题

**关键词**：云数据仓库, 内存过载查询, 准入控制框架, 混合模型, 自调配额管理, 开源基准

## 3 点简述
- 核心问题：内存过载是云数据仓库常见资源耗尽形式，导致查询失败和资源浪费，现有框架识别精度有限且缺乏公开数据集。
- 方法要点：SafeLoad结合可解释判别规则、全局与集群级混合模型、误预测校正模块及自调配额管理，高效识别内存过载查询。
- 实验或效果：实验显示SafeLoad提升精度达66%，减少CPU时间浪费8.09倍，并发布开源基准SafeBench含1.5亿查询。

## 摘要（原文）

> Memory overload is a common form of resource exhaustion in cloud data warehouses. When database queries fail due to memory overload, it not only wastes critical resources such as CPU time but also disrupts the execution of core business processes, as memory-overloading (MO) queries are typically part of complex workflows. If such queries are identified in advance and scheduled to memory-rich serverless clusters, it can prevent resource wastage and query execution failure. Therefore, cloud data warehouses desire an admission control framework with high prediction precision, interpretability, efficiency, and adaptability to effectively identify MO queries. However, existing admission control frameworks primarily focus on scenarios like SLA satisfaction and resource isolation, with limited precision in identifying MO queries. Moreover, there is a lack of publicly available MO-labeled datasets with workloads for training and benchmarking. To tackle these challenges, we propose SafeLoad, the first query admission control framework specifically designed to identify MO queries. Alongside, we release SafeBench, an open-source, industrial-scale benchmark for this task, which includes 150 million real queries. SafeLoad first filters out memory-safe queries using the interpretable discriminative rule. It then applies a hybrid architecture that integrates both a global model and cluster-level models, supplemented by a misprediction correction module to identify MO queries. Additionally, a self-tuning quota management mechanism dynamically adjusts prediction quotas per cluster to improve precision. Experimental results show that SafeLoad achieves state-of-the-art prediction performance with low online and offline time overhead. Specifically, SafeLoad improves precision by up to 66% over the best baseline and reduces wasted CPU time by up to 8.09x compared to scenarios without SafeLoad.

