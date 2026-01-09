---
layout: default
title: Data-Driven Terramechanics Approach Towards a Realistic Real-Time Simulator for Lunar Rovers
---

# Data-Driven Terramechanics Approach Towards a Realistic Real-Time Simulator for Lunar Rovers
**arXiv**：[2601.04547v1](https://arxiv.org/abs/2601.04547) · [PDF](https://arxiv.org/pdf/2601.04547.pdf)  
**作者**：Jakob M. Kern, James M. Hurrell, Shreya Santra, Keisuke Takehana, Kentaro Uno, Kazuya Yoshida  

**一句话要点**：提出数据驱动地形力学方法，实现月球车高保真实时仿真

**关键词**：月球车仿真, 数据驱动地形力学, 实时仿真, 车轮-土壤交互, 回归模型, 高保真可视化

## 3 点简述
- 核心问题：现有仿真器视觉真实或物理准确单一，难以全面复现月球表面条件。
- 方法要点：采用数据驱动回归模型，基于实验数据预测车轮滑移和沉陷，结合高视觉保真度。
- 实验或效果：模型在平坦和20度斜坡上准确模拟稳态与动态滑移及沉陷，经实地测试验证。

## 摘要（原文）

> High-fidelity simulators for the lunar surface provide a digital environment for extensive testing of rover operations and mission planning. However, current simulators focus on either visual realism or physical accuracy, which limits their capability to replicate lunar conditions comprehensively. This work addresses that gap by combining high visual fidelity with realistic terrain interaction for a realistic representation of rovers on the lunar surface. Because direct simulation of wheel-soil interactions is computationally expensive, a data-driven approach was adopted, using regression models for slip and sinkage from data collected in both full-rover and single-wheel experiments and simulations. The resulting regression-based terramechanics model accurately reproduced steady-state and dynamic slip, as well as sinkage behavior, on flat terrain and slopes up to 20 degrees, with validation against field test results. Additionally, improvements were made to enhance the realism of terrain deformation and wheel trace visualization. This method supports real-time applications that require physically plausible terrain response alongside high visual fidelity.

