---
layout: default
title: MobileManiBench: Simplifying Model Verification for Mobile Manipulation
---

# MobileManiBench: Simplifying Model Verification for Mobile Manipulation
**arXiv**：[2602.05233v1](https://arxiv.org/abs/2602.05233) · [PDF](https://arxiv.org/pdf/2602.05233.pdf)  
**作者**：Wenbo Wang, Fangyun Wei, QiXiu Li, Xi Chen, Yaobo Liang, Chang Xu, Jiaolong Yang, Baining Guo  

**一句话要点**：提出MobileManiBench仿真基准以简化移动操作模型的验证

**关键词**：移动操作基准, 仿真验证, 视觉-语言-动作模型, 强化学习生成, 机器人仿真

## 3 点简述
- 核心问题：现有视觉-语言-动作模型依赖静态桌面场景数据集，限制移动操作验证。
- 方法要点：基于NVIDIA Isaac Sim和强化学习，自动生成多样化轨迹与丰富标注的仿真框架。
- 实验或效果：包含300K轨迹，支持机器人本体、感知模态和策略架构的受控研究。

## 摘要（原文）

> Vision-language-action models have advanced robotic manipulation but remain constrained by reliance on the large, teleoperation-collected datasets dominated by the static, tabletop scenes. We propose a simulation-first framework to verify VLA architectures before real-world deployment and introduce MobileManiBench, a large-scale benchmark for mobile-based robotic manipulation. Built on NVIDIA Isaac Sim and powered by reinforcement learning, our pipeline autonomously generates diverse manipulation trajectories with rich annotations (language instructions, multi-view RGB-depth-segmentation images, synchronized object/robot states and actions). MobileManiBench features 2 mobile platforms (parallel-gripper and dexterous-hand robots), 2 synchronized cameras (head and right wrist), 630 objects in 20 categories, 5 skills (open, close, pull, push, pick) with over 100 tasks performed in 100 realistic scenes, yielding 300K trajectories. This design enables controlled, scalable studies of robot embodiments, sensing modalities, and policy architectures, accelerating research on data efficiency and generalization. We benchmark representative VLA models and report insights into perception, reasoning, and control in complex simulated environments.

