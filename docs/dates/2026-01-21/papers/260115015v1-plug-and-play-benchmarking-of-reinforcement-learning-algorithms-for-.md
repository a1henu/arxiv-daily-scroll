---
layout: default
title: Plug-and-Play Benchmarking of Reinforcement Learning Algorithms for Large-Scale Flow Control
---

# Plug-and-Play Benchmarking of Reinforcement Learning Algorithms for Large-Scale Flow Control
**arXiv**：[2601.15015v1](https://arxiv.org/abs/2601.15015) · [PDF](https://arxiv.org/pdf/2601.15015.pdf)  
**作者**：Jannis Becktepe, Aleksandra Franz, Nils Thuerey, Sebastian Peitz  

**一句话要点**：提出FluidGym基准套件以解决强化学习在主动流控制中的评估标准化问题

**关键词**：强化学习, 主动流控制, 基准测试, 可微分模拟, 计算流体动力学, 多智能体系统

## 3 点简述
- 现有主动流控制基准依赖外部CFD求解器，缺乏可微性和3D多智能体支持
- FluidGym基于PyTorch和GPU加速PICT求解器，提供全可微、独立运行的标准化环境
- 发布PPO和SAC基线结果，公开环境、数据集和模型，支持系统比较和未来研究

## 摘要（原文）

> Reinforcement learning (RL) has shown promising results in active flow control (AFC), yet progress in the field remains difficult to assess as existing studies rely on heterogeneous observation and actuation schemes, numerical setups, and evaluation protocols. Current AFC benchmarks attempt to address these issues but heavily rely on external computational fluid dynamics (CFD) solvers, are not fully differentiable, and provide limited 3D and multi-agent support. To overcome these limitations, we introduce FluidGym, the first standalone, fully differentiable benchmark suite for RL in AFC. Built entirely in PyTorch on top of the GPU-accelerated PICT solver, FluidGym runs in a single Python stack, requires no external CFD software, and provides standardized evaluation protocols. We present baseline results with PPO and SAC and release all environments, datasets, and trained models as public resources. FluidGym enables systematic comparison of control methods, establishes a scalable foundation for future research in learning-based flow control, and is available at https://github.com/safe-autonomous-systems/fluidgym.

