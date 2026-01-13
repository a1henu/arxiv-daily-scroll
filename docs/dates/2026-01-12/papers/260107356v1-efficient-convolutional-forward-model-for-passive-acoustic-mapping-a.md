---
layout: default
title: Efficient Convolutional Forward Model for Passive Acoustic Mapping and Temporal Monitoring
---

# Efficient Convolutional Forward Model for Passive Acoustic Mapping and Temporal Monitoring
**arXiv**：[2601.07356v1](https://arxiv.org/abs/2601.07356) · [PDF](https://arxiv.org/pdf/2601.07356.pdf)  
**作者**：Tatiana Gelvez-Barrera, Barbara Nicolas, Bruno Gilles, Adrian Basarab, Denis Kouamé  

**一句话要点**：提出基于时域卷积的被动声学映射框架，以高效监测治疗超声中的空化活动。

**关键词**：被动声学映射, 治疗超声, 空化成像, 时域卷积, 波束成形, 逆问题

## 3 点简述
- 被动声学映射在治疗超声中用于空化成像，但现有方法计算负担重且时间分辨率低。
- 将被动声学映射建模为逆问题，采用时域卷积前向算子，结合正则化算法融入先验知识。
- 实验表明，该方法优于经典波束成形，提供比频域技术更高的时间分辨率，计算负担显著降低。

## 摘要（原文）

> Passive acoustic mapping (PAM) is a key imaging technique for characterizing cavitation activity in therapeutic ultrasound applications. Recent model-based beamforming algorithms offer high reconstruction quality and strong physical interpretability. However, their computational burden and limited temporal resolution restrict their use in applications with time-evolving cavitation. To address these challenges, we introduce a PAM beamforming framework based on a novel convolutional formulation in the time domain, which enables efficient computation. In this framework, PAM is formulated as an inverse problem in which the forward operator maps spatiotemporal cavitation activity to recorded radio-frequency signals accounting for time-of-flight delays defined by the acquisition geometry. We then formulate a regularized inversion algorithm that incorporates prior knowledge on cavitation activity. Experimental results demonstrate that our framework outperforms classical beamforming methods, providing higher temporal resolution than frequency-domain techniques while substantially reducing computational burden compared with iterative time-domain formulations.

