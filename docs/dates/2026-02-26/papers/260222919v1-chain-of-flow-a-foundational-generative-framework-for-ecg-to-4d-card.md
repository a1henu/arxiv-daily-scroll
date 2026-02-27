---
layout: default
title: Chain of Flow: A Foundational Generative Framework for ECG-to-4D Cardiac Digital Twins
---

# Chain of Flow: A Foundational Generative Framework for ECG-to-4D Cardiac Digital Twins
**arXiv**：[2602.22919v1](https://arxiv.org/abs/2602.22919) · [PDF](https://arxiv.org/pdf/2602.22919.pdf)  
**作者**：Haofan Wu, Nay Aung, Theodoros N. Arvanitis, Joao A. C. Lima, Steffen E. Petersen, Le Zhang  

**一句话要点**：提出Chain of Flow框架，从单周期心电图生成4D心脏数字孪生，解决现有模型任务特定、非患者特异性问题。

**关键词**：心脏数字孪生, 心电图生成, 4D重建, 多模态学习, 虚拟心脏模拟

## 3 点简述
- 核心问题：现有心脏数字孪生框架局限于任务特定预测，缺乏患者特异性、可操控的虚拟心脏。
- 方法要点：集成电影心脏磁共振和12导联心电图，学习心脏几何、电生理和运动动力学的统一表示。
- 实验或效果：在多样队列中评估，准确恢复心脏解剖、腔室功能和动态运动模式，支持下游任务如容积测量和虚拟电影合成。

## 摘要（原文）

> A clinically actionable Cardiac Digital Twin (CDT) should reconstruct individualised cardiac anatomy and physiology, update its internal state from multimodal signals, and enable a broad range of downstream simulations beyond isolated tasks. However, existing CDT frameworks remain limited to task-specific predictors rather than building a patient-specific, manipulable virtual heart. In this work, we introduce Chain of Flow (COF), a foundational ECG-driven generative framework that reconstructs full 4D cardiac structure and motion from a single cardiac cycle. The method integrates cine-CMR and 12-lead ECG during training to learn a unified representation of cardiac geometry, electrophysiology, and motion dynamics. We evaluate Chain of Flow on diverse cohorts and demonstrate accurate recovery of cardiac anatomy, chamber-wise function, and dynamic motion patterns. The reconstructed 4D hearts further support downstream CDT tasks such as volumetry, regional function analysis, and virtual cine synthesis. By enabling full 4D organ reconstruction directly from ECG, COF transforms cardiac digital twins from narrow predictive models into fully generative, patient-specific virtual hearts. Code will be released after review.

