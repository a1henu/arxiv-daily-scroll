---
layout: default
title: Optical Linear Systems Framework for Event Sensing and Computational Neuromorphic Imaging
---

# Optical Linear Systems Framework for Event Sensing and Computational Neuromorphic Imaging
**arXiv**：[2601.13498v1](https://arxiv.org/abs/2601.13498) · [PDF](https://arxiv.org/pdf/2601.13498.pdf)  
**作者**：Nimrod Kruger, Nicholas Owen Ralph, Gregory Cohen, Paul Hurley  

**一句话要点**：提出基于光学线性系统的事件感知框架，以桥接事件传感与动态光学系统的计算成像。

**关键词**：事件视觉传感器, 计算成像, 线性系统模型, 动态光学系统, 逆滤波, Wiener反卷积

## 3 点简述
- 事件视觉传感器输出非线性事件流，难以与基于线性模型的传统计算成像方法集成。
- 通过物理基础处理将事件流映射为对数强度和导数估计，并嵌入动态线性系统模型。
- 在模拟和真实事件数据中验证，实现点源定位和分离，适用于调制离焦等动态光学系统。

## 摘要（原文）

> Event vision sensors (neuromorphic cameras) output sparse, asynchronous ON/OFF events triggered by log-intensity threshold crossings, enabling microsecond-scale sensing with high dynamic range and low data bandwidth. As a nonlinear system, this event representation does not readily integrate with the linear forward models that underpin most computational imaging and optical system design. We present a physics-grounded processing pipeline that maps event streams to estimates of per-pixel log-intensity and intensity derivatives, and embeds these measurements in a dynamic linear systems model with a time-varying point spread function. This enables inverse filtering directly from event data, using frequency-domain Wiener deconvolution with a known (or parameterised) dynamic transfer function. We validate the approach in simulation for single and overlapping point sources under modulated defocus, and on real event data from a tunable-focus telescope imaging a star field, demonstrating source localisation and separability. The proposed framework provides a practical bridge between event sensing and model-based computational imaging for dynamic optical systems.

