---
layout: default
title: Test-Time Adaptation for Anomaly Segmentation via Topology-Aware Optimal Transport Chaining
---

# Test-Time Adaptation for Anomaly Segmentation via Topology-Aware Optimal Transport Chaining
**arXiv**：[2601.20333v1](https://arxiv.org/abs/2601.20333) · [PDF](https://arxiv.org/pdf/2601.20333.pdf)  
**作者**：Ali Zia, Usman Ali, Umer Ramzan, Abdul Rehman, Abdelwahed Khamis, Wei Xiang  

**一句话要点**：提出TopoOT框架，通过拓扑感知最优传输链实现异常分割的测试时适应

**关键词**：异常分割, 拓扑数据分析, 最优传输, 测试时适应, 持久性图, 伪标签学习

## 3 点简述
- 核心问题：异常分割在分布偏移下易受局部波动影响，需捕捉全局结构不变性。
- 方法要点：结合多过滤持久性图与最优传输链，生成跨尺度稳定性分数作为伪标签。
- 实验或效果：在2D和3D基准测试中达到最先进性能，F1分数显著提升。

## 摘要（原文）

> Deep topological data analysis (TDA) offers a principled framework for capturing structural invariants such as connectivity and cycles that persist across scales, making it a natural fit for anomaly segmentation (AS). Unlike thresholdbased binarisation, which produces brittle masks under distribution shift, TDA allows anomalies to be characterised as disruptions to global structure rather than local fluctuations. We introduce TopoOT, a topology-aware optimal transport (OT) framework that integrates multi-filtration persistence diagrams (PDs) with test-time adaptation (TTA). Our key innovation is Optimal Transport Chaining, which sequentially aligns PDs across thresholds and filtrations, yielding geodesic stability scores that identify features consistently preserved across scales. These stabilityaware pseudo-labels supervise a lightweight head trained online with OT-consistency and contrastive objectives, ensuring robust adaptation under domain shift. Across standard 2D and 3D anomaly detection benchmarks, TopoOT achieves state-of-the-art performance, outperforming the most competitive methods by up to +24.1% mean F1 on 2D datasets and +10.2% on 3D AS benchmarks.

