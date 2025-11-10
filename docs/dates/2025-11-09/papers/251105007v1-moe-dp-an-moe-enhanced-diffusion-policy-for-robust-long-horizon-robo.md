---
layout: default
title: MoE-DP: An MoE-Enhanced Diffusion Policy for Robust Long-Horizon Robotic Manipulation with Skill Decomposition and Failure Recovery
---

# MoE-DP: An MoE-Enhanced Diffusion Policy for Robust Long-Horizon Robotic Manipulation with Skill Decomposition and Failure Recovery
**arXiv**：[2511.05007v1](https://arxiv.org/abs/2511.05007) · [PDF](https://arxiv.org/pdf/2511.05007.pdf)  
**作者**：Baiye Cheng, Tianhai Liang, Suning Huang, Maanping Shao, Feihong Zhang, Botian Xu, Zhengrong Xue, Huazhe Xu  

**一句话要点**：提出MoE-DP以增强长视野机器人操作中的鲁棒性和可解释性

**关键词**：扩散策略, 机器人操作, 专家混合, 技能分解, 失败恢复, 可解释学习

## 3 点简述
- 扩散策略在长视野多阶段任务中缺乏从子任务失败中恢复的鲁棒性
- 在视觉编码器和扩散模型间插入MoE层，分解知识为专家处理不同任务阶段
- 在6个模拟任务中，扰动条件下成功率平均相对提升36%，并验证于真实世界

## 摘要（原文）

> Diffusion policies have emerged as a powerful framework for robotic
> visuomotor control, yet they often lack the robustness to recover from subtask
> failures in long-horizon, multi-stage tasks and their learned representations
> of observations are often difficult to interpret. In this work, we propose the
> Mixture of Experts-Enhanced Diffusion Policy (MoE-DP), where the core idea is
> to insert a Mixture of Experts (MoE) layer between the visual encoder and the
> diffusion model. This layer decomposes the policy's knowledge into a set of
> specialized experts, which are dynamically activated to handle different phases
> of a task. We demonstrate through extensive experiments that MoE-DP exhibits a
> strong capability to recover from disturbances, significantly outperforming
> standard baselines in robustness. On a suite of 6 long-horizon simulation
> tasks, this leads to a 36% average relative improvement in success rate under
> disturbed conditions. This enhanced robustness is further validated in the real
> world, where MoE-DP also shows significant performance gains. We further show
> that MoE-DP learns an interpretable skill decomposition, where distinct experts
> correspond to semantic task primitives (e.g., approaching, grasping). This
> learned structure can be leveraged for inference-time control, allowing for the
> rearrangement of subtasks without any re-training.Our video and code are
> available at the https://moe-dp-website.github.io/MoE-DP-Website/.

