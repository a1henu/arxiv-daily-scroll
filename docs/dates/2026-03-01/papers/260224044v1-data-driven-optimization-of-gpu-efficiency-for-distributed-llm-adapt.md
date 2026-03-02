---
layout: default
title: Data Driven Optimization of GPU efficiency for Distributed LLM Adapter Serving
---

# Data Driven Optimization of GPU efficiency for Distributed LLM Adapter Serving
**arXiv**：[2602.24044v1](https://arxiv.org/abs/2602.24044) · [PDF](https://arxiv.org/pdf/2602.24044.pdf)  
**作者**：Ferran Agullo, Joan Oliveras, Chen Wang, Alberto Gutierrez-Torre, Olivier Tardieu, Alaa Youssef, Jordi Torres, Josep Ll. Berral  

**一句话要点**：提出数据驱动管道以优化分布式LLM适配器服务的GPU效率

**关键词**：分布式LLM服务, GPU效率优化, 适配器放置, 数字孪生, 机器学习预测, 贪心算法

## 3 点简述
- 核心问题：分布式LLM适配器服务中，多适配器并发导致GPU资源效率低下，现有工作多关注延迟最小化。
- 方法要点：集成数字孪生、机器学习模型和贪心放置算法，基于性能预测计算最小GPU需求的适配器放置。
- 实验或效果：数字孪生吞吐量估计误差低于5%，加速90倍；管道显著减少GPU数量，提升效率，可扩展至延迟最小化等目标。

## 摘要（原文）

> Large Language Model (LLM) adapters enable low-cost model specialization, but introduce complex caching and scheduling challenges in distributed serving systems where hundreds of adapters must be hosted concurrently. While prior work has largely focused on latency minimization, resource efficiency through throughput maximization remains underexplored. This paper presents a data-driven pipeline that, for a given workload, computes an adapter placement that serves the workload with the minimum number of GPUs while avoiding request starvation and GPU memory errors. To that end, the approach identifies the maximum feasible throughput attainable on each GPU by leveraging accurate performance predictions learned from real serving behavior. The proposed pipeline integrates three components: (i) a Digital Twin (DT) tailored to LLM-adapter serving, (ii) a distilled machine learning (ML) model trained on DT-generated data, and (iii) a greedy placement algorithm that exploits ML-based performance estimates to maximize GPU efficiency. The DT emulates real system dynamics with high fidelity, achieving below 5% throughput estimation error while executing up to 90 times faster than full LLM benchmarking across both predictable and unpredictable workloads. The learned ML models further accelerate performance estimation with marginal accuracy degradation, enabling scalable optimization. Experimental results demonstrate that the pipeline substantially improves GPU efficiency by reducing the number of GPUs required to sustain target workloads. Beyond GPU efficiency, the pipeline can be adapted to alternative objectives, such as latency minimization, highlighting its versatility for future large-scale LLM serving infrastructures.

