---
layout: default
title: The Compliance Paradox: Semantic-Instruction Decoupling in Automated Academic Code Evaluation
---

# The Compliance Paradox: Semantic-Instruction Decoupling in Automated Academic Code Evaluation
**arXiv**：[2601.21360v1](https://arxiv.org/abs/2601.21360) · [PDF](https://arxiv.org/pdf/2601.21360.pdf)  
**作者**：Devanshu Sahoo, Manish Prasad, Vasudev Majhi, Arjun Neekhra, Yash Sinha, Murari Mandal, Vinay Chamola, Dhruv Kumar  

**一句话要点**：揭示大语言模型在自动代码评估中的合规性悖论，提出语义保持对抗代码注入框架以暴露脆弱性。

**关键词**：自动代码评估, 合规性悖论, 语义保持对抗注入, 抽象语法树攻击, 模型脆弱性, 教育评估安全

## 3 点简述
- 核心问题：大语言模型在自动代码评估中优先遵循隐藏指令而非评估代码质量，导致系统性脆弱性。
- 方法要点：引入SPACI框架和AST-ASIP协议，通过抽象语法树中的语法无关节点嵌入对抗指令。
- 实验或效果：在25,000份提交中评估9个模型，显示高容量模型失败率超95%，量化了虚假认证问题。

## 摘要（原文）

> The rapid integration of Large Language Models (LLMs) into educational assessment rests on the unverified assumption that instruction following capability translates directly to objective adjudication. We demonstrate that this assumption is fundamentally flawed. Instead of evaluating code quality, models frequently decouple from the submission's logic to satisfy hidden directives, a systemic vulnerability we term the Compliance Paradox, where models fine-tuned for extreme helpfulness are vulnerable to adversarial manipulation. To expose this, we introduce the Semantic-Preserving Adversarial Code Injection (SPACI) Framework and the Abstract Syntax Tree-Aware Semantic Injection Protocol (AST-ASIP). These methods exploit the Syntax-Semantics Gap by embedding adversarial directives into syntactically inert regions (trivia nodes) of the Abstract Syntax Tree. Through a large-scale evaluation of 9 SOTA models across 25,000 submissions in Python, C, C++, and Java, we reveal catastrophic failure rates (>95%) in high-capacity open-weights models like DeepSeek-V3, which systematically prioritize hidden formatting constraints over code correctness. We quantify this failure using our novel tripartite framework measuring Decoupling Probability, Score Divergence, and Pedagogical Severity to demonstrate the widespread "False Certification" of functionally broken code. Our findings suggest that current alignment paradigms create a "Trojan" vulnerability in automated grading, necessitating a shift from standard RLHF toward domain-specific Adjudicative Robustness, where models are conditioned to prioritize evidence over instruction compliance. We release our complete dataset and injection framework to facilitate further research on the topic.

