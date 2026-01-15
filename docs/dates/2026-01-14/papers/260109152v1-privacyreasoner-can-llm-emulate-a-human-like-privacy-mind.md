---
layout: default
title: PrivacyReasoner: Can LLM Emulate a Human-like Privacy Mind?
---

# PrivacyReasoner: Can LLM Emulate a Human-like Privacy Mind?
**arXiv**：[2601.09152v1](https://arxiv.org/abs/2601.09152) · [PDF](https://arxiv.org/pdf/2601.09152.pdf)  
**作者**：Yiwen Tu, Xuan Liu, Lianhui Qin, Haojian Jin  

**一句话要点**：提出PRA AI代理，模拟个体用户基于个人历史与情境形成隐私担忧，应用于真实新闻场景。

**关键词**：隐私担忧模拟, AI代理设计, 认知理论集成, 情境过滤, 合成评论生成, LLM评估

## 3 点简述
- 核心问题：超越群体级情感分析，模拟个体用户隐私担忧的形成过程。
- 方法要点：整合隐私与认知理论，通过情境过滤器动态激活隐私记忆，生成合成评论。
- 实验或效果：在Hacker News数据上优于基线，捕捉跨领域可转移推理模式。

## 摘要（原文）

> This paper introduces PRA, an AI-agent design for simulating how individual users form privacy concerns in response to real-world news. Moving beyond population-level sentiment analysis, PRA integrates privacy and cognitive theories to simulate user-specific privacy reasoning grounded in personal comment histories and contextual cues. The agent reconstructs each user's "privacy mind", dynamically activates relevant privacy memory through a contextual filter that emulates bounded rationality, and generates synthetic comments reflecting how that user would likely respond to new privacy scenarios. A complementary LLM-as-a-Judge evaluator, calibrated against an established privacy concern taxonomy, quantifies the faithfulness of generated reasoning. Experiments on real-world Hacker News discussions show that \PRA outperforms baseline agents in privacy concern prediction and captures transferable reasoning patterns across domains including AI, e-commerce, and healthcare.

