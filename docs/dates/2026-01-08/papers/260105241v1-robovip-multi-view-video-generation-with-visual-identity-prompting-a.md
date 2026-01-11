---
layout: default
title: RoboVIP: Multi-View Video Generation with Visual Identity Prompting Augments Robot Manipulation
---

# RoboVIP: Multi-View Video Generation with Visual Identity Prompting Augments Robot Manipulation
**arXiv**：[2601.05241v1](https://arxiv.org/abs/2601.05241) · [PDF](https://arxiv.org/pdf/2601.05241.pdf)  
**作者**：Boyang Wang, Haoran Zhang, Shujie Zhang, Jinkun Hao, Mingda Jia, Qi Lv, Yucheng Mao, Zhaoyang Lyu, Jia Zeng, Xudong Xu, Jiangmiao Pang  

**一句话要点**：提出视觉身份提示方法，通过多视角视频生成增强机器人操作数据

**关键词**：视觉身份提示, 多视角视频生成, 机器人操作数据增强, 扩散模型, 视觉语言动作策略

## 3 点简述
- 机器人操作数据受硬件限制难以大规模收集，现有文本提示方法无法保证多视角和时间一致性
- 引入视觉身份提示，使用示例图像作为条件输入，指导生成所需场景设置，并构建可扩展管道从大型数据集中筛选视觉身份池
- 使用增强数据训练下游策略模型，在仿真和真实机器人环境中均获得性能提升

## 摘要（原文）

> The diversity, quantity, and quality of manipulation data are critical for training effective robot policies. However, due to hardware and physical setup constraints, collecting large-scale real-world manipulation data remains difficult to scale across diverse environments. Recent work uses text-prompt conditioned image diffusion models to augment manipulation data by altering the backgrounds and tabletop objects in the visual observations. However, these approaches often overlook the practical need for multi-view and temporally coherent observations required by state-of-the-art policy models. Further, text prompts alone cannot reliably specify the scene setup. To provide the diffusion model with explicit visual guidance, we introduce visual identity prompting, which supplies exemplar images as conditioning inputs to guide the generation of the desired scene setup. To this end, we also build a scalable pipeline to curate a visual identity pool from large robotics datasets. Using our augmented manipulation data to train downstream vision-language-action and visuomotor policy models yields consistent performance gains in both simulation and real-robot settings.

