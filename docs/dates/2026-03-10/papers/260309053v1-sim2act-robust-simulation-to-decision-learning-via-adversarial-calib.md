---
layout: default
title: Sim2Act: Robust Simulation-to-Decision Learning via Adversarial Calibration and Group-Relative Perturbation
---

# Sim2Act: Robust Simulation-to-Decision Learning via Adversarial Calibration and Group-Relative Perturbation
**arXiv**：[2603.09053v1](https://arxiv.org/abs/2603.09053) · [PDF](https://arxiv.org/pdf/2603.09053.pdf)  
**作者**：Hongyu Cao, Jinghan Zhang, Kunpeng Liu, Dongjie Wang, Feng Xia, Haifeng Chen, Xiaohua Hu, Yanjie Fu  

**一句话要点**：提出Sim2Act框架，通过对抗校准和组相对扰动增强仿真到决策学习的鲁棒性。

**关键词**：仿真到决策学习, 对抗校准, 组相对扰动, 鲁棒性增强, 供应链优化

## 3 点简述
- 核心问题：基于噪声或偏差数据学习的仿真器在决策关键区域存在预测误差，导致动作排序不稳定和策略不可靠。
- 方法要点：引入对抗校准机制重加权仿真误差，并开发组相对扰动策略稳定策略学习。
- 实验或效果：在多个供应链基准测试中，展示了改进的仿真鲁棒性和更稳定的决策性能。

## 摘要（原文）

> Simulation-to-decision learning enables safe policy training in digital environments without risking real-world deployment, and has become essential in mission-critical domains such as supply chains and industrial systems. However, simulators learned from noisy or biased real-world data often exhibit prediction errors in decision-critical regions, leading to unstable action ranking and unreliable policies. Existing approaches either focus on improving average simulation fidelity or adopt conservative regularization, which may cause policy collapse by discarding high-risk high-reward actions.
>   We propose Sim2Act, a robust simulation-to-decision framework that addresses both simulator and policy robustness. First, we introduce an adversarial calibration mechanism that re-weights simulation errors in decision-critical state-action pairs to align surrogate fidelity with downstream decision impact. Second, we develop a group-relative perturbation strategy that stabilizes policy learning under simulator uncertainty without enforcing overly pessimistic constraints. Extensive experiments on multiple supply chain benchmarks demonstrate improved simulation robustness and more stable decision performance under structured and unstructured perturbations.

