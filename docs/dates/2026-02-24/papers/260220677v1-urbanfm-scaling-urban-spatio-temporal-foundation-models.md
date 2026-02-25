---
layout: default
title: UrbanFM: Scaling Urban Spatio-Temporal Foundation Models
---

# UrbanFM: Scaling Urban Spatio-Temporal Foundation Models
**arXiv**：[2602.20677v1](https://arxiv.org/abs/2602.20677) · [PDF](https://arxiv.org/pdf/2602.20677.pdf)  
**作者**：Wei Chen, Yuqian Wu, Junle Chen, Xiaofang Zhou, Yuxuan Liang  

**一句话要点**：提出UrbanFM以构建城市时空基础模型，通过数据、计算和架构缩放实现零样本泛化

**关键词**：城市时空基础模型, 数据缩放, 计算缩放, 架构缩放, 零样本泛化, 时空数据统一建模

## 3 点简述
- 核心问题：城市计算因场景特定模型而碎片化，缺乏泛化能力，阻碍基础模型发展
- 方法要点：基于异质性、相关性和动态性三原则，通过WorldST数据缩放、MiniST计算缩放和UrbanFM架构缩放统一建模
- 实验或效果：在EvalST基准上，UrbanFM在未见城市和任务上实现显著零样本泛化

## 摘要（原文）

> Urban systems, as dynamic complex systems, continuously generate spatio-temporal data streams that encode the fundamental laws of human mobility and city evolution. While AI for Science has witnessed the transformative power of foundation models in disciplines like genomics and meteorology, urban computing remains fragmented due to "scenario-specific" models, which are overfitted to specific regions or tasks, hindering their generalizability. To bridge this gap and advance spatio-temporal foundation models for urban systems, we adopt scaling as the central perspective and systematically investigate two key questions: what to scale and how to scale. Grounded in first-principles analysis, we identify three critical dimensions: heterogeneity, correlation, and dynamics, aligning these principles with the fundamental scientific properties of urban spatio-temporal data. Specifically, to address heterogeneity through data scaling, we construct WorldST. This billion-scale corpus standardizes diverse physical signals, such as traffic flow and speed, from over 100 global cities into a unified data format. To enable computation scaling for modeling correlations, we introduce the MiniST unit, a novel split mechanism that discretizes continuous spatio-temporal fields into learnable computational units to unify representations of grid-based and sensor-based observations. Finally, addressing dynamics via architecture scaling, we propose UrbanFM, a minimalist self-attention architecture designed with limited inductive biases to autonomously learn dynamic spatio-temporal dependencies from massive data. Furthermore, we establish EvalST, the largest-scale urban spatio-temporal benchmark to date. Extensive experiments demonstrate that UrbanFM achieves remarkable zero-shot generalization across unseen cities and tasks, marking a pivotal first step toward large-scale urban spatio-temporal foundation models.

