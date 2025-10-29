---
layout: default
title: Benchmarking Microsaccade Recognition with Event Cameras: A Novel Dataset and Evaluation
---

# Benchmarking Microsaccade Recognition with Event Cameras: A Novel Dataset and Evaluation
**arXiv**：[2510.24231v1](https://arxiv.org/abs/2510.24231) · [PDF](https://arxiv.org/pdf/2510.24231.pdf)  
**作者**：Waseem Shariff, Timothy Hanley, Maciej Stec, Hossein Javidnia, Peter Corcoran  

**一句话要点**：提出事件相机微扫视数据集与评估方法，以支持精细眼动研究。

**关键词**：事件相机, 微扫视识别, 脉冲神经网络, 数据集构建, 光学流增强, 眼动分析

## 3 点简述
- 核心问题：传统眼动追踪方法成本高、扩展性差，难以捕捉微扫视的精细动态。
- 方法要点：使用Blender模拟微扫视，并通过v2e转换为事件流，构建七类角位移数据集。
- 实验或效果：采用Spiking-VGG模型，平均准确率达约90%，成功分类微扫视角位移。

## 摘要（原文）

> Microsaccades are small, involuntary eye movements vital for visual
> perception and neural processing. Traditional microsaccade studies typically
> use eye trackers or frame-based analysis, which, while precise, are costly and
> limited in scalability and temporal resolution. Event-based sensing offers a
> high-speed, low-latency alternative by capturing fine-grained spatiotemporal
> changes efficiently. This work introduces a pioneering event-based microsaccade
> dataset to support research on small eye movement dynamics in cognitive
> computing. Using Blender, we render high-fidelity eye movement scenarios and
> simulate microsaccades with angular displacements from 0.5 to 2.0 degrees,
> divided into seven distinct classes. These are converted to event streams using
> v2e, preserving the natural temporal dynamics of microsaccades, with durations
> ranging from 0.25 ms to 2.25 ms. We evaluate the dataset using Spiking-VGG11,
> Spiking-VGG13, and Spiking-VGG16, and propose Spiking-VGG16Flow, an
> optical-flow-enhanced variant implemented in SpikingJelly. The models achieve
> around 90 percent average accuracy, successfully classifying microsaccades by
> angular displacement, independent of event count or duration. These results
> demonstrate the potential of spiking neural networks for fine motion
> recognition and establish a benchmark for event-based vision research. The
> dataset, code, and trained models will be publicly available at
> https://waseemshariff126.github.io/microsaccades/ .

