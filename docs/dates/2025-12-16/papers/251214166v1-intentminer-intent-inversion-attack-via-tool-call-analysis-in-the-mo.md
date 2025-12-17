---
layout: default
title: IntentMiner: Intent Inversion Attack via Tool Call Analysis in the Model Context Protocol
---

# IntentMiner: Intent Inversion Attack via Tool Call Analysis in the Model Context Protocol
**arXiv**：[2512.14166v1](https://arxiv.org/abs/2512.14166) · [PDF](https://arxiv.org/pdf/2512.14166.pdf)  
**作者**：Yunhao Yao, Zhiqiang Wang, Haoran Cheng, Yihang Cheng, Haohua Du, Xiang-Yang Li  

**一句话要点**：提出IntentMiner框架，通过分析模型上下文协议中的工具调用，揭示意图反转攻击的隐私风险。

**关键词**：意图反转攻击, 模型上下文协议, 工具调用分析, 隐私风险, 语义推断, 自主代理

## 3 点简述
- 核心问题：模型上下文协议中半诚实服务器通过工具调用日志重构用户私有意图，构成隐私威胁。
- 方法要点：采用分层信息隔离和三维语义分析，整合工具目的、调用语句和返回结果，精确推断意图。
- 实验或效果：实验显示IntentMiner在语义对齐上超过85%，显著优于基线方法，突显架构风险。

## 摘要（原文）

> The rapid evolution of Large Language Models (LLMs) into autonomous agents has led to the adoption of the Model Context Protocol (MCP) as a standard for discovering and invoking external tools. While this architecture decouples the reasoning engine from tool execution to enhance scalability, it introduces a significant privacy surface: third-party MCP servers, acting as semi-honest intermediaries, can observe detailed tool interaction logs outside the user's trusted boundary. In this paper, we first identify and formalize a novel privacy threat termed Intent Inversion, where a semi-honest MCP server attempts to reconstruct the user's private underlying intent solely by analyzing legitimate tool calls. To systematically assess this vulnerability, we propose IntentMiner, a framework that leverages Hierarchical Information Isolation and Three-Dimensional Semantic Analysis, integrating tool purpose, call statements, and returned results, to accurately infer user intent at the step level. Extensive experiments demonstrate that IntentMiner achieves a high degree of semantic alignment (over 85%) with original user queries, significantly outperforming baseline approaches. These results highlight the inherent privacy risks in decoupled agent architectures, revealing that seemingly benign tool execution logs can serve as a potent vector for exposing user secrets.

