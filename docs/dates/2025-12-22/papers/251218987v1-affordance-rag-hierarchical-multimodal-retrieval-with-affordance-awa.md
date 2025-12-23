---
layout: default
title: Affordance RAG: Hierarchical Multimodal Retrieval with Affordance-Aware Embodied Memory for Mobile Manipulation
---

# Affordance RAG: Hierarchical Multimodal Retrieval with Affordance-Aware Embodied Memory for Mobile Manipulation
**arXiv**：[2512.18987v1](https://arxiv.org/abs/2512.18987) · [PDF](https://arxiv.org/pdf/2512.18987.pdf)  
**作者**：Ryosuke Korekata, Quanting Xie, Yonatan Bisk, Komei Sugiura  

**一句话要点**：提出Affordance RAG框架，通过零样本分层多模态检索解决开放词汇移动操作问题。

**关键词**：移动操作, 多模态检索, 可执行性感知, 零样本学习, 分层检索, 具身记忆

## 3 点简述
- 核心问题：开放词汇移动操作中，机器人需基于自然语言指令理解视觉语义和操作可执行性。
- 方法要点：构建可执行性感知的具身记忆，通过分层检索和可执行性评分重排序候选目标。
- 实验或效果：在大规模室内环境中检索性能领先，真实世界任务成功率85%，优于现有方法。

## 摘要（原文）

> In this study, we address the problem of open-vocabulary mobile manipulation, where a robot is required to carry a wide range of objects to receptacles based on free-form natural language instructions. This task is challenging, as it involves understanding visual semantics and the affordance of manipulation actions. To tackle these challenges, we propose Affordance RAG, a zero-shot hierarchical multimodal retrieval framework that constructs Affordance-Aware Embodied Memory from pre-explored images. The model retrieves candidate targets based on regional and visual semantics and reranks them with affordance scores, allowing the robot to identify manipulation options that are likely to be executable in real-world environments. Our method outperformed existing approaches in retrieval performance for mobile manipulation instruction in large-scale indoor environments. Furthermore, in real-world experiments where the robot performed mobile manipulation in indoor environments based on free-form instructions, the proposed method achieved a task success rate of 85%, outperforming existing methods in both retrieval performance and overall task success.

