---
layout: default
title: FedARKS: Federated Aggregation via Robust and Discriminative Knowledge Selection and Integration for Person Re-identification
---

# FedARKS: Federated Aggregation via Robust and Discriminative Knowledge Selection and Integration for Person Re-identification
**arXiv**：[2603.06122v1](https://arxiv.org/abs/2603.06122) · [PDF](https://arxiv.org/pdf/2603.06122.pdf)  
**作者**：Xin Xu, Binchang Ma, Zhixi Yu, Wei Liu  

**一句话要点**：提出FedARKS框架，通过鲁棒知识选择与集成解决联邦域泛化行人重识别中的特征与聚合问题

**关键词**：联邦学习, 域泛化, 行人重识别, 知识选择, 鲁棒特征提取

## 3 点简述
- 核心问题：现有方法依赖全局特征和平均聚合，难以捕获局部细节且忽略客户端差异，影响域泛化能力
- 方法要点：引入鲁棒知识（RK）机制增强局部特征提取，结合知识选择（KS）机制差异化聚合客户端模型
- 实验或效果：未知，但旨在提升模型在未见域的泛化性能，同时保护数据隐私

## 摘要（原文）

> The application of federated domain generalization in person re-identification (FedDG-ReID) aims to enhance the model's generalization ability in unseen domains while protecting client data privacy. However, existing mainstream methods typically rely on global feature representations and simple averaging operations for model aggregation, leading to two limitations in domain generalization: (1) Using only global features makes it difficult to capture subtle, domain-invariant local details (such as accessories or textures); (2) Uniform parameter averaging treats all clients as equivalent, ignoring their differences in robust feature extraction capabilities, thereby diluting the contributions of high quality clients. To address these issues, we propose a novel federated learning framework, Federated Aggregation via Robust and Discriminative Knowledge Selection and Integration (FedARKS), comprising two mechanisms: RK (Robust Knowledge) and KS (Knowledge Selection).

