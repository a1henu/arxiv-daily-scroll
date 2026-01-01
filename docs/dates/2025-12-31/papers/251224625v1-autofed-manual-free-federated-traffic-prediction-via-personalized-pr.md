---
layout: default
title: AutoFed: Manual-Free Federated Traffic Prediction via Personalized Prompt
---

# AutoFed: Manual-Free Federated Traffic Prediction via Personalized Prompt
**arXiv**：[2512.24625v1](https://arxiv.org/abs/2512.24625) · [PDF](https://arxiv.org/pdf/2512.24625.pdf)  
**作者**：Zijian Zhao, Yitong Shang, Sen Li  

**一句话要点**：提出AutoFed联邦学习框架，通过个性化提示实现免手动调参的交通预测。

**关键词**：联邦学习, 交通预测, 个性化学习, 提示学习, 非独立同分布数据, 免手动调参

## 3 点简述
- 核心问题：联邦学习中非独立同分布数据导致交通预测性能受限，且现有方法依赖手动超参数调优。
- 方法要点：引入联邦表示器，使用客户端对齐适配器将本地数据蒸馏为共享提示矩阵，驱动个性化预测器。
- 实验或效果：在真实数据集上验证，AutoFed在多种场景下均表现优异，代码已开源。

## 摘要（原文）

> Accurate traffic prediction is essential for Intelligent Transportation Systems, including ride-hailing, urban road planning, and vehicle fleet management. However, due to significant privacy concerns surrounding traffic data, most existing methods rely on local training, resulting in data silos and limited knowledge sharing. Federated Learning (FL) offers an efficient solution through privacy-preserving collaborative training; however, standard FL struggles with the non-independent and identically distributed (non-IID) problem among clients. This challenge has led to the emergence of Personalized Federated Learning (PFL) as a promising paradigm. Nevertheless, current PFL frameworks require further adaptation for traffic prediction tasks, such as specialized graph feature engineering, data processing, and network architecture design. A notable limitation of many prior studies is their reliance on hyper-parameter optimization across datasets-information that is often unavailable in real-world scenarios-thus impeding practical deployment. To address this challenge, we propose AutoFed, a novel PFL framework for traffic prediction that eliminates the need for manual hyper-parameter tuning. Inspired by prompt learning, AutoFed introduces a federated representor that employs a client-aligned adapter to distill local data into a compact, globally shared prompt matrix. This prompt then conditions a personalized predictor, allowing each client to benefit from cross-client knowledge while maintaining local specificity. Extensive experiments on real-world datasets demonstrate that AutoFed consistently achieves superior performance across diverse scenarios. The code of this paper is provided at https://github.com/RS2002/AutoFed .

