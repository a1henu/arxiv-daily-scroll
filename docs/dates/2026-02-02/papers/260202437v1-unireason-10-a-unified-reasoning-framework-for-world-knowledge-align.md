---
layout: default
title: UniReason 1.0: A Unified Reasoning Framework for World Knowledge Aligned Image Generation and Editing
---

# UniReason 1.0: A Unified Reasoning Framework for World Knowledge Aligned Image Generation and Editing
**arXiv**：[2602.02437v1](https://arxiv.org/abs/2602.02437) · [PDF](https://arxiv.org/pdf/2602.02437.pdf)  
**作者**：Dianyi Wang, Chaofan Ma, Feng Han, Size Wu, Wei Song, Yibin Wang, Zhixiong Zhang, Tianhang Wang, Siyuan Wang, Zhongyu Wei, Jiaqi Wang  

**一句话要点**：提出UniReason统一框架，通过双推理范式解决多模态模型在复杂合成任务中推理不足的问题。

**关键词**：统一推理框架, 世界知识对齐, 图像生成与编辑, 双推理范式, 视觉自校正

## 3 点简述
- 核心问题：多模态模型在需要深度推理的复杂合成任务中表现不佳，且常将文本到图像生成和图像编辑视为孤立能力。
- 方法要点：采用世界知识增强规划进行生成，并利用编辑能力进行视觉自校正，统一两者于共享表示中。
- 实验或效果：在WISE、KrisBench和UniREditBench等推理密集型基准上取得先进性能，同时保持优越的通用合成能力。

## 摘要（原文）

> Unified multimodal models often struggle with complex synthesis tasks that demand deep reasoning, and typically treat text-to-image generation and image editing as isolated capabilities rather than interconnected reasoning steps. To address this, we propose UniReason, a unified framework that harmonizes these two tasks through a dual reasoning paradigm. We formulate generation as world knowledge-enhanced planning to inject implicit constraints, and leverage editing capabilities for fine-grained visual refinement to further correct visual errors via self-reflection. This approach unifies generation and editing within a shared representation, mirroring the human cognitive process of planning followed by refinement. We support this framework by systematically constructing a large-scale reasoning-centric dataset (~300k samples) covering five major knowledge domains (e.g., cultural commonsense, physics, etc.) for planning, alongside an agent-generated corpus for visual self-correction. Extensive experiments demonstrate that UniReason achieves advanced performance on reasoning-intensive benchmarks such as WISE, KrisBench and UniREditBench, while maintaining superior general synthesis capabilities.

