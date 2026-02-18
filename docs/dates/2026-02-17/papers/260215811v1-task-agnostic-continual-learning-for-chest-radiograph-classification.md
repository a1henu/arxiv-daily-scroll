---
layout: default
title: Task-Agnostic Continual Learning for Chest Radiograph Classification
---

# Task-Agnostic Continual Learning for Chest Radiograph Classification
**arXiv**：[2602.15811v1](https://arxiv.org/abs/2602.15811) · [PDF](https://arxiv.org/pdf/2602.15811.pdf)  
**作者**：Muthu Subash Kavitha, Anas Zafar, Amgad Muneer, Jia Wu  

**一句话要点**：提出CARL-XRay框架以解决胸片分类中任务不可知持续学习问题

**关键词**：胸片分类, 持续学习, 任务不可知学习, 适配器路由, 特征回放, 临床部署

## 3 点简述
- 核心问题：胸片分类模型需在不重训旧数据或性能退化下，适应新数据集序列，且推理时任务标识未知。
- 方法要点：采用固定主干网络，增量分配轻量任务特定适配器和分类头，结合原型和特征回放进行任务选择与适应。
- 实验或效果：在大规模公开数据集上，优于联合训练，路由准确率75.0%，AUROC达0.75，参数更少。

## 摘要（原文）

> Clinical deployment of chest radiograph classifiers requires models that can be updated as new datasets become available without retraining on previously ob- served data or degrading validated performance. We study, for the first time, a task-incremental continual learning setting for chest radiograph classification, in which heterogeneous chest X-ray datasets arrive sequentially and task identifiers are unavailable at inference. We propose a continual adapter-based routing learning strategy for Chest X-rays (CARL-XRay) that maintains a fixed high-capacity backbone and incrementally allocates lightweight task-specific adapters and classifier heads. A latent task selector operates on task-adapted features and leverages both current and historical context preserved through compact prototypes and feature-level experience replay. This design supports stable task identification and adaptation across sequential updates while avoiding raw-image storage. Experiments on large-scale public chest radiograph datasets demonstrate robust performance retention and reliable task-aware inference under continual dataset ingestion. CARL-XRay outperforms joint training under task-unknown deployment, achieving higher routing accuracy (75.0\% vs.\ 62.5\%), while maintaining competitive diagnostic performance with AUROC of 0.74 in the oracle setting with ground-truth task identity and 0.75 under task-unknown inference, using significantly fewer trainable parameters. Finally, the proposed framework provides a practical alternative to joint training and repeated full retraining in continual clinical deployment.

