---
layout: default
title: Human-AI Divergence in Ego-centric Action Recognition under Spatial and Spatiotemporal Manipulations
---

# Human-AI Divergence in Ego-centric Action Recognition under Spatial and Spatiotemporal Manipulations
**arXiv**：[2603.08317v1](https://arxiv.org/abs/2603.08317) · [PDF](https://arxiv.org/pdf/2603.08317.pdf)  
**作者**：Sadegh Rahmaniboldaji, Filip Rybansky, Quoc C. Vuong, Anya C. Hurlbert, Frank Guerin, Andrew Gilbert  

**一句话要点**：提出基于最小可识别裁剪的人机对比研究，揭示在空间与时空扰动下自我中心动作识别的性能差异

**关键词**：自我中心动作识别, 人机对比, 最小可识别裁剪, 时空扰动, 手物交互, 性能差距分析

## 3 点简述
- 核心问题：人类在动作识别中优于AI，尤其在低分辨率、遮挡等挑战条件下，需探究性能差距来源
- 方法要点：使用Epic ReduAct数据集，通过空间裁剪和时序打乱生成最小可识别区域，结合定量指标和定性分析
- 实验或效果：人类依赖稀疏语义线索如手物交互，模型更依赖上下文和中低层特征，对时空扰动敏感性不同

## 摘要（原文）

> Humans consistently outperform state-of-the-art AI models in action recognition, particularly in challenging real-world conditions involving low resolution, occlusion, and visual clutter. Understanding the sources of this performance gap is essential for developing more robust and human-aligned models. In this paper, we present a large-scale human-AI comparative study of egocentric action recognition using Minimal Identifiable Recognition Crops (MIRCs), defined as the smallest spatial or spatiotemporal regions sufficient for reliable human recognition. We used our previously introduced, Epic ReduAct, a systematically spatially reduced and temporally scrambled dataset derived from 36 EPIC KITCHENS videos, spanning multiple spatial reduction levels and temporal conditions. Recognition performance is evaluated using over 3,000 human participants and the Side4Video model. Our analysis combines quantitative metrics, Average Reduction Rate and Recognition Gap, with qualitative analyses of spatial (high-, mid-, and low-level visual features) and spatiotemporal factors, including a categorisation of actions into Low Temporal Actions (LTA) and High Temporal Actions (HTA). Results show that human performance exhibits sharp declines when transitioning from MIRCs to subMIRCs, reflecting a strong reliance on sparse, semantically critical cues such as hand-object interactions. In contrast, the model degrades more gradually and often relies on contextual and mid- to low-level features, sometimes even exhibiting increased confidence under spatial reduction. Temporally, humans remain robust to scrambling when key spatial cues are preserved, whereas the model often shows insensitivity to temporal disruption, revealing class-dependent temporal sensitivities.

