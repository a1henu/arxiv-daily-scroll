---
layout: default
title: PhysicsMind: Sim and Real Mechanics Benchmarking for Physical Reasoning and Prediction in Foundational VLMs and World Models
---

# PhysicsMind: Sim and Real Mechanics Benchmarking for Physical Reasoning and Prediction in Foundational VLMs and World Models
**arXiv**：[2601.16007v1](https://arxiv.org/abs/2601.16007) · [PDF](https://arxiv.org/pdf/2601.16007.pdf)  
**作者**：Chak-Wing Mak, Guanyu Zhu, Boyi Zhang, Hongji Li, Xiaowei Chi, Kevin Zhang, Yichen Wu, Yangfan He, Chun-Kai Fan, Wentao Lu, Kuangzhi Ge, Xinyu Fang, Hongyang He, Kuan Lu, Tianxiang Xu, Li Zhang, Yongxin Ni, Youhua Li, Shanghang Zhang  

**一句话要点**：提出PhysicsMind基准，结合仿真与真实环境评估多模态大模型和世界模型的物理推理与预测能力

**关键词**：物理推理基准, 多模态大模型评估, 视频生成任务, 力学原理, 仿真与真实环境, 视觉问答

## 3 点简述
- 核心问题：现有基准在评估多模态大模型和世界模型的物理理解方面存在碎片化，依赖合成数据或与物理定律无关的感知质量
- 方法要点：引入统一基准，包含真实和仿真环境，基于质心、杠杆平衡和牛顿第一定律设计视觉问答和视频生成任务
- 实验或效果：评估多种模型，发现它们依赖外观启发式并常违反基本力学，表明当前训练不足，PhysicsMind可作为物理感知模型的测试平台

## 摘要（原文）

> Modern foundational Multimodal Large Language Models (MLLMs) and video world models have advanced significantly in mathematical, common-sense, and visual reasoning, but their grasp of the underlying physics remains underexplored. Existing benchmarks attempting to measure this matter rely on synthetic, Visual Question Answer templates or focus on perceptual video quality that is tangential to measuring how well the video abides by physical laws. To address this fragmentation, we introduce PhysicsMind, a unified benchmark with both real and simulation environments that evaluates law-consistent reasoning and generation over three canonical principles: Center of Mass, Lever Equilibrium, and Newton's First Law. PhysicsMind comprises two main tasks: i) VQA tasks, testing whether models can reason and determine physical quantities and values from images or short videos, and ii) Video Generation(VG) tasks, evaluating if predicted motion trajectories obey the same center-of-mass, torque, and inertial constraints as the ground truth. A broad range of recent models and video generation models is evaluated on PhysicsMind and found to rely on appearance heuristics while often violating basic mechanics. These gaps indicate that current scaling and training are still insufficient for robust physical understanding, underscoring PhysicsMind as a focused testbed for physics-aware multimodal models. Our data will be released upon acceptance.

