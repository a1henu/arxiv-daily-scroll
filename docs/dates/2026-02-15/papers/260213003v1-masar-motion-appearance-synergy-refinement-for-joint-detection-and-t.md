---
layout: default
title: MASAR: Motion-Appearance Synergy Refinement for Joint Detection and Trajectory Forecasting
---

# MASAR: Motion-Appearance Synergy Refinement for Joint Detection and Trajectory Forecasting
**arXiv**：[2602.13003v1](https://arxiv.org/abs/2602.13003) · [PDF](https://arxiv.org/pdf/2602.13003.pdf)  
**作者**：Mohammed Amine Bencheikh Lehocine, Julian Schmidt, Frank Moosmann, Dikshant Gupta, Fabian Flohr  

**一句话要点**：提出MASAR框架，通过运动-外观协同优化联合3D检测与轨迹预测，解决传统系统信息流受限问题。

**关键词**：联合检测与预测, 运动-外观协同, 3D目标检测, 轨迹预测, 自动驾驶感知

## 3 点简述
- 核心问题：传统自动驾驶系统感知与预测模块分离，导致信息流受限和误差传播。
- 方法要点：采用对象中心时空机制，联合编码外观与运动特征，通过预测并优化过去轨迹捕获长期依赖。
- 实验或效果：在nuScenes数据集上，minADE和minFDE提升超20%，同时保持稳健检测性能。

## 摘要（原文）

> Classical autonomous driving systems connect perception and prediction modules via hand-crafted bounding-box interfaces, limiting information flow and propagating errors to downstream tasks. Recent research aims to develop end-to-end models that jointly address perception and prediction; however, they often fail to fully exploit the synergy between appearance and motion cues, relying mainly on short-term visual features. We follow the idea of "looking backward to look forward", and propose MASAR, a novel fully differentiable framework for joint 3D detection and trajectory forecasting compatible with any transformer-based 3D detector. MASAR employs an object-centric spatio-temporal mechanism that jointly encodes appearance and motion features. By predicting past trajectories and refining them using guidance from appearance cues, MASAR captures long-term temporal dependencies that enhance future trajectory forecasting. Experiments conducted on the nuScenes dataset demonstrate MASAR's effectiveness, showing improvements of over 20% in minADE and minFDE while maintaining robust detection performance. Code and models are available at https://github.com/aminmed/MASAR.

