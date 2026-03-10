---
layout: default
title: Towards Human-Like Manipulation through RL-Augmented Teleoperation and Mixture-of-Dexterous-Experts VLA
---

# Towards Human-Like Manipulation through RL-Augmented Teleoperation and Mixture-of-Dexterous-Experts VLA
**arXiv**：[2603.08122v1](https://arxiv.org/abs/2603.08122) · [PDF](https://arxiv.org/pdf/2603.08122.pdf)  
**作者**：Tutian Tang, Xingyu Ji, Wanli Xing, Ce Hao, Wenqiang Xu, Lin Shao, Cewu Lu, Qiaojun Yu, Jiangmiao Pang, Kaifeng Zhang  

**一句话要点**：提出IMCopilot与MoDE-VLA框架，以增强VLA模型在双手灵巧接触操作中的性能。

**关键词**：视觉语言动作模型, 灵巧操作, 强化学习, 多模态融合, 遥操作, 接触感知

## 3 点简述
- 核心问题：VLA模型在双手灵巧接触操作中面临数据获取、多技能学习和多模态融合挑战。
- 方法要点：结合强化学习技能辅助遥操作数据收集，并集成力触觉模态到VLA骨干网络。
- 实验或效果：在复杂任务中验证，相比基线在接触丰富任务中成功率翻倍提升。

## 摘要（原文）

> While Vision-Language-Action (VLA) models have demonstrated remarkable success in robotic manipulation, their application has largely been confined to low-degree-of-freedom end-effectors performing simple, vision-guided pick-and-place tasks. Extending these models to human-like, bimanual dexterous manipulation-specifically contact-rich in-hand operations-introduces critical challenges in high-fidelity data acquisition, multi-skill learning, and multimodal sensory fusion. In this paper, we propose an integrated framework to address these bottlenecks, built upon two components. First, we introduce IMCopilot (In-hand Manipulation Copilot), a suite of reinforcement learning-trained atomic skills that plays a dual role: it acts as a shared-autonomy assistant to simplify teleoperation data collection, and it serves as a callable low-level execution primitive for the VLA. Second, we present MoDE-VLA (Mixture-of-Dexterous-Experts VLA), an architecture that seamlessly integrates heterogeneous force and tactile modalities into a pretrained VLA backbone. By utilizing a residual injection mechanism, MoDE-VLA enables contact-aware refinement without degrading the model's pretrained knowledge. We validate our approach on four tasks of escalating complexity, demonstrating doubled success rate improvement over the baseline in dexterous contact-rich tasks.

