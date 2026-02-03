---
layout: default
title: Why Steering Works: Toward a Unified View of Language Model Parameter Dynamics
---

# Why Steering Works: Toward a Unified View of Language Model Parameter Dynamics
**arXiv**：[2602.02343v1](https://arxiv.org/abs/2602.02343) · [PDF](https://arxiv.org/pdf/2602.02343.pdf)  
**作者**：Ziwen Xu, Chenyan Wu, Hengyu Sun, Haiwen Hong, Mengru Wang, Yunzhi Yao, Longtao Huang, Hui Xue, Shumin Deng, Zhixuan Chu, Huajun Chen, Ningyu Zhang  

**一句话要点**：提出统一框架分析语言模型控制方法，揭示偏好与效用的权衡，并基于此设计新方法SPLIT以提升控制效果。

**关键词**：语言模型控制, 偏好-效用分析, 动态权重更新, 激活流形, 统一框架, SPLIT方法

## 3 点简述
- 核心问题：现有语言模型控制方法孤立研究，缺乏统一比较框架，难以理解其内在联系与效果差异。
- 方法要点：将控制方法统一为动态权重更新，引入偏好-效用分析框架，在共享尺度上量化控制效果。
- 实验或效果：发现控制强度与偏好正相关、与效用负相关的权衡，基于激活流形视角解释此行为，并验证SPLIT方法在提升偏好时更好保持效用。

## 摘要（原文）

> Methods for controlling large language models (LLMs), including local weight fine-tuning, LoRA-based adaptation, and activation-based interventions, are often studied in isolation, obscuring their connections and making comparison difficult. In this work, we present a unified view that frames these interventions as dynamic weight updates induced by a control signal, placing them within a single conceptual framework. Building on this view, we propose a unified preference-utility analysis that separates control effects into preference, defined as the tendency toward a target concept, and utility, defined as coherent and task-valid generation, and measures both on a shared log-odds scale using polarity-paired contrastive examples. Across methods, we observe a consistent trade-off between preference and utility: stronger control increases preference while predictably reducing utility. We further explain this behavior through an activation manifold perspective, in which control shifts representations along target-concept directions to enhance preference, while utility declines primarily when interventions push representations off the model's valid-generation manifold. Finally, we introduce a new steering approach SPLIT guided by this analysis that improves preference while better preserving utility. Code is available at https://github.com/zjunlp/EasyEdit/blob/main/examples/SPLIT.md.

