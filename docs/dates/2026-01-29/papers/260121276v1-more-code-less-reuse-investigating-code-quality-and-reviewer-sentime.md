---
layout: default
title: More Code, Less Reuse: Investigating Code Quality and Reviewer Sentiment towards AI-generated Pull Requests
---

# More Code, Less Reuse: Investigating Code Quality and Reviewer Sentiment towards AI-generated Pull Requests
**arXiv**：[2601.21276v1](https://arxiv.org/abs/2601.21276) · [PDF](https://arxiv.org/pdf/2601.21276.pdf)  
**作者**：Haoming Huang, Pongchai Jaisri, Shota Shimizu, Lingfeng Chen, Sota Nakashima, Gema Rodríguez-Pérez  

**一句话要点**：研究AI生成PR的代码质量与评审者情感，揭示冗余增加与情感偏差问题

**关键词**：AI生成代码, 代码质量评估, 评审者情感分析, 技术债务, 人机协作, 代码复用

## 3 点简述
- 核心问题：现有指标仅关注通过率，忽略AI生成代码对长期可维护性和可读性的影响
- 方法要点：基于代码指标评估客观特性，分析开发者对AI生成PR的情感反应
- 实验或效果：发现AI代理常忽视代码复用，导致冗余高于人类，但评审者情感更中性或积极

## 摘要（原文）

> Large Language Model (LLM) Agents are advancing quickly, with the increasing leveraging of LLM Agents to assist in development tasks such as code generation. While LLM Agents accelerate code generation, studies indicate they may introduce adverse effects on development. However, existing metrics solely measure pass rates, failing to reflect impacts on long-term maintainability and readability, and failing to capture human intuitive evaluations of PR. To increase the comprehensiveness of this problem, we investigate and evaluate the characteristics of LLM to know the pull requests' characteristics beyond the pass rate. We observe the code quality and maintainability within PRs based on code metrics to evaluate objective characteristics and developers' reactions to the pull requests from both humans and LLM's generation. Evaluation results indicate that LLM Agents frequently disregard code reuse opportunities, resulting in higher levels of redundancy compared to human developers. In contrast to the quality issues, our emotions analysis reveals that reviewers tend to express more neutral or positive emotions towards AI-generated contributions than human ones. This disconnect suggests that the surface-level plausibility of AI code masks redundancy, leading to the silent accumulation of technical debt in real-world development environments. Our research provides insights for improving human-AI collaboration.

