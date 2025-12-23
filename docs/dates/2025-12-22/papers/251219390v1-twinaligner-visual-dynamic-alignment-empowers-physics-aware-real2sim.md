---
layout: default
title: TwinAligner: Visual-Dynamic Alignment Empowers Physics-aware Real2Sim2Real for Robotic Manipulation
---

# TwinAligner: Visual-Dynamic Alignment Empowers Physics-aware Real2Sim2Real for Robotic Manipulation
**arXiv**：[2512.19390v1](https://arxiv.org/abs/2512.19390) · [PDF](https://arxiv.org/pdf/2512.19390.pdf)  
**作者**：Hongwei Fan, Hang Dai, Jiyao Zhang, Jinzhou Li, Qiyang Yan, Yujie Zhao, Mingju Gao, Jinghang Wu, Hao Tang, Hao Dong  

**一句话要点**：提出TwinAligner系统，通过视觉与动态对齐解决机器人操作中的仿真到现实差距问题。

**关键词**：机器人操作, 仿真到现实, 视觉对齐, 动态对齐, 零样本泛化, 数据驱动学习

## 3 点简述
- 核心问题：仿真与现实间的视觉和动态差距阻碍机器人策略的有效迁移。
- 方法要点：视觉对齐模块基于SDF重建和可编辑3DGS渲染实现像素级对齐；动态对齐模块通过机器人-物体交互识别刚性物理确保动态一致性。
- 实验或效果：系统支持零样本泛化，提升策略性能一致性，加速算法开发。

## 摘要（原文）

> The robotics field is evolving towards data-driven, end-to-end learning, inspired by multimodal large models. However, reliance on expensive real-world data limits progress. Simulators offer cost-effective alternatives, but the gap between simulation and reality challenges effective policy transfer. This paper introduces TwinAligner, a novel Real2Sim2Real system that addresses both visual and dynamic gaps. The visual alignment module achieves pixel-level alignment through SDF reconstruction and editable 3DGS rendering, while the dynamic alignment module ensures dynamic consistency by identifying rigid physics from robot-object interaction. TwinAligner improves robot learning by providing scalable data collection and establishing a trustworthy iterative cycle, accelerating algorithm development. Quantitative evaluations highlight TwinAligner's strong capabilities in visual and dynamic real-to-sim alignment. This system enables policies trained in simulation to achieve strong zero-shot generalization to the real world. The high consistency between real-world and simulated policy performance underscores TwinAligner's potential to advance scalable robot learning. Code and data will be released on https://twin-aligner.github.io

