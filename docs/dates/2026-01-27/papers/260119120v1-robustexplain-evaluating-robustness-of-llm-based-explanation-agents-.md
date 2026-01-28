---
layout: default
title: RobustExplain: Evaluating Robustness of LLM-Based Explanation Agents for Recommendation
---

# RobustExplain: Evaluating Robustness of LLM-Based Explanation Agents for Recommendation
**arXiv**：[2601.19120v1](https://arxiv.org/abs/2601.19120) · [PDF](https://arxiv.org/pdf/2601.19120.pdf)  
**作者**：Guilin Zhang, Kai Zhao, Jeffrey Friedman, Xu Chu  

**一句话要点**：提出RobustExplain框架，评估推荐系统中基于LLM的解释代理在用户行为噪声下的鲁棒性

**关键词**：推荐系统, 大语言模型, 解释生成, 鲁棒性评估, 用户行为噪声

## 3 点简述
- 核心问题：LLM生成的推荐解释对现实用户行为噪声的鲁棒性尚未被系统评估
- 方法要点：引入五种现实用户行为扰动和四维鲁棒性指标，建立任务级评估框架
- 实验效果：在四个代表性LLM上测试，当前模型仅具中等鲁棒性，大模型稳定性提升最高8%

## 摘要（原文）

> Large Language Models (LLMs) are increasingly used to generate natural-language explanations in recommender systems, acting as explanation agents that reason over user behavior histories. While prior work has focused on explanation fluency and relevance under fixed inputs, the robustness of LLM-generated explanations to realistic user behavior noise remains largely unexplored. In real-world web platforms, interaction histories are inherently noisy due to accidental clicks, temporal inconsistencies, missing values, and evolving preferences, raising concerns about explanation stability and user trust. We present RobustExplain, the first systematic evaluation framework for measuring the robustness of LLM-generated recommendation explanations. RobustExplain introduces five realistic user behavior perturbations evaluated across multiple severity levels and a multi-dimensional robustness metric capturing semantic, keyword, structural, and length consistency. Our goal is to establish a principled, task-level evaluation framework and initial robustness baselines, rather than to provide a comprehensive leaderboard across all available LLMs. Experiments on four representative LLMs (7B--70B) show that current models exhibit only moderate robustness, with larger models achieving up to 8% higher stability. Our results establish the first robustness benchmarks for explanation agents and highlight robustness as a critical dimension for trustworthy, agent-driven recommender systems at web scale.

