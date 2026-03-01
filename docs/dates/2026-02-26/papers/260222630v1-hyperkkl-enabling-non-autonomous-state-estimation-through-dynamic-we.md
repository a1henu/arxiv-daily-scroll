---
layout: default
title: HyperKKL: Enabling Non-Autonomous State Estimation through Dynamic Weight Conditioning
---

# HyperKKL: Enabling Non-Autonomous State Estimation through Dynamic Weight Conditioning
**arXiv**：[2602.22630v1](https://arxiv.org/abs/2602.22630) · [PDF](https://arxiv.org/pdf/2602.22630.pdf)  
**作者**：Yahia Salaheldin Shaaban, Salem Lahlou, Abdelrahman Sayed Sayed  

**一句话要点**：提出HyperKKL以通过动态权重调节实现非自治系统的状态估计

**关键词**：非自治系统, KKL观测器, 超网络, 状态估计, 非线性系统, 数值模拟

## 3 点简述
- 核心问题：现有基于学习的KKL观测器主要针对自治系统，难以泛化到非自治系统，需昂贵重训练或在线更新。
- 方法要点：采用超网络架构编码外生输入信号，即时生成KKL观测器参数，学习由外部驱动参数化的浸入映射族。
- 实验或效果：在Duffing、Van der Pol、Lorenz和Rössler系统等基准示例上进行数值模拟评估，对比课程学习策略。

## 摘要（原文）

> This paper proposes HyperKKL, a novel learning approach for designing Kazantzis-Kravaris/Luenberger (KKL) observers for non-autonomous nonlinear systems. While KKL observers offer a rigorous theoretical framework by immersing nonlinear dynamics into a stable linear latent space, its practical realization relies on solving Partial Differential Equations (PDE) that are analytically intractable. Current existing learning-based approximations of the KKL observer are mostly designed for autonomous systems, failing to generalize to driven dynamics without expensive retraining or online gradient updates. HyperKKL addresses this by employing a hypernetwork architecture that encodes the exogenous input signal to instantaneously generate the parameters of the KKL observer, effectively learning a family of immersion maps parameterized by the external drive. We rigorously evaluate this approach against a curriculum learning strategy that attempts to generalize from autonomous regimes via training heuristics alone. The novel approach is illustrated on four numerical simulations in benchmark examples including the Duffing, Van der Pol, Lorenz, and Rössler systems.

