---
layout: default
title: RoboVIP: Multi-View Video Generation with Visual Identity Prompting Augments Robot Manipulation
---

# RoboVIP: Multi-View Video Generation with Visual Identity Prompting Augments Robot Manipulation
**arXiv**：[2601.05241v1](https://arxiv.org/abs/2601.05241) · [PDF](https://arxiv.org/pdf/2601.05241.pdf)  
**作者**：Boyang Wang, Haoran Zhang, Shujie Zhang, Jinkun Hao, Mingda Jia, Qi Lv, Yucheng Mao, Zhaoyang Lyu, Jia Zeng, Xudong Xu, Jiangmiao Pang  

**一句话要点**：提出视觉身份提示方法，通过多视角视频生成增强机器人操作数据

**关键词**：机器人操作, 数据增强, 多视角视频生成, 视觉身份提示, 扩散模型

## 3 点简述
- 机器人操作数据受硬件限制难以大规模收集，影响策略训练效果
- 引入视觉身份提示，利用示例图像指导扩散模型生成多视角、时序一致的场景
- 在仿真和真实机器人实验中，增强数据训练下游模型带来性能提升

## 摘要（原文）

> The diversity, quantity, and quality of manipulation data are critical for training effective robot policies. However, due to hardware and physical setup constraints, collecting large-scale real-world manipulation data remains difficult to scale across diverse environments. Recent work uses text-prompt conditioned image diffusion models to augment manipulation data by altering the backgrounds and tabletop objects in the visual observations. However, these approaches often overlook the practical need for multi-view and temporally coherent observations required by state-of-the-art policy models. Further, text prompts alone cannot reliably specify the scene setup. To provide the diffusion model with explicit visual guidance, we introduce visual identity prompting, which supplies exemplar images as conditioning inputs to guide the generation of the desired scene setup. To this end, we also build a scalable pipeline to curate a visual identity pool from large robotics datasets. Using our augmented manipulation data to train downstream vision-language-action and visuomotor policy models yields consistent performance gains in both simulation and real-robot settings.

