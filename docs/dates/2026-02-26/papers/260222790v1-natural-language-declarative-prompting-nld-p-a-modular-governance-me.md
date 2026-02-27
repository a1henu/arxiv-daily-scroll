---
layout: default
title: Natural Language Declarative Prompting (NLD-P): A Modular Governance Method for Prompt Design Under Model Drift
---

# Natural Language Declarative Prompting (NLD-P): A Modular Governance Method for Prompt Design Under Model Drift
**arXiv**：[2602.22790v1](https://arxiv.org/abs/2602.22790) · [PDF](https://arxiv.org/pdf/2602.22790.pdf)  
**作者**：Hyunwoo Kim, Hanau Yi, Jaehee Bae, Yumin Kim  

**一句话要点**：提出自然语言声明式提示（NLD-P）作为模块化治理方法，以应对大语言模型漂移下的提示设计挑战。

**关键词**：自然语言声明式提示, 模型漂移治理, 提示工程, 模块化控制, 非开发者框架

## 3 点简述
- 核心问题：大语言模型快速演进导致提示行为不稳定，传统方法难以确保可控性和可解释性。
- 方法要点：NLD-P将提示设计重构为声明式治理框架，分离来源、约束逻辑、任务内容和后生成评估。
- 实验或效果：定义了最小合规标准，分析了模型对模式的接受度，并定位为非开发者可访问的治理工具。

## 摘要（原文）

> The rapid evolution of large language models (LLMs) has transformed prompt engineering from a localized craft into a systems-level governance challenge. As models scale and update across generations, prompt behavior becomes sensitive to shifts in instruction-following policies, alignment regimes, and decoding strategies, a phenomenon we characterize as GPT-scale model drift. Under such conditions, surface-level formatting conventions and ad hoc refinement are insufficient to ensure stable, interpretable control. This paper reconceptualizes Natural Language Declarative Prompting (NLD-P) as a declarative governance method rather than a rigid field template. NLD-P is formalized as a modular control abstraction that separates provenance, constraint logic, task content, and post-generation evaluation, encoded directly in natural language without reliance on external orchestration code. We define minimal compliance criteria, analyze model-dependent schema receptivity, and position NLD-P as an accessible governance framework for non-developer practitioners operating within evolving LLM ecosystems. Portions of drafting and editorial refinement employed a schema-bound LLM assistant configured under NLD-P. All conceptual framing, methodological claims, and final revisions were directed, reviewed, and approved by the human author under a documented human-in-the-loop protocol. The paper concludes by outlining implications for declarative control under ongoing model evolution and identifying directions for future empirical validation.

