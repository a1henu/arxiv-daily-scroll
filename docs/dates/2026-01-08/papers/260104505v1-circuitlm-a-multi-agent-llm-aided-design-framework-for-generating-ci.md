---
layout: default
title: CircuitLM: A Multi-Agent LLM-Aided Design Framework for Generating Circuit Schematics from Natural Language Prompts
---

# CircuitLM: A Multi-Agent LLM-Aided Design Framework for Generating Circuit Schematics from Natural Language Prompts
**arXiv**：[2601.04505v1](https://arxiv.org/abs/2601.04505) · [PDF](https://arxiv.org/pdf/2601.04505.pdf)  
**作者**：Khandakar Shakib Al Hasan, Syed Rifat Raiyan, Hasin Mahtab Alvee, Wahid Sadik  

**一句话要点**：提出CircuitLM多智能体框架，通过结构化流程从自然语言生成电路图以解决LLM幻觉问题。

**关键词**：电路图生成, 多智能体系统, 自然语言处理, 电气约束验证, 嵌入式系统设计, 知识库增强

## 3 点简述
- 核心问题：LLM生成电路图时易产生细节幻觉、违反电气约束且输出非机器可读。
- 方法要点：采用五阶段多智能体流程，结合知识库和验证机制生成结构化CircuitJSON。
- 实验或效果：在100个嵌入式系统提示上评估，引入DMCV框架验证结构电气有效性，实现高保真度。

## 摘要（原文）

> Generating accurate circuit schematics from high-level natural language descriptions remains a persistent challenge in electronics design, as large language models (LLMs) frequently hallucinate in granular details, violate electrical constraints, and produce non-machine-readable outputs. We present CircuitLM, a novel multi-agent LLM-aided circuit design pipeline that translates user prompts into structured, visually interpretable CircuitJSON schematics through five sequential stages: (i) LLM-based component identification, (ii) canonical pinout retrieval, (iii) chain-of-thought reasoning by an electronics expert agent, (iv) JSON schematic synthesis, and (v) force-directed SVG visualization. Anchored by a curated, embedding-powered component knowledge base. While LLMs often violate electrical constraints, CircuitLM bridges this gap by grounding generation in a verified and dynamically extensible component database, initially comprising 50 components. To ensure safety, we incorporate a hybrid evaluation framework, namely Dual-Metric Circuit Validation (DMCV), validated against human-expert assessments, which achieves high fidelity in microcontroller-centric designs. We evaluate the system on 100 diverse embedded-systems prompts across six LLMs and introduce DMCV to assess both structural and electrical validity. This work bridges natural language input to deployable hardware designs, enabling reliable circuit prototyping by non-experts. Our code and data will be made public upon acceptance.

