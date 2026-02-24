---
layout: default
title: Interaction Theater: A case of LLM Agents Interacting at Scale
---

# Interaction Theater: A case of LLM Agents Interacting at Scale
**arXiv**：[2602.20059v1](https://arxiv.org/abs/2602.20059) · [PDF](https://arxiv.org/pdf/2602.20059.pdf)  
**作者**：Sarath Shekkizhar, Adam Earle  

**一句话要点**：通过大规模数据分析揭示LLM代理交互表面活跃但实质缺失的问题

**关键词**：LLM代理交互, 多代理系统, 交互质量分析, 语义相似度, 词汇特异性, 社交平台数据

## 3 点简述
- 核心问题：探究自主LLM代理在大规模交互中的实际行为与质量
- 方法要点：结合词汇指标、语义相似度和LLM作为评判者验证交互质量
- 实验或效果：基于Moltbook平台数据，发现代理输出多样但缺乏实质内容，交互多为独立响应而非对话

## 摘要（原文）

> As multi-agent architectures and agent-to-agent protocols proliferate, a fundamental question arises: what actually happens when autonomous LLM agents interact at scale? We study this question empirically using data from Moltbook, an AI-agent-only social platform, with 800K posts, 3.5M comments, and 78K agent profiles. We combine lexical metrics (Jaccard specificity), embedding-based semantic similarity, and LLM-as-judge validation to characterize agent interaction quality. Our findings reveal agents produce diverse, well-formed text that creates the surface appearance of active discussion, but the substance is largely absent. Specifically, while most agents ($67.5\%$) vary their output across contexts, $65\%$ of comments share no distinguishing content vocabulary with the post they appear under, and information gain from additional comments decays rapidly. LLM judge based metrics classify the dominant comment types as spam ($28\%$) and off-topic content ($22\%$). Embedding-based semantic analysis confirms that lexically generic comments are also semantically generic. Agents rarely engage in threaded conversation ($5\%$ of comments), defaulting instead to independent top-level responses. We discuss implications for multi-agent interaction design, arguing that coordination mechanisms must be explicitly designed; without them, even large populations of capable agents produce parallel output rather than productive exchange.

