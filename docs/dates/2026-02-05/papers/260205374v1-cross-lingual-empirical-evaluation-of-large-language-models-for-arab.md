---
layout: default
title: Cross-Lingual Empirical Evaluation of Large Language Models for Arabic Medical Tasks
---

# Cross-Lingual Empirical Evaluation of Large Language Models for Arabic Medical Tasks
**arXiv**：[2602.05374v1](https://arxiv.org/abs/2602.05374) · [PDF](https://arxiv.org/pdf/2602.05374.pdf)  
**作者**：Chaimae Abouzahir, Congbo Ma, Nizar Habash, Farah E. Shamout  

**一句话要点**：通过跨语言实证分析揭示大语言模型在阿拉伯语医疗任务中的性能差距与结构问题

**关键词**：跨语言评估, 医疗问答, 大语言模型, 阿拉伯语处理, 分词分析, 可靠性评估

## 3 点简述
- 核心问题：大语言模型在英语以外的语言（如阿拉伯语）医疗任务中性能下降，原因不明。
- 方法要点：对比分析阿拉伯语和英语医疗问答，结合分词和可靠性分析探究性能差距。
- 实验或效果：发现语言驱动的性能差距随任务复杂度增加而加剧，分词结构碎片化且模型置信度与正确性相关性低。

## 摘要（原文）

> In recent years, Large Language Models (LLMs) have become widely used in medical applications, such as clinical decision support, medical education, and medical question answering. Yet, these models are often English-centric, limiting their robustness and reliability for linguistically diverse communities. Recent work has highlighted discrepancies in performance in low-resource languages for various medical tasks, but the underlying causes remain poorly understood. In this study, we conduct a cross-lingual empirical analysis of LLM performance on Arabic and English medical question and answering. Our findings reveal a persistent language-driven performance gap that intensifies with increasing task complexity. Tokenization analysis exposes structural fragmentation in Arabic medical text, while reliability analysis suggests that model-reported confidence and explanations exhibit limited correlation with correctness. Together, these findings underscore the need for language-aware design and evaluation strategies in LLMs for medical tasks.

