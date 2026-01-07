---
layout: default
title: MixTTE: Multi-Level Mixture-of-Experts for Scalable and Adaptive Travel Time Estimation
---

# MixTTE: Multi-Level Mixture-of-Experts for Scalable and Adaptive Travel Time Estimation
**arXiv**：[2601.02943v1](https://arxiv.org/abs/2601.02943) · [PDF](https://arxiv.org/pdf/2601.02943.pdf)  
**作者**：Wenzhao Jiang, Jindong Han, Ruiqian Han, Hao Liu  

**一句话要点**：提出MixTTE框架以解决网约车平台中大规模城市网络旅行时间估计的准确性和适应性问题。

**关键词**：旅行时间估计, 时空注意力, 混合专家网络, 增量学习, 网约车平台

## 3 点简述
- 核心问题：现有系统难以捕捉城市尺度交通动态和长尾场景，导致预测不可靠。
- 方法要点：结合链路级建模与工业级路线级系统，采用时空外部注意力模块和图混合专家网络。
- 实验或效果：在真实数据集上显著降低预测误差，已在滴滴部署，提升服务准确性和稳定性。

## 摘要（原文）

> Accurate Travel Time Estimation (TTE) is critical for ride-hailing platforms, where errors directly impact user experience and operational efficiency. While existing production systems excel at holistic route-level dependency modeling, they struggle to capture city-scale traffic dynamics and long-tail scenarios, leading to unreliable predictions in large urban networks. In this paper, we propose \model, a scalable and adaptive framework that synergistically integrates link-level modeling with industrial route-level TTE systems. Specifically, we propose a spatio-temporal external attention module to capture global traffic dynamic dependencies across million-scale road networks efficiently. Moreover, we construct a stabilized graph mixture-of-experts network to handle heterogeneous traffic patterns while maintaining inference efficiency. Furthermore, an asynchronous incremental learning strategy is tailored to enable real-time and stable adaptation to dynamic traffic distribution shifts. Experiments on real-world datasets validate MixTTE significantly reduces prediction errors compared to seven baselines. MixTTE has been deployed in DiDi, substantially improving the accuracy and stability of the TTE service.

