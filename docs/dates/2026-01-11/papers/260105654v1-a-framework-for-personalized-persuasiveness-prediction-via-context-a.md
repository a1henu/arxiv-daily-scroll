---
layout: default
title: A Framework for Personalized Persuasiveness Prediction via Context-Aware User Profiling
---

# A Framework for Personalized Persuasiveness Prediction via Context-Aware User Profiling
**arXiv**：[2601.05654v1](https://arxiv.org/abs/2601.05654) · [PDF](https://arxiv.org/pdf/2601.05654.pdf)  
**作者**：Sejun Park, Yoonah Park, Jongwon Lim, Yohan Jo  

**一句话要点**：提出上下文感知用户画像框架，通过检索和总结历史记录优化个性化说服力预测。

**关键词**：个性化说服力预测, 上下文感知用户画像, 查询生成器, 画像器, ChangeMyView数据集, F1分数提升

## 3 点简述
- 核心问题：缺乏系统框架利用用户历史活动优化说服力预测，需考虑用户特征如价值观和推理风格。
- 方法要点：设计可训练查询生成器和画像器，从用户历史检索相关记录并总结为上下文依赖的画像。
- 实验或效果：在ChangeMyView Reddit数据集上评估，F1分数提升最高达13.77%，优于现有方法。

## 摘要（原文）

> Estimating the persuasiveness of messages is critical in various applications, from recommender systems to safety assessment of LLMs. While it is imperative to consider the target persuadee's characteristics, such as their values, experiences, and reasoning styles, there is currently no established systematic framework to optimize leveraging a persuadee's past activities (e.g., conversations) to the benefit of a persuasiveness prediction model. To address this problem, we propose a context-aware user profiling framework with two trainable components: a query generator that generates optimal queries to retrieve persuasion-relevant records from a user's history, and a profiler that summarizes these records into a profile to effectively inform the persuasiveness prediction model. Our evaluation on the ChangeMyView Reddit dataset shows consistent improvements over existing methods across multiple predictor models, with gains of up to +13.77%p in F1 score. Further analysis shows that effective user profiles are context-dependent and predictor-specific, rather than relying on static attributes or surface-level similarity. Together, these results highlight the importance of task-oriented, context-dependent user profiling for personalized persuasiveness prediction.

