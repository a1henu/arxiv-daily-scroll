---
layout: default
title: Multi-view Phase-aware Pedestrian-Vehicle Incident Reasoning Framework with Vision-Language Models
---

# Multi-view Phase-aware Pedestrian-Vehicle Incident Reasoning Framework with Vision-Language Models
**arXiv**：[2511.14120v1](https://arxiv.org/abs/2511.14120) · [PDF](https://arxiv.org/pdf/2511.14120.pdf)  
**作者**：Hao Zhen, Yunxiang Yang, Jidong J. Yang  

**一句话要点**：提出多视角阶段感知行人-车辆事故推理框架，以提升城市交通安全分析

**关键词**：多视角视频分析, 行人行为阶段分割, 视觉语言模型, 事故推理, 交通安全诊断

## 3 点简述
- 核心问题：现有视频系统难以解析行人行为认知阶段，限制事故因果分析。
- 方法要点：框架分四阶段处理多视角视频，集成专用视觉语言模型进行阶段分割与分析。
- 实验或效果：在Woven数据集上验证，能生成可操作报告，问答准确率达64.70%。

## 摘要（原文）

> Pedestrian-vehicle incidents remain a critical urban safety challenge, with pedestrians accounting for over 20% of global traffic fatalities. Although existing video-based systems can detect when incidents occur, they provide little insight into how these events unfold across the distinct cognitive phases of pedestrian behavior. Recent vision-language models (VLMs) have shown strong potential for video understanding, but they remain limited in that they typically process videos in isolation, without explicit temporal structuring or multi-view integration. This paper introduces Multi-view Phase-aware Pedestrian-Vehicle Incident Reasoning (MP-PVIR), a unified framework that systematically processes multi-view video streams into structured diagnostic reports through four stages: (1) event-triggered multi-view video acquisition, (2) pedestrian behavior phase segmentation, (3) phase-specific multi-view reasoning, and (4) hierarchical synthesis and diagnostic reasoning. The framework operationalizes behavioral theory by automatically segmenting incidents into cognitive phases, performing synchronized multi-view analysis within each phase, and synthesizing results into causal chains with targeted prevention strategies. Particularly, two specialized VLMs underpin the MP-PVIR pipeline: TG-VLM for behavioral phase segmentation (mIoU = 0.4881) and PhaVR-VLM for phase-aware multi-view analysis, achieving a captioning score of 33.063 and up to 64.70% accuracy on question answering. Finally, a designated large language model is used to generate comprehensive reports detailing scene understanding, behavior interpretation, causal reasoning, and prevention recommendations. Evaluation on the Woven Traffic Safety dataset shows that MP-PVIR effectively translates multi-view video data into actionable insights, advancing AI-driven traffic safety analytics for vehicle-infrastructure cooperative systems.

