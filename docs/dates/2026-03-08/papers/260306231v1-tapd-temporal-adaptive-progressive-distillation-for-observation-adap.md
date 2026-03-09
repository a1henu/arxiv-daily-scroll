---
layout: default
title: TaPD: Temporal-adaptive Progressive Distillation for Observation-Adaptive Trajectory Forecasting in Autonomous Driving
---

# TaPD: Temporal-adaptive Progressive Distillation for Observation-Adaptive Trajectory Forecasting in Autonomous Driving
**arXiv**：[2603.06231v1](https://arxiv.org/abs/2603.06231) · [PDF](https://arxiv.org/pdf/2603.06231.pdf)  
**作者**：Mingyu Fan, Yi Liu, Hao Zhou, Deheng Qian, Mohammad Haziq Khan, Matthias Raetsch  

**一句话要点**：提出TaPD框架以解决自动驾驶中可变历史长度轨迹预测的性能下降问题。

**关键词**：轨迹预测, 知识蒸馏, 自动驾驶, 观测自适应, 时序建模

## 3 点简述
- 核心问题：现有轨迹预测器在观测长度可变或极短时性能显著下降。
- 方法要点：结合渐进知识蒸馏和时序回填模块，实现观测自适应预测。
- 实验或效果：在Argoverse数据集上优于基线，尤其在短观测下提升显著。

## 摘要（原文）

> Trajectory prediction is essential for autonomous driving, enabling vehicles to anticipate the motion of surrounding agents to support safe planning. However, most existing predictors assume fixed-length histories and suffer substantial performance degradation when observations are variable or extremely short in real-world settings (e.g., due to occlusion or a limited sensing range). We propose TaPD (Temporal-adaptive Progressive Distillation), a unified plug-and-play framework for observation-adaptive trajectory forecasting under variable history lengths. TaPD comprises two cooperative modules: an Observation-Adaptive Forecaster (OAF) for future prediction and a Temporal Backfilling Module (TBM) for explicit reconstruction of the past. OAF is built on progressive knowledge distillation (PKD), which transfers motion pattern knowledge from long-horizon "teachers" to short-horizon "students" via hierarchical feature regression, enabling short observations to recover richer motion context. We further introduce a cosine-annealed distillation weighting scheme to balance forecasting supervision and feature alignment, improving optimization stability and cross-length consistency. For extremely short histories where implicit alignment is insufficient, TBM backfills missing historical segments conditioned on scene evolution, producing context-rich trajectories that strengthen PKD and thereby improve OAF. We employ a decoupled pretrain-reconstruct-finetune protocol to preserve real-motion priors while adapting to backfilled inputs. Extensive experiments on Argoverse 1 and Argoverse 2 show that TaPD consistently outperforms strong baselines across all observation lengths, delivers especially large gains under very short inputs, and improves other predictors (e.g., HiVT) in a plug-and-play manner. Code will be available at https://github.com/zhouhao94/TaPD.

