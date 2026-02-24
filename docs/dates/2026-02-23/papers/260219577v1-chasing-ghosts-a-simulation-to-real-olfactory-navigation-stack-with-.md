---
layout: default
title: Chasing Ghosts: A Simulation-to-Real Olfactory Navigation Stack with Optional Vision Augmentation
---

# Chasing Ghosts: A Simulation-to-Real Olfactory Navigation Stack with Optional Vision Augmentation
**arXiv**：[2602.19577v1](https://arxiv.org/abs/2602.19577) · [PDF](https://arxiv.org/pdf/2602.19577.pdf)  
**作者**：Kordel K. France, Ovidiu Daescu, Latifur Khan, Rohith Peddi  

**一句话要点**：提出基于模拟到真实学习的无人机嗅觉导航系统，用于气味源定位，可选视觉增强。

**关键词**：无人机嗅觉导航, 模拟到真实学习, 气味源定位, 最小传感器系统, 开源系统, 视觉增强

## 3 点简述
- 核心问题：无人机嗅觉导航面临湍流、稀疏延迟信号及严格载荷计算限制。
- 方法要点：集成定制嗅觉硬件与学习策略，无需外部定位或显式气体分布图。
- 实验或效果：在大型室内环境中验证，使用乙醇源展示稳定源寻找行为。

## 摘要（原文）

> Autonomous odor source localization remains a challenging problem for aerial robots due to turbulent airflow, sparse and delayed sensory signals, and strict payload and compute constraints. While prior unmanned aerial vehicle (UAV)-based olfaction systems have demonstrated gas distribution mapping or reactive plume tracing, they rely on predefined coverage patterns, external infrastructure, or extensive sensing and coordination. In this work, we present a complete, open-source UAV system for online odor source localization using a minimal sensor suite. The system integrates custom olfaction hardware, onboard sensing, and a learning-based navigation policy trained in simulation and deployed on a real quadrotor. Through our minimal framework, the UAV is able to navigate directly toward an odor source without constructing an explicit gas distribution map or relying on external positioning systems. Vision is incorporated as an optional complementary modality to accelerate navigation under certain conditions. We validate the proposed system through real-world flight experiments in a large indoor environment using an ethanol source, demonstrating consistent source-finding behavior under realistic airflow conditions. The primary contribution of this work is a reproducible system and methodological framework for UAV-based olfactory navigation and source finding under minimal sensing assumptions. We elaborate on our hardware design and open source our UAV firmware, simulation code, olfaction-vision dataset, and circuit board to the community. Code, data, and designs will be made available at https://github.com/KordelFranceTech/ChasingGhosts.

