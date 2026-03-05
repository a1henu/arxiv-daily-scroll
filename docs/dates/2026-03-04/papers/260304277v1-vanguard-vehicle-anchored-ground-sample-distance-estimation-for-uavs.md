---
layout: default
title: VANGUARD: Vehicle-Anchored Ground Sample Distance Estimation for UAVs in GPS-Denied Environments
---

# VANGUARD: Vehicle-Anchored Ground Sample Distance Estimation for UAVs in GPS-Denied Environments
**arXiv**：[2603.04277v1](https://arxiv.org/abs/2603.04277) · [PDF](https://arxiv.org/pdf/2603.04277.pdf)  
**作者**：Yifei Chen, Xupeng Chen, Feng Wang, Niangang Jiao, Jiayin Liu  

**一句话要点**：提出VANGUARD工具，通过车辆锚点估计地面采样距离，解决GPS缺失环境下无人机尺度感知问题。

**关键词**：地面采样距离估计, GPS缺失环境, 无人机感知, 几何感知技能, 车辆锚点检测, 自主空间推理

## 3 点简述
- 核心问题：GPS缺失环境中，无人机无法获取相机元数据，导致场景绝对尺度丢失，影响自主空间推理安全。
- 方法要点：利用检测到的车辆定向边界框，通过核密度估计稳健计算像素长度，结合预校准参考长度转换为地面采样距离。
- 实验或效果：在DOTA v1.5基准上，VANGUARD实现6.87%中位误差，集成下游测量后误差降低，优于视觉语言模型基线。

## 摘要（原文）

> Autonomous aerial robots operating in GPS-denied or communication-degraded environments frequently lose access to camera metadata and telemetry, leaving onboard perception systems unable to recover the absolute metric scale of the scene. As LLM/VLM-based planners are increasingly adopted as high-level agents for embodied systems, their ability to reason about physical dimensions becomes safety-critical -- yet our experiments show that five state-of-the-art VLMs suffer from spatial scale hallucinations, with median area estimation errors exceeding 50%. We propose VANGUARD, a lightweight, deterministic Geometric Perception Skill designed as a callable tool that any LLM-based agent can invoke to recover Ground Sample Distance (GSD) from ubiquitous environmental anchors: small vehicles detected via oriented bounding boxes, whose modal pixel length is robustly estimated through kernel density estimation and converted to GSD using a pre-calibrated reference length. The tool returns both a GSD estimate and a composite confidence score, enabling the calling agent to autonomously decide whether to trust the measurement or fall back to alternative strategies. On the DOTA~v1.5 benchmark, VANGUARD achieves 6.87% median GSD error on 306~images. Integrated with SAM-based segmentation for downstream area measurement, the pipeline yields 19.7% median error on a 100-entry benchmark -- with 2.6x lower category dependence and 4x fewer catastrophic failures than the best VLM baseline -- demonstrating that equipping agents with deterministic geometric tools is essential for safe autonomous spatial reasoning.

