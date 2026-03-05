---
layout: default
title: One-Step Face Restoration via Shortcut-Enhanced Coupling Flow
---

# One-Step Face Restoration via Shortcut-Enhanced Coupling Flow
**arXiv**：[2603.03648v1](https://arxiv.org/abs/2603.03648) · [PDF](https://arxiv.org/pdf/2603.03648.pdf)  
**作者**：Xiaohui Sun, Hanlin Wu  

**一句话要点**：提出SCFlowFR以通过数据依赖耦合和捷径约束实现一步人脸恢复

**关键词**：人脸恢复, 流匹配, 一步推理, 数据依赖耦合, 捷径约束, 条件均值估计

## 3 点简述
- 核心问题：现有流匹配方法从高斯噪声开始，忽略低质量与高质量数据间的依赖，导致路径交叉和多步采样需求。
- 方法要点：建立数据依赖耦合建模依赖，使用条件均值估计细化源锚点，并引入捷径约束监督平均速度以实现一步推理。
- 实验或效果：SCFlowFR实现最先进的一步人脸恢复质量，推理速度与传统非扩散方法相当。

## 摘要（原文）

> Face restoration has advanced significantly with generative models like diffusion models and flow matching (FM), which learn continuous-time mappings between distributions. However, existing FM-based approaches often start from Gaussian noise, ignoring the inherent dependency between low-quality (LQ) and high-quality (HQ) data, resulting in path crossovers, curved trajectories, and multi-step sampling requirements. To address these issues, we propose Shortcut-enhanced Coupling flow for Face Restoration (SCFlowFR). First, it establishes a \textit{data-dependent coupling} that explicitly models the LQ--HQ dependency, minimizing path crossovers and promoting near-linear transport. Second, we employ conditional mean estimation to obtain a coarse prediction that refines the source anchor to tighten coupling and conditions the velocity field to stabilize large-step updates. Third, a shortcut constraint supervises average velocities over arbitrary time intervals, enabling accurate one-step inference. Experiments demonstrate that SCFlowFR achieves state-of-the-art one-step face restoration quality with inference speed comparable to traditional non-diffusion methods.

