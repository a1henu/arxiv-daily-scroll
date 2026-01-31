---
layout: default
title: AIR-VLA: Vision-Language-Action Systems for Aerial Manipulation
---

# AIR-VLA: Vision-Language-Action Systems for Aerial Manipulation
**arXiv**：[2601.21602v1](https://arxiv.org/abs/2601.21602) · [PDF](https://arxiv.org/pdf/2601.21602.pdf)  
**作者**：Jianli Sun, Bin Tian, Qiyao Zhang, Chengxiang Li, Zihan Song, Zhiyong Cui, Yisheng Lv, Yonglin Tian  

**一句话要点**：提出AIR-VLA基准以解决空中操作系统中视觉-语言-动作模型的适应性问题

**关键词**：空中操作系统, 视觉-语言-动作模型, 多模态数据集, 长时程规划, 物理仿真, 基准测试

## 3 点简述
- 核心问题：现有VLA模型难以适应空中操作系统的浮动基座动力学和长时程任务挑战
- 方法要点：构建基于物理的仿真环境和高质量多模态数据集，涵盖多种任务类型
- 实验或效果：系统评估主流模型，验证VLA范式向空中系统转移的可行性并揭示模型能力边界

## 摘要（原文）

> While Vision-Language-Action (VLA) models have achieved remarkable success in ground-based embodied intelligence, their application to Aerial Manipulation Systems (AMS) remains a largely unexplored frontier. The inherent characteristics of AMS, including floating-base dynamics, strong coupling between the UAV and the manipulator, and the multi-step, long-horizon nature of operational tasks, pose severe challenges to existing VLA paradigms designed for static or 2D mobile bases. To bridge this gap, we propose AIR-VLA, the first VLA benchmark specifically tailored for aerial manipulation. We construct a physics-based simulation environment and release a high-quality multimodal dataset comprising 3000 manually teleoperated demonstrations, covering base manipulation, object & spatial understanding, semantic reasoning, and long-horizon planning. Leveraging this platform, we systematically evaluate mainstream VLA models and state-of-the-art VLM models. Our experiments not only validate the feasibility of transferring VLA paradigms to aerial systems but also, through multi-dimensional metrics tailored to aerial tasks, reveal the capabilities and boundaries of current models regarding UAV mobility, manipulator control, and high-level planning. AIR-VLA establishes a standardized testbed and data foundation for future research in general-purpose aerial robotics. The resource of AIR-VLA will be available at https://anonymous.4open.science/r/AIR-VLA-dataset-B5CC/.

