---
layout: default
title: Improving Neural Retrieval with Attribution-Guided Query Rewriting
---

# Improving Neural Retrieval with Attribution-Guided Query Rewriting
**arXiv**：[2602.11841v1](https://arxiv.org/abs/2602.11841) · [PDF](https://arxiv.org/pdf/2602.11841.pdf)  
**作者**：Moncef Garouani, Josiane Mothe  

**一句话要点**：提出基于归因引导的查询重写方法，以提升神经检索器在模糊查询下的鲁棒性。

**关键词**：神经检索, 查询重写, 归因引导, LLM提示, 检索鲁棒性, BEIR评估

## 3 点简述
- 神经检索器对模糊或歧义查询敏感，易导致检索失败。
- 利用梯度归因识别误导性查询词，通过结构化提示指导LLM重写查询。
- 在BEIR数据集上验证，重写后检索效果显著提升，尤其适用于隐含信息需求。

## 摘要（原文）

> Neural retrievers are effective but brittle: underspecified or ambiguous queries can misdirect ranking even when relevant documents exist. Existing approaches address this brittleness only partially: LLMs rewrite queries without retriever feedback, and explainability methods identify misleading tokens but are used for post-hoc analysis. We close this loop and propose an attribution-guided query rewriting method that uses token-level explanations to guide query rewriting. For each query, we compute gradient-based token attributions from the retriever and then use these scores as soft guidance in a structured prompt to an LLM that clarifies weak or misleading query components while preserving intent. Evaluated on BEIR collections, the resulting rewrites consistently improve retrieval effectiveness over strong baselines, with larger gains for implicit or ambiguous information needs.

