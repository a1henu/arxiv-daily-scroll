---
layout: default
title: FedBiCross: A Bi-Level Optimization Framework to Tackle Non-IID Challenges in Data-Free One-Shot Federated Learning on Medical Data
---

# FedBiCross: A Bi-Level Optimization Framework to Tackle Non-IID Challenges in Data-Free One-Shot Federated Learning on Medical Data
**arXiv**：[2601.01901v1](https://arxiv.org/abs/2601.01901) · [PDF](https://arxiv.org/pdf/2601.01901.pdf)  
**作者**：Yuexuan Xia, Yinghao Zhang, Yalin Liu, Hong-Ning Dai, Yong Xia  

**一句话要点**：提出FedBiCross框架以解决非独立同分布数据下无数据单轮联邦学习的负迁移问题

**关键词**：联邦学习, 知识蒸馏, 非独立同分布数据, 医学图像分析, 个性化学习, 单轮通信

## 3 点简述
- 核心问题：非独立同分布数据导致全局教师模型预测平均后产生近均匀软标签，削弱蒸馏监督效果
- 方法要点：通过聚类形成子集成，采用双层跨集群优化自适应权重，选择性利用有益知识并抑制负迁移
- 实验或效果：在四个医学图像数据集上验证，FedBiCross在不同非独立同分布程度下均优于现有基线方法

## 摘要（原文）

> Data-free knowledge distillation-based one-shot federated learning (OSFL) trains a model in a single communication round without sharing raw data, making OSFL attractive for privacy-sensitive medical applications. However, existing methods aggregate predictions from all clients to form a global teacher. Under non-IID data, conflicting predictions cancel out during averaging, yielding near-uniform soft labels that provide weak supervision for distillation. We propose FedBiCross, a personalized OSFL framework with three stages: (1) clustering clients by model output similarity to form coherent sub-ensembles, (2) bi-level cross-cluster optimization that learns adaptive weights to selectively leverage beneficial cross-cluster knowledge while suppressing negative transfer, and (3) personalized distillation for client-specific adaptation. Experiments on four medical image datasets demonstrate that FedBiCross consistently outperforms state-of-the-art baselines across different non-IID degrees.

