---
layout: default
title: Assessing Deanonymization Risks with Stylometry-Assisted LLM Agent
---

# Assessing Deanonymization Risks with Stylometry-Assisted LLM Agent
**arXiv**：[2602.23079v1](https://arxiv.org/abs/2602.23079) · [PDF](https://arxiv.org/pdf/2602.23079.pdf)  
**作者**：Boyang Zhang, Yang Zhang  

**一句话要点**：提出SALA方法评估与缓解大语言模型在新闻文本中的去匿名化风险

**关键词**：去匿名化风险, 大语言模型代理, 文体分析, 作者归属, 隐私保护, 文本重写

## 3 点简述
- 核心问题：大语言模型增强的作者推断能力可能导致新闻文本等数据的意外去匿名化风险
- 方法要点：结合定量文体特征与大语言模型推理，构建可解释的SALA框架进行稳健作者归属
- 实验或效果：在大规模新闻数据集上验证SALA高准确性，并提出引导重写策略降低作者可识别性

## 摘要（原文）

> The rapid advancement of large language models (LLMs) has enabled powerful authorship inference capabilities, raising growing concerns about unintended deanonymization risks in textual data such as news articles. In this work, we introduce an LLM agent designed to evaluate and mitigate such risks through a structured, interpretable pipeline. Central to our framework is the proposed $\textit{SALA}$ (Stylometry-Assisted LLM Analysis) method, which integrates quantitative stylometric features with LLM reasoning for robust and transparent authorship attribution. Experiments on large-scale news datasets demonstrate that $\textit{SALA}$, particularly when augmented with a database module, achieves high inference accuracy in various scenarios. Finally, we propose a guided recomposition strategy that leverages the agent's reasoning trace to generate rewriting prompts, effectively reducing authorship identifiability while preserving textual meaning. Our findings highlight both the deanonymization potential of LLM agents and the importance of interpretable, proactive defenses for safeguarding author privacy.

