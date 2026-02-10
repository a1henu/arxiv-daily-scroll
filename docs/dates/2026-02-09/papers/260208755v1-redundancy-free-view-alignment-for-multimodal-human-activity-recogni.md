---
layout: default
title: Redundancy-Free View Alignment for Multimodal Human Activity Recognition with Arbitrarily Missing Views
---

# Redundancy-Free View Alignment for Multimodal Human Activity Recognition with Arbitrarily Missing Views
**arXiv**：[2602.08755v1](https://arxiv.org/abs/2602.08755) · [PDF](https://arxiv.org/pdf/2602.08755.pdf)  
**作者**：Duc-Anh Nguyen, Nhien-An Le-Khac  

**一句话要点**：提出RALIS模型，通过调整中心对比损失和专家混合模块，解决多模态人类活动识别中任意视图缺失的冗余问题。

**关键词**：多模态学习, 视图对齐, 对比学习, 专家混合, 人类活动识别, 缺失视图处理

## 3 点简述
- 核心问题：现有方法难以处理任意视图组合、数量和异质模态的灵活配置，影响多视图融合效果。
- 方法要点：使用调整中心对比损失进行自监督表示学习和视图对齐，结合专家混合模块适应任意视图组合，降低计算复杂度。
- 实验或效果：在四个包含惯性和人体姿态模态的数据集上验证，视图数从三到九，展示性能和灵活性。

## 摘要（原文）

> Multimodal multiview learning seeks to integrate information from diverse sources to enhance task performance. Existing approaches often struggle with flexible view configurations, including arbitrary view combinations, numbers of views, and heterogeneous modalities. Focusing on the context of human activity recognition, we propose RALIS, a model that combines multiview contrastive learning with a mixture-of-experts module to support arbitrary view availability during both training and inference. Instead of trying to reconstruct missing views, an adjusted center contrastive loss is used for self-supervised representation learning and view alignment, mitigating the impact of missing views on multiview fusion. This loss formulation allows for the integration of view weights to account for view quality. Additionally, it reduces computational complexity from $O(V^2)$ to $O(V)$, where $V$ is the number of views. To address residual discrepancies not captured by contrastive learning, we employ a mixture-of-experts module with a specialized load balancing strategy, tasked with adapting to arbitrary view combinations. We highlight the geometric relationship among components in our model and how they combine well in the latent space. RALIS is validated on four datasets encompassing inertial and human pose modalities, with the number of views ranging from three to nine, demonstrating its performance and flexibility.

