---
layout: default
title: Force-Aware Residual DAgger via Trajectory Editing for Precision Insertion with Impedance Control
---

# Force-Aware Residual DAgger via Trajectory Editing for Precision Insertion with Impedance Control
**arXiv**：[2603.04038v1](https://arxiv.org/abs/2603.04038) · [PDF](https://arxiv.org/pdf/2603.04038.pdf)  
**作者**：Yiou Huang, Ma Ning, Weichu Zhao, Zinuo Liu, Jun Sun, Qiufeng Wang, Yaran Chen  

**一句话要点**：提出TER-DAgger框架，通过轨迹编辑和力感知机制解决模仿学习在接触式精密插入任务中的协变量偏移和专家监控问题。

**关键词**：模仿学习, 轨迹编辑, 力感知, 阻抗控制, 精密插入, 人机交互

## 3 点简述
- 核心问题：模仿学习在接触式精密插入任务中面临协变量偏移和执行失败需持续专家监控的挑战。
- 方法要点：基于轨迹编辑学习残差策略，融合策略执行与人类校正轨迹，并引入力感知失败预测机制。
- 实验或效果：在仿真和真实任务中，相比基线方法平均成功率提升超过37%，验证了框架的有效性。

## 摘要（原文）

> Imitation learning (IL) has shown strong potential for contact-rich precision insertion tasks. However, its practical deployment is often hindered by covariate shift and the need for continuous expert monitoring to recover from failures during execution. In this paper, we propose Trajectory Editing Residual Dataset Aggregation (TER-DAgger), a scalable and force-aware human-in-the-loop imitation learning framework that mitigates covariate shift by learning residual policies through optimization-based trajectory editing. This approach smoothly fuses policy rollouts with human corrective trajectories, providing consistent and stable supervision. Second, we introduce a force-aware failure anticipation mechanism that triggers human intervention only when discrepancies arise between predicted and measured end-effector forces, significantly reducing the requirement for continuous expert monitoring. Third, all learned policies are executed within a Cartesian impedance control framework, ensuring compliant and safe behavior during contact-rich interactions. Extensive experiments in both simulation and real-world precision insertion tasks show that TER-DAgger improves the average success rate by over 37\% compared to behavior cloning, human-guided correction, retraining, and fine-tuning baselines, demonstrating its effectiveness in mitigating covariate shift and enabling scalable deployment in contact-rich manipulation.

