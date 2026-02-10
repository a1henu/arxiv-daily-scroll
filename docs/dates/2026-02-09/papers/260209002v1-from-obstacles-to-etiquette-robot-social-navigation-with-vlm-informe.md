---
layout: default
title: From Obstacles to Etiquette: Robot Social Navigation with VLM-Informed Path Selection
---

# From Obstacles to Etiquette: Robot Social Navigation with VLM-Informed Path Selection
**arXiv**：[2602.09002v1](https://arxiv.org/abs/2602.09002) · [PDF](https://arxiv.org/pdf/2602.09002.pdf)  
**作者**：Zilin Fang, Anxing Xiao, David Hsu, Gim Hee Lee  

**一句话要点**：提出基于视觉语言模型的社会机器人导航框架，通过路径选择优化社交规范遵守。

**关键词**：社会机器人导航, 视觉语言模型, 路径规划, 社交规范, 实时适应, 蒸馏推理

## 3 点简述
- 核心问题：机器人导航需满足几何约束外，还需避免干扰人类活动或违反社交规范。
- 方法要点：结合几何规划与上下文社会推理，使用微调VLM评估候选路径以选择社交优化路径。
- 实验或效果：在四种社交导航场景中，实现最低个人空间侵犯时长、最少面向行人时间且无社交区域入侵。

## 摘要（原文）

> Navigating socially in human environments requires more than satisfying geometric constraints, as collision-free paths may still interfere with ongoing activities or conflict with social norms. Addressing this challenge calls for analyzing interactions between agents and incorporating common-sense reasoning into planning. This paper presents a social robot navigation framework that integrates geometric planning with contextual social reasoning. The system first extracts obstacles and human dynamics to generate geometrically feasible candidate paths, then leverages a fine-tuned vision-language model (VLM) to evaluate these paths, informed by contextually grounded social expectations, selecting a socially optimized path for the controller. This task-specific VLM distills social reasoning from large foundation models into a smaller and efficient model, allowing the framework to perform real-time adaptation in diverse human-robot interaction contexts. Experiments in four social navigation contexts demonstrate that our method achieves the best overall performance with the lowest personal space violation duration, the minimal pedestrian-facing time, and no social zone intrusions. Project page: https://path-etiquette.github.io

