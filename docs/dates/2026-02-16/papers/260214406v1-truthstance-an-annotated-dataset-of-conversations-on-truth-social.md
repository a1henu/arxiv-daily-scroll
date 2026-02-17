---
layout: default
title: TruthStance: An Annotated Dataset of Conversations on Truth Social
---

# TruthStance: An Annotated Dataset of Conversations on Truth Social
**arXiv**：[2602.14406v1](https://arxiv.org/abs/2602.14406) · [PDF](https://arxiv.org/pdf/2602.14406.pdf)  
**作者**：Fathima Ameen, Danielle Brown, Manusha Malgareddy, Amanul Haque  

**一句话要点**：提出TruthStance数据集以分析Truth Social平台上的论辩挖掘和立场检测

**关键词**：论辩挖掘, 立场检测, Truth Social, 对话数据集, LLM评估, 社交媒体分析

## 3 点简述
- 核心问题：主流平台外，alt-tech平台如Truth Social的对话结构研究不足。
- 方法要点：构建大规模Truth Social对话数据集，含人工标注基准和LLM生成标签。
- 实验或效果：评估LLM提示策略，提供标注数据支持深度、主题和用户模式分析。

## 摘要（原文）

> Argument mining and stance detection are central to understanding how opinions are formed and contested in online discourse. However, most publicly available resources focus on mainstream platforms such as Twitter and Reddit, leaving conversational structure on alt-tech platforms comparatively under-studied. We introduce TruthStance, a large-scale dataset of Truth Social conversation threads spanning 2023-2025, consisting of 24,378 posts and 523,360 comments with reply-tree structure preserved. We provide a human-annotated benchmark of 1,500 instances across argument mining and claim-based stance detection, including inter-annotator agreement, and use it to evaluate large language model (LLM) prompting strategies. Using the best-performing configuration, we release additional LLM-generated labels for 24,352 posts (argument presence) and 107,873 comments (stance to parent), enabling analysis of stance and argumentation patterns across depth, topics, and users. All code and data are released publicly.

