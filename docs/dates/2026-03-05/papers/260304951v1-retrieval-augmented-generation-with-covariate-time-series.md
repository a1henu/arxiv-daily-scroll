---
layout: default
title: Retrieval-Augmented Generation with Covariate Time Series
---

# Retrieval-Augmented Generation with Covariate Time Series
**arXiv**：[2603.04951v1](https://arxiv.org/abs/2603.04951) · [PDF](https://arxiv.org/pdf/2603.04951.pdf)  
**作者**：Kenny Ye Liang, Zhongyi Pei, Huan Zhang, Yuhui Liu, Shaoxu Song, Jianmin Wang  

**一句话要点**：提出RAG4CTS框架以解决压力调节关断阀预测性维护中的时间序列检索增强生成挑战

**关键词**：时间序列检索增强生成, 协变量时间序列, 预测性维护, 工业物联网, 无训练框架, 状态感知检索

## 3 点简述
- 核心问题：时间序列基础模型在数据稀缺、序列短暂和协变量耦合的工业场景中，现有检索增强方法难以区分相似状态。
- 方法要点：构建分层原生知识库，设计两阶段双加权检索机制，并采用代理驱动策略动态优化上下文。
- 实验或效果：在PRSOV数据集上预测精度显著优于基线，部署于中国南方航空Apache IoTDB，两个月内成功识别一次故障且无虚警。

## 摘要（原文）

> While RAG has greatly enhanced LLMs, extending this paradigm to Time-Series Foundation Models (TSFMs) remains a challenge. This is exemplified in the Predictive Maintenance of the Pressure Regulating and Shut-Off Valve (PRSOV), a high-stakes industrial scenario characterized by (1) data scarcity, (2) short transient sequences, and (3) covariate coupled dynamics. Unfortunately, existing time-series RAG approaches predominantly rely on generated static vector embeddings and learnable context augmenters, which may fail to distinguish similar regimes in such scarce, transient, and covariate coupled scenarios. To address these limitations, we propose RAG4CTS, a regime-aware, training-free RAG framework for Covariate Time-Series. Specifically, we construct a hierarchal time-series native knowledge base to enable lossless storage and physics-informed retrieval of raw historical regimes. We design a two-stage bi-weighted retrieval mechanism that aligns historical trends through point-wise and multivariate similarities. For context augmentation, we introduce an agent-driven strategy to dynamically optimize context in a self-supervised manner. Extensive experiments on PRSOV demonstrate that our framework significantly outperforms state-of-the-art baselines in prediction accuracy. The proposed system is deployed in Apache IoTDB within China Southern Airlines. Since deployment, our method has successfully identified one PRSOV fault in two months with zero false alarm.

