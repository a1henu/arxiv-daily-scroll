---
layout: default
title: Sampling-Based Optimization with Parallelized Physics Simulator for Bimanual Manipulation
---

# Sampling-Based Optimization with Parallelized Physics Simulator for Bimanual Manipulation
**arXiv**：[2511.21264v1](https://arxiv.org/abs/2511.21264) · [PDF](https://arxiv.org/pdf/2511.21264.pdf)  
**作者**：Iryna Hurova, Alinjar Dan, Karl Kruusamäe, Arun Kumar Singh  

**一句话要点**：提出基于采样的优化框架，利用GPU加速物理模拟器解决双手机器人在杂乱环境中的操作任务

**关键词**：双手机器人操作, 采样优化, GPU加速模拟, 模型预测控制, 模拟到真实转移

## 3 点简述
- 核心问题：端到端学习方法在双手机器人操作中难以泛化到新场景，尤其在杂乱环境。
- 方法要点：定制MPPI算法，结合任务特定成本函数和GPU加速MuJoCo模拟器进行高效优化。
- 实验或效果：在PerAct²基准任务上实现实时性能和成功模拟到真实世界的转移。

## 摘要（原文）

> In recent years, dual-arm manipulation has become an area of strong interest in robotics, with end-to-end learning emerging as the predominant strategy for solving bimanual tasks. A critical limitation of such learning-based approaches, however, is their difficulty in generalizing to novel scenarios, especially within cluttered environments. This paper presents an alternative paradigm: a sampling-based optimization framework that utilizes a GPU-accelerated physics simulator as its world model. We demonstrate that this approach can solve complex bimanual manipulation tasks in the presence of static obstacles. Our contribution is a customized Model Predictive Path Integral Control (MPPI) algorithm, \textbf{guided by carefully designed task-specific cost functions,} that uses GPU-accelerated MuJoCo for efficiently evaluating robot-object interaction. We apply this method to solve significantly more challenging versions of tasks from the PerAct$^{2}$ benchmark, such as requiring the point-to-point transfer of a ball through an obstacle course. Furthermore, we establish that our method achieves real-time performance on commodity GPUs and facilitates successful sim-to-real transfer by leveraging unique features within MuJoCo. The paper concludes with a statistical analysis of the sample complexity and robustness, quantifying the performance of our approach. The project website is available at: https://sites.google.com/view/bimanualakslabunitartu .

