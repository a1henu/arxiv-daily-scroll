---
layout: default
title: VIGOR: Visual Goal-In-Context Inference for Unified Humanoid Fall Safety
---

# VIGOR: Visual Goal-In-Context Inference for Unified Humanoid Fall Safety
**arXiv**：[2602.16511v1](https://arxiv.org/abs/2602.16511) · [PDF](https://arxiv.org/pdf/2602.16511.pdf)  
**作者**：Osher Azulay, Zhengjie Xu, Andrew Scheffer, Stella X. Yu  

**一句话要点**：提出VIGOR方法，通过目标在上下文推理实现人形机器人统一跌倒安全恢复

**关键词**：人形机器人, 跌倒安全, 蒸馏训练, 目标在上下文推理, 零样本泛化, 感知-运动集成

## 3 点简述
- 核心问题：现有方法将跌倒安全分割为独立问题或依赖端到端策略，缺乏统一性和泛化能力。
- 方法要点：利用人类演示训练特权教师模型，通过蒸馏到仅依赖深度和本体感知的学生模型，实现目标在上下文表示。
- 实验或效果：在仿真和真实Unitree G1人形机器人上展示零样本跨非平坦环境的鲁棒跌倒安全恢复。

## 摘要（原文）

> Reliable fall recovery is critical for humanoids operating in cluttered environments. Unlike quadrupeds or wheeled robots, humanoids experience high-energy impacts, complex whole-body contact, and large viewpoint changes during a fall, making recovery essential for continued operation. Existing methods fragment fall safety into separate problems such as fall avoidance, impact mitigation, and stand-up recovery, or rely on end-to-end policies trained without vision through reinforcement learning or imitation learning, often on flat terrain. At a deeper level, fall safety is treated as monolithic data complexity, coupling pose, dynamics, and terrain and requiring exhaustive coverage, limiting scalability and generalization. We present a unified fall safety approach that spans all phases of fall recovery. It builds on two insights: 1) Natural human fall and recovery poses are highly constrained and transferable from flat to complex terrain through alignment, and 2) Fast whole-body reactions require integrated perceptual-motor representations. We train a privileged teacher using sparse human demonstrations on flat terrain and simulated complex terrains, and distill it into a deployable student that relies only on egocentric depth and proprioception. The student learns how to react by matching the teacher's goal-in-context latent representation, which combines the next target pose with the local terrain, rather than separately encoding what it must perceive and how it must act. Results in simulation and on a real Unitree G1 humanoid demonstrate robust, zero-shot fall safety across diverse non-flat environments without real-world fine-tuning. The project page is available at https://vigor2026.github.io/

