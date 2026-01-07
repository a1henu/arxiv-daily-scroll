---
layout: default
title: ClearAIR: A Human-Visual-Perception-Inspired All-in-One Image Restoration
---

# ClearAIR: A Human-Visual-Perception-Inspired All-in-One Image Restoration
**arXiv**：[2601.02763v1](https://arxiv.org/abs/2601.02763) · [PDF](https://arxiv.org/pdf/2601.02763.pdf)  
**作者**：Xu Zhang, Huan Zhang, Guoli Wang, Qian Zhang, Lefei Zhang  

**一句话要点**：提出ClearAIR框架，基于人类视觉感知实现全场景图像恢复，解决复杂退化导致的过平滑和伪影问题。

**关键词**：全场景图像恢复, 人类视觉感知, 多模态质量评估, 区域感知恢复, 内部线索重用, 分层恢复策略

## 3 点简述
- 现有全场景图像恢复方法依赖退化特定表示，易导致过平滑和伪影。
- ClearAIR采用分层粗到细策略，结合MLLM质量评估、区域感知和内部线索重用机制。
- 实验显示在合成和真实数据集上性能优越，细节恢复显著增强。

## 摘要（原文）

> All-in-One Image Restoration (AiOIR) has advanced significantly, offering promising solutions for complex real-world degradations. However, most existing approaches rely heavily on degradation-specific representations, often resulting in oversmoothing and artifacts. To address this, we propose ClearAIR, a novel AiOIR framework inspired by Human Visual Perception (HVP) and designed with a hierarchical, coarse-to-fine restoration strategy. First, leveraging the global priority of early HVP, we employ a Multimodal Large Language Model (MLLM)-based Image Quality Assessment (IQA) model for overall evaluation. Unlike conventional IQA, our method integrates cross-modal understanding to more accurately characterize complex, composite degradations. Building upon this overall assessment, we then introduce a region awareness and task recognition pipeline. A semantic cross-attention, leveraging semantic guidance unit, first produces coarse semantic prompts. Guided by this regional context, a degradation-aware module implicitly captures region-specific degradation characteristics, enabling more precise local restoration. Finally, to recover fine details, we propose an internal clue reuse mechanism. It operates in a self-supervised manner to mine and leverage the intrinsic information of the image itself, substantially enhancing detail restoration. Experimental results show that ClearAIR achieves superior performance across diverse synthetic and real-world datasets.

