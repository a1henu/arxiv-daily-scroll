---
layout: default
title: UniSTOK: Uniform Inductive Spatio-Temporal Kriging
---

# UniSTOK: Uniform Inductive Spatio-Temporal Kriging
**arXiv**：[2603.05301v1](https://arxiv.org/abs/2603.05301) · [PDF](https://arxiv.org/pdf/2603.05301.pdf)  
**作者**：Lewei Xie, Haoyu Zhang, Juan Yuan, Liangjun You, Yulong Chen, Yifan Zhang  

**一句话要点**：提出UniSTOK框架以增强缺失观测下的时空克里金模型性能

**关键词**：时空克里金, 缺失数据处理, 双分支网络, 注意力融合, 传感器网络, 环境监测

## 3 点简述
- 核心问题：传感器观测值存在异构缺失，导致传统模型依赖粗糙插值输入，影响推断准确性。
- 方法要点：采用双分支输入（原始观测与拼图增强）和共享时空骨干网络，通过缺失掩码调制和双通道注意力自适应融合。
- 实验或效果：在多种真实数据集和缺失模式下，实验显示模型性能得到一致且显著提升。

## 摘要（原文）

> Spatio-temporal kriging aims to infer signals at unobserved locations from observed sensors and is critical to applications such as transportation and environmental monitoring. In practice, however, observed sensors themselves often exhibit heterogeneous missingness, forcing inductive kriging models to rely on crudely imputed inputs. This setting brings three key challenges: (1) it is unclear whether an value is a true signal or a missingness-induced artifact; (2) missingness is highly heterogeneous across sensors and time; (3) missing observations distort the local spatio-temporal structure. To address these issues, we propose Uniform Inductive Spatio-Temporal Kriging (UniSTOK), a plug-and-play framework that enhances existing inductive kriging backbones under missing observation. Our framework forms a dual-branch input consisting of the original observations and a jigsaw-augmented counterpart that synthesizes proxy signals only at missing entries. The two branches are then processed in parallel by a shared spatio-temporal backbone with explicit missingness mask modulation. Their outputs are finally adaptively fused via dual-channel attention. Experiments on multiple real-world datasets under diverse missing patterns demonstrate consistent and significant improvements.

