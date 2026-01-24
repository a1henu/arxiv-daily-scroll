---
layout: default
title: Region-aware Spatiotemporal Modeling with Collaborative Domain Generalization for Cross-Subject EEG Emotion Recognition
---

# Region-aware Spatiotemporal Modeling with Collaborative Domain Generalization for Cross-Subject EEG Emotion Recognition
**arXiv**：[2601.15615v1](https://arxiv.org/abs/2601.15615) · [PDF](https://arxiv.org/pdf/2601.15615.pdf)  
**作者**：Weiwei Wu, Yueyang Li, Yuhu Shi, Weiming Zeng, Lang Qin, Yang Yang, Ke Zhou, Zhiguo Zhang, Wai Ting Siok, Nizhuan Wang  

**一句话要点**：提出RSM-CoDG框架，结合脑区先验与多尺度建模，提升跨被试EEG情绪识别的泛化能力。

**关键词**：跨被试EEG情绪识别, 时空建模, 域泛化, 脑区先验, 多尺度时间分析

## 3 点简述
- 核心问题：跨被试EEG情绪识别受个体差异和时空复杂性影响，现有方法难以统一处理。
- 方法要点：基于脑功能分区构建区域级空间表示，并采用多尺度时间建模与协作域泛化策略。
- 实验或效果：在SEED数据集上优于现有方法，代码开源，验证了鲁棒性提升。

## 摘要（原文）

> Cross-subject EEG-based emotion recognition (EER) remains challenging due to strong inter-subject variability, which induces substantial distribution shifts in EEG signals, as well as the high complexity of emotion-related neural representations in both spatial organization and temporal evolution. Existing approaches typically improve spatial modeling, temporal modeling, or generalization strategies in isolation, which limits their ability to align representations across subjects while capturing multi-scale dynamics and suppressing subject-specific bias within a unified framework. To address these gaps, we propose a Region-aware Spatiotemporal Modeling framework with Collaborative Domain Generalization (RSM-CoDG) for cross-subject EEG emotion recognition. RSM-CoDG incorporates neuroscience priors derived from functional brain region partitioning to construct region-level spatial representations, thereby improving cross-subject comparability. It also employs multi-scale temporal modeling to characterize the dynamic evolution of emotion-evoked neural activity. In addition, the framework employs a collaborative domain generalization strategy, incorporating multidimensional constraints to reduce subject-specific bias in a fully unseen target subject setting, which enhances the generalization to unknown individuals. Extensive experimental results on SEED series datasets demonstrate that RSM-CoDG consistently outperforms existing competing methods, providing an effective approach for improving robustness. The source code is available at https://github.com/RyanLi-X/RSM-CoDG.

