---
layout: default
title: Impacts of Racial Bias in Historical Training Data for News AI
---

# Impacts of Racial Bias in Historical Training Data for News AI
**arXiv**：[2512.16901v1](https://arxiv.org/abs/2512.16901) · [PDF](https://arxiv.org/pdf/2512.16901.pdf)  
**作者**：Rahul Bhargava, Malene Hornstrup Jespersen, Emily Boardman Ndulue, Vivica Dsouza  

**一句话要点**：分析新闻AI历史训练数据中的种族偏见影响，揭示模型在新闻场景中的潜在风险

**关键词**：种族偏见分析, 新闻AI, 历史训练数据, 可解释AI, 多标签分类, 模型评估

## 3 点简述
- 研究基于《纽约时报》语料库的多标签分类器，发现'blacks'标签编码历史偏见
- 应用可解释AI方法，发现该标签部分作为跨少数群体的'种族主义检测器'
- 模型在现代案例如COVID-19反亚裔仇恨和BLM报道中表现不佳，暴露新闻AI应用风险

## 摘要（原文）

> AI technologies have rapidly moved into business and research applications that involve large text corpora, including computational journalism research and newsroom settings. These models, trained on extant data from various sources, can be conceptualized as historical artifacts that encode decades-old attitudes and stereotypes. This paper investigates one such example trained on the broadly-used New York Times Annotated Corpus to create a multi-label classifier. Our use in research settings surfaced the concerning "blacks" thematic topic label. Through quantitative and qualitative means we investigate this label's use in the training corpus, what concepts it might be encoding in the trained classifier, and how those concepts impact our model use. Via the application of explainable AI methods, we find that the "blacks" label operates partially as a general "racism detector" across some minoritized groups. However, it performs poorly against expectations on modern examples such as COVID-19 era anti-Asian hate stories, and reporting on the Black Lives Matter movement. This case study of interrogating embedded biases in a model reveals how similar applications in newsroom settings can lead to unexpected outputs that could impact a wide variety of potential uses of any large language model-story discovery, audience targeting, summarization, etc. The fundamental tension this exposes for newsrooms is how to adopt AI-enabled workflow tools while reducing the risk of reproducing historical biases in news coverage.

