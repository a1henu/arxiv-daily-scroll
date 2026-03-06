---
layout: default
title: MPCEval: A Benchmark for Multi-Party Conversation Generation
---

# MPCEval: A Benchmark for Multi-Party Conversation Generation
**arXiv**：[2603.04969v1](https://arxiv.org/abs/2603.04969) · [PDF](https://arxiv.org/pdf/2603.04969.pdf)  
**作者**：Minxing Zhang, Yi Yang, Zhuofan Jia, Xuan Yang, Jian Pei, Yuchen Zang, Xingwang Deng, Xianglong Chen  

**一句话要点**：提出MPCEval基准以评估多轮多方对话生成质量

**关键词**：多方对话生成, 评估基准, 无参考指标, 角色建模, 内容一致性

## 3 点简述
- 核心问题：多方对话生成评估存在瓶颈，涉及复杂轮转和角色行为
- 方法要点：分解质量维度，提供无参考、可复现的量化指标
- 实验或效果：应用于多数据集，揭示模型在参与平衡和内容一致性上的差异

## 摘要（原文）

> Multi-party conversation generation, such as smart reply and collaborative assistants, is an increasingly important capability of generative AI, yet its evaluation remains a critical bottleneck. Compared to two-party dialogue, multi-party settings introduce distinct challenges, including complex turn-taking, role-dependent speaker behavior, long-range conversational structure, and multiple equally valid continuations. Accordingly, we introduce MPCEval, a task-aware evaluation and benchmarking suite for multi-party conversation generation. MPCEval decomposes generation quality into speaker modeling, content quality, and speaker--content consistency, and explicitly distinguishes local next-turn prediction from global full-conversation generation. It provides novel, quantitative, reference-free, and reproducible metrics that scale across datasets and models. We apply MPCEval to diverse public and real-world datasets and evaluate modern generation methods alongside human-authored conversations. The results reveal systematic, dimension-specific model characteristics in participation balance, content progression and novelty, and speaker--content consistency, demonstrating that evaluation objectives critically shape model assessment and that single-score evaluation obscures fundamental differences in multi-party conversational behavior. The implementation of MPCEval and the associated evaluation code are publicly available at https://github.com/Owen-Yang-18/MPCEval.

