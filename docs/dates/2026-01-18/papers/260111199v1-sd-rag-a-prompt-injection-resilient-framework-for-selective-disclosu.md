---
layout: default
title: SD-RAG: A Prompt-Injection-Resilient Framework for Selective Disclosure in Retrieval-Augmented Generation
---

# SD-RAG: A Prompt-Injection-Resilient Framework for Selective Disclosure in Retrieval-Augmented Generation
**arXiv**：[2601.11199v1](https://arxiv.org/abs/2601.11199) · [PDF](https://arxiv.org/pdf/2601.11199.pdf)  
**作者**：Aiman Al Masoud, Marco Arazzi, Antonino Nocera  

**一句话要点**：提出SD-RAG框架，通过检索阶段控制选择性披露，以增强RAG系统的隐私保护和抗提示注入攻击能力。

**关键词**：检索增强生成, 隐私保护, 选择性披露, 提示注入攻击, 图数据模型, 语义约束

## 3 点简述
- 核心问题：现有RAG方法易暴露敏感信息，且LLMs易受提示注入攻击，导致隐私泄露风险。
- 方法要点：在检索阶段应用净化与披露控制，结合语义机制和优化图数据模型，实现细粒度策略感知检索。
- 实验或效果：实验显示SD-RAG在隐私评分上提升达58%，并展现出对提示注入攻击的强韧性。

## 摘要（原文）

> Retrieval-Augmented Generation (RAG) has attracted significant attention due to its ability to combine the generative capabilities of Large Language Models (LLMs) with knowledge obtained through efficient retrieval mechanisms over large-scale data collections. Currently, the majority of existing approaches overlook the risks associated with exposing sensitive or access-controlled information directly to the generation model. Only a few approaches propose techniques to instruct the generative model to refrain from disclosing sensitive information; however, recent studies have also demonstrated that LLMs remain vulnerable to prompt injection attacks that can override intended behavioral constraints. For these reasons, we propose a novel approach to Selective Disclosure in Retrieval-Augmented Generation, called SD-RAG, which decouples the enforcement of security and privacy constraints from the generation process itself. Rather than relying on prompt-level safeguards, SD-RAG applies sanitization and disclosure controls during the retrieval phase, prior to augmenting the language model's input. Moreover, we introduce a semantic mechanism to allow the ingestion of human-readable dynamic security and privacy constraints together with an optimized graph-based data model that supports fine-grained, policy-aware retrieval. Our experimental evaluation demonstrates the superiority of SD-RAG over baseline existing approaches, achieving up to a $58\%$ improvement in the privacy score, while also showing a strong resilience to prompt injection attacks targeting the generative model.

