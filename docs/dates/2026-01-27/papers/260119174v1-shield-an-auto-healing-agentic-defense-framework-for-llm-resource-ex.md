---
layout: default
title: SHIELD: An Auto-Healing Agentic Defense Framework for LLM Resource Exhaustion Attacks
---

# SHIELD: An Auto-Healing Agentic Defense Framework for LLM Resource Exhaustion Attacks
**arXiv**：[2601.19174v1](https://arxiv.org/abs/2601.19174) · [PDF](https://arxiv.org/pdf/2601.19174.pdf)  
**作者**：Nirhoshan Sivaroopan, Kanchana Thilakarathna, Albert Zomaya, Manu, Yi Guo, Jo Plested, Tim Lynar, Jack Yang, Wangli Yang  

**一句话要点**：提出SHIELD多代理自愈防御框架以应对LLM资源耗尽攻击

**关键词**：LLM安全, 资源耗尽攻击, 多代理系统, 自愈防御, 语义攻击检测

## 3 点简述
- 核心问题：海绵攻击通过诱导过度计算威胁LLM系统，现有防御方法难以适应攻击策略演变。
- 方法要点：基于三阶段防御代理，集成语义相似性检索、模式匹配和LLM推理，辅以知识更新和提示优化代理形成自愈循环。
- 实验或效果：在非语义和语义海绵攻击中均实现高F1分数，优于基于困惑度和独立LLM的防御方法。

## 摘要（原文）

> Sponge attacks increasingly threaten LLM systems by inducing excessive computation and DoS. Existing defenses either rely on statistical filters that fail on semantically meaningful attacks or use static LLM-based detectors that struggle to adapt as attack strategies evolve. We introduce SHIELD, a multi-agent, auto-healing defense framework centered on a three-stage Defense Agent that integrates semantic similarity retrieval, pattern matching, and LLM-based reasoning. Two auxiliary agents, a Knowledge Updating Agent and a Prompt Optimization Agent, form a closed self-healing loop, when an attack bypasses detection, the system updates an evolving knowledgebase, and refines defense instructions. Extensive experiments show that SHIELD consistently outperforms perplexity-based and standalone LLM defenses, achieving high F1 scores across both non-semantic and semantic sponge attacks, demonstrating the effectiveness of agentic self-healing against evolving resource-exhaustion threats.

