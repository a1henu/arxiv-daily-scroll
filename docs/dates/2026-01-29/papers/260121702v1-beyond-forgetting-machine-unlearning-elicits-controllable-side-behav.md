---
layout: default
title: Beyond Forgetting: Machine Unlearning Elicits Controllable Side Behaviors and Capabilities
---

# Beyond Forgetting: Machine Unlearning Elicits Controllable Side Behaviors and Capabilities
**arXiv**：[2601.21702v1](https://arxiv.org/abs/2601.21702) · [PDF](https://arxiv.org/pdf/2601.21702.pdf)  
**作者**：Tien Dang, The-Hai Nguyen, Dinh Mai Phuong, Nguyen Minh Phuong, Hoang Thanh-Tung, Le-Minh Nguyen, Naoya Inoue  

**一句话要点**：提出基于线性表示假设的表示误导方法，探索机器遗忘引发的可控侧行为和能力增强

**关键词**：机器遗忘, 表示误导, 线性表示假设, 可控行为, 能力增强, 大语言模型

## 3 点简述
- 核心问题：表示误导方法中目标向量的作用未充分探索，影响遗忘效果和潜在风险
- 方法要点：利用线性表示假设，在遗忘表示空间中对概念向量进行线性操作，实现可控行为
- 实验或效果：在行为控制和能力增强任务中验证假设，揭示遗忘可能带来隐藏风险或可利用机制

## 摘要（原文）

> We consider representation misdirection (RM), a class of LLM unlearning methods that achieves forgetting by manipulating the forget-representations, that is, latent representations of forget samples. Despite being important, the roles of target vectors used in RM, however, remain underexplored. Here, we approach and revisit RM through the lens of the linear representation hypothesis. Specifically, if one can somehow identify a one-dimensional representation corresponding to a high-level concept, the linear representation hypothesis enables linear operations on this concept vector within the forget-representation space. Under this view, we hypothesize that, beyond forgetting, machine unlearning elicits controllable side behaviors and stronger side capabilities corresponding to the high-level concept. Our hypothesis is empirically validated across a wide range of tasks, including behavioral control (e.g., controlling unlearned models' truth, sentiment, and refusal) and capability enhancement (e.g., improving unlearned models' in-context learning capability). Our findings reveal that this fairly attractive phenomenon could be either a hidden risk if misused or a mechanism that can be harnessed for developing models that require stronger capabilities and controllable behaviors.

