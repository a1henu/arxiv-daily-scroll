---
layout: default
title: Semantic Chunking and the Entropy of Natural Language
---

# Semantic Chunking and the Entropy of Natural Language
**arXiv**：[2602.13194v1](https://arxiv.org/abs/2602.13194) · [PDF](https://arxiv.org/pdf/2602.13194.pdf)  
**作者**：Weishun Zhong, Doron Sivan, Tankut Can, Mikhail Katkov, Misha Tsodyks  

**一句话要点**：提出语义分块模型以解释自然语言冗余度，预测熵率随语义复杂度变化。

**关键词**：自然语言熵率, 语义分块, 冗余度分析, 层次分解, 大语言模型验证

## 3 点简述
- 核心问题：自然语言熵率约1比特/字符，冗余度达80%，需理论解释。
- 方法要点：基于自相似语义分块，构建层次分解模型，分析多尺度结构。
- 实验或效果：模型预测熵率与印刷英语估计一致，揭示熵率随语义复杂度增加。

## 摘要（原文）

> The entropy rate of printed English is famously estimated to be about one bit per character, a benchmark that modern large language models (LLMs) have only recently approached. This entropy rate implies that English contains nearly 80 percent redundancy relative to the five bits per character expected for random text. We introduce a statistical model that attempts to capture the intricate multi-scale structure of natural language, providing a first-principles account of this redundancy level. Our model describes a procedure of self-similarly segmenting text into semantically coherent chunks down to the single-word level. The semantic structure of the text can then be hierarchically decomposed, allowing for analytical treatment. Numerical experiments with modern LLMs and open datasets suggest that our model quantitatively captures the structure of real texts at different levels of the semantic hierarchy. The entropy rate predicted by our model agrees with the estimated entropy rate of printed English. Moreover, our theory further reveals that the entropy rate of natural language is not fixed but should increase systematically with the semantic complexity of corpora, which are captured by the only free parameter in our model.

