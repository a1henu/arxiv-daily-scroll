---
layout: default
title: BOFA: Bridge-Layer Orthogonal Low-Rank Fusion for CLIP-Based Class-Incremental Learning
---

# BOFA: Bridge-Layer Orthogonal Low-Rank Fusion for CLIP-Based Class-Incremental Learning
**arXiv**：[2511.11421v1](https://arxiv.org/abs/2511.11421) · [PDF](https://arxiv.org/pdf/2511.11421.pdf)  
**作者**：Lan Li, Tao Hu, Da-Wei Zhou, Han-Jia Ye, De-Chuan Zhan  

**一句话要点**：提出BOFA框架以解决CLIP在类增量学习中的遗忘与模态融合问题

**关键词**：类增量学习, CLIP模型, 正交低秩融合, 多模态融合, 桥接层适应, 无回放学习

## 3 点简述
- 核心问题：CLIP应用于类增量学习时，额外模块增加复杂性且易遗忘，多模态潜力未充分挖掘
- 方法要点：仅在CLIP桥接层进行正交低秩融合，无额外参数，约束更新至安全子空间防遗忘
- 实验或效果：标准基准测试显示BOFA在准确性和效率上优于现有方法，无需数据回放

## 摘要（原文）

> Class-Incremental Learning (CIL) aims to continually learn new categories without forgetting previously acquired knowledge. Vision-language models such as CLIP offer strong transferable representations via multi-modal supervision, making them promising for CIL. However, applying CLIP to CIL poses two major challenges: (1) adapting to downstream tasks often requires additional learnable modules, increasing model complexity and susceptibility to forgetting; and (2) while multi-modal representations offer complementary strengths, existing methods have yet to fully realize their potential in effectively integrating visual and textual modalities. To address these issues, we propose BOFA (Bridge-layer Orthogonal Fusion for Adaptation), a novel framework for CIL. BOFA confines all model adaptation exclusively to CLIP's existing cross-modal bridge-layer, thereby adding no extra parameters or inference cost. To prevent forgetting within this layer, it leverages Orthogonal Low-Rank Fusion, a mechanism that constrains parameter updates to a low-rank ``safe subspace" mathematically constructed to be orthogonal to past task features. This ensures stable knowledge accumulation without data replay. Furthermore, BOFA employs a cross-modal hybrid prototype that synergizes stable textual prototypes with visual counterparts derived from our stably adapted bridge-layer, enhancing classification performance. Extensive experiments on standard benchmarks show that BOFA achieves superior accuracy and efficiency compared to existing methods.

