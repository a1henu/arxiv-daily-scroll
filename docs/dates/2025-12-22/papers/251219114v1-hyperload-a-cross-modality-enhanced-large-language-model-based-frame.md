---
layout: default
title: HyperLoad: A Cross-Modality Enhanced Large Language Model-Based Framework for Green Data Center Cooling Load Prediction
---

# HyperLoad: A Cross-Modality Enhanced Large Language Model-Based Framework for Green Data Center Cooling Load Prediction
**arXiv**：[2512.19114v1](https://arxiv.org/abs/2512.19114) · [PDF](https://arxiv.org/pdf/2512.19114.pdf)  
**作者**：Haoyu Jiang, Boan Qu, Junjie Zhu, Fanjie Zeng, Xiaojie Lin, Wei Zhong  

**一句话要点**：提出HyperLoad框架，利用大语言模型解决绿色数据中心冷却负荷预测中的数据稀缺问题。

**关键词**：绿色数据中心, 冷却负荷预测, 大语言模型, 跨模态学习, 小样本学习, 时序依赖建模

## 3 点简述
- 核心问题：绿色数据中心因冷启动、数据碎片化等导致小样本场景，现有方法预测困难。
- 方法要点：通过跨模态知识对齐和多尺度特征建模，注入文本先验并捕获设备间时序依赖。
- 实验或效果：在公开数据集上，数据充足和稀缺设置下均超越现有最佳方法，验证实用性。

## 摘要（原文）

> The rapid growth of artificial intelligence is exponentially escalating computational demand, inflating data center energy use and carbon emissions, and spurring rapid deployment of green data centers to relieve resource and environmental stress. Achieving sub-minute orchestration of renewables, storage, and loads, while minimizing PUE and lifecycle carbon intensity, hinges on accurate load forecasting. However, existing methods struggle to address small-sample scenarios caused by cold start, load distortion, multi-source data fragmentation, and distribution shifts in green data centers. We introduce HyperLoad, a cross-modality framework that exploits pre-trained large language models (LLMs) to overcome data scarcity. In the Cross-Modality Knowledge Alignment phase, textual priors and time-series data are mapped to a common latent space, maximizing the utility of prior knowledge. In the Multi-Scale Feature Modeling phase, domain-aligned priors are injected through adaptive prefix-tuning, enabling rapid scenario adaptation, while an Enhanced Global Interaction Attention mechanism captures cross-device temporal dependencies. The public DCData dataset is released for benchmarking. Under both data sufficient and data scarce settings, HyperLoad consistently surpasses state-of-the-art (SOTA) baselines, demonstrating its practicality for sustainable green data center management.

