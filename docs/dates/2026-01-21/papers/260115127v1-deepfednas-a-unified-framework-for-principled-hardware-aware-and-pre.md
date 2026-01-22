---
layout: default
title: DeepFedNAS: A Unified Framework for Principled, Hardware-Aware, and Predictor-Free Federated Neural Architecture Search
---

# DeepFedNAS: A Unified Framework for Principled, Hardware-Aware, and Predictor-Free Federated Neural Architecture Search
**arXiv**：[2601.15127v1](https://arxiv.org/abs/2601.15127) · [PDF](https://arxiv.org/pdf/2601.15127.pdf)  
**作者**：Bostan Khan, Masoud Daneshtalab  

**一句话要点**：提出DeepFedNAS框架，通过原则性多目标适应度函数和预测器无关搜索，解决联邦神经架构搜索中训练无指导和搜索成本高的问题。

**关键词**：联邦学习, 神经架构搜索, 多目标优化, 帕累托最优, 预测器无关搜索, 硬件感知部署

## 3 点简述
- 核心问题：联邦神经架构搜索存在训练无指导和搜索成本高的瓶颈，导致模型次优且耗时。
- 方法要点：采用两阶段框架，包括基于帕累托最优缓存的联邦训练和预测器无关搜索，以多目标适应度函数直接代理精度。
- 实验或效果：在CIFAR-100上实现最高1.21%精度提升，搜索速度提升约61倍，总时间从20多小时降至约20分钟。

## 摘要（原文）

> Federated Neural Architecture Search (FedNAS) aims to automate model design for privacy-preserving Federated Learning (FL) but currently faces two critical bottlenecks: unguided supernet training that yields suboptimal models, and costly multi-hour pipelines for post-training subnet discovery. We introduce DeepFedNAS, a novel, two-phase framework underpinned by a principled, multi-objective fitness function that synthesizes mathematical network design with architectural heuristics. Enabled by a re-engineered supernet, DeepFedNAS introduces Federated Pareto Optimal Supernet Training, which leverages a pre-computed Pareto-optimal cache of high-fitness architectures as an intelligent curriculum to optimize shared supernet weights. Subsequently, its Predictor-Free Search Method eliminates the need for costly accuracy surrogates by utilizing this fitness function as a direct, zero-cost proxy for accuracy, enabling on-demand subnet discovery in mere seconds. DeepFedNAS achieves state-of-the-art accuracy (e.g., up to 1.21% absolute improvement on CIFAR-100), superior parameter and communication efficiency, and a substantial ~61x speedup in total post-training search pipeline time. By reducing the pipeline from over 20 hours to approximately 20 minutes (including initial cache generation) and enabling 20-second individual subnet searches, DeepFedNAS makes hardware-aware FL deployments instantaneous and practical. The complete source code and experimental scripts are available at: https://github.com/bostankhan6/DeepFedNAS

