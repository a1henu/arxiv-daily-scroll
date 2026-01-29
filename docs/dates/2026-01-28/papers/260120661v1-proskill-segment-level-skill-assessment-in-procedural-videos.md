---
layout: default
title: ProSkill: Segment-Level Skill Assessment in Procedural Videos
---

# ProSkill: Segment-Level Skill Assessment in Procedural Videos
**arXiv**：[2601.20661v1](https://arxiv.org/abs/2601.20661) · [PDF](https://arxiv.org/pdf/2601.20661.pdf)  
**作者**：Michele Mazzamuto, Daniele Di Mauro, Gianpiero Francesca, Giovanni Maria Farinella, Antonino Furnari  

**一句话要点**：提出ProSkill基准数据集以解决程序性视频中动作级技能评估的挑战

**关键词**：程序性视频, 技能评估, 基准数据集, 成对比较, ELO评分, 动作级分析

## 3 点简述
- 核心问题：现有技能评估研究缺乏大规模程序性任务数据集，且多限于二元或成对评估。
- 方法要点：引入可扩展标注协议，基于瑞士锦标赛和ELO评分系统生成绝对技能排名。
- 实验或效果：基准测试显示当前先进算法表现欠佳，凸显数据集价值。

## 摘要（原文）

> Skill assessment in procedural videos is crucial for the objective evaluation of human performance in settings such as manufacturing and procedural daily tasks. Current research on skill assessment has predominantly focused on sports and lacks large-scale datasets for complex procedural activities. Existing studies typically involve only a limited number of actions, focus on either pairwise assessments (e.g., A is better than B) or on binary labels (e.g., good execution vs needs improvement). In response to these shortcomings, we introduce ProSkill, the first benchmark dataset for action-level skill assessment in procedural tasks. ProSkill provides absolute skill assessment annotations, along with pairwise ones. This is enabled by a novel and scalable annotation protocol that allows for the creation of an absolute skill assessment ranking starting from pairwise assessments. This protocol leverages a Swiss Tournament scheme for efficient pairwise comparisons, which are then aggregated into consistent, continuous global scores using an ELO-based rating system. We use our dataset to benchmark the main state-of-the-art skill assessment algorithms, including both ranking-based and pairwise paradigms. The suboptimal results achieved by the current state-of-the-art highlight the challenges and thus the value of ProSkill in the context of skill assessment for procedural videos. All data and code are available at https://fpv-iplab.github.io/ProSkill/

