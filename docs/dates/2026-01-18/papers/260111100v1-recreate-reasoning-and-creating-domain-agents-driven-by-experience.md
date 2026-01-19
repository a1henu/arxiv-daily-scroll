---
layout: default
title: ReCreate: Reasoning and Creating Domain Agents Driven by Experience
---

# ReCreate: Reasoning and Creating Domain Agents Driven by Experience
**arXiv**：[2601.11100v1](https://arxiv.org/abs/2601.11100) · [PDF](https://arxiv.org/pdf/2601.11100.pdf)  
**作者**：Zhezheng Hao, Hong Wang, Jian Luo, Jianqing Zhang, Yuyan Zhou, Qiang Lin, Can Wang, Hande Dong, Jiawei Chen  

**一句话要点**：提出ReCreate框架，通过经验驱动自动创建和适应领域智能体

**关键词**：智能体生成, 经验驱动, 推理-创建协同, 领域适应, 交互历史分析

## 3 点简述
- 核心问题：现有自动化智能体生成方法依赖黑盒过程，忽略成功或失败原因，计算成本高
- 方法要点：引入智能体即优化器范式，基于交互历史进行经验存储、推理-创建协同和层次化更新
- 实验或效果：在多个领域实验中，ReCreate优于人工设计智能体和现有自动化方法，即使从最小种子开始

## 摘要（原文）

> Large Language Model agents are reshaping the industrial landscape. However, most practical agents remain human-designed because tasks differ widely, making them labor-intensive to build. This situation poses a central question: can we automatically create and adapt domain agents in the wild? While several recent approaches have sought to automate agent creation, they typically treat agent generation as a black-box procedure and rely solely on final performance metrics to guide the process. Such strategies overlook critical evidence explaining why an agent succeeds or fails, and often require high computational costs. To address these limitations, we propose ReCreate, an experience-driven framework for the automatic creation of domain agents. ReCreate systematically leverages agent interaction histories, which provide rich concrete signals on both the causes of success or failure and the avenues for improvement. Specifically, we introduce an agent-as-optimizer paradigm that effectively learns from experience via three key components: (i) an experience storage and retrieval mechanism for on-demand inspection; (ii) a reasoning-creating synergy pipeline that maps execution experience into scaffold edits; and (iii) hierarchical updates that abstract instance-level details into reusable domain patterns. In experiments across diverse domains, ReCreate consistently outperforms human-designed agents and existing automated agent generation methods, even when starting from minimal seed scaffolds.

