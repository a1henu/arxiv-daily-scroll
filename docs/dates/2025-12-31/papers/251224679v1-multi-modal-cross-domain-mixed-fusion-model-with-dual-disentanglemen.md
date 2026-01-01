---
layout: default
title: Multi-modal cross-domain mixed fusion model with dual disentanglement for fault diagnosis under unseen working conditions
---

# Multi-modal cross-domain mixed fusion model with dual disentanglement for fault diagnosis under unseen working conditions
**arXiv**：[2512.24679v1](https://arxiv.org/abs/2512.24679) · [PDF](https://arxiv.org/pdf/2512.24679.pdf)  
**作者**：Pengcheng Xia, Yixiang Huang, Chengjin Qin, Chengliang Liu  

**一句话要点**：提出多模态跨域混合融合模型，通过双重解耦解决未见工况下的故障诊断问题。

**关键词**：故障诊断, 多模态融合, 域泛化, 双重解耦, 跨域学习, 未见工况

## 3 点简述
- 核心问题：现有方法在未见工况下性能下降，且多依赖单模态信号，忽略多模态互补性。
- 方法要点：开发双重解耦框架分离模态不变/特定和域不变/特定特征，设计跨域混合融合策略增强多样性。
- 实验或效果：在感应电机故障诊断实验中，模型在未见工况下优于先进方法，消融研究验证组件有效性。

## 摘要（原文）

> Intelligent fault diagnosis has become an indispensable technique for ensuring machinery reliability. However, existing methods suffer significant performance decline in real-world scenarios where models are tested under unseen working conditions, while domain adaptation approaches are limited to their reliance on target domain samples. Moreover, most existing studies rely on single-modal sensing signals, overlooking the complementary nature of multi-modal information for improving model generalization. To address these limitations, this paper proposes a multi-modal cross-domain mixed fusion model with dual disentanglement for fault diagnosis. A dual disentanglement framework is developed to decouple modality-invariant and modality-specific features, as well as domain-invariant and domain-specific representations, enabling both comprehensive multi-modal representation learning and robust domain generalization. A cross-domain mixed fusion strategy is designed to randomly mix modality information across domains for modality and domain diversity augmentation. Furthermore, a triple-modal fusion mechanism is introduced to adaptively integrate multi-modal heterogeneous information. Extensive experiments are conducted on induction motor fault diagnosis under both unseen constant and time-varying working conditions. The results demonstrate that the proposed method consistently outperforms advanced methods and comprehensive ablation studies further verify the effectiveness of each proposed component and multi-modal fusion. The code is available at: https://github.com/xiapc1996/MMDG.

