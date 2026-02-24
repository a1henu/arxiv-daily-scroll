---
layout: default
title: Can Large Language Models Replace Human Coders? Introducing ContentBench
---

# Can Large Language Models Replace Human Coders? Introducing ContentBench
**arXiv**：[2602.19467v1](https://arxiv.org/abs/2602.19467) · [PDF](https://arxiv.org/pdf/2602.19467.pdf)  
**作者**：Michael Haman  

**一句话要点**：提出ContentBench基准套件以评估低成本大语言模型在内容分析编码任务中的替代潜力

**关键词**：大语言模型评估, 内容分析编码, 基准测试, 低成本模型, 社交媒体文本分类

## 3 点简述
- 核心问题：低成本大语言模型能否替代人类进行内容分析的编码工作
- 方法要点：构建公开基准套件，使用合成社交媒体帖子数据集，基于多模型一致性和人工审核生成参考标签
- 实验或效果：最佳低成本模型与参考标签一致性达97-99%，成本低至数美元处理5万帖子，但小模型在讽刺内容上表现差

## 摘要（原文）

> Can low-cost large language models (LLMs) take over the interpretive coding work that still anchors much of empirical content analysis? This paper introduces ContentBench, a public benchmark suite that helps answer this replacement question by tracking how much agreement low-cost LLMs achieve and what they cost on the same interpretive coding tasks. The suite uses versioned tracks that invite researchers to contribute new benchmark datasets. I report results from the first track, ContentBench-ResearchTalk v1.0: 1,000 synthetic, social-media-style posts about academic research labeled into five categories spanning praise, critique, sarcasm, questions, and procedural remarks. Reference labels are assigned only when three state-of-the-art reasoning models (GPT-5, Gemini 2.5 Pro, and Claude Opus 4.1) agree unanimously, and all final labels are checked by the author as a quality-control audit. Among the 59 evaluated models, the best low-cost LLMs reach roughly 97-99% agreement with these jury labels, far above GPT-3.5 Turbo, the model behind early ChatGPT and the initial wave of LLM-based text annotation. Several top models can code 50,000 posts for only a few dollars, pushing large-scale interpretive coding from a labor bottleneck toward questions of validation, reporting, and governance. At the same time, small open-weight models that run locally still struggle on sarcasm-heavy items (for example, Llama 3.2 3B reaches only 4% agreement on hard-sarcasm). ContentBench is released with data, documentation, and an interactive quiz at contentbench.github.io to support comparable evaluations over time and to invite community extensions.

