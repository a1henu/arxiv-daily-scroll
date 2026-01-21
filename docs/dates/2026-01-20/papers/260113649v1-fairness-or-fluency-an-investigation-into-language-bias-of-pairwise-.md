---
layout: default
title: Fairness or Fluency? An Investigation into Language Bias of Pairwise LLM-as-a-Judge
---

# Fairness or Fluency? An Investigation into Language Bias of Pairwise LLM-as-a-Judge
**arXiv**：[2601.13649v1](https://arxiv.org/abs/2601.13649) · [PDF](https://arxiv.org/pdf/2601.13649.pdf)  
**作者**：Xiaolin Zhou, Zheng Luo, Yicheng Gao, Qixuan Chen, Xiyang Hu, Yue Zhao, Ruishan Liu  

**一句话要点**：研究LLM作为裁判在成对比较中的语言偏见，揭示跨语言性能差异与主要语言偏好。

**关键词**：LLM作为裁判, 语言偏见, 成对比较, 性能差异, 跨语言评估, 困惑度分析

## 3 点简述
- 核心问题：LLM作为裁判存在语言偏见，影响评估公平性，与人类偏好不一致。
- 方法要点：分析同语言和跨语言场景下的偏见，包括性能差异和语言偏好。
- 实验或效果：发现欧洲语言优于非洲语言，英语答案更受青睐，困惑度仅部分相关。

## 摘要（原文）

> Recent advances in Large Language Models (LLMs) have incentivized the development of LLM-as-a-judge, an application of LLMs where they are used as judges to decide the quality of a certain piece of text given a certain context. However, previous studies have demonstrated that LLM-as-a-judge can be biased towards different aspects of the judged texts, which often do not align with human preference. One of the identified biases is language bias, which indicates that the decision of LLM-as-a-judge can differ based on the language of the judged texts. In this paper, we study two types of language bias in pairwise LLM-as-a-judge: (1) performance disparity between languages when the judge is prompted to compare options from the same language, and (2) bias towards options written in major languages when the judge is prompted to compare options of two different languages. We find that for same-language judging, there exist significant performance disparities across language families, with European languages consistently outperforming African languages, and this bias is more pronounced in culturally-related subjects. For inter-language judging, we observe that most models favor English answers, and that this preference is influenced more by answer language than question language. Finally, we investigate whether language bias is in fact caused by low-perplexity bias, a previously identified bias of LLM-as-a-judge, and we find that while perplexity is slightly correlated with language bias, language bias cannot be fully explained by perplexity only.

