---
layout: default
title: FlyCo: Foundation Model-Empowered Drones for Autonomous 3D Structure Scanning in Open-World Environments
---

# FlyCo: Foundation Model-Empowered Drones for Autonomous 3D Structure Scanning in Open-World Environments
**arXiv**：[2601.07558v1](https://arxiv.org/abs/2601.07558) · [PDF](https://arxiv.org/pdf/2601.07558.pdf)  
**作者**：Chen Feng, Guiyong Zheng, Tengkai Zhuang, Yongqian Wu, Fangzhan He, Haojia Li, Juepeng Zheng, Shaojie Shen, Boyu Zhou  

**一句话要点**：提出FlyCo系统，利用基础模型实现无人机在开放世界环境中自主3D结构扫描。

**关键词**：无人机自主扫描, 基础模型集成, 感知-预测-规划循环, 开放世界环境, 3D结构重建

## 3 点简述
- 核心问题：如何设计系统架构有效集成基础模型知识，实现无人机在未知开放世界中的自主3D目标扫描。
- 方法要点：采用感知-预测-规划循环，通过融合多模态数据与基础模型，实现目标定位、几何推断和路径生成。
- 实验或效果：在真实世界和仿真实验中，FlyCo展现出高精度、高效率和安全实时性，优于现有方法。

## 摘要（原文）

> Autonomous 3D scanning of open-world target structures via drones remains challenging despite broad applications. Existing paradigms rely on restrictive assumptions or effortful human priors, limiting practicality, efficiency, and adaptability. Recent foundation models (FMs) offer great potential to bridge this gap. This paper investigates a critical research problem: What system architecture can effectively integrate FM knowledge for this task? We answer it with FlyCo, a principled FM-empowered perception-prediction-planning loop enabling fully autonomous, prompt-driven 3D target scanning in diverse unknown open-world environments. FlyCo directly translates low-effort human prompts (text, visual annotations) into precise adaptive scanning flights via three coordinated stages: (1) perception fuses streaming sensor data with vision-language FMs for robust target grounding and tracking; (2) prediction distills FM knowledge and combines multi-modal cues to infer the partially observed target's complete geometry; (3) planning leverages predictive foresight to generate efficient and safe paths with comprehensive target coverage. Building on this, we further design key components to boost open-world target grounding efficiency and robustness, enhance prediction quality in terms of shape accuracy, zero-shot generalization, and temporal stability, and balance long-horizon flight efficiency with real-time computability and online collision avoidance. Extensive challenging real-world and simulation experiments show FlyCo delivers precise scene understanding, high efficiency, and real-time safety, outperforming existing paradigms with lower human effort and verifying the proposed architecture's practicality. Comprehensive ablations validate each component's contribution. FlyCo also serves as a flexible, extensible blueprint, readily leveraging future FM and robotics advances. Code will be released.

