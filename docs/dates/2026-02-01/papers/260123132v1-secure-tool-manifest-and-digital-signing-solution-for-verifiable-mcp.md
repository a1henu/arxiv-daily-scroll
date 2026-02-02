---
layout: default
title: Secure Tool Manifest and Digital Signing Solution for Verifiable MCP and LLM Pipelines
---

# Secure Tool Manifest and Digital Signing Solution for Verifiable MCP and LLM Pipelines
**arXiv**：[2601.23132v1](https://arxiv.org/abs/2601.23132) · [PDF](https://arxiv.org/pdf/2601.23132.pdf)  
**作者**：Saeid Jamshidi, Kawser Wazed Nafi, Arghavan Moradi Dakhel, Foutse Khomh, Amin Nikanjam, Mohammad Adnan Hamdaqa  

**一句话要点**：提出安全工具清单与数字签名框架以增强LLM执行管道的可验证性

**关键词**：大型语言模型, 模型上下文协议, 数字签名, 执行验证, 安全框架, 管道完整性

## 3 点简述
- LLM在敏感领域应用时，执行管道易受操纵且行为不可验证
- 框架通过加密签名清单、透明验证日志和元数据隔离确保执行完整性
- 评估显示框架线性扩展，有效接受合法执行并拒绝非法执行

## 摘要（原文）

> Large Language Models (LLMs) are increasingly adopted in sensitive domains such as healthcare and financial institutions' data analytics; however, their execution pipelines remain vulnerable to manipulation and unverifiable behavior. Existing control mechanisms, such as the Model Context Protocol (MCP), define compliance policies for tool invocation but lack verifiable enforcement and transparent validation of model actions. To address this gap, we propose a novel Secure Tool Manifest and Digital Signing Framework, a structured and security-aware extension of Model Context Protocols. The framework enforces cryptographically signed manifests, integrates transparent verification logs, and isolates model-internal execution metadata from user-visible components to ensure verifiable execution integrity. Furthermore, the evaluation demonstrates that the framework scales nearly linearly (R-squared = 0.998), achieves near-perfect acceptance of valid executions while consistently rejecting invalid ones, and maintains balanced model utilization across execution pipelines.

