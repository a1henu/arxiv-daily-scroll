---
layout: default
title: STRIDE: Structured Lagrangian and Stochastic Residual Dynamics via Flow Matching
---

# STRIDE: Structured Lagrangian and Stochastic Residual Dynamics via Flow Matching
**arXiv**：[2603.08478v1](https://arxiv.org/abs/2603.08478) · [PDF](https://arxiv.org/pdf/2603.08478.pdf)  
**作者**：Prakrut Kotecha, Ganga Nair B, Shishir Kolathaya  

**一句话要点**：提出STRIDE框架，通过结构化拉格朗日与随机残差动力学解决机器人不确定环境中的建模问题。

**关键词**：动力学学习, 拉格朗日神经网络, 条件流匹配, 机器人建模, 不确定性处理, 物理一致性

## 3 点简述
- 核心问题：机器人非结构化环境中存在间歇接触、摩擦变化等不确定性，现有模型难以平衡物理一致性与复杂交互效应。
- 方法要点：结合拉格朗日神经网络保持保守力学结构，使用条件流匹配捕捉多模态随机残差力，端到端联合训练。
- 实验或效果：在摆、四足机器人、人形机器人上验证，相比确定性基线，长时预测误差减少20%，接触力预测误差减少30%。

## 摘要（原文）

> Robotic systems operating in unstructured environments must operate under significant uncertainty arising from intermittent contacts, frictional variability, and unmodeled compliance. While recent model-free approaches have demonstrated impressive performance, many deployment settings still require predictive models that support planning, constraint handling, and online adaptation. Analytical rigid-body models provide strong physical structure but often fail to capture complex interaction effects, whereas purely data-driven models may violate physical consistency, exhibit data bias, and accumulate long-horizon drift. In this work, we propose STRIDE, a dynamics learning framework that explicitly separates conservative rigid-body mechanics from uncertain, effectively stochastic non-conservative interaction effects. The structured component is modeled using a Lagrangian Neural Network (LNN) to preserve energy-consistent inertial dynamics, while residual interaction forces are represented using Conditional Flow Matching (CFM) to capture multi-modal interaction phenomena. The two components are trained jointly end-to-end, enabling the model to retain physical structure while representing complex stochastic behavior. We evaluate STRIDE on systems of increasing complexity, including a pendulum, the Unitree Go1 quadruped, and the Unitree G1 humanoid. Results show 20% reduction in long-horizon prediction error and 30% reduction in contact force prediction error compared to deterministic residual baselines, supporting more reliable model-based control in uncertain robotic environments.

