---
layout: default
title: Self-adapting Robotic Agents through Online Continual Reinforcement Learning with World Model Feedback
---

# Self-adapting Robotic Agents through Online Continual Reinforcement Learning with World Model Feedback
**arXiv**：[2603.04029v1](https://arxiv.org/abs/2603.04029) · [PDF](https://arxiv.org/pdf/2603.04029.pdf)  
**作者**：Fabian Domberg, Georg Schildbach  

**一句话要点**：提出基于世界模型反馈的在线持续强化学习框架，使机器人能在部署中自适应环境变化。

**关键词**：在线持续强化学习, 世界模型反馈, 机器人自适应控制, 分布外检测, 模型微调

## 3 点简述
- 核心问题：离线训练的机器人控制器难以应对部署中的未预见变化，适应能力有限。
- 方法要点：基于DreamerV3，利用世界模型预测残差检测分布外事件，自动触发微调，无需外部监督评估收敛。
- 实验或效果：在连续控制问题中验证，包括四足机器人仿真和真实模型车辆，展示自适应性能与权衡。

## 摘要（原文）

> As learning-based robotic controllers are typically trained offline and deployed with fixed parameters, their ability to cope with unforeseen changes during operation is limited. Biologically inspired, this work presents a framework for online Continual Reinforcement Learning that enables automated adaptation during deployment. Building on DreamerV3, a model-based Reinforcement Learning algorithm, the proposed method leverages world model prediction residuals to detect out-of-distribution events and automatically trigger finetuning. Adaptation progress is monitored using both task-level performance signals and internal training metrics, allowing convergence to be assessed without external supervision and domain knowledge. The approach is validated on a variety of contemporary continuous control problems, including a quadruped robot in high-fidelity simulation, and a real-world model vehicle. Relevant metrics and their interpretation are presented and discussed, as well as resulting trade-offs described. The results sketch out how autonomous robotic agents could once move beyond static training regimes toward adaptive systems capable of self-reflection and -improvement during operation, just like their biological counterparts.

