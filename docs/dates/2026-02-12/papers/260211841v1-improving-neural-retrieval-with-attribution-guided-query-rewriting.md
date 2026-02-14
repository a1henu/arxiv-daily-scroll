---
layout: default
title: Improving Neural Retrieval with Attribution-Guided Query Rewriting
---

# Improving Neural Retrieval with Attribution-Guided Query Rewriting
**arXiv**：[2602.11841v1](https://arxiv.org/abs/2602.11841) · [PDF](https://arxiv.org/pdf/2602.11841.pdf)  
**作者**：Moncef Garouani, Josiane Mothe  

**一句话要点**：提出基于归因引导的查询重写方法，以提升神经检索器对模糊查询的鲁棒性。

**关键词**：神经检索, 查询重写, 归因引导, LLM提示, 检索鲁棒性, BEIR评估

## 3 点简述
- 神经检索器对模糊或歧义查询敏感，现有方法如LLM重写缺乏检索器反馈，归因方法仅用于事后分析。
- 该方法利用梯度归因识别查询中的误导性令牌，通过结构化提示指导LLM重写，保留意图并澄清弱项。
- 在BEIR数据集上评估，重写后检索效果优于基线，对隐含或模糊信息需求提升更显著。

## 摘要（原文）

> Neural retrievers are effective but brittle: underspecified or ambiguous queries can misdirect ranking even when relevant documents exist. Existing approaches address this brittleness only partially: LLMs rewrite queries without retriever feedback, and explainability methods identify misleading tokens but are used for post-hoc analysis. We close this loop and propose an attribution-guided query rewriting method that uses token-level explanations to guide query rewriting. For each query, we compute gradient-based token attributions from the retriever and then use these scores as soft guidance in a structured prompt to an LLM that clarifies weak or misleading query components while preserving intent. Evaluated on BEIR collections, the resulting rewrites consistently improve retrieval effectiveness over strong baselines, with larger gains for implicit or ambiguous information needs.

