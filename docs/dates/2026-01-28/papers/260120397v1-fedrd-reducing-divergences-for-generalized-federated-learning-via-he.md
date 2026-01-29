---
layout: default
title: FedRD: Reducing Divergences for Generalized Federated Learning via Heterogeneity-aware Parameter Guidance
---

# FedRD: Reducing Divergences for Generalized Federated Learning via Heterogeneity-aware Parameter Guidance
**arXiv**：[2601.20397v1](https://arxiv.org/abs/2601.20397) · [PDF](https://arxiv.org/pdf/2601.20397.pdf)  
**作者**：Kaile Wang, Jiannong Cao, Yu Yang, Xiaoyin Li, Mingjin Zhang  

**一句话要点**：提出FedRD以减少异构联邦学习中的优化与性能分歧，提升模型泛化能力

**关键词**：异构联邦学习, 联邦域泛化, 参数引导, 去偏分类, 多域数据集

## 3 点简述
- 核心问题：异构联邦学习中，新客户端加入时存在优化分歧和性能分歧，影响模型泛化到未见客户端
- 方法要点：通过异构感知参数引导的全局泛化聚合和局部去偏分类，协同减少分歧
- 实验或效果：在公开多域数据集上，FedRD相比基线方法展现出显著性能优势

## 摘要（原文）

> Heterogeneous federated learning (HFL) aims to ensure effective and privacy-preserving collaboration among different entities. As newly joined clients require significant adjustments and additional training to align with the existing system, the problem of generalizing federated learning models to unseen clients under heterogeneous data has become progressively crucial. Consequently, we highlight two unsolved challenging issues in federated domain generalization: Optimization Divergence and Performance Divergence. To tackle the above challenges, we propose FedRD, a novel heterogeneity-aware federated learning algorithm that collaboratively utilizes parameter-guided global generalization aggregation and local debiased classification to reduce divergences, aiming to obtain an optimal global model for participating and unseen clients. Extensive experiments on public multi-domain datasets demonstrate that our approach exhibits a substantial performance advantage over competing baselines in addressing this specific problem.

