---
layout: default
title: Scaling Foundation Models for Radar Scene Understanding
---

# Scaling Foundation Models for Radar Scene Understanding
**arXiv**：[2511.21105v1](https://arxiv.org/abs/2511.21105) · [PDF](https://arxiv.org/pdf/2511.21105.pdf)  
**作者**：Pushkal Mishra, Kshitiz Bansal, Dinesh Bharadia  

**一句话要点**：提出RadarFM雷达基础模型，通过结构化语言监督统一场景表示以解决任务碎片化问题。

**关键词**：雷达基础模型, 结构化语言监督, 对比学习, 场景理解, 自动驾驶模拟, 空间定位指标

## 3 点简述
- 雷达感知在恶劣条件下可靠，但现有方法任务特定，缺乏跨任务迁移能力。
- 采用结构化字幕框架和哈希感知对比学习，实现连续场景相似性量化与精细空间推理。
- 利用CARLA模拟器生成大规模数据集，并引入定位感知指标评估空间准确性。

## 摘要（原文）

> Radar sensors provide reliable perception across adverse weather, lighting, and long-range conditions. Recent advances in foundation models have transformed visual and language understanding, yet their integration with radar sensing remains largely underexplored. Existing radar approaches are fragmented and task-specific; each downstream task employs distinct architectures and training objectives, preventing transfer across tasks. In this work, we introduce RadarFM: a radar foundation model that learns unified scene-level representations through structured spatial language supervision. We make two key contributions: (1) a structured caption framework that encodes vehicle distributions in native radar coordinates, and (2) a hash-aware contrastive learning objective that quantifies continuous scene similarity rather than binary matching, enabling fine-grained spatial reasoning. Leveraging the CARLA simulator, we generate large-scale, well-annotated radar datasets across diverse driving scenarios. We also propose localization-aware metrics that assess spatial accuracy beyond traditional detection measures.

