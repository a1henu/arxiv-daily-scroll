---
layout: default
title: ArtiWorld: LLM-Driven Articulation of 3D Objects in Scenes
---

# ArtiWorld: LLM-Driven Articulation of 3D Objects in Scenes
**arXiv**：[2511.12977v1](https://arxiv.org/abs/2511.12977) · [PDF](https://arxiv.org/pdf/2511.12977.pdf)  
**作者**：Yixuan Yang, Luyang Xie, Zhen Luo, Zixiang Zhao, Mingqi Gao, Feng Zheng  

**一句话要点**：提出ArtiWorld以自动将场景中的刚性3D对象转换为可交互的铰接模型

**关键词**：3D铰接对象, 大语言模型, URDF生成, 点云处理, 机器人仿真

## 3 点简述
- 核心问题：现有3D资产多为刚性，手动转换为铰接对象成本高且耗时
- 方法要点：利用LLM先验知识和3D点云，通过Arti4URDF生成URDF模型
- 实验或效果：在模拟和真实场景中优于现有方法，保持几何形状和交互性

## 摘要（原文）

> Building interactive simulators and scalable robot-learning environments requires a large number of articulated assets. However, most existing 3D assets in simulation are rigid, and manually converting them into articulated objects is extremely labor- and cost-intensive. This raises a natural question: can we automatically identify articulable objects in a scene and convert them into articulated assets directly? In this paper, we present ArtiWorld, a scene-aware pipeline that localizes candidate articulable objects from textual scene descriptions and reconstructs executable URDF models that preserve the original geometry. At the core of this pipeline is Arti4URDF, which leverages 3D point cloud, prior knowledge of a large language model (LLM), and a URDF-oriented prompt design to rapidly convert rigid objects into interactive URDF-based articulated objects while maintaining their 3D shape. We evaluate ArtiWorld at three levels: 3D simulated objects, full 3D simulated scenes, and real-world scan scenes. Across all three settings, our method consistently outperforms existing approaches and achieves state-of-the-art performance, while preserving object geometry and correctly capturing object interactivity to produce usable URDF-based articulated models. This provides a practical path toward building interactive, robot-ready simulation environments directly from existing 3D assets. Code and data will be released.

