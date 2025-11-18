---
layout: default
title: PhysX-Anything: Simulation-Ready Physical 3D Assets from Single Image
---

# PhysX-Anything: Simulation-Ready Physical 3D Assets from Single Image
**arXiv**：[2511.13648v1](https://arxiv.org/abs/2511.13648) · [PDF](https://arxiv.org/pdf/2511.13648.pdf)  
**作者**：Ziang Cao, Fangzhou Hong, Zhaoxi Chen, Liang Pan, Ziwei Liu  

**一句话要点**：提出PhysX-Anything框架，从单张图像生成仿真就绪的物理3D资产，以解决现有方法忽略物理属性的问题。

**关键词**：物理3D生成, 仿真就绪资产, 视觉语言模型, 几何token化, 具身AI, 物理模拟

## 3 点简述
- 核心问题：现有3D生成方法忽视物理和关节属性，限制在具身AI中的应用。
- 方法要点：基于VLM的物理3D生成模型，新3D表示将几何token数减少193倍。
- 实验或效果：在PhysX-Mobility数据集和野外图像上验证强生成性能和泛化能力。

## 摘要（原文）

> 3D modeling is shifting from static visual representations toward physical, articulated assets that can be directly used in simulation and interaction. However, most existing 3D generation methods overlook key physical and articulation properties, thereby limiting their utility in embodied AI. To bridge this gap, we introduce PhysX-Anything, the first simulation-ready physical 3D generative framework that, given a single in-the-wild image, produces high-quality sim-ready 3D assets with explicit geometry, articulation, and physical attributes. Specifically, we propose the first VLM-based physical 3D generative model, along with a new 3D representation that efficiently tokenizes geometry. It reduces the number of tokens by 193x, enabling explicit geometry learning within standard VLM token budgets without introducing any special tokens during fine-tuning and significantly improving generative quality. In addition, to overcome the limited diversity of existing physical 3D datasets, we construct a new dataset, PhysX-Mobility, which expands the object categories in prior physical 3D datasets by over 2x and includes more than 2K common real-world objects with rich physical annotations. Extensive experiments on PhysX-Mobility and in-the-wild images demonstrate that PhysX-Anything delivers strong generative performance and robust generalization. Furthermore, simulation-based experiments in a MuJoCo-style environment validate that our sim-ready assets can be directly used for contact-rich robotic policy learning. We believe PhysX-Anything can substantially empower a broad range of downstream applications, especially in embodied AI and physics-based simulation.

