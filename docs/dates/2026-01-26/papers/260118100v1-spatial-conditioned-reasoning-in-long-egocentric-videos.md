---
layout: default
title: Spatial-Conditioned Reasoning in Long-Egocentric Videos
---

# Spatial-Conditioned Reasoning in Long-Egocentric Videos
**arXiv**：[2601.18100v1](https://arxiv.org/abs/2601.18100) · [PDF](https://arxiv.org/pdf/2601.18100.pdf)  
**作者**：James Tribble, Hao Wang, Si-En Hong, Chaoyi Zhou, Ashish Bastola, Siyu Huang, Abolfazl Razi  

**一句话要点**：提出Sanpo-D数据集与深度融合方法，以增强长视角视频中的空间推理能力

**关键词**：长视角视频, 空间推理, 视觉语言模型, 深度融合, 数据集标注, 安全关键任务

## 3 点简述
- 核心问题：长视角视频因视角漂移和几何上下文缺失，导致视觉导航和空间推理困难
- 方法要点：通过融合深度图与RGB帧，在不修改模型架构下提升视觉语言模型的空间推理性能
- 实验或效果：基准测试显示深度感知表示能改善行人检测等安全关键任务，但存在通用性与空间专业化权衡

## 摘要（原文）

> Long-horizon egocentric video presents significant challenges for visual navigation due to viewpoint drift and the absence of persistent geometric context. Although recent vision-language models perform well on image and short-video reasoning, their spatial reasoning capability in long egocentric sequences remains limited. In this work, we study how explicit spatial signals influence VLM-based video understanding without modifying model architectures or inference procedures. We introduce Sanpo-D, a fine-grained re-annotation of the Google Sanpo dataset, and benchmark multiple VLMs on navigation-oriented spatial queries. To examine input-level inductive bias, we further fuse depth maps with RGB frames and evaluate their impact on spatial reasoning. Our results reveal a trade-off between general-purpose accuracy and spatial specialization, showing that depth-aware and spatially grounded representations can improve performance on safety-critical tasks such as pedestrian and obstruction detection.

