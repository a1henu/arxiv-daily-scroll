---
layout: default
title: ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation
---

# ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation
**arXiv**：[2603.03279v1](https://arxiv.org/abs/2603.03279) · [PDF](https://arxiv.org/pdf/2603.03279.pdf)  
**作者**：Xialin He, Sirui Xu, Xinyao Li, Runpei Dong, Liuyu Bian, Yu-Xiong Wang, Liang-Yan Gui  

**一句话要点**：提出ULTRA框架以解决人形机器人全身运动操控的自主性与泛化性问题

**关键词**：人形机器人, 全身运动操控, 多模态控制, 神经重定向, 强化学习, 自我中心感知

## 3 点简述
- 核心问题：现有方法依赖预定义运动参考，难以从感知和高级任务规范生成行为，且技能库扩展受限
- 方法要点：结合物理驱动神经重定向算法和统一多模态控制器，支持密集参考与稀疏任务规范，通过强化学习微调提升鲁棒性
- 实验或效果：在仿真和真实人形机器人上评估，ULTRA从自我中心感知实现自主目标条件全身操控，优于仅跟踪基线

## 摘要（原文）

> Achieving autonomous and versatile whole-body loco-manipulation remains a central barrier to making humanoids practically useful. Yet existing approaches are fundamentally constrained: retargeted data are often scarce or low-quality; methods struggle to scale to large skill repertoires; and, most importantly, they rely on tracking predefined motion references rather than generating behavior from perception and high-level task specifications. To address these limitations, we propose ULTRA, a unified framework with two key components. First, we introduce a physics-driven neural retargeting algorithm that translates large-scale motion capture to humanoid embodiments while preserving physical plausibility for contact-rich interactions. Second, we learn a unified multimodal controller that supports both dense references and sparse task specifications, under sensing ranging from accurate motion-capture state to noisy egocentric visual inputs. We distill a universal tracking policy into this controller, compress motor skills into a compact latent space, and apply reinforcement learning finetuning to expand coverage and improve robustness under out-of-distribution scenarios. This enables coordinated whole-body behavior from sparse intent without test-time reference motions. We evaluate ULTRA in simulation and on a real Unitree G1 humanoid. Results show that ULTRA generalizes to autonomous, goal-conditioned whole-body loco-manipulation from egocentric perception, consistently outperforming tracking-only baselines with limited skills.

