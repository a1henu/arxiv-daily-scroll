---
layout: default
title: SPEAR-1: Scaling Beyond Robot Demonstrations via 3D Understanding
---

# SPEAR-1: Scaling Beyond Robot Demonstrations via 3D Understanding
**arXiv**：[2511.17411v1](https://arxiv.org/abs/2511.17411) · [PDF](https://arxiv.org/pdf/2511.17411.pdf)  
**作者**：Nikolay Nikolov, Giuliano Albanese, Sombit Dey, Aleksandar Yanev, Luc Van Gool, Jan-Nico Zaech, Danda Pani Paudel  

**一句话要点**：提出SPEAR-1机器人基础模型，通过增强3D感知解决机器人控制泛化问题

**关键词**：机器人基础模型, 3D空间推理, 视觉语言模型, 单图像3D坐标推断, 语言指令控制, 数据高效训练

## 3 点简述
- 核心问题：机器人基础模型泛化能力受限，因依赖缺乏3D空间推理的2D视觉语言模型
- 方法要点：训练SPEAR-VLM从单张2D图像推断3D坐标，并集成到语言指令控制中
- 实验或效果：在24个数据集上训练，性能优于或匹配先进模型，且机器人演示数据减少20倍

## 摘要（原文）

> Robotic Foundation Models (RFMs) hold great promise as generalist, end-to-end systems for robot control. Yet their ability to generalize across new environments, tasks, and embodiments remains limited. We argue that a major bottleneck lies in their foundations: most RFMs are built by fine-tuning internet-pretrained Vision-Language Models (VLMs). However, these VLMs are trained on 2D image-language tasks and lack the 3D spatial reasoning inherently required for embodied control in the 3D world. Bridging this gap directly with large-scale robotic data is costly and difficult to scale. Instead, we propose to enrich easy-to-collect non-robotic image data with 3D annotations and enhance a pretrained VLM with 3D understanding capabilities. Following this strategy, we train SPEAR-VLM, a 3D-aware VLM that infers object coordinates in 3D space from a single 2D image. Building on SPEAR-VLM, we introduce our main contribution, $~\textbf{SPEAR-1}$: a robotic foundation model that integrates grounded 3D perception with language-instructed embodied control. Trained on $\sim$45M frames from 24 Open X-Embodiment datasets, SPEAR-1 outperforms or matches state-of-the-art models such as $π_0$-FAST and $π_{0.5}$, while it uses 20$\times$ fewer robot demonstrations. This carefully-engineered training strategy unlocks new VLM capabilities and as a consequence boosts the reliability of embodied control beyond what is achievable with only robotic data. We make our model weights and 3D-annotated datasets publicly available.

