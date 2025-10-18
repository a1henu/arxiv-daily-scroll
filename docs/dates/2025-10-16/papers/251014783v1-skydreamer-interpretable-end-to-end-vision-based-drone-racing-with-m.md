---
layout: default
title: SkyDreamer: Interpretable End-to-End Vision-Based Drone Racing with Model-Based Reinforcement Learning
---

# SkyDreamer: Interpretable End-to-End Vision-Based Drone Racing with Model-Based Reinforcement Learning
**arXiv**：[2510.14783v1](https://arxiv.org/abs/2510.14783) · [PDF](https://arxiv.org/pdf/2510.14783.pdf)  
**作者**：Aderik Verraest, Stavrow Bahnam, Robin Ferede, Guido de Croon, Christophe De Wagter  

**一句话要点**：提出SkyDreamer以解决端到端视觉无人机竞速的鲁棒性与高性能问题

**关键词**：无人机竞速, 端到端视觉, 模型强化学习, 仿真到真实转移, 板载执行, 状态估计

## 3 点简述
- 核心问题：现有自主无人机竞速系统缺乏端到端视觉方法，无法同时实现全仿真到真实转移、板载执行和冠军级性能。
- 方法要点：基于模型强化学习，世界模型解码特权信息，作为隐式状态估计器，提升可解释性。
- 实验或效果：在真实世界实现高速飞行，速度达21 m/s，加速度6 g，并展示对视觉模糊和电池耗尽的鲁棒性。

## 摘要（原文）

> Autonomous drone racing (ADR) systems have recently achieved champion-level
> performance, yet remain highly specific to drone racing. While end-to-end
> vision-based methods promise broader applicability, no system to date
> simultaneously achieves full sim-to-real transfer, onboard execution, and
> champion-level performance. In this work, we present SkyDreamer, to the best of
> our knowledge, the first end-to-end vision-based ADR policy that maps directly
> from pixel-level representations to motor commands. SkyDreamer builds on
> informed Dreamer, a model-based reinforcement learning approach where the world
> model decodes to privileged information only available during training. By
> extending this concept to end-to-end vision-based ADR, the world model
> effectively functions as an implicit state and parameter estimator, greatly
> improving interpretability. SkyDreamer runs fully onboard without external aid,
> resolves visual ambiguities by tracking progress using the state decoded from
> the world model's hidden state, and requires no extrinsic camera calibration,
> enabling rapid deployment across different drones without retraining.
> Real-world experiments show that SkyDreamer achieves robust, high-speed flight,
> executing tight maneuvers such as an inverted loop, a split-S and a ladder,
> reaching speeds of up to 21 m/s and accelerations of up to 6 g. It further
> demonstrates a non-trivial visual sim-to-real transfer by operating on
> poor-quality segmentation masks, and exhibits robustness to battery depletion
> by accurately estimating the maximum attainable motor RPM and adjusting its
> flight path in real-time. These results highlight SkyDreamer's adaptability to
> important aspects of the reality gap, bringing robustness while still achieving
> extremely high-speed, agile flight.

