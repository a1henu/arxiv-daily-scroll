---
layout: default
title: XCR-Bench: A Multi-Task Benchmark for Evaluating Cultural Reasoning in LLMs
---

# XCR-Bench: A Multi-Task Benchmark for Evaluating Cultural Reasoning in LLMs
**arXiv**：[2601.14063v1](https://arxiv.org/abs/2601.14063) · [PDF](https://arxiv.org/pdf/2601.14063.pdf)  
**作者**：Mohsinul Kabir, Tasnim Ahmed, Md Mezbaur Rahman, Shaoxiong Ji, Hassan Alhuzali, Sophia Ananiadou  

**一句话要点**：提出XCR-Bench以解决大语言模型跨文化推理评估中高质量数据稀缺问题

**关键词**：跨文化推理, 大语言模型评估, 文化特定项目, 平行句子对, 文化偏见分析

## 3 点简述
- 核心问题：大语言模型跨文化能力评估缺乏高质量文化特定项目标注的平行句子对数据
- 方法要点：构建包含4.9k平行句子和1,098个文化特定项目的基准，整合Newmark和Hall文化理论
- 实验或效果：发现先进模型在社交礼仪和文化参考适应方面存在弱点，并编码区域和民族宗教偏见

## 摘要（原文）

> Cross-cultural competence in large language models (LLMs) requires the ability to identify Culture-Specific Items (CSIs) and to adapt them appropriately across cultural contexts. Progress in evaluating this capability has been constrained by the scarcity of high-quality CSI-annotated corpora with parallel cross-cultural sentence pairs. To address this limitation, we introduce XCR-Bench, a Cross(X)-Cultural Reasoning Benchmark consisting of 4.9k parallel sentences and 1,098 unique CSIs, spanning three distinct reasoning tasks with corresponding evaluation metrics. Our corpus integrates Newmark's CSI framework with Hall's Triad of Culture, enabling systematic analysis of cultural reasoning beyond surface-level artifacts and into semi-visible and invisible cultural elements such as social norms, beliefs, and values. Our findings show that state-of-the-art LLMs exhibit consistent weaknesses in identifying and adapting CSIs related to social etiquette and cultural reference. Additionally, we find evidence that LLMs encode regional and ethno-religious biases even within a single linguistic setting during cultural adaptation. We release our corpus and code to facilitate future research on cross-cultural NLP.

