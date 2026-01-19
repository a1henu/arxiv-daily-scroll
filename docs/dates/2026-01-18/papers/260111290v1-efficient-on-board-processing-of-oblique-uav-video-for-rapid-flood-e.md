---
layout: default
title: Efficient On-Board Processing of Oblique UAV Video for Rapid Flood Extent Mapping
---

# Efficient On-Board Processing of Oblique UAV Video for Rapid Flood Extent Mapping
**arXiv**：[2601.11290v1](https://arxiv.org/abs/2601.11290) · [PDF](https://arxiv.org/pdf/2601.11290.pdf)  
**作者**：Vishisht Sharma, Sam Leroux, Lisa Landuyt, Nick Witvrouwen, Pieter Simoens  

**一句话要点**：提出Temporal Token Reuse以解决无人机上倾斜视频实时分割的SWaP约束问题

**关键词**：无人机视频处理, 实时视频分割, 边缘计算优化, 时空冗余利用, 洪水监测

## 3 点简述
- 核心问题：无人机上高分辨率倾斜视频处理受限于严格的SWaP约束，导致边缘硬件上低延迟推理困难。
- 方法要点：TTR利用时空冗余，通过轻量相似度度量动态识别静态区域并传播预计算特征，减少冗余计算。
- 实验或效果：在边缘硬件上，TTR降低30%推理延迟，分割精度损失可忽略（<0.5% mIoU）。

## 摘要（原文）

> Effective disaster response relies on rapid disaster response, where oblique aerial video is the primary modality for initial scouting due to its ability to maximize spatial coverage and situational awareness in limited flight time. However, the on-board processing of high-resolution oblique streams is severely bottlenecked by the strict Size, Weight, and Power (SWaP) constraints of Unmanned Aerial Vehicles (UAVs). The computational density required to process these wide-field-of-view streams precludes low-latency inference on standard edge hardware. To address this, we propose Temporal Token Reuse (TTR), an adaptive inference framework capable of accelerating video segmentation on embedded devices. TTR exploits the intrinsic spatiotemporal redundancy of aerial video by formulating image patches as tokens; it utilizes a lightweight similarity metric to dynamically identify static regions and propagate their precomputed deep features, thereby bypassing redundant backbone computations. We validate the framework on standard benchmarks and a newly curated Oblique Floodwater Dataset designed for hydrological monitoring. Experimental results on edge-grade hardware demonstrate that TTR achieves a 30% reduction in inference latency with negligible degradation in segmentation accuracy (< 0.5% mIoU). These findings confirm that TTR effectively shifts the operational Pareto frontier, enabling high-fidelity, real-time oblique video understanding for time-critical remote sensing missions

