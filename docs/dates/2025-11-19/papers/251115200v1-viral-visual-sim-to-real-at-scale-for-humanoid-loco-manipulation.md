---
layout: default
title: VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation
---

# VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation
**arXiv**：[2511.15200v1](https://arxiv.org/abs/2511.15200) · [PDF](https://arxiv.org/pdf/2511.15200.pdf)  
**作者**：Tairan He, Zi Wang, Haoru Xue, Qingwei Ben, Zhengyi Luo, Wenli Xiao, Ye Yuan, Xingye Da, Fernando Castañeda, Shankar Sastry, Changliu Liu, Guanya Shi, Linxi Fan, Yuke Zhu  

**一句话要点**：提出VIRAL视觉模拟到现实框架，实现人形机器人零样本部署的自主移动操作

**关键词**：人形机器人, 模拟到现实, 视觉策略, 师生蒸馏, 域随机化, 移动操作

## 3 点简述
- 核心问题：人形机器人缺乏自主移动操作技能，阻碍真实世界部署。
- 方法要点：采用师生设计，特权强化学习教师蒸馏视觉学生策略，结合大规模模拟和视觉域随机化。
- 实验效果：在Unitree G1人形机器人上实现连续移动操作，泛化性强，无需真实世界微调。

## 摘要（原文）

> A key barrier to the real-world deployment of humanoid robots is the lack of autonomous loco-manipulation skills. We introduce VIRAL, a visual sim-to-real framework that learns humanoid loco-manipulation entirely in simulation and deploys it zero-shot to real hardware. VIRAL follows a teacher-student design: a privileged RL teacher, operating on full state, learns long-horizon loco-manipulation using a delta action space and reference state initialization. A vision-based student policy is then distilled from the teacher via large-scale simulation with tiled rendering, trained with a mixture of online DAgger and behavior cloning. We find that compute scale is critical: scaling simulation to tens of GPUs (up to 64) makes both teacher and student training reliable, while low-compute regimes often fail. To bridge the sim-to-real gap, VIRAL combines large-scale visual domain randomization over lighting, materials, camera parameters, image quality, and sensor delays--with real-to-sim alignment of the dexterous hands and cameras. Deployed on a Unitree G1 humanoid, the resulting RGB-based policy performs continuous loco-manipulation for up to 54 cycles, generalizing to diverse spatial and appearance variations without any real-world fine-tuning, and approaching expert-level teleoperation performance. Extensive ablations dissect the key design choices required to make RGB-based humanoid loco-manipulation work in practice.

