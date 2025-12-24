---
layout: default
title: FedDPC : Handling Data Heterogeneity and Partial Client Participation in Federated Learning
---

# FedDPC : Handling Data Heterogeneity and Partial Client Participation in Federated Learning
**arXiv**：[2512.20329v1](https://arxiv.org/abs/2512.20329) · [PDF](https://arxiv.org/pdf/2512.20329.pdf)  
**作者**：Mrinmay Sen, Subhrajit Nag  

**一句话要点**：提出FedDPC以解决联邦学习中数据异构性和部分客户端参与问题

**关键词**：联邦学习, 数据异构性, 部分客户端参与, 模型更新方差控制, 自适应缩放, 图像分类

## 3 点简述
- 核心问题：数据异构性和部分客户端参与导致模型更新方差大，影响全局模型收敛和性能。
- 方法要点：通过将本地更新投影到前一轮全局更新来控制方差，并采用自适应缩放加速训练。
- 实验或效果：在图像分类任务中验证，FedDPC优于现有方法，实现更快损失下降和更高测试准确率。

## 摘要（原文）

> Data heterogeneity is a significant challenge in modern federated learning (FL) as it creates variance in local model updates, causing the aggregated global model to shift away from the true global optimum. Partial client participation in FL further exacerbates this issue by skewing the aggregation of local models towards the data distribution of participating clients. This creates additional variance in the global model updates, causing the global model to converge away from the optima of the global objective. These variances lead to instability in FL training, which degrades global model performance and slows down FL training. While existing literature primarily focuses on addressing data heterogeneity, the impact of partial client participation has received less attention. In this paper, we propose FedDPC, a novel FL method, designed to improve FL training and global model performance by mitigating both data heterogeneity and partial client participation. FedDPC addresses these issues by projecting each local update onto the previous global update, thereby controlling variance in both local and global updates. To further accelerate FL training, FedDPC employs adaptive scaling for each local update before aggregation. Extensive experiments on image classification tasks with multiple heterogeneously partitioned datasets validate the effectiveness of FedDPC. The results demonstrate that FedDPC outperforms state-of-the-art FL algorithms by achieving faster reduction in training loss and improved test accuracy across communication rounds.

