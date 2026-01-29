---
layout: default
title: Proactive SFC Provisioning with Forecast-Driven DRL in Data Centers
---

# Proactive SFC Provisioning with Forecast-Driven DRL in Data Centers
**arXiv**：[2601.20229v1](https://arxiv.org/abs/2601.20229) · [PDF](https://arxiv.org/pdf/2601.20229.pdf)  
**作者**：Parisa Fard Moshiri, Poonam Lohan, Burak Kantarci, Emil Janulewicz  

**一句话要点**：提出预测驱动的深度强化学习框架以优化数据中心服务功能链资源分配

**关键词**：服务功能链, 深度强化学习, 时空图神经网络, 资源分配优化, 数据中心管理

## 3 点简述
- 核心问题：数据中心动态流量导致静态资源分配效率低下，易引发过载或欠载。
- 方法要点：结合深度强化学习生成数据集，训练时空图神经网络等模型，集成预测以指导主动资源分配。
- 实验或效果：显著提升延迟敏感服务接受率，如增强现实从30%增至50%，并降低端到端延迟达34.8%。

## 摘要（原文）

> Service Function Chaining (SFC) requires efficient placement of Virtual Network Functions (VNFs) to satisfy diverse service requirements while maintaining high resource utilization in Data Centers (DCs). Conventional static resource allocation often leads to overprovisioning or underprovisioning due to the dynamic nature of traffic loads and application demands. To address this challenge, we propose a hybrid forecast-driven Deep reinforcement learning (DRL) framework that combines predictive intelligence with SFC provisioning. Specifically, we leverage DRL to generate datasets capturing DC resource utilization and service demands, which are then used to train deep learning forecasting models. Using Optuna-based hyperparameter optimization, the best-performing models, Spatio-Temporal Graph Neural Network, Temporal Graph Neural Network, and Long Short-Term Memory, are combined into an ensemble to enhance stability and accuracy. The ensemble predictions are integrated into the DC selection process, enabling proactive placement decisions that consider both current and future resource availability. Experimental results demonstrate that the proposed method not only sustains high acceptance ratios for resource-intensive services such as Cloud Gaming and VoIP but also significantly improves acceptance ratios for latency-critical categories such as Augmented Reality increases from 30% to 50%, while Industry 4.0 improves from 30% to 45%. Consequently, the prediction-based model achieves significantly lower E2E latencies of 20.5%, 23.8%, and 34.8% reductions for VoIP, Video Streaming, and Cloud Gaming, respectively. This strategy ensures more balanced resource allocation, and reduces contention.

