---
layout: default
title: Multi-Agent Comedy Club: Investigating Community Discussion Effects on LLM Humor Generation
---

# Multi-Agent Comedy Club: Investigating Community Discussion Effects on LLM Humor Generation
**arXiv**：[2602.14770v1](https://arxiv.org/abs/2602.14770) · [PDF](https://arxiv.org/pdf/2602.14770.pdf)  
**作者**：Shiwei Hong, Lingyao Li, Ethan Z. Rong, Chenxinran Shen, Zhicong Lu  

**一句话要点**：提出多智能体喜剧俱乐部方法，通过社区讨论提升LLM幽默生成效果

**关键词**：多智能体系统, LLM幽默生成, 社区讨论, 社会记忆, 受控实验

## 3 点简述
- 核心问题：现有LLM写作评估忽视在线社区持续公共反馈对幽默生成的影响
- 方法要点：在受控多智能体沙箱中，记录并利用社区讨论作为社会记忆来条件化后续生成
- 实验或效果：讨论条件在75.6%实例中胜出，显著提升Craft/Clarity和Social Response指标

## 摘要（原文）

> Prior work has explored multi-turn interaction and feedback for LLM writing, but evaluations still largely center on prompts and localized feedback, leaving persistent public reception in online communities underexamined. We test whether broadcast community discussion improves stand-up comedy writing in a controlled multi-agent sandbox: in the discussion condition, critic and audience threads are recorded, filtered, stored as social memory, and later retrieved to condition subsequent generations, whereas the baseline omits discussion. Across 50 rounds (250 paired monologues) judged by five expert annotators using A/B preference and a 15-item rubric, discussion wins 75.6% of instances and improves Craft/Clarity (Δ = 0.440) and Social Response (Δ = 0.422), with occasional increases in aggressive humor.

