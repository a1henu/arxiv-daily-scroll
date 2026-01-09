---
layout: default
title: Beyond the "Truth": Investigating Election Rumors on Truth Social During the 2024 Election
---

# Beyond the "Truth": Investigating Election Rumors on Truth Social During the 2024 Election
**arXiv**：[2601.04631v1](https://arxiv.org/abs/2601.04631) · [PDF](https://arxiv.org/pdf/2601.04631.pdf)  
**作者**：Etienne Casanova, R. Michael Alvarez  

**一句话要点**：提出多阶段谣言检测代理，利用大语言模型分析2024年选举期间Truth Social平台上的谣言传播心理动态。

**关键词**：谣言检测, 大语言模型应用, 心理测量, 社交网络分析, 错觉真相效应, 选举谣言

## 3 点简述
- 核心问题：研究小众替代技术平台上的选举谣言传播，量化自然环境中错觉真相效应的心理动态。
- 方法要点：开发结合微调RoBERTa分类器、关键词过滤和GPT-4o mini两阶段验证的多阶段谣言检测代理。
- 实验或效果：发现分享概率随曝光次数增加而上升，模拟显示四轮传播后近四分之一用户被感染。

## 摘要（原文）

> Large language models (LLMs) offer unprecedented opportunities for analyzing social phenomena at scale. This paper demonstrates the value of LLMs in psychological measurement by (1) compiling the first large-scale dataset of election rumors on a niche alt-tech platform, (2) developing a multistage Rumor Detection Agent that leverages LLMs for high-precision content classification, and (3) quantifying the psychological dynamics of rumor propagation, specifically the "illusory truth effect" in a naturalistic setting. The Rumor Detection Agent combines (i) a synthetic data-augmented, fine-tuned RoBERTa classifier, (ii) precision keyword filtering, and (iii) a two-pass LLM verification pipeline using GPT-4o mini. The findings reveal that sharing probability rises steadily with each additional exposure, providing large-scale empirical evidence for dose-response belief reinforcement in ideologically homogeneous networks. Simulation results further demonstrate rapid contagion effects: nearly one quarter of users become "infected" within just four propagation iterations. Taken together, these results illustrate how LLMs can transform psychological science by enabling the rigorous measurement of belief dynamics and misinformation spread in massive, real-world datasets.

