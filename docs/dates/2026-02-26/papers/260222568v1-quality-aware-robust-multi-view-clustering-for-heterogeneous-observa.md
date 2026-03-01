---
layout: default
title: Quality-Aware Robust Multi-View Clustering for Heterogeneous Observation Noise
---

# Quality-Aware Robust Multi-View Clustering for Heterogeneous Observation Noise
**arXiv**：[2602.22568v1](https://arxiv.org/abs/2602.22568) · [PDF](https://arxiv.org/pdf/2602.22568.pdf)  
**作者**：Peihan Wu, Guanjie Cheng, Yufei Tong, Meng Xi, Shuiguang Deng  

**一句话要点**：提出质量感知鲁棒多视图聚类框架，以解决异构观测噪声下的聚类问题。

**关键词**：多视图聚类, 异构噪声, 信息瓶颈, 质量感知, 对比学习, 鲁棒性

## 3 点简述
- 核心问题：现有方法假设噪声为二元，忽略了现实中噪声强度连续变化的异构性。
- 方法要点：利用信息瓶颈提取语义，通过重建差异量化噪声强度，并集成质量分数进行分层学习。
- 实验或效果：在五个基准数据集上优于现有方法，尤其在异构噪声场景中表现突出。

## 摘要（原文）

> Deep multi-view clustering has achieved remarkable progress but remains vulnerable to complex noise in real-world applications. Existing noisy robust methods predominantly rely on a simplified binary assumption, treating data as either perfectly clean or completely corrupted. This overlooks the prevalent existence of heterogeneous observation noise, where contamination intensity varies continuously across data. To bridge this gap, we propose a novel framework termed Quality-Aware Robust Multi-View Clustering (QARMVC). Specifically, QARMVC employs an information bottleneck mechanism to extract intrinsic semantics for view reconstruction. Leveraging the insight that noise disrupts semantic integrity and impedes reconstruction, we utilize the resulting reconstruction discrepancy to precisely quantify fine-grained contamination intensity and derive instance-level quality scores. These scores are integrated into a hierarchical learning strategy: at the feature level, a quality-weighted contrastive objective is designed to adaptively suppress the propagation of noise; at the fusion level, a high-quality global consensus is constructed via quality-weighted aggregation, which is subsequently utilized to align and rectify local views via mutual information maximization. Extensive experiments on five benchmark datasets demonstrate that QARMVC consistently outperforms state-of-the-art baselines, particularly in scenarios with heterogeneous noise intensities.

