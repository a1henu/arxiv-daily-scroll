---
layout: default
title: VIGIL: Defending LLM Agents Against Tool Stream Injection via Verify-Before-Commit
---

# VIGIL: Defending LLM Agents Against Tool Stream Injection via Verify-Before-Commit
**arXiv**：[2601.05755v1](https://arxiv.org/abs/2601.05755) · [PDF](https://arxiv.org/pdf/2601.05755.pdf)  
**作者**：Junda Lin, Zhaomeng Zhou, Zhi Zheng, Shuochen Liu, Tong Xu, Yong Chen, Enhong Chen  

**一句话要点**：提出VIGIL框架以防御LLM代理在开放环境中的工具流注入攻击

**关键词**：LLM代理安全, 工具流注入防御, 验证前提交协议, 意图验证, 动态基准测试

## 3 点简述
- 核心问题：LLM代理面临工具流中的间接提示注入风险，现有防御在严格对齐与自适应推理间存在冲突
- 方法要点：采用验证前提交协议，通过推测性假设生成和基于意图的验证确保安全
- 实验或效果：在SIREN基准上，VIGIL降低攻击成功率超22%，相比静态基线提升效用超一倍

## 摘要（原文）

> LLM agents operating in open environments face escalating risks from indirect prompt injection, particularly within the tool stream where manipulated metadata and runtime feedback hijack execution flow. Existing defenses encounter a critical dilemma as advanced models prioritize injected rules due to strict alignment while static protection mechanisms sever the feedback loop required for adaptive reasoning. To reconcile this conflict, we propose \textbf{VIGIL}, a framework that shifts the paradigm from restrictive isolation to a verify-before-commit protocol. By facilitating speculative hypothesis generation and enforcing safety through intent-grounded verification, \textbf{VIGIL} preserves reasoning flexibility while ensuring robust control. We further introduce \textbf{SIREN}, a benchmark comprising 959 tool stream injection cases designed to simulate pervasive threats characterized by dynamic dependencies. Extensive experiments demonstrate that \textbf{VIGIL} outperforms state-of-the-art dynamic defenses by reducing the attack success rate by over 22\% while more than doubling the utility under attack compared to static baselines, thereby achieving an optimal balance between security and utility. Code is available at https://anonymous.4open.science/r/VIGIL-378B/.

