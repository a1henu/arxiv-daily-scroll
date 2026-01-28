---
layout: default
title: AgenticSCR: An Autonomous Agentic Secure Code Review for Immature Vulnerabilities Detection
---

# AgenticSCR: An Autonomous Agentic Secure Code Review for Immature Vulnerabilities Detection
**arXiv**：[2601.19138v1](https://arxiv.org/abs/2601.19138) · [PDF](https://arxiv.org/pdf/2601.19138.pdf)  
**作者**：Wachiraphan Charoenwet, Kla Tantithamthavorn, Patanamon Thongtanunam, Hong Yi Lin, Minwoo Jeong, Ming Wu  

**一句话要点**：提出AgenticSCR以解决预提交阶段不成熟漏洞检测问题

**关键词**：安全代码审查, 不成熟漏洞检测, Agentic AI, 预提交阶段, 语义记忆

## 3 点简述
- 核心问题：现有SAST工具噪声大且易漏检不成熟漏洞，LLMs受限于上下文窗口和工具使用。
- 方法要点：结合LLMs与自主决策、工具调用和代码导航的Agentic AI，增强安全语义记忆。
- 实验或效果：在定制基准上评估，AgenticSCR正确代码审查评论相对基线提升至少153%，显著优于SAST工具。

## 摘要（原文）

> Secure code review is critical at the pre-commit stage, where vulnerabilities must be caught early under tight latency and limited-context constraints. Existing SAST-based checks are noisy and often miss immature, context-dependent vulnerabilities, while standalone Large Language Models (LLMs) are constrained by context windows and lack explicit tool use. Agentic AI, which combine LLMs with autonomous decision-making, tool invocation, and code navigation, offer a promising alternative, but their effectiveness for pre-commit secure code review is not yet well understood. In this work, we introduce AgenticSCR, an agentic AI for secure code review for detecting immature vulnerabilities during the pre-commit stage, augmented by security-focused semantic memories. Using our own curated benchmark of immature vulnerabilities, tailored to the pre-commit secure code review, we empirically evaluate how accurate is our AgenticSCR for localizing, detecting, and explaining immature vulnerabilities. Our results show that AgenticSCR achieves at least 153% relatively higher percentage of correct code review comments than the static LLM-based baseline, and also substantially surpasses SAST tools. Moreover, AgenticSCR generates more correct comments in four out of five vulnerability types, consistently and significantly outperforming all other baselines. These findings highlight the importance of Agentic Secure Code Review, paving the way towards an emerging research area of immature vulnerability detection.

