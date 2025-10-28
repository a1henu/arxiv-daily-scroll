---
layout: default
title: Seq-DeepIPC: Sequential Sensing for End-to-End Control in Legged Robot Navigation
---

# Seq-DeepIPC: Sequential Sensing for End-to-End Control in Legged Robot Navigation
**arXiv**：[2510.23057v1](https://arxiv.org/abs/2510.23057) · [PDF](https://arxiv.org/pdf/2510.23057.pdf)  
**作者**：Oskar Natan, Jun Miura  

**一句话要点**：提出Seq-DeepIPC以实现腿式机器人在真实环境中的端到端导航控制

**关键词**：腿式机器人导航, 端到端控制, 多模态感知, 序列融合, 语义分割, 深度估计

## 3 点简述
- 核心问题：腿式机器人导航中感知与控制的高效集成与实时部署。
- 方法要点：使用多模态感知与序列融合，联合预测语义分割和深度估计。
- 实验或效果：在机器人狗上验证，序列输入提升性能，模型尺寸合理。

## 摘要（原文）

> We present Seq-DeepIPC, a sequential end-to-end perception-to-control model
> for legged robot navigation in realworld environments. Seq-DeepIPC advances
> intelligent sensing for autonomous legged navigation by tightly integrating
> multi-modal perception (RGB-D + GNSS) with temporal fusion and control. The
> model jointly predicts semantic segmentation and depth estimation, giving
> richer spatial features for planning and control. For efficient deployment on
> edge devices, we use EfficientNet-B0 as the encoder, reducing computation while
> maintaining accuracy. Heading estimation is simplified by removing the noisy
> IMU and instead computing the bearing angle directly from consecutive GNSS
> positions. We collected a larger and more diverse dataset that includes both
> road and grass terrains, and validated Seq-DeepIPC on a robot dog. Comparative
> and ablation studies show that sequential inputs improve perception and control
> in our models, while other baselines do not benefit. Seq-DeepIPC achieves
> competitive or better results with reasonable model size; although GNSS-only
> heading is less reliable near tall buildings, it is robust in open areas.
> Overall, Seq-DeepIPC extends end-to-end navigation beyond wheeled robots to
> more versatile and temporally-aware systems. To support future research, we
> will release the codes to our GitHub repository at
> https://github.com/oskarnatan/Seq-DeepIPC.

