---
layout: default
title: ExPrIS: Knowledge-Level Expectations as Priors for Object Interpretation from Sensor Data
---

# ExPrIS: Knowledge-Level Expectations as Priors for Object Interpretation from Sensor Data
**arXiv**：[2601.15025v1](https://arxiv.org/abs/2601.15025) · [PDF](https://arxiv.org/pdf/2601.15025.pdf)  
**作者**：Marian Renz, Martin Günther, Felix Igelbrink, Oscar Lima, Martin Atzmueller  

**一句话要点**：提出ExPrIS项目，通过知识级期望作为先验，提升传感器数据的物体解释

**关键词**：物体识别, 语义场景图, 图神经网络, 知识先验, 机器人感知

## 3 点简述
- 核心问题：纯数据驱动的机器人物体识别缺乏语义一致性，未利用环境先验知识。
- 方法要点：基于3D语义场景图，整合上下文先验和外部语义知识，嵌入异构图神经网络进行期望偏置推理。
- 实验或效果：增强场景理解的鲁棒性和一致性，计划集成到移动机器人平台。

## 摘要（原文）

> While deep learning has significantly advanced robotic object recognition, purely data-driven approaches often lack semantic consistency and fail to leverage valuable, pre-existing knowledge about the environment. This report presents the ExPrIS project, which addresses this challenge by investigating how knowledge-level expectations can serve as to improve object interpretation from sensor data. Our approach is based on the incremental construction of a 3D Semantic Scene Graph (3DSSG). We integrate expectations from two sources: contextual priors from past observations and semantic knowledge from external graphs like ConceptNet. These are embedded into a heterogeneous Graph Neural Network (GNN) to create an expectation-biased inference process. This method moves beyond static, frame-by-frame analysis to enhance the robustness and consistency of scene understanding over time. The report details this architecture, its evaluation, and outlines its planned integration on a mobile robotic platform.

