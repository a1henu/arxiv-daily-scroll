---
layout: default
title: FraudShield: Knowledge Graph Empowered Defense for LLMs against Fraud Attacks
---

# FraudShield: Knowledge Graph Empowered Defense for LLMs against Fraud Attacks
**arXiv**：[2601.22485v1](https://arxiv.org/abs/2601.22485) · [PDF](https://arxiv.org/pdf/2601.22485.pdf)  
**作者**：Naen Xu, Jinghuai Zhang, Ping He, Chunyi Zhou, Jun Wang, Zhihui Fu, Tianyu Du, Zhaoxiang Wang, Shouling Ji  

**一句话要点**：提出FraudShield框架，利用知识图谱增强LLMs对欺诈攻击的防御能力

**关键词**：欺诈防御, 知识图谱, 大语言模型, 可解释性, 自动化流程

## 3 点简述
- 核心问题：LLMs在关键自动化流程中易受欺诈信息操纵，现有防御方法在效果、可解释性和泛化性上存在局限
- 方法要点：构建欺诈战术-关键词知识图谱，通过结构化知识增强输入，引导LLMs生成更安全的响应
- 实验或效果：在四种主流LLMs和五种欺诈类型上优于先进防御方法，并提供可解释的生成线索

## 摘要（原文）

> Large language models (LLMs) have been widely integrated into critical automated workflows, including contract review and job application processes. However, LLMs are susceptible to manipulation by fraudulent information, which can lead to harmful outcomes. Although advanced defense methods have been developed to address this issue, they often exhibit limitations in effectiveness, interpretability, and generalizability, particularly when applied to LLM-based applications. To address these challenges, we introduce FraudShield, a novel framework designed to protect LLMs from fraudulent content by leveraging a comprehensive analysis of fraud tactics. Specifically, FraudShield constructs and refines a fraud tactic-keyword knowledge graph to capture high-confidence associations between suspicious text and fraud techniques. The structured knowledge graph augments the original input by highlighting keywords and providing supporting evidence, guiding the LLM toward more secure responses. Extensive experiments show that FraudShield consistently outperforms state-of-the-art defenses across four mainstream LLMs and five representative fraud types, while also offering interpretable clues for the model's generations.

