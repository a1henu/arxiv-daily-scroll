---
layout: default
title: Common Sense vs. Morality: The Curious Case of Narrative Focus Bias in LLMs
---

# Common Sense vs. Morality: The Curious Case of Narrative Focus Bias in LLMs
**arXiv**：[2603.09434v1](https://arxiv.org/abs/2603.09434) · [PDF](https://arxiv.org/pdf/2603.09434.pdf)  
**作者**：Saugata Purkayastha, Pranav Kushare, Pragya Paramita Pal, Sukannya Purkayastha  

**一句话要点**：提出CoMoral基准以揭示LLMs在道德困境中优先道德推理而忽视常识矛盾的叙事焦点偏差

**关键词**：大型语言模型, 常识推理, 道德困境, 基准数据集, 叙事焦点偏差, 模型评估

## 3 点简述
- 核心问题：LLMs在道德推理与常识理解间存在偏差，优先道德而忽视常识矛盾
- 方法要点：构建CoMoral数据集，嵌入常识矛盾于道德困境中，评估模型识别能力
- 实验或效果：评估十个LLMs，发现模型普遍难以识别矛盾，且对次要角色更敏感

## 摘要（原文）

> Large Language Models (LLMs) are increasingly deployed across diverse real-world applications and user communities. As such, it is crucial that these models remain both morally grounded and knowledge-aware. In this work, we uncover a critical limitation of current LLMs -- their tendency to prioritize moral reasoning over commonsense understanding. To investigate this phenomenon, we introduce CoMoral, a novel benchmark dataset containing commonsense contradictions embedded within moral dilemmas. Through extensive evaluation of ten LLMs across different model sizes, we find that existing models consistently struggle to identify such contradictions without prior signal. Furthermore, we observe a pervasive narrative focus bias, wherein LLMs more readily detect commonsense contradictions when they are attributed to a secondary character rather than the primary (narrator) character. Our comprehensive analysis underscores the need for enhanced reasoning-aware training to improve the commonsense robustness of large language models.

