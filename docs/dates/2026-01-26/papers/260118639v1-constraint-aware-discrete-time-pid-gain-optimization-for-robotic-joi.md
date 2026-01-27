---
layout: default
title: Constraint-Aware Discrete-Time PID Gain Optimization for Robotic Joint Control Under Actuator Saturation
---

# Constraint-Aware Discrete-Time PID Gain Optimization for Robotic Joint Control Under Actuator Saturation
**arXiv**：[2601.18639v1](https://arxiv.org/abs/2601.18639) · [PDF](https://arxiv.org/pdf/2601.18639.pdf)  
**作者**：Ojasva Mishra, Xiaolong Wu, Min Xu  

**一句话要点**：提出约束感知离散时间PID增益优化方法，以解决机器人关节控制中执行器饱和下的鲁棒性问题。

**关键词**：机器人关节控制, 离散时间PID, 执行器饱和, 贝叶斯优化, 鲁棒控制, 抗饱和设计

## 3 点简述
- 核心问题：离散时间执行、执行器饱和及小延迟导致PID控制偏离连续时间理论，影响机器人关节精确调节。
- 方法要点：基于Jury准则推导PI稳定性区域，评估反计算抗饱和实现，并设计混合认证贝叶斯优化工作流优化鲁棒IAE目标。
- 实验或效果：在模拟不确定性、延迟、噪声和更紧饱和条件下，鲁棒调优将中位数IAE从0.843降至0.430，超调低于2%。

## 摘要（原文）

> The precise regulation of rotary actuation is fundamental in autonomous robotics, yet practical PID loops deviate from continuous-time theory due to discrete-time execution, actuator saturation, and small delays and measurement imperfections. We present an implementation-aware analysis and tuning workflow for saturated discrete-time joint control. We (i) derive PI stability regions under Euler and exact zero-order-hold (ZOH) discretizations using the Jury criterion, (ii) evaluate a discrete back-calculation anti-windup realization under saturation-dominant regimes, and (iii) propose a hybrid-certified Bayesian optimization workflow that screens analytically unstable candidates and behaviorally unsafe transients while optimizing a robust IAE objective with soft penalties on overshoot and saturation duty. Baseline sweeps ($τ=1.0$~s, $Δt=0.01$~s, $u\in[-10,10]$) quantify rise/settle trends for P/PI/PID. Under a randomized model family emulating uncertainty, delay, noise, quantization, and tighter saturation, robustness-oriented tuning improves median IAE from $0.843$ to $0.430$ while keeping median overshoot below $2\%$. In simulation-only tuning, the certification screen rejects $11.6\%$ of randomly sampled gains within bounds before full robust evaluation, improving sample efficiency without hardware experiments.

