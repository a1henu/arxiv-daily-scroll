---
layout: default
title: Curiosity Driven Knowledge Retrieval for Mobile Agents
---

# Curiosity Driven Knowledge Retrieval for Mobile Agents
**arXiv**：[2601.19306v1](https://arxiv.org/abs/2601.19306) · [PDF](https://arxiv.org/pdf/2601.19306.pdf)  
**作者**：Sijia Li, Xiaoyu Tan, Shahir Ali, Niels Schmidt, Gengchen Ma, Xihe Qiu  

**一句话要点**：提出好奇心驱动知识检索框架以提升移动代理在复杂应用中的性能

**关键词**：移动代理, 知识检索, 好奇心驱动, AppCards, 智能手机自动化, AndroidWorld基准

## 3 点简述
- 移动代理在复杂应用中受限于知识不完整和泛化能力弱
- 框架将执行不确定性量化为好奇心分数，触发外部知识检索并组织为结构化AppCards
- 在AndroidWorld基准测试中平均提升6个百分点，结合GPT-5达到88.8%的新SOTA成功率

## 摘要（原文）

> Mobile agents have made progress toward reliable smartphone automation, yet performance in complex applications remains limited by incomplete knowledge and weak generalization to unseen environments. We introduce a curiosity driven knowledge retrieval framework that formalizes uncertainty during execution as a curiosity score. When this score exceeds a threshold, the system retrieves external information from documentation, code repositories, and historical trajectories. Retrieved content is organized into structured AppCards, which encode functional semantics, parameter conventions, interface mappings, and interaction patterns. During execution, an enhanced agent selectively integrates relevant AppCards into its reasoning process, thereby compensating for knowledge blind spots and improving planning reliability. Evaluation on the AndroidWorld benchmark shows consistent improvements across backbones, with an average gain of six percentage points and a new state of the art success rate of 88.8\% when combined with GPT-5. Analysis indicates that AppCards are particularly effective for multi step and cross application tasks, while improvements depend on the backbone model. Case studies further confirm that AppCards reduce ambiguity, shorten exploration, and support stable execution trajectories. Task trajectories are publicly available at https://lisalsj.github.io/Droidrun-appcard/.

