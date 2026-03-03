---
layout: default
title: Unifying Heterogeneous Multi-Modal Remote Sensing Detection Via Language-Pivoted Pretraining
---

# Unifying Heterogeneous Multi-Modal Remote Sensing Detection Via Language-Pivoted Pretraining
**arXiv**：[2603.01758v1](https://arxiv.org/abs/2603.01758) · [PDF](https://arxiv.org/pdf/2603.01758.pdf)  
**作者**：Yuxuan Li, Yuming Chen, Yunheng Li, Ming-Ming Cheng, Xiang Li, Jian Yang  

**一句话要点**：提出BabelRS框架，通过语言枢轴预训练统一异构多模态遥感检测。

**关键词**：多模态遥感检测, 语言枢轴预训练, 模态对齐, 异构传感器, 视觉语义融合, 对象检测

## 3 点简述
- 核心问题：异构多模态遥感检测中，模态对齐与下游任务优化耦合导致训练不稳定和泛化差。
- 方法要点：采用概念共享指令对齐和层级视觉语义退火，以语言为枢轴解耦模态对齐与任务学习。
- 实验或效果：实验表明BabelRS稳定训练，无需额外技巧即超越现有方法。

## 摘要（原文）

> Heterogeneous multi-modal remote sensing object detection aims to accurately detect objects from diverse sensors (e.g., RGB, SAR, Infrared). Existing approaches largely adopt a late alignment paradigm, in which modality alignment and task-specific optimization are entangled during downstream fine-tuning. This tight coupling complicates optimization and often results in unstable training and suboptimal generalization. To address these limitations, we propose BabelRS, a unified language-pivoted pretraining framework that explicitly decouples modality alignment from downstream task learning. BabelRS comprises two key components: Concept-Shared Instruction Aligning (CSIA) and Layerwise Visual-Semantic Annealing (LVSA). CSIA aligns each sensor modality to a shared set of linguistic concepts, using language as a semantic pivot to bridge heterogeneous visual representations. To further mitigate the granularity mismatch between high-level language representations and dense detection objectives, LVSA progressively aggregates multi-scale visual features to provide fine-grained semantic guidance. Extensive experiments demonstrate that BabelRS stabilizes training and consistently outperforms state-of-the-art methods without bells and whistles. Code: https://github.com/zcablii/SM3Det.

