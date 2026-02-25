---
layout: default
title: VAGNet: Grounding 3D Affordance from Human-Object Interactions in Videos
---

# VAGNet: Grounding 3D Affordance from Human-Object Interactions in Videos
**arXiv**：[2602.20608v1](https://arxiv.org/abs/2602.20608) · [PDF](https://arxiv.org/pdf/2602.20608.pdf)  
**作者**：Aihua Mao, Kaihang Huang, Yong-Jin Liu, Chee Seng Chan, Ying He  

**一句话要点**：提出VAGNet框架，利用视频动态交互序列解决3D物体可供性定位中的静态线索模糊问题。

**关键词**：3D物体可供性定位, 人-物交互, 视频引导学习, 动态交互序列, PVAD数据集

## 3 点简述
- 核心问题：现有方法依赖静态视觉或文本线索，难以准确定位真实交互中的接触区域。
- 方法要点：通过视频引导的3D可供性定位，对齐视频交互线索与3D结构以消除歧义。
- 实验或效果：在PVAD数据集上实现最先进性能，显著优于基于静态的基线方法。

## 摘要（原文）

> 3D object affordance grounding aims to identify regions on 3D objects that support human-object interaction (HOI), a capability essential to embodied visual reasoning. However, most existing approaches rely on static visual or textual cues, neglecting that affordances are inherently defined by dynamic actions. As a result, they often struggle to localize the true contact regions involved in real interactions. We take a different perspective. Humans learn how to use objects by observing and imitating actions, not just by examining shapes. Motivated by this intuition, we introduce video-guided 3D affordance grounding, which leverages dynamic interaction sequences to provide functional supervision. To achieve this, we propose VAGNet, a framework that aligns video-derived interaction cues with 3D structure to resolve ambiguities that static cues cannot address. To support this new setting, we introduce PVAD, the first HOI video-3D pairing affordance dataset, providing functional supervision unavailable in prior works. Extensive experiments on PVAD show that VAGNet achieves state-of-the-art performance, significantly outperforming static-based baselines. The code and dataset will be open publicly.

