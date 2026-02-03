---
layout: default
title: UV-M3TL: A Unified and Versatile Multimodal Multi-Task Learning Framework for Assistive Driving Perception
---

# UV-M3TL: A Unified and Versatile Multimodal Multi-Task Learning Framework for Assistive Driving Perception
**arXiv**：[2602.01594v1](https://arxiv.org/abs/2602.01594) · [PDF](https://arxiv.org/pdf/2602.01594.pdf)  
**作者**：Wenzhuo Liu, Qiannan Guo, Zhen Wang, Wenshuo Wang, Lei Yang, Yicheng Qiao, Lening Wang, Zhiwei Li, Chen Lv, Shanghang Zhang, Junqiang Xi, Huaping Liu  

**一句话要点**：提出UV-M3TL框架以解决辅助驾驶感知中多任务学习的负迁移问题

**关键词**：多任务学习, 辅助驾驶感知, 负迁移缓解, 多模态嵌入, 自适应损失, 统一框架

## 3 点简述
- 核心问题：辅助驾驶系统需同时感知驾驶员行为、情绪、车辆行为和交通环境，但多任务联合学习易导致任务间负迁移，降低性能。
- 方法要点：采用双分支空间通道多模态嵌入（DB-SCME）显式建模任务共享与特定特征，结合自适应特征解耦多任务损失（AFD-Loss）优化学习过程。
- 实验或效果：在AIDE数据集上实现四项任务的最优性能，并在多个公开基准测试中验证了框架的通用性和强性能。

## 摘要（原文）

> Advanced Driver Assistance Systems (ADAS) need to understand human driver behavior while perceiving their navigation context, but jointly learning these heterogeneous tasks would cause inter-task negative transfer and impair system performance. Here, we propose a Unified and Versatile Multimodal Multi-Task Learning (UV-M3TL) framework to simultaneously recognize driver behavior, driver emotion, vehicle behavior, and traffic context, while mitigating inter-task negative transfer. Our framework incorporates two core components: dual-branch spatial channel multimodal embedding (DB-SCME) and adaptive feature-decoupled multi-task loss (AFD-Loss). DB-SCME enhances cross-task knowledge transfer while mitigating task conflicts by employing a dual-branch structure to explicitly model salient task-shared and task-specific features. AFD-Loss improves the stability of joint optimization while guiding the model to learn diverse multi-task representations by introducing an adaptive weighting mechanism based on learning dynamics and feature decoupling constraints. We evaluate our method on the AIDE dataset, and the experimental results demonstrate that UV-M3TL achieves state-of-the-art performance across all four tasks. To further prove the versatility, we evaluate UV-M3TL on additional public multi-task perception benchmarks (BDD100K, CityScapes, NYUD-v2, and PASCAL-Context), where it consistently delivers strong performance across diverse task combinations, attaining state-of-the-art results on most tasks.

