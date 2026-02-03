---
layout: default
title: RAPT: Model-Predictive Out-of-Distribution Detection and Failure Diagnosis for Sim-to-Real Humanoid Robots
---

# RAPT: Model-Predictive Out-of-Distribution Detection and Failure Diagnosis for Sim-to-Real Humanoid Robots
**arXiv**：[2602.01515v1](https://arxiv.org/abs/2602.01515) · [PDF](https://arxiv.org/pdf/2602.01515.pdf)  
**作者**：Humphrey Munn, Brendan Tidd, Peter Bohm, Marcus Gallagher, David Howard  

**一句话要点**：提出RAPT模型预测方法，用于人形机器人仿真到现实部署中的分布外检测与故障诊断

**关键词**：人形机器人, 分布外检测, 仿真到现实转移, 故障诊断, 模型预测监控, 可解释性分析

## 3 点简述
- 核心问题：仿真到现实转移中，策略在分布外状态可能自信执行，导致无声故障和硬件风险
- 方法要点：学习仿真中名义执行的概率时空流形，通过预测偏差实现校准的在线检测和可解释性度量
- 实验或效果：在仿真和物理硬件上评估，RAPT提升检测率并提供可操作的故障根因分析，准确率达75%

## 摘要（原文）

> Deploying learned control policies on humanoid robots is challenging: policies that appear robust in simulation can execute confidently in out-of-distribution (OOD) states after Sim-to-Real transfer, leading to silent failures that risk hardware damage. Although anomaly detection can mitigate these failures, prior methods are often incompatible with high-rate control, poorly calibrated at the extremely low false-positive rates required for practical deployment, or operate as black boxes that provide a binary stop signal without explaining why the robot drifted from nominal behavior. We present RAPT, a lightweight, self-supervised deployment-time monitor for 50Hz humanoid control. RAPT learns a probabilistic spatio-temporal manifold of nominal execution from simulation and evaluates execution-time predictive deviation as a calibrated, per-dimension signal. This yields (i) reliable online OOD detection under strict false-positive constraints and (ii) a continuous, interpretable measure of Sim-to-Real mismatch that can be tracked over time to quantify how far deployment has drifted from training. Beyond detection, we introduce an automated post-hoc root-cause analysis pipeline that combines gradient-based temporal saliency derived from RAPT's reconstruction objective with LLM-based reasoning conditioned on saliency and joint kinematics to produce semantic failure diagnoses in a zero-shot setting. We evaluate RAPT on a Unitree G1 humanoid across four complex tasks in simulation and on physical hardware. In large-scale simulation, RAPT improves True Positive Rate (TPR) by 37% over the strongest baseline at a fixed episode-level false positive rate of 0.5%. On real-world deployments, RAPT achieves a 12.5% TPR improvement and provides actionable interpretability, reaching 75% root-cause classification accuracy across 16 real-world failures using only proprioceptive data.

