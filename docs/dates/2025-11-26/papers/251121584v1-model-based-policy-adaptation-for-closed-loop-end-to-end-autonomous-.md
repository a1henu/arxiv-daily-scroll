---
layout: default
title: Model-Based Policy Adaptation for Closed-Loop End-to-End Autonomous Driving
---

# Model-Based Policy Adaptation for Closed-Loop End-to-End Autonomous Driving
**arXiv**：[2511.21584v1](https://arxiv.org/abs/2511.21584) · [PDF](https://arxiv.org/pdf/2511.21584.pdf)  
**作者**：Haohong Lin, Yunzhi Zhang, Wenhao Ding, Jiajun Wu, Ding Zhao  

**一句话要点**：提出模型策略适应框架以增强端到端自动驾驶在闭环中的鲁棒性

**关键词**：端到端自动驾驶, 模型策略适应, 反事实轨迹生成, 扩散模型, 闭环仿真, 鲁棒性增强

## 3 点简述
- 端到端自动驾驶模型在闭环中易出现级联错误和泛化差问题
- 使用几何一致模拟生成反事实轨迹，训练扩散策略适配器和多步Q值模型
- 在nuScenes基准上显著提升域内、域外和安全关键场景性能

## 摘要（原文）

> End-to-end (E2E) autonomous driving models have demonstrated strong performance in open-loop evaluations but often suffer from cascading errors and poor generalization in closed-loop settings. To address this gap, we propose Model-based Policy Adaptation (MPA), a general framework that enhances the robustness and safety of pretrained E2E driving agents during deployment. MPA first generates diverse counterfactual trajectories using a geometry-consistent simulation engine, exposing the agent to scenarios beyond the original dataset. Based on this generated data, MPA trains a diffusion-based policy adapter to refine the base policy's predictions and a multi-step Q value model to evaluate long-term outcomes. At inference time, the adapter proposes multiple trajectory candidates, and the Q value model selects the one with the highest expected utility. Experiments on the nuScenes benchmark using a photorealistic closed-loop simulator demonstrate that MPA significantly improves performance across in-domain, out-of-domain, and safety-critical scenarios. We further investigate how the scale of counterfactual data and inference-time guidance strategies affect overall effectiveness.

