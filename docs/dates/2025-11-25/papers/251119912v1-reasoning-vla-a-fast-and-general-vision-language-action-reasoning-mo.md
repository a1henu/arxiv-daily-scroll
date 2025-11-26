---
layout: default
title: Reasoning-VLA: A Fast and General Vision-Language-Action Reasoning Model for Autonomous Driving
---

# Reasoning-VLA: A Fast and General Vision-Language-Action Reasoning Model for Autonomous Driving
**arXiv**：[2511.19912v1](https://arxiv.org/abs/2511.19912) · [PDF](https://arxiv.org/pdf/2511.19912.pdf)  
**作者**：Dapeng Zhang, Zhenlong Yuan, Zhangquan Chen, Chih-Ting Liao, Yinda Chen, Fei Shen, Qingguo Zhou, Tat-Seng Chua  

**一句话要点**：提出Reasoning-VLA以解决自动驾驶中推理效率低和泛化能力差的问题

**关键词**：自动驾驶, 视觉语言动作模型, 推理增强, 动作轨迹生成, 泛化能力, 快速推理

## 3 点简述
- 现有VLA模型在自动驾驶中推理效率低且难以泛化到新场景和车辆配置
- 使用可学习动作查询与推理增强特征并行生成连续动作轨迹
- 整合多数据集训练，在多个基准测试中实现最优性能和快速推理

## 摘要（原文）

> Vision-Language-Action (VLA) models have recently shown strong decision-making capabilities in autonomous driving. However, existing VLAs often struggle with achieving efficient inference and generalizing to novel autonomous vehicle configurations and driving scenarios. In this paper, we propose Reasoning-VLA, a general and fast action-generation VLA framework. The proposed model employs a set of learnable action queries, initialized via Gaussian sampling from ground-truth trajectories within the training corpus. These learnable queries interact with reasoning-enhanced vision-language features to generate continuous action trajectories in parallel. To promote robust generalization, we consolidate eight publicly available autonomous driving datasets into a standardized, Chain-of-Thought reasoning-based, and easy-to-use data format for model training. Leveraging both supervised learning and reinforcement learning fine-tuning, extensive empirical evaluations across multiple benchmarks demonstrate that Reasoning-VLA achieves state-of-the-art performance, superior generalization capability, and the excellent inference speed reported to date.

