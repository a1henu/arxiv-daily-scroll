---
layout: default
title: PosterOmni: Generalized Artistic Poster Creation via Task Distillation and Unified Reward Feedback
---

# PosterOmni: Generalized Artistic Poster Creation via Task Distillation and Unified Reward Feedback
**arXiv**：[2602.12127v1](https://arxiv.org/abs/2602.12127) · [PDF](https://arxiv.org/pdf/2602.12127.pdf)  
**作者**：Sixiang Chen, Jianyu Lai, Jialin Gao, Hengyu Shi, Zhongying Liu, Tian Ye, Junfeng Luo, Xiaoming Wei, Lei Zhu  

**一句话要点**：提出PosterOmni框架，通过任务蒸馏与统一奖励反馈解决图像到海报生成的局部编辑与全局创作挑战

**关键词**：图像到海报生成, 任务蒸馏, 统一奖励反馈, 局部编辑, 全局创作, 美学评估

## 3 点简述
- 核心问题：图像到海报生成需兼顾局部实体保留与全局设计概念理解，是多维耦合过程
- 方法要点：构建多场景数据集，通过知识蒸馏和统一奖励反馈整合局部与全局任务
- 实验或效果：在PosterOmni-Bench上优于开源基线，部分超越专有系统，提升参考依从性和美学和谐

## 摘要（原文）

> Image-to-poster generation is a high-demand task requiring not only local adjustments but also high-level design understanding. Models must generate text, layout, style, and visual elements while preserving semantic fidelity and aesthetic coherence. The process spans two regimes: local editing, where ID-driven generation, rescaling, filling, and extending must preserve concrete visual entities; and global creation, where layout- and style-driven tasks rely on understanding abstract design concepts. These intertwined demands make image-to-poster a multi-dimensional process coupling entity-preserving editing with concept-driven creation under image-prompt control. To address these challenges, we propose PosterOmni, a generalized artistic poster creation framework that unlocks the potential of a base edit model for multi-task image-to-poster generation. PosterOmni integrates the two regimes, namely local editing and global creation, within a single system through an efficient data-distillation-reward pipeline: (i) constructing multi-scenario image-to-poster datasets covering six task types across entity-based and concept-based creation; (ii) distilling knowledge between local and global experts for supervised fine-tuning; and (iii) applying unified PosterOmni Reward Feedback to jointly align visual entity-preserving and aesthetic preference across all tasks. Additionally, we establish PosterOmni-Bench, a unified benchmark for evaluating both local editing and global creation. Extensive experiments show that PosterOmni significantly enhances reference adherence, global composition quality, and aesthetic harmony, outperforming all open-source baselines and even surpassing several proprietary systems.

