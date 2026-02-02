---
layout: default
title: SplineFlow: Flow Matching for Dynamical Systems with B-Spline Interpolants
---

# SplineFlow: Flow Matching for Dynamical Systems with B-Spline Interpolants
**arXiv**：[2601.23072v1](https://arxiv.org/abs/2601.23072) · [PDF](https://arxiv.org/pdf/2601.23072.pdf)  
**作者**：Santanu Subhash Rathod, Pietro Liò, Xiao Zhang  

**一句话要点**：提出SplineFlow，利用B样条插值解决动态系统中流匹配建模高阶动力学的问题。

**关键词**：流匹配, 动态系统建模, B样条插值, 生成模型, 轨迹推断

## 3 点简述
- 核心问题：现有流匹配方法使用线性插值，难以准确建模动态系统的高阶动力学，尤其在不规则采样观测下。
- 方法要点：引入B样条插值构建条件路径，利用其平滑性和稳定性满足多边际约束，以结构化方式学习复杂动力学。
- 实验或效果：在多种确定性和随机动态系统及细胞轨迹推断任务中，SplineFlow相比基线方法表现出显著改进。

## 摘要（原文）

> Flow matching is a scalable generative framework for characterizing continuous normalizing flows with wide-range applications. However, current state-of-the-art methods are not well-suited for modeling dynamical systems, as they construct conditional paths using linear interpolants that may not capture the underlying state evolution, especially when learning higher-order dynamics from irregular sampled observations. Constructing unified paths that satisfy multi-marginal constraints across observations is challenging, since naïve higher-order polynomials tend to be unstable and oscillatory. We introduce SplineFlow, a theoretically grounded flow matching algorithm that jointly models conditional paths across observations via B-spline interpolation. Specifically, SplineFlow exploits the smoothness and stability of B-spline bases to learn the complex underlying dynamics in a structured manner while ensuring the multi-marginal requirements are met. Comprehensive experiments across various deterministic and stochastic dynamical systems of varying complexity, as well as on cellular trajectory inference tasks, demonstrate the strong improvement of SplineFlow over existing baselines. Our code is available at: https://github.com/santanurathod/SplineFlow.

