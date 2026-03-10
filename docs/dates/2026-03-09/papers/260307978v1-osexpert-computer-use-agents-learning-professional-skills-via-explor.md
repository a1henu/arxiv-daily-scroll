---
layout: default
title: OSExpert: Computer-Use Agents Learning Professional Skills via Exploration
---

# OSExpert: Computer-Use Agents Learning Professional Skills via Exploration
**arXiv**：[2603.07978v1](https://arxiv.org/abs/2603.07978) · [PDF](https://arxiv.org/pdf/2603.07978.pdf)  
**作者**：Jiateng Liu, Zhenhailong Wang, Rushi Wang, Bingxuan Li, Jeonghwan Kim, Aditi Tiwari, Pengfei Yu, Denghui Zhang, Heng Ji  

**一句话要点**：提出GUI-DFS探索算法与技能自构建方法，以提升计算机使用代理的专业技能与效率

**关键词**：计算机使用代理, GUI探索算法, 技能自构建, 动作原语数据库, OSExpert-Eval基准, 效率优化

## 3 点简述
- 现有计算机使用代理在复杂任务中效率低、泛化差，难以处理精细动作序列
- 引入GUI-DFS算法探索环境单元功能，通过技能组合性自构建课程学习复合任务
- 实验显示在OSExpert-Eval基准上性能提升约20%，效率差距缩小约80%

## 摘要（原文）

> General-purpose computer-use agents have shown impressive performance across diverse digital environments. However, our new benchmark, OSExpert-Eval, indicates they remain far less helpful than human experts. Although inference-time scaling enables adaptation, these agents complete complex tasks inefficiently with degraded performance, transfer poorly to unseen UIs, and struggle with fine-grained action sequences. To solve the problem, we introduce a GUI-based depth-first search (GUI-DFS) exploration algorithm to comprehensively explore and verify an environment's unit functions. The agent then exploits compositionality between unit skills to self-construct a curriculum for composite tasks. To support fine-grained actions, we curate a database of action primitives for agents to discover during exploration; these are saved as a skill set once the exploration is complete. We use the learned skills to improve the agent's performance and efficiency by (1) enriching agents with ready-to-use procedural knowledge, allowing them to plan only once for long trajectories and generate accurate actions, and (2) enabling them to end inference-time scaling earlier by realizing their boundary of capabilities. Extensive experiments show that our environment-learned agent takes a meaningful step toward expert-level computer use, achieving a around 20 percent performance gain on OSExpert-Eval and closing the efficiency gap to humans by around 80 percent

