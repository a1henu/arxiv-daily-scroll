---
layout: default
title: METIS: Multi-Source Egocentric Training for Integrated Dexterous Vision-Language-Action Model
---

# METIS: Multi-Source Egocentric Training for Integrated Dexterous Vision-Language-Action Model
**arXiv**：[2511.17366v1](https://arxiv.org/abs/2511.17366) · [PDF](https://arxiv.org/pdf/2511.17366.pdf)  
**作者**：Yankai Fu, Ning Chen, Junkai Zhao, Shaozhe Shan, Guocai Yao, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang  

**一句话要点**：提出METIS模型，通过多源自我中心数据训练解决灵巧操作的数据稀缺问题

**关键词**：灵巧操作, 视觉语言动作模型, 多源数据集成, 运动表示, 自我中心视觉

## 3 点简述
- 核心问题：灵巧操作缺乏大规模动作标注数据，人类与机器人视觉差异大
- 方法要点：构建EgoAtlas数据集，统一动作空间并提取运动感知动态表示
- 实验或效果：在六项真实任务中达到最高平均成功率，泛化性强

## 摘要（原文）

> Building a generalist robot that can perceive, reason, and act across diverse tasks remains an open challenge, especially for dexterous manipulation. A major bottleneck lies in the scarcity of large-scale, action-annotated data for dexterous skills, as teleoperation is difficult and costly. Human data, with its vast scale and diverse manipulation behaviors, provides rich priors for learning robotic actions. While prior works have explored leveraging human demonstrations, they are often constrained by limited scenarios and a large visual gap between human and robots. To eliminate these limitations, we propose METIS, a vision-language-action (VLA) model for dexterous manipulation pretrained on multi-source egocentric datasets. We first construct EgoAtlas, which integrates large-scale human and robotic data from multiple sources, all unified under a consistent action space. We further extract motion-aware dynamics, a compact and discretized motion representation, which provides efficient and expressive supervision for VLA training. Built upon them, METIS integrates reasoning and acting into a unified framework, enabling effective deployment to downstream dexterous manipulation tasks. Our method demonstrates exceptional dexterous manipulation capabilities, achieving highest average success rate in six real-world tasks. Experimental results also highlight the superior generalization and robustness to out-of-distribution scenarios. These findings emphasize METIS as a promising step toward a generalist model for dexterous manipulation.

