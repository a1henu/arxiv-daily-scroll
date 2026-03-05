---
layout: default
title: Structure-Aware Distributed Backdoor Attacks in Federated Learning
---

# Structure-Aware Distributed Backdoor Attacks in Federated Learning
**arXiv**：[2603.03865v1](https://arxiv.org/abs/2603.03865) · [PDF](https://arxiv.org/pdf/2603.03865.pdf)  
**作者**：Wang Jian, Shen Hong, Ke Wei, Liu Xue Hua  

**一句话要点**：提出结构感知分形扰动注入框架以分析联邦学习中模型架构对后门攻击的影响

**关键词**：联邦学习, 后门攻击, 模型架构, 结构感知, 分形扰动, 防御设计

## 3 点简述
- 核心问题：现有研究忽略模型架构对后门扰动有效性的影响，假设相同扰动在不同架构中行为相似
- 方法要点：引入结构响应分数和结构兼容系数度量模型对扰动的敏感性和偏好，开发结构感知分形扰动注入框架
- 实验或效果：实验表明模型架构显著影响扰动传播与聚合，多路径特征融合网络能放大分形扰动，结构兼容系数与攻击成功率强相关

## 摘要（原文）

> While federated learning protects data privacy, it also makes the model update process vulnerable to long-term stealthy perturbations. Existing studies on backdoor attacks in federated learning mainly focus on trigger design or poisoning strategies, typically assuming that identical perturbations behave similarly across different model architectures. This assumption overlooks the impact of model structure on perturbation effectiveness. From a structure-aware perspective, this paper analyzes the coupling relationship between model architectures and backdoor perturbations. We introduce two metrics, Structural Responsiveness Score (SRS) and Structural Compatibility Coefficient (SCC), to measure a model's sensitivity to perturbations and its preference for fractal perturbations. Based on these metrics, we develop a structure-aware fractal perturbation injection framework (TFI) to study the role of architectural properties in the backdoor injection process. Experimental results show that model architecture significantly influences the propagation and aggregation of perturbations. Networks with multi-path feature fusion can amplify and retain fractal perturbations even under low poisoning ratios, while models with low structural compatibility constrain their effectiveness. Further analysis reveals a strong correlation between SCC and attack success rate, suggesting that SCC can predict perturbation survivability. These findings highlight that backdoor behaviors in federated learning depend not only on perturbation design or poisoning intensity but also on the interaction between model architecture and aggregation mechanisms, offering new insights for structure-aware defense design.

