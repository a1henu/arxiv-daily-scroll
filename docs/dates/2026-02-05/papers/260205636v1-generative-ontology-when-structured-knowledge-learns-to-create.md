---
layout: default
title: Generative Ontology: When Structured Knowledge Learns to Create
---

# Generative Ontology: When Structured Knowledge Learns to Create
**arXiv**：[2602.05636v1](https://arxiv.org/abs/2602.05636) · [PDF](https://arxiv.org/pdf/2602.05636.pdf)  
**作者**：Benny Cheung  

**一句话要点**：提出生成式本体框架，结合本体与LLM以生成结构有效且具创造性的领域设计

**关键词**：生成式本体, 多智能体系统, 检索增强生成, 结构化生成, 游戏设计生成

## 3 点简述
- 核心问题：传统本体无法生成新内容，LLM生成缺乏结构有效性，导致幻觉输出
- 方法要点：将领域知识编码为可执行模式，通过多智能体管道约束LLM生成，确保结构完整
- 实验或效果：在GameGrammar系统中生成完整桌面游戏设计，满足本体约束并保持创造性

## 摘要（原文）

> Traditional ontologies excel at describing domain structure but cannot generate novel artifacts. Large language models generate fluently but produce outputs that lack structural validity, hallucinating mechanisms without components, goals without end conditions. We introduce Generative Ontology, a framework that synthesizes these complementary strengths: ontology provides the grammar; the LLM provides the creativity.
>   Generative Ontology encodes domain knowledge as executable Pydantic schemas that constrain LLM generation via DSPy signatures. A multi-agent pipeline assigns specialized roles to different ontology domains: a Mechanics Architect designs game systems, a Theme Weaver integrates narrative, a Balance Critic identifies exploits. Each agent carrying a professional "anxiety" that prevents shallow, agreeable outputs. Retrieval-augmented generation grounds novel designs in precedents from existing exemplars, while iterative validation ensures coherence between mechanisms and components.
>   We demonstrate the framework through GameGrammar, a system for generating complete tabletop game designs. Given a thematic prompt ("bioluminescent fungi competing in a cave ecosystem"), the pipeline produces structurally complete, playable game specifications with mechanisms, components, victory conditions, and setup instructions. These outputs satisfy ontological constraints while remaining genuinely creative.
>   The pattern generalizes beyond games. Any domain with expert vocabulary, validity constraints, and accumulated exemplars (music composition, software architecture, culinary arts) is a candidate for Generative Ontology. We argue that constraints do not limit creativity but enable it: just as grammar makes poetry possible, ontology makes structured generation possible.

