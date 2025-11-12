---
layout: default
title: Foam Segmentation in Wastewater Treatment Plants: A Federated Learning Approach with Segment Anything Model 2
---

# Foam Segmentation in Wastewater Treatment Plants: A Federated Learning Approach with Segment Anything Model 2
**arXiv**：[2511.08130v1](https://arxiv.org/abs/2511.08130) · [PDF](https://arxiv.org/pdf/2511.08130.pdf)  
**作者**：Mehmet Batuhan Duman, Alejandro Carnero, Cristian Martín, Daniel Garrido, Manuel Díaz  

**一句话要点**：提出联邦学习与SAM2结合框架以解决污水处理厂泡沫分割中的数据隐私与稀缺问题

**关键词**：联邦学习, 图像分割, 污水处理, 隐私保护, 模型微调, 实时监测

## 3 点简述
- 污水处理厂泡沫形成降低效率，需实时监测但数据标注困难且隐私受限
- 采用联邦学习在分布式客户端微调SAM2，保护隐私并加速训练收敛
- 使用真实与合成数据集验证，提升分割性能并实现泛化应用

## 摘要（原文）

> Foam formation in Wastewater Treatment Plants (WTPs) is a major challenge that can reduce treatment efficiency and increase costs. The ability to automatically examine changes in real-time with respect to the percentage of foam can be of great benefit to the plant. However, large amounts of labeled data are required to train standard Machine Learning (ML) models. The development of these systems is slow due to the scarcity and heterogeneity of labeled data. Additionally, the development is often hindered by the fact that different WTPs do not share their data due to privacy concerns. This paper proposes a new framework to address these challenges by combining Federated Learning (FL) with the state-of-the-art base model for image segmentation, Segment Anything Model 2 (SAM2). The FL paradigm enables collaborative model training across multiple WTPs without centralizing sensitive operational data, thereby ensuring privacy. The framework accelerates training convergence and improves segmentation performance even with limited local datasets by leveraging SAM2's strong pre-trained weights for initialization. The methodology involves fine-tuning SAM2 on distributed clients (edge nodes) using the Flower framework, where a central Fog server orchestrates the process by aggregating model weights without accessing private data. The model was trained and validated using various data collections, including real-world images captured at a WTPs in Granada, Spain, a synthetically generated foam dataset, and images from publicly available datasets to improve generalization. This research offers a practical, scalable, and privacy-aware solution for automatic foam tracking in WTPs. The findings highlight the significant potential of integrating large-scale foundational models into FL systems to solve real-world industrial challenges characterized by distributed and sensitive data.

