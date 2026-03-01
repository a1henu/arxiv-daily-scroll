---
layout: default
title: Sensor Generalization for Adaptive Sensing in Event-based Object Detection via Joint Distribution Training
---

# Sensor Generalization for Adaptive Sensing in Event-based Object Detection via Joint Distribution Training
**arXiv**：[2602.23357v1](https://arxiv.org/abs/2602.23357) · [PDF](https://arxiv.org/pdf/2602.23357.pdf)  
**作者**：Aheli Saha, René Schuster, Didier Stricker  

**一句话要点**：提出联合分布训练方法，以增强事件相机在物体检测中的传感器泛化能力。

**关键词**：事件相机, 物体检测, 传感器泛化, 联合分布训练, 参数分析

## 3 点简述
- 核心问题：事件相机数据变异性有限，缺乏对信号参数影响的深入分析。
- 方法要点：通过分析内在参数对模型性能的影响，采用联合分布训练提升传感器无关鲁棒性。
- 实验或效果：未知具体实验细节，但旨在扩展下游模型对传感器变化的适应性。

## 摘要（原文）

> Bio-inspired event cameras have recently attracted significant research due to their asynchronous and low-latency capabilities. These features provide a high dynamic range and significantly reduce motion blur. However, because of the novelty in the nature of their output signals, there is a gap in the variability of available data and a lack of extensive analysis of the parameters characterizing their signals. This paper addresses these issues by providing readers with an in-depth understanding of how intrinsic parameters affect the performance of a model trained on event data, specifically for object detection. We also use our findings to expand the capabilities of the downstream model towards sensor-agnostic robustness.

