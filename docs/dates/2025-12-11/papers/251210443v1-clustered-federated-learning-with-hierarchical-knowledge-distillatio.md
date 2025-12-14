---
layout: default
title: Clustered Federated Learning with Hierarchical Knowledge Distillation
---

# Clustered Federated Learning with Hierarchical Knowledge Distillation
**arXiv**：[2512.10443v1](https://arxiv.org/abs/2512.10443) · [PDF](https://arxiv.org/pdf/2512.10443.pdf)  
**作者**：Sabtain Ahmad, Meerzhan Kanatbekova, Ivona Brandic, Atakan Aral  

**一句话要点**：提出CFLHKD方案，通过分层知识蒸馏解决聚类联邦学习中的知识共享与个性化平衡问题。

**关键词**：聚类联邦学习, 知识蒸馏, 分层聚合, 个性化模型, 物联网环境

## 3 点简述
- 核心问题：传统聚类联邦学习模型独立训练，缺乏集群间知识共享，导致学习碎片化。
- 方法要点：采用分层聚合与多教师知识蒸馏，实现集群间知识传递，同时保持个性化模型。
- 实验或效果：在标准数据集上，CFLHKD在集群特定和全局模型准确率上优于基线，提升3.32-7.57%。

## 摘要（原文）

> Clustered Federated Learning (CFL) has emerged as a powerful approach for addressing data heterogeneity and ensuring privacy in large distributed IoT environments. By clustering clients and training cluster-specific models, CFL enables personalized models tailored to groups of heterogeneous clients. However, conventional CFL approaches suffer from fragmented learning for training independent global models for each cluster and fail to take advantage of collective cluster insights. This paper advocates a shift to hierarchical CFL, allowing bi-level aggregation to train cluster-specific models at the edge and a unified global model at the cloud. This shift improves training efficiency yet might introduce communication challenges. To this end, we propose CFLHKD, a novel personalization scheme for integrating hierarchical cluster knowledge into CFL. Built upon multi-teacher knowledge distillation, CFLHKD enables inter-cluster knowledge sharing while preserving cluster-specific personalization. CFLHKD adopts a bi-level aggregation to bridge the gap between local and global learning. Extensive evaluations of standard benchmark datasets demonstrate that CFLHKD outperforms representative baselines in cluster-specific and global model accuracy and achieves a performance improvement of 3.32-7.57\%.

