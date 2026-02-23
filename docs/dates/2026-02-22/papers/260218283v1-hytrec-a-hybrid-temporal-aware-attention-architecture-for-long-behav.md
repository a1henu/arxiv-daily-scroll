---
layout: default
title: HyTRec: A Hybrid Temporal-Aware Attention Architecture for Long Behavior Sequential Recommendation
---

# HyTRec: A Hybrid Temporal-Aware Attention Architecture for Long Behavior Sequential Recommendation
**arXiv**：[2602.18283v1](https://arxiv.org/abs/2602.18283) · [PDF](https://arxiv.org/pdf/2602.18283.pdf)  
**作者**：Lei Xin, Yuhao Zheng, Ke Cheng, Changjiang Jiang, Zifan Zhang, Fanhu Zeng  

**一句话要点**：提出HyTRec混合注意力架构，以解决长行为序列推荐中效率与精度的权衡问题。

**关键词**：长行为序列推荐, 混合注意力, 时间感知网络, 线性注意力, softmax注意力, 工业规模推荐

## 3 点简述
- 核心问题：长序列建模中线性注意力效率高但精度低，softmax注意力精度高但计算开销大。
- 方法要点：设计混合注意力，分离长期偏好与短期意图，并引入时间感知网络动态加权新信号。
- 实验或效果：在工业数据集上，模型保持线性推理速度，对超长序列用户命中率提升超8%。

## 摘要（原文）

> Modeling long sequences of user behaviors has emerged as a critical frontier in generative recommendation. However, existing solutions face a dilemma: linear attention mechanisms achieve efficiency at the cost of retrieval precision due to limited state capacity, while softmax attention suffers from prohibitive computational overhead. To address this challenge, we propose HyTRec, a model featuring a Hybrid Attention architecture that explicitly decouples long-term stable preferences from short-term intent spikes. By assigning massive historical sequences to a linear attention branch and reserving a specialized softmax attention branch for recent interactions, our approach restores precise retrieval capabilities within industrial-scale contexts involving ten thousand interactions. To mitigate the lag in capturing rapid interest drifts within the linear layers, we furthermore design Temporal-Aware Delta Network (TADN) to dynamically upweight fresh behavioral signals while effectively suppressing historical noise. Empirical results on industrial-scale datasets confirm the superiority that our model maintains linear inference speed and outperforms strong baselines, notably delivering over 8% improvement in Hit Rate for users with ultra-long sequences with great efficiency.

