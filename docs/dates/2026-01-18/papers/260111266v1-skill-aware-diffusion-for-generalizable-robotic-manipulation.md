---
layout: default
title: Skill-Aware Diffusion for Generalizable Robotic Manipulation
---

# Skill-Aware Diffusion for Generalizable Robotic Manipulation
**arXiv**：[2601.11266v1](https://arxiv.org/abs/2601.11266) · [PDF](https://arxiv.org/pdf/2601.11266.pdf)  
**作者**：Aoshen Huang, Jiaming Chen, Jiyu Cheng, Ran Song, Wei Pan, Wei Zhang  

**一句话要点**：提出技能感知扩散模型以提升机器人操作的泛化能力

**关键词**：机器人操作, 扩散模型, 技能感知, 泛化学习, 运动流生成

## 3 点简述
- 核心问题：现有方法依赖数据和网络扩展，忽视技能级信息，导致泛化受限
- 方法要点：通过技能感知编码和技能约束扩散模型，生成以物体为中心的运动流
- 实验或效果：在仿真和真实环境中验证了模型在多种操作任务中的良好性能和泛化

## 摘要（原文）

> Robust generalization in robotic manipulation is crucial for robots to adapt flexibly to diverse environments. Existing methods usually improve generalization by scaling data and networks, but model tasks independently and overlook skill-level information. Observing that tasks within the same skill share similar motion patterns, we propose Skill-Aware Diffusion (SADiff), which explicitly incorporates skill-level information to improve generalization. SADiff learns skill-specific representations through a skill-aware encoding module with learnable skill tokens, and conditions a skill-constrained diffusion model to generate object-centric motion flow. A skill-retrieval transformation strategy further exploits skill-specific trajectory priors to refine the mapping from 2D motion flow to executable 3D actions. Furthermore, we introduce IsaacSkill, a high-fidelity dataset containing fundamental robotic skills for comprehensive evaluation and sim-to-real transfer. Experiments in simulation and real-world settings show that SADiff achieves good performance and generalization across various manipulation tasks. Code, data, and videos are available at https://sites.google.com/view/sa-diff.

