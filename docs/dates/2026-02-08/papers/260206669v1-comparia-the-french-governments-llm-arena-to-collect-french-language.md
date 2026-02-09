---
layout: default
title: compar:IA: The French Government's LLM arena to collect French-language human prompts and preference data
---

# compar:IA: The French Government's LLM arena to collect French-language human prompts and preference data
**arXiv**：[2602.06669v1](https://arxiv.org/abs/2602.06669) · [PDF](https://arxiv.org/pdf/2602.06669.pdf)  
**作者**：Lucie Termignon, Simonas Zilinskas, Hadrien Pélissier, Aurélien Barrot, Nicolas Chesnais, Elie Gavoty  

**一句话要点**：提出compar:IA平台以收集法语人类提示和偏好数据，解决非英语语言模型性能与对齐问题。

**关键词**：人类偏好数据收集, 多语言模型对齐, 开源数字公共服务, 盲对比较界面, 法语语言模型评估

## 3 点简述
- 核心问题：非英语语言模型因缺乏人类偏好数据，性能、文化对齐和安全鲁棒性降低。
- 方法要点：开发开源数字公共服务，通过盲对比较界面收集大规模法语提示和用户偏好。
- 实验或效果：截至2026-02-07，收集超60万提示和25万投票，89%为法语，发布三个开放数据集。

## 摘要（原文）

> Large Language Models (LLMs) often show reduced performance, cultural alignment, and safety robustness in non-English languages, partly because English dominates both pre-training data and human preference alignment datasets. Training methods like Reinforcement Learning from Human Feedback (RLHF) and Direct Preference Optimization (DPO) require human preference data, which remains scarce and largely non-public for many languages beyond English. To address this gap, we introduce compar:IA, an open-source digital public service developed inside the French government and designed to collect large-scale human preference data from a predominantly French-speaking general audience. The platform uses a blind pairwise comparison interface to capture unconstrained, real-world prompts and user judgments across a diverse set of language models, while maintaining low participation friction and privacy-preserving automated filtering. As of 2026-02-07, compar:IA has collected over 600,000 free-form prompts and 250,000 preference votes, with approximately 89% of the data in French. We release three complementary datasets -- conversations, votes, and reactions -- under open licenses, and present initial analyses, including a French-language model leaderboard and user interaction patterns. Beyond the French context, compar:IA is evolving toward an international digital public good, offering reusable infrastructure for multilingual model training, evaluation, and the study of human-AI interaction.

