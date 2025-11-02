---
layout: default
title: RoboOS-NeXT: A Unified Memory-based Framework for Lifelong, Scalable, and Robust Multi-Robot Collaboration
---

# RoboOS-NeXT: A Unified Memory-based Framework for Lifelong, Scalable, and Robust Multi-Robot Collaboration
**arXiv**：[2510.26536v1](https://arxiv.org/abs/2510.26536) · [PDF](https://arxiv.org/pdf/2510.26536.pdf)  
**作者**：Huajie Tan, Cheng Chi, Xiansheng Chen, Yuheng Ji, Zhongxia Zhao, Xiaoshuai Hao, Yaoxu Lyu, Mingyu Cao, Junkai Zhao, Huaihai Lyu, Enshen Zhou, Ning Chen, Yankai Fu, Cheng Peng, Wei Guo, Dong Liang, Zhuo Chen, Mengsi Lyu, Chenrui He, Yulong Ao, Yonghua Lin, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang  

**一句话要点**：提出RoboOS-NeXT框架以解决多机器人协作中的终身适应、可扩展和鲁棒性问题

**关键词**：多机器人协作, 统一记忆框架, 终身学习, 异构团队, 鲁棒调度, 空间-时间-体现记忆

## 3 点简述
- 核心问题：现有方法依赖有限个体记忆，难以实现终身学习、异构团队扩展和故障恢复
- 方法要点：引入STEM统一记忆，集成空间、时间和体现信息，支持脑-小脑框架的全局规划与本地执行
- 实验或效果：在餐厅、超市和家庭等场景中验证，RoboOS-NeXT在异构体现下表现优越

## 摘要（原文）

> The proliferation of collaborative robots across diverse tasks and
> embodiments presents a central challenge: achieving lifelong adaptability,
> scalable coordination, and robust scheduling in multi-agent systems. Existing
> approaches, from vision-language-action (VLA) models to hierarchical
> frameworks, fall short due to their reliance on limited or dividual-agent
> memory. This fundamentally constrains their ability to learn over long
> horizons, scale to heterogeneous teams, or recover from failures, highlighting
> the need for a unified memory representation. To address these limitations, we
> introduce RoboOS-NeXT, a unified memory-based framework for lifelong, scalable,
> and robust multi-robot collaboration. At the core of RoboOS-NeXT is the novel
> Spatio-Temporal-Embodiment Memory (STEM), which integrates spatial scene
> geometry, temporal event history, and embodiment profiles into a shared
> representation. This memory-centric design is integrated into a
> brain-cerebellum framework, where a high-level brain model performs global
> planning by retrieving and updating STEM, while low-level controllers execute
> actions locally. This closed loop between cognition, memory, and execution
> enables dynamic task allocation, fault-tolerant collaboration, and consistent
> state synchronization. We conduct extensive experiments spanning complex
> coordination tasks in restaurants, supermarkets, and households. Our results
> demonstrate that RoboOS-NeXT achieves superior performance across heterogeneous
> embodiments, validating its effectiveness in enabling lifelong, scalable, and
> robust multi-robot collaboration. Project website:
> https://flagopen.github.io/RoboOS/

