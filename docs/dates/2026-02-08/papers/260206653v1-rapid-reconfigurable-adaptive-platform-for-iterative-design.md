---
layout: default
title: RAPID: Reconfigurable, Adaptive Platform for Iterative Design
---

# RAPID: Reconfigurable, Adaptive Platform for Iterative Design
**arXiv**：[2602.06653v1](https://arxiv.org/abs/2602.06653) · [PDF](https://arxiv.org/pdf/2602.06653.pdf)  
**作者**：Zi Yin, Fanhong Li, Shurui Zheng, Jia Liu  

**一句话要点**：提出RAPID可重构平台以加速机器人操作策略的迭代设计

**关键词**：机器人操作, 可重构平台, 模块化硬件, 实时配置感知, 传感器热插拔, 迭代设计

## 3 点简述
- 核心问题：机器人操作策略开发中，末端执行器微小改动常需机械重装和系统重集成，迭代缓慢。
- 方法要点：基于免工具模块化硬件架构和匹配软件栈，通过USB事件驱动的物理掩码实现实时硬件配置感知。
- 实验或效果：系统实验显示，多模态配置设置时间减少两个数量级，支持运行时传感器热插拔下的策略持续执行。

## 摘要（原文）

> Developing robotic manipulation policies is iterative and hypothesis-driven: researchers test tactile sensing, gripper geometries, and sensor placements through real-world data collection and training. Yet even minor end-effector changes often require mechanical refitting and system re-integration, slowing iteration. We present RAPID, a full-stack reconfigurable platform designed to reduce this friction. RAPID is built around a tool-free, modular hardware architecture that unifies handheld data collection and robot deployment, and a matching software stack that maintains real-time awareness of the underlying hardware configuration through a driver-level Physical Mask derived from USB events. This modular hardware architecture reduces reconfiguration to seconds and makes systematic multi-modal ablation studies practical, allowing researchers to sweep diverse gripper and sensing configurations without repeated system bring-up. The Physical Mask exposes modality presence as an explicit runtime signal, enabling auto-configuration and graceful degradation under sensor hot-plug events, so policies can continue executing when sensors are physically added or removed. System-centric experiments show that RAPID reduces the setup time for multi-modal configurations by two orders of magnitude compared to traditional workflows and preserves policy execution under runtime sensor hot-unplug events. The hardware designs, drivers, and software stack are open-sourced at https://rapid-kit.github.io/ .

