---
layout: default
title: Communication-Efficient Federated Risk Difference Estimation for Time-to-Event Clinical Outcomes
---

# Communication-Efficient Federated Risk Difference Estimation for Time-to-Event Clinical Outcomes
**arXiv**：[2601.14609v1](https://arxiv.org/abs/2601.14609) · [PDF](https://arxiv.org/pdf/2601.14609.pdf)  
**作者**：Ziwen Wang, Siqi Li, Marcus Eng Hock Ong, Nan Liu  

**一句话要点**：提出FedRD框架以解决隐私受限多中心临床研究中绝对风险估计的通信效率问题

**关键词**：联邦学习, 生存分析, 风险差估计, 通信效率, 隐私保护, 临床研究

## 3 点简述
- 核心问题：隐私保护模型协同训练在医疗研究中受限于服务器依赖架构和缺乏临床可解释性的相对效应度量
- 方法要点：FedRD为分布式生存数据提供服务器无关的联邦风险差估计，通信轮次少，支持置信区间和假设检验
- 实验或效果：理论证明FedRD渐近等价于个体级分析，仿真和真实应用显示其在估计准确性和预测性能上优于基线

## 摘要（原文）

> Privacy-preserving model co-training in medical research is often hindered by server-dependent architectures incompatible with protected hospital data systems and by the predominant focus on relative effect measures (hazard ratios) which lack clinical interpretability for absolute survival risk assessment. We propose FedRD, a communication-efficient framework for federated risk difference estimation in distributed survival data. Unlike typical federated learning frameworks (e.g., FedAvg) that require persistent server connections and extensive iterative communication, FedRD is server-independent with minimal communication: one round of summary statistics exchange for the stratified model and three rounds for the unstratified model. Crucially, FedRD provides valid confidence intervals and hypothesis testing--capabilities absent in FedAvg-based frameworks. We provide theoretical guarantees by establishing the asymptotic properties of FedRD and prove that FedRD (unstratified) is asymptotically equivalent to pooled individual-level analysis. Simulation studies and real-world clinical applications across different countries demonstrate that FedRD outperforms local and federated baselines in both estimation accuracy and prediction performance, providing an architecturally feasible solution for absolute risk assessment in privacy-restricted, multi-site clinical studies.

