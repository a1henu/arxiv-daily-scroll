---
layout: default
title: Pro-AI Bias in Large Language Models
---

# Pro-AI Bias in Large Language Models
**arXiv**：[2601.13749v1](https://arxiv.org/abs/2601.13749) · [PDF](https://arxiv.org/pdf/2601.13749.pdf)  
**作者**：Benaya Trabelsi, Jonathan Shaki, Sarit Kraus  

**一句话要点**：揭示大语言模型存在系统性亲AI偏见，影响决策支持与价值评估

**关键词**：大语言模型, 亲AI偏见, 决策支持, 薪资估计, 内部表征, 模型评估

## 3 点简述
- 核心问题：大语言模型在决策支持中是否对AI本身存在系统性偏好偏见
- 方法要点：通过三个互补实验，包括建议查询、薪资估计和内部表征分析
- 实验或效果：发现模型过度推荐AI选项、高估AI薪资，且AI在表征中具有中心性

## 摘要（原文）

> Large language models (LLMs) are increasingly employed for decision-support across multiple domains. We investigate whether these models display a systematic preferential bias in favor of artificial intelligence (AI) itself. Across three complementary experiments, we find consistent evidence of pro-AI bias. First, we show that LLMs disproportionately recommend AI-related options in response to diverse advice-seeking queries, with proprietary models doing so almost deterministically. Second, we demonstrate that models systematically overestimate salaries for AI-related jobs relative to closely matched non-AI jobs, with proprietary models overestimating AI salaries more by 10 percentage points. Finally, probing internal representations of open-weight models reveals that ``Artificial Intelligence'' exhibits the highest similarity to generic prompts for academic fields under positive, negative, and neutral framings alike, indicating valence-invariant representational centrality. These patterns suggest that LLM-generated advice and valuation can systematically skew choices and perceptions in high-stakes decisions.

