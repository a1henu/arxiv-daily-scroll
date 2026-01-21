---
layout: default
title: HiT: History-Injection Transformers for Onboard Continuous Flood Change Detection
---

# HiT: History-Injection Transformers for Onboard Continuous Flood Change Detection
**arXiv**：[2601.13751v1](https://arxiv.org/abs/2601.13751) · [PDF](https://arxiv.org/pdf/2601.13751.pdf)  
**作者**：Daniel Kyselica, Jonáš Herec, Oliver Kutis, Rado Pitoňák  

**一句话要点**：提出历史注入Transformer（HiT）以解决小卫星上连续洪水检测的内存与计算限制问题

**关键词**：洪水检测, Transformer模型, 历史注入机制, 小卫星计算, 连续监测, 实时处理

## 3 点简述
- 核心问题：卫星连续监测洪水需处理多时相数据，但受限于小卫星的内存和计算能力。
- 方法要点：HiT机制在Transformer中注入历史上下文，减少99%以上数据存储，保持检测精度。
- 实验或效果：在STTORM-CD数据集上验证HiT-Prithvi模型，在Jetson Orin Nano硬件上实现43 FPS，支持实时灾害评估。

## 摘要（原文）

> Natural disaster monitoring through continuous satellite observation requires processing multi-temporal data under strict operational constraints. This paper addresses flood detection, a critical application for hazard management, by developing an onboard change detection system that operates within the memory and computational limits of small satellites. We propose History Injection mechanism for Transformer models (HiT), that maintains historical context from previous observations while reducing data storage by over 99\% of original image size. Moreover, testing on the STTORM-CD flood dataset confirms that the HiT mechanism within the Prithvi-tiny foundation model maintains detection accuracy compared to the bitemporal baseline. The proposed HiT-Prithvi model achieved 43 FPS on Jetson Orin Nano, a representative onboard hardware used in nanosats. This work establishes a practical framework for satellite-based continuous monitoring of natural disasters, supporting real-time hazard assessment without dependency on ground-based processing infrastructure. Architecture as well as model checkpoints is available at https://github.com/zaitra/HiT-change-detection

