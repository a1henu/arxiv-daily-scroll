---
layout: default
title: Heterogeneity-Aware Client Selection Methodology For Efficient Federated Learning
---

# Heterogeneity-Aware Client Selection Methodology For Efficient Federated Learning
**arXiv**：[2602.20450v1](https://arxiv.org/abs/2602.20450) · [PDF](https://arxiv.org/pdf/2602.20450.pdf)  
**作者**：Nihal Balivada, Shrey Gupta, Shashank Shreedhar Bhatt, Suyash Gupta  

**一句话要点**：提出Terraform方法以解决联邦学习中统计异构性导致的精度下降问题

**关键词**：联邦学习, 客户端选择, 统计异构性, 梯度更新, 确定性算法, 模型精度

## 3 点简述
- 核心问题：联邦学习中客户端数据统计异构性导致全局模型精度低于传统机器学习
- 方法要点：使用梯度更新和确定性选择算法，选择异构客户端进行重训练
- 实验或效果：相比先前工作，精度提升最高达47%，并通过消融研究和训练时间分析验证效率

## 摘要（原文）

> Federated Learning (FL) enables a distributed client-server architecture where multiple clients collaboratively train a global Machine Learning (ML) model without sharing sensitive local data. However, FL often results in lower accuracy than traditional ML algorithms due to statistical heterogeneity across clients. Prior works attempt to address this by using model updates, such as loss and bias, from client models to select participants that can improve the global model's accuracy. However, these updates neither accurately represent a client's heterogeneity nor are their selection methods deterministic. We mitigate these limitations by introducing Terraform, a novel client selection methodology that uses gradient updates and a deterministic selection algorithm to select heterogeneous clients for retraining. This bi-pronged approach allows Terraform to achieve up to 47 percent higher accuracy over prior works. We further demonstrate its efficiency through comprehensive ablation studies and training time analyses, providing strong justification for the robustness of Terraform.

