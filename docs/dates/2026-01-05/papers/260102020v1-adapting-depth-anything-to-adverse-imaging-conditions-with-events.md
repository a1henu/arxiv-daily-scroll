---
layout: default
title: Adapting Depth Anything to Adverse Imaging Conditions with Events
---

# Adapting Depth Anything to Adverse Imaging Conditions with Events
**arXiv**：[2601.02020v1](https://arxiv.org/abs/2601.02020) · [PDF](https://arxiv.org/pdf/2601.02020.pdf)  
**作者**：Shihan Peng, Yuyang Xiong, Hanyu Zhou, Zhiwei Shi, Haoyue Liu, Gang Chen, Luxin Yan, Yi Chang  

**一句话要点**：提出ADAE框架，通过事件相机增强Depth Anything在恶劣成像条件下的深度估计

**关键词**：深度估计, 事件相机, 恶劣成像条件, 时空融合, 基础模型适应, 信息熵策略

## 3 点简述
- 核心问题：深度基础模型在极端光照和运动模糊等恶劣条件下性能下降，事件相机融合方法未能继承基础模型的开放世界知识
- 方法要点：采用熵感知空间融合和运动引导时间校正，自适应整合帧与事件特征以补偿退化
- 实验或效果：通过广泛实验验证了方法在恶劣成像条件下的优越性，代码将在接受后发布

## 摘要（原文）

> Robust depth estimation under dynamic and adverse lighting conditions is essential for robotic systems. Currently, depth foundation models, such as Depth Anything, achieve great success in ideal scenes but remain challenging under adverse imaging conditions such as extreme illumination and motion blur. These degradations corrupt the visual signals of frame cameras, weakening the discriminative features of frame-based depths across the spatial and temporal dimensions. Typically, existing approaches incorporate event cameras to leverage their high dynamic range and temporal resolution, aiming to compensate for corrupted frame features. However, such specialized fusion models are predominantly trained from scratch on domain-specific datasets, thereby failing to inherit the open-world knowledge and robust generalization inherent to foundation models. In this work, we propose ADAE, an event-guided spatiotemporal fusion framework for Depth Anything in degraded scenes. Our design is guided by two key insights: 1) Entropy-Aware Spatial Fusion. We adaptively merge frame-based and event-based features using an information entropy strategy to indicate illumination-induced degradation. 2) Motion-Guided Temporal Correction. We resort to the event-based motion cue to recalibrate ambiguous features in blurred regions. Under our unified framework, the two components are complementary to each other and jointly enhance Depth Anything under adverse imaging conditions. Extensive experiments have been performed to verify the superiority of the proposed method. Our code will be released upon acceptance.

