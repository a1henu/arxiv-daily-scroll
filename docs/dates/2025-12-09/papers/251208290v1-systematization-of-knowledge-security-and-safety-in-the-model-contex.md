---
layout: default
title: Systematization of Knowledge: Security and Safety in the Model Context Protocol Ecosystem
---

# Systematization of Knowledge: Security and Safety in the Model Context Protocol Ecosystem
**arXiv**：[2512.08290v1](https://arxiv.org/abs/2512.08290) · [PDF](https://arxiv.org/pdf/2512.08290.pdf)  
**作者**：Shiva Gaire, Srijan Gyawali, Saroj Mishra, Suman Niroula, Dilip Thakur, Umesh Yadav  

**一句话要点**：系统化分析模型上下文协议生态中的安全与安全风险，提出分类与防御路线图

**关键词**：模型上下文协议, 安全风险分类, 对抗性威胁, 认知性危害, 多代理环境, 防御路线图

## 3 点简述
- 核心问题：模型上下文协议（MCP）作为LLM连接外部数据和工具的标准，模糊了幻觉与安全漏洞的边界，引入新威胁。
- 方法要点：建立风险分类学，区分对抗性安全威胁（如间接提示注入）和认知性安全危害（如分布式工具委托中的对齐失败）。
- 实验或效果：分析MCP原语（资源、提示、工具）的结构性漏洞，并调查从加密来源到运行时意图验证的先进防御方法。

## 摘要（原文）

> The Model Context Protocol (MCP) has emerged as the de facto standard for connecting Large Language Models (LLMs) to external data and tools, effectively functioning as the "USB-C for Agentic AI." While this decoupling of context and execution solves critical interoperability challenges, it introduces a profound new threat landscape where the boundary between epistemic errors (hallucinations) and security breaches (unauthorized actions) dissolves. This Systematization of Knowledge (SoK) aims to provide a comprehensive taxonomy of risks in the MCP ecosystem, distinguishing between adversarial security threats (e.g., indirect prompt injection, tool poisoning) and epistemic safety hazards (e.g., alignment failures in distributed tool delegation). We analyze the structural vulnerabilities of MCP primitives, specifically Resources, Prompts, and Tools, and demonstrate how "context" can be weaponized to trigger unauthorized operations in multi-agent environments. Furthermore, we survey state-of-the-art defenses, ranging from cryptographic provenance (ETDI) to runtime intent verification, and conclude with a roadmap for securing the transition from conversational chatbots to autonomous agentic operating systems.

