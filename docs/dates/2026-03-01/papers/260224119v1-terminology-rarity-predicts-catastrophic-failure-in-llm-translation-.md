---
layout: default
title: Terminology Rarity Predicts Catastrophic Failure in LLM Translation of Low-Resource Ancient Languages: Evidence from Ancient Greek
---

# Terminology Rarity Predicts Catastrophic Failure in LLM Translation of Low-Resource Ancient Languages: Evidence from Ancient Greek
**arXiv**：[2602.24119v1](https://arxiv.org/abs/2602.24119) · [PDF](https://arxiv.org/pdf/2602.24119.pdf)  
**作者**：James L. Zainaldin, Cameron Pattison, Manuela Marai, Jacob Wu, Mark J. Schiefsky  

**一句话要点**：提出术语稀有度预测LLM在低资源古语言翻译中的灾难性失败，以古希腊语为例

**关键词**：低资源古语言翻译, 术语稀有度预测, LLM翻译评估, 古希腊语技术散文, 专家人工评估, 自动评估指标

## 3 点简述
- 核心问题：评估LLM在低资源古语言（古希腊语）技术散文翻译中的质量，特别是未翻译文本的失败风险。
- 方法要点：结合自动评估指标和专家人工评估（MQM框架），分析三个商业LLM对盖伦著作的翻译。
- 实验或效果：发现术语稀有度与翻译失败强相关（r=-0.97），在未翻译文本中质量方差大，自动指标在高质翻译中区分度有限。

## 摘要（原文）

> This study presents the first systematic, reference-free human evaluation of large language model (LLM) machine translation (MT) for Ancient Greek (AG) technical prose. We evaluate translations by three commercial LLMs (Claude, Gemini, ChatGPT) of twenty paragraph-length passages from two works by the Greek physician Galen of Pergamum (ca. 129-216 CE): On Mixtures, which has two published English translations, and On the Composition of Drugs according to Kinds, which has never been fully translated into English. We assess translation quality using both standard automated evaluation metrics (BLEU, chrF++, METEOR, ROUGE-L, BERTScore, COMET, BLEURT) and expert human evaluation via a modified Multidimensional Quality Metrics (MQM) framework applied to all 60 translations by a team of domain specialists. On the previously translated expository text, LLMs achieved high translation quality (mean MQM score 95.2/100), with performance approaching expert level. On the untranslated pharmacological text, aggregate quality was lower (79.9/100) but with high variance driven by two passages presenting extreme terminological density; excluding these, scores converged to within 4 points of the translated text. Terminology rarity, operationalized via corpus frequency in the literary Diorisis Ancient Greek Corpus, emerged as a strong predictor of translation failure (r = -.97 for passage-level quality on the untranslated text). Automated metrics showed moderate correlation with human judgment overall on the text with a wide quality spread (Composition), but no metric discriminated among high-quality translations. We discuss implications for the use of LLMs in Classical scholarship and for the design of automated evaluation pipelines for low-resource ancient languages.

