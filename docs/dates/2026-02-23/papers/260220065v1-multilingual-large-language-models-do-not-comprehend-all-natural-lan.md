---
layout: default
title: Multilingual Large Language Models do not comprehend all natural languages to equal degrees
---

# Multilingual Large Language Models do not comprehend all natural languages to equal degrees
**arXiv**：[2602.20065v1](https://arxiv.org/abs/2602.20065) · [PDF](https://arxiv.org/pdf/2602.20065.pdf)  
**作者**：Natalia Moskvina, Raquel Montero, Masaya Yoshida, Ferdy Hubers, Paolo Morosi, Walid Irhaymi, Jin Yan, Tamara Serrano, Elena Pagliarini, Fritz Günther, Evelina Leivada  

**一句话要点**：评估多语言大语言模型在12种语言上的理解能力，发现英语并非最佳表现语言。

**关键词**：多语言大语言模型, 语言理解评估, 低资源语言, 分词影响, 训练数据偏差, 跨语系比较

## 3 点简述
- 核心问题：多语言大语言模型在不同语言上的理解能力存在差异，但现有基准主要评估高资源语言。
- 方法要点：通过语言理解任务测试3个流行模型在12种语言上的表现，涵盖多个语系。
- 实验或效果：模型在所有语言上均落后于人类基线，英语被多个罗曼语超越，性能受分词、训练数据等因素影响。

## 摘要（原文）

> Large Language Models (LLMs) play a critical role in how humans access information. While their core use relies on comprehending written requests, our understanding of this ability is currently limited, because most benchmarks evaluate LLMs in high-resource languages predominantly spoken by Western, Educated, Industrialised, Rich, and Democratic (WEIRD) communities. The default assumption is that English is the best-performing language for LLMs, while smaller, low-resource languages are linked to less reliable outputs, even in multilingual, state-of-the-art models. To track variation in the comprehension abilities of LLMs, we prompt 3 popular models on a language comprehension task across 12 languages, representing the Indo-European, Afro-Asiatic, Turkic, Sino-Tibetan, and Japonic language families. Our results suggest that the models exhibit remarkable linguistic accuracy across typologically diverse languages, yet they fall behind human baselines in all of them, albeit to different degrees. Contrary to what was expected, English is not the best-performing language, as it was systematically outperformed by several Romance languages, even lower-resource ones. We frame the results by discussing the role of several factors that drive LLM performance, such as tokenization, language distance from Spanish and English, size of training data, and data origin in high- vs. low-resource languages and WEIRD vs. non-WEIRD communities.

