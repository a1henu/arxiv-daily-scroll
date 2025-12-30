---
layout: default
title: Physics-Informed Neural Networks for Device and Circuit Modeling: A Case Study of NeuroSPICE
---

# Physics-Informed Neural Networks for Device and Circuit Modeling: A Case Study of NeuroSPICE
**arXiv**：[2512.23624v1](https://arxiv.org/abs/2512.23624) · [PDF](https://arxiv.org/pdf/2512.23624.pdf)  
**作者**：Chien-Ting Tung, Chenming Hu  

**一句话要点**：提出NeuroSPICE框架，利用物理信息神经网络进行器件与电路建模，以替代传统SPICE模拟。

**关键词**：物理信息神经网络, 电路模拟, 微分代数方程, 器件建模, 代理模型, 非线性系统

## 3 点简述
- 核心问题：传统SPICE依赖时间离散数值求解器，难以高效处理高度非线性系统如铁电存储器。
- 方法要点：采用物理信息神经网络，通过反向传播最小化微分代数方程残差，实现时域波形建模。
- 实验或效果：NeuroSPICE在训练速度和精度上未超越SPICE，但提供设计优化和逆问题的代理模型优势。

## 摘要（原文）

> We present NeuroSPICE, a physics-informed neural network (PINN) framework for device and circuit simulation. Unlike conventional SPICE, which relies on time-discretized numerical solvers, NeuroSPICE leverages PINNs to solve circuit differential-algebraic equations (DAEs) by minimizing the residual of the equations through backpropagation. It models device and circuit waveforms using analytical equations in time domain with exact temporal derivatives. While PINNs do not outperform SPICE in speed or accuracy during training, they offer unique advantages such as surrogate models for design optimization and inverse problems. NeuroSPICE's flexibility enables the simulation of emerging devices, including highly nonlinear systems such as ferroelectric memories.

