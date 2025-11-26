---
layout: default
title: GazeProphetV2: Head-Movement-Based Gaze Prediction Enabling Efficient Foveated Rendering on Mobile VR
---

# GazeProphetV2: Head-Movement-Based Gaze Prediction Enabling Efficient Foveated Rendering on Mobile VR
**arXiv**：[2511.19988v1](https://arxiv.org/abs/2511.19988) · [PDF](https://arxiv.org/pdf/2511.19988.pdf)  
**作者**：Farhaan Ebadulla, Chiraag Mudlpaur, Shreya Chaurasia, Gaurav BV  

**一句话要点**：提出多模态方法结合头部运动预测VR注视，以优化移动VR渲染效率

**关键词**：虚拟现实注视预测, 多模态融合, 头部运动分析, 门控注意力机制, 渲染优化

## 3 点简述
- 核心问题：VR中注视行为预测困难，影响渲染优化和界面设计。
- 方法要点：融合时间注视模式、头部运动和视觉场景，使用门控融合与跨模态注意力。
- 实验或效果：在22个VR场景数据集上验证，多模态组合提升预测准确率至93.1%。

## 摘要（原文）

> Predicting gaze behavior in virtual reality environments remains a significant challenge with implications for rendering optimization and interface design. This paper introduces a multimodal approach to VR gaze prediction that combines temporal gaze patterns, head movement data, and visual scene information. By leveraging a gated fusion mechanism with cross-modal attention, the approach learns to adaptively weight gaze history, head movement, and scene content based on contextual relevance. Evaluations using a dataset spanning 22 VR scenes with 5.3M gaze samples demonstrate improvements in predictive accuracy when combining modalities compared to using individual data streams alone. The results indicate that integrating past gaze trajectories with head orientation and scene content enhances prediction accuracy across 1-3 future frames. Cross-scene generalization testing shows consistent performance with 93.1% validation accuracy and temporal consistency in predicted gaze trajectories. These findings contribute to understanding attention mechanisms in virtual environments while suggesting potential applications in rendering optimization, interaction design, and user experience evaluation. The approach represents a step toward more efficient virtual reality systems that can anticipate user attention patterns without requiring expensive eye tracking hardware.

