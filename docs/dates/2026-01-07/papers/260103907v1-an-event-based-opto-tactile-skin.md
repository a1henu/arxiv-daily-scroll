---
layout: default
title: An Event-Based Opto-Tactile Skin
---

# An Event-Based Opto-Tactile Skin
**arXiv**：[2601.03907v1](https://arxiv.org/abs/2601.03907) · [PDF](https://arxiv.org/pdf/2601.03907.pdf)  
**作者**：Mohammadreza Koolani, Simeon Bamford, Petr Trunin, Simon F. Müller-Cleve, Matteo Lo Preti, Fulvio Mastrogiovanni, Lucia Beccai, Chiara Bartolozzi  

**一句话要点**：提出基于事件驱动的光触觉皮肤系统，用于软体机器人中的大面积触觉感知。

**关键词**：事件驱动触觉感知, 动态视觉传感器, 柔性光学皮肤, 三角定位, 软体机器人, 低功耗计算

## 3 点简述
- 核心问题：传统触觉传感器在大面积柔性皮肤中难以实现高效、低功耗的实时感知。
- 方法要点：采用动态视觉传感器与柔性光学波导皮肤结合，通过立体视觉三角定位和DBSCAN聚类估计按压位置。
- 实验或效果：在4620 mm²区域测试，定位均方根误差为4.66毫米，事件数据大幅减少时仍保持功能。

## 摘要（原文）

> This paper presents a neuromorphic, event-driven tactile sensing system for soft, large-area skin, based on the Dynamic Vision Sensors (DVS) integrated with a flexible silicone optical waveguide skin. Instead of repetitively scanning embedded photoreceivers, this design uses a stereo vision setup comprising two DVS cameras looking sideways through the skin. Such a design produces events as changes in brightness are detected, and estimates press positions on the 2D skin surface through triangulation, utilizing Density-Based Spatial Clustering of Applications with Noise (DBSCAN) to find the center of mass of contact events resulting from pressing actions. The system is evaluated over a 4620 mm2 probed area of the skin using a meander raster scan. Across 95 % of the presses visible to both cameras, the press localization achieved a Root-Mean-Squared Error (RMSE) of 4.66 mm. The results highlight the potential of this approach for wide-area flexible and responsive tactile sensors in soft robotics and interactive environments. Moreover, we examined how the system performs when the amount of event data is strongly reduced. Using stochastic down-sampling, the event stream was reduced to 1/1024 of its original size. Under this extreme reduction, the average localization error increased only slightly (from 4.66 mm to 9.33 mm), and the system still produced valid press localizations for 85 % of the trials. This reduction in pass rate is expected, as some presses no longer produce enough events to form a reliable cluster for triangulation. These results show that the sensing approach remains functional even with very sparse event data, which is promising for reducing power consumption and computational load in future implementations. The system exhibits a detection latency distribution with a characteristic width of 31 ms.

