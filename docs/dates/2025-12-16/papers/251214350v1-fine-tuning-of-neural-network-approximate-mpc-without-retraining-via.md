---
layout: default
title: Fine-Tuning of Neural Network Approximate MPC without Retraining via Bayesian Optimization
---

# Fine-Tuning of Neural Network Approximate MPC without Retraining via Bayesian Optimization
**arXiv**：[2512.14350v1](https://arxiv.org/abs/2512.14350) · [PDF](https://arxiv.org/pdf/2512.14350.pdf)  
**作者**：Henrik Hose, Paul Brunzema, Alexander von Rohr, Alexander Gräfe, Angela P. Schoellig, Sebastian Trimpe  

**一句话要点**：提出基于贝叶斯优化的近似模型预测控制微调方法，无需重新训练神经网络

**关键词**：近似模型预测控制, 贝叶斯优化, 神经网络微调, 硬件实验, 自动参数调整

## 3 点简述
- 核心问题：近似模型预测控制部署时需手动微调参数，过程繁琐且不直观
- 方法要点：利用贝叶斯优化结合实验数据自动调整参数，避免重新生成数据集和训练
- 实验或效果：在硬件实验中实现优于名义近似模型预测控制的性能，如倒立摆和独轮机器人控制

## 摘要（原文）

> Approximate model-predictive control (AMPC) aims to imitate an MPC's behavior with a neural network, removing the need to solve an expensive optimization problem at runtime. However, during deployment, the parameters of the underlying MPC must usually be fine-tuned. This often renders AMPC impractical as it requires repeatedly generating a new dataset and retraining the neural network. Recent work addresses this problem by adapting AMPC without retraining using approximated sensitivities of the MPC's optimization problem. Currently, this adaption must be done by hand, which is labor-intensive and can be unintuitive for high-dimensional systems. To solve this issue, we propose using Bayesian optimization to tune the parameters of AMPC policies based on experimental data. By combining model-based control with direct and local learning, our approach achieves superior performance to nominal AMPC on hardware, with minimal experimentation. This allows automatic and data-efficient adaptation of AMPC to new system instances and fine-tuning to cost functions that are difficult to directly implement in MPC. We demonstrate the proposed method in hardware experiments for the swing-up maneuver on an inverted cartpole and yaw control of an under-actuated balancing unicycle robot, a challenging control problem.

