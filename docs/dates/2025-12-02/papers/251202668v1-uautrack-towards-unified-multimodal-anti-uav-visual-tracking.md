---
layout: default
title: UAUTrack: Towards Unified Multimodal Anti-UAV Visual Tracking
---

# UAUTrack: Towards Unified Multimodal Anti-UAV Visual Tracking
**arXiv**：[2512.02668v1](https://arxiv.org/abs/2512.02668) · [PDF](https://arxiv.org/pdf/2512.02668.pdf)  
**作者**：Qionglin Ren, Dawei Zhang, Chunxu Tian, Dan Zhang  

**一句话要点**：提出UAUTrack统一框架以解决反无人机多模态跟踪中的跨模态协作问题

**关键词**：反无人机跟踪, 多模态融合, 统一框架, 文本先验提示, 单流架构, 端到端学习

## 3 点简述
- 核心问题：反无人机跟踪缺乏统一框架，现有方法忽视跨模态信息共享，多模态融合效果不佳
- 方法要点：基于单流单阶段端到端架构，引入文本先验提示策略，有效整合RGB、TIR等多模态数据
- 实验或效果：在Anti-UAV和DUT Anti-UAV数据集上达到最先进性能，在Anti-UAV410数据集上平衡精度与速度

## 摘要（原文）

> Research in Anti-UAV (Unmanned Aerial Vehicle) tracking has explored various modalities, including RGB, TIR, and RGB-T fusion. However, a unified framework for cross-modal collaboration is still lacking. Existing approaches have primarily focused on independent models for individual tasks, often overlooking the potential for cross-modal information sharing. Furthermore, Anti-UAV tracking techniques are still in their infancy, with current solutions struggling to achieve effective multimodal data fusion. To address these challenges, we propose UAUTrack, a unified single-target tracking framework built upon a single-stream, single-stage, end-to-end architecture that effectively integrates multiple modalities. UAUTrack introduces a key component: a text prior prompt strategy that directs the model to focus on UAVs across various scenarios. Experimental results show that UAUTrack achieves state-of-the-art performance on the Anti-UAV and DUT Anti-UAV datasets, and maintains a favourable trade-off between accuracy and speed on the Anti-UAV410 dataset, demonstrating both high accuracy and practical efficiency across diverse Anti-UAV scenarios.

