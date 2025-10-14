---
layout: default
title: Phys2Real: Fusing VLM Priors with Interactive Online Adaptation for Uncertainty-Aware Sim-to-Real Manipulation
---

# Phys2Real: Fusing VLM Priors with Interactive Online Adaptation for Uncertainty-Aware Sim-to-Real Manipulation
**arXiv**：[2510.11689v1](https://arxiv.org/abs/2510.11689) · [PDF](https://arxiv.org/pdf/2510.11689.pdf)  
**作者**：Maggie Wang, Stephen Tian, Aiden Swann, Ola Shorinwa, Jiajun Wu, Mac Schwager  

**一句话要点**：提出Phys2Real方法，融合VLM先验与在线适应以解决仿真到真实机器人操作中的不确定性挑战

**关键词**：仿真到真实转移, 机器人操作, 不确定性融合, 视觉语言模型, 在线适应, 物理参数估计

## 3 点简述
- 核心问题：仿真到真实机器人操作转移困难，尤其涉及精确动力学任务
- 方法要点：结合VLM推断物理参数先验与在线交互数据，通过不确定性融合优化策略
- 实验效果：在T块和锤子推动任务中，成功率显著提升，优于领域随机化基线

## 摘要（原文）

> Learning robotic manipulation policies directly in the real world can be
> expensive and time-consuming. While reinforcement learning (RL) policies
> trained in simulation present a scalable alternative, effective sim-to-real
> transfer remains challenging, particularly for tasks that require precise
> dynamics. To address this, we propose Phys2Real, a real-to-sim-to-real RL
> pipeline that combines vision-language model (VLM)-inferred physical parameter
> estimates with interactive adaptation through uncertainty-aware fusion. Our
> approach consists of three core components: (1) high-fidelity geometric
> reconstruction with 3D Gaussian splatting, (2) VLM-inferred prior distributions
> over physical parameters, and (3) online physical parameter estimation from
> interaction data. Phys2Real conditions policies on interpretable physical
> parameters, refining VLM predictions with online estimates via ensemble-based
> uncertainty quantification. On planar pushing tasks of a T-block with varying
> center of mass (CoM) and a hammer with an off-center mass distribution,
> Phys2Real achieves substantial improvements over a domain randomization
> baseline: 100% vs 79% success rate for the bottom-weighted T-block, 57% vs 23%
> in the challenging top-weighted T-block, and 15% faster average task completion
> for hammer pushing. Ablation studies indicate that the combination of VLM and
> interaction information is essential for success. Project website:
> https://phys2real.github.io/ .

