---
layout: default
title: Task-Oriented Robot-Human Handovers on Legged Manipulators
---

# Task-Oriented Robot-Human Handovers on Legged Manipulators
**arXiv**：[2602.05760v1](https://arxiv.org/abs/2602.05760) · [PDF](https://arxiv.org/pdf/2602.05760.pdf)  
**作者**：Andreea Tulbure, Carmen Scheidemann, Elias Steiner, Marco Hutter  

**一句话要点**：提出AFT-Handover框架，结合LLM推理与纹理化可转移性，实现零样本任务导向机器人-人交接于腿式操纵器。

**关键词**：任务导向交接, 可转移性推理, 零样本泛化, 腿式操纵器, 人机协作

## 3 点简述
- 核心问题：现有任务导向交接方法基于对象或任务特定可转移性，泛化能力有限。
- 方法要点：利用LLM驱动可转移性推理与基于纹理的可转移性转移，实现零样本泛化。
- 实验或效果：在多样任务-对象对上评估，提升交接成功率，用户研究显示优于现有方法。

## 摘要（原文）

> Task-oriented handovers (TOH) are fundamental to effective human-robot collaboration, requiring robots to present objects in a way that supports the human's intended post-handover use. Existing approaches are typically based on object- or task-specific affordances, but their ability to generalize to novel scenarios is limited. To address this gap, we present AFT-Handover, a framework that integrates large language model (LLM)-driven affordance reasoning with efficient texture-based affordance transfer to achieve zero-shot, generalizable TOH. Given a novel object-task pair, the method retrieves a proxy exemplar from a database, establishes part-level correspondences via LLM reasoning, and texturizes affordances for feature-based point cloud transfer. We evaluate AFT-Handover across diverse task-object pairs, showing improved handover success rates and stronger generalization compared to baselines. In a comparative user study, our framework is significantly preferred over the current state-of-the-art, effectively reducing human regrasping before tool use. Finally, we demonstrate TOH on legged manipulators, highlighting the potential of our framework for real-world robot-human handovers.

