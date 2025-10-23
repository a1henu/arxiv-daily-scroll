---
layout: default
title: LaViRA: Language-Vision-Robot Actions Translation for Zero-Shot Vision Language Navigation in Continuous Environments
---

# LaViRA: Language-Vision-Robot Actions Translation for Zero-Shot Vision Language Navigation in Continuous Environments
**arXiv**：[2510.19655v1](https://arxiv.org/abs/2510.19655) · [PDF](https://arxiv.org/pdf/2510.19655.pdf)  
**作者**：Hongyu Ding, Ziming Xu, Yudong Fang, You Wu, Zixuan Chen, Jieqi Shi, Jing Huo, Yifan Zhang, Yang Gao  

**一句话要点**：提出LaViRA框架以解决零样本视觉语言导航中的泛化与推理权衡问题

**关键词**：零样本导航, 视觉语言导航, 多模态大模型, 动作分解, 连续环境

## 3 点简述
- 核心问题：零样本视觉语言导航在连续环境中面临泛化与推理能力的权衡
- 方法要点：采用语言-视觉-机器人动作的粗到细层次分解，利用多模态大模型优势
- 实验或效果：在VLN-CE基准上显著超越现有方法，展示优越泛化能力

## 摘要（原文）

> Zero-shot Vision-and-Language Navigation in Continuous Environments (VLN-CE)
> requires an agent to navigate unseen environments based on natural language
> instructions without any prior training. Current methods face a critical
> trade-off: either rely on environment-specific waypoint predictors that limit
> scene generalization, or underutilize the reasoning capabilities of large
> models during navigation. We introduce LaViRA, a simple yet effective zero-shot
> framework that addresses this dilemma by decomposing action into a
> coarse-to-fine hierarchy: Language Action for high-level planning, Vision
> Action for perceptual grounding, and Robot Action for robust navigation. This
> modular decomposition allows us to leverage the distinct strengths of different
> scales of Multimodal Large Language Models (MLLMs) at each stage, creating a
> system that is powerful in its reasoning, grounding and practical control.
> LaViRA significantly outperforms existing state-of-the-art methods on the
> VLN-CE benchmark, demonstrating superior generalization capabilities in unseen
> environments, while maintaining transparency and efficiency for real-world
> deployment.

