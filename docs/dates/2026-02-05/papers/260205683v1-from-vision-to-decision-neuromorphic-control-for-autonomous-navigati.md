---
layout: default
title: From Vision to Decision: Neuromorphic Control for Autonomous Navigation and Tracking
---

# From Vision to Decision: Neuromorphic Control for Autonomous Navigation and Tracking
**arXiv**：[2602.05683v1](https://arxiv.org/abs/2602.05683) · [PDF](https://arxiv.org/pdf/2602.05683.pdf)  
**作者**：Chuwei Wang, Eduardo Sebastián, Amanda Prorok, Anastasia Bizyaeva  

**一句话要点**：提出神经形态控制框架以解决视觉导航中反应式与决策式控制的融合问题

**关键词**：神经形态控制, 视觉导航, 动态分岔, 机器人自主性, 实时系统, 目标跟踪

## 3 点简述
- 核心问题：机器人导航中反应式控制与模型规划器决策能力难以协调，目标选项对称时易导致犹豫
- 方法要点：使用动态神经元群将视觉像素直接编码为运动命令，通过动态分岔机制延迟决策以打破对称性
- 实验或效果：在仿真和四旋翼平台上验证，实现实时自主导航，计算负担小且参数可解释

## 摘要（原文）

> Robotic navigation has historically struggled to reconcile reactive, sensor-based control with the decisive capabilities of model-based planners. This duality becomes critical when the absence of a predominant option among goals leads to indecision, challenging reactive systems to break symmetries without computationally-intense planners. We propose a parsimonious neuromorphic control framework that bridges this gap for vision-guided navigation and tracking. Image pixels from an onboard camera are encoded as inputs to dynamic neuronal populations that directly transform visual target excitation into egocentric motion commands. A dynamic bifurcation mechanism resolves indecision by delaying commitment until a critical point induced by the environmental geometry. Inspired by recently proposed mechanistic models of animal cognition and opinion dynamics, the neuromorphic controller provides real-time autonomy with a minimal computational burden, a small number of interpretable parameters, and can be seamlessly integrated with application-specific image processing pipelines. We validate our approach in simulation environments as well as on an experimental quadrotor platform.

