---
layout: default
title: LagMemo: Language 3D Gaussian Splatting Memory for Multi-modal Open-vocabulary Multi-goal Visual Navigation
---

# LagMemo: Language 3D Gaussian Splatting Memory for Multi-modal Open-vocabulary Multi-goal Visual Navigation
**arXiv**：[2510.24118v1](https://arxiv.org/abs/2510.24118) · [PDF](https://arxiv.org/pdf/2510.24118.pdf)  
**作者**：Haotian Zhou, Xiaole Wang, He Li, Fusheng Sun, Shengyu Guo, Guolei Qi, Jianghuan Xu, Huijing Zhao  

**一句话要点**：提出LagMemo系统，利用语言3D高斯泼溅记忆解决多模态开放词汇多目标视觉导航问题

**关键词**：视觉导航, 多模态学习, 开放词汇, 3D高斯泼溅, 多目标导航, 语言记忆

## 3 点简述
- 核心问题：传统视觉导航方法局限于单目标、单模态和封闭集目标设置，无法满足多模态开放词汇多目标需求。
- 方法要点：构建统一3D语言记忆，通过查询预测候选目标位置，并集成局部感知验证机制动态匹配目标。
- 实验或效果：在GOAT-Core基准上，LagMemo在开放词汇目标定位和多目标导航中优于现有方法。

## 摘要（原文）

> Navigating to a designated goal using visual information is a fundamental
> capability for intelligent robots. Most classical visual navigation methods are
> restricted to single-goal, single-modality, and closed set goal settings. To
> address the practical demands of multi-modal, open-vocabulary goal queries and
> multi-goal visual navigation, we propose LagMemo, a navigation system that
> leverages a language 3D Gaussian Splatting memory. During exploration, LagMemo
> constructs a unified 3D language memory. With incoming task goals, the system
> queries the memory, predicts candidate goal locations, and integrates a local
> perception-based verification mechanism to dynamically match and validate goals
> during navigation. For fair and rigorous evaluation, we curate GOAT-Core, a
> high-quality core split distilled from GOAT-Bench tailored to multi-modal
> open-vocabulary multi-goal visual navigation. Experimental results show that
> LagMemo's memory module enables effective multi-modal open-vocabulary goal
> localization, and that LagMemo outperforms state-of-the-art methods in
> multi-goal visual navigation. Project page:
> https://weekgoodday.github.io/lagmemo

