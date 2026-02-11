---
layout: default
title: Would a Large Language Model Pay Extra for a View? Inferring Willingness to Pay from Subjective Choices
---

# Would a Large Language Model Pay Extra for a View? Inferring Willingness to Pay from Subjective Choices
**arXiv**：[2602.09802v1](https://arxiv.org/abs/2602.09802) · [PDF](https://arxiv.org/pdf/2602.09802.pdf)  
**作者**：Manon Reusens, Sofie Goethals, Toon Calders, David Martens  

**一句话要点**：提出基于选择困境推断大语言模型支付意愿的方法，评估其在旅行辅助场景中的主观决策能力。

**关键词**：大语言模型, 支付意愿推断, 主观决策, 旅行辅助, 多项Logit模型, 模型偏差

## 3 点简述
- 研究大语言模型在无客观正确答案场景中的主观决策，如旅行辅助。
- 使用多项Logit模型分析模型响应，推导隐含支付意愿并与人类基准比较。
- 实验显示模型能生成有意义支付意愿，但存在系统性偏差，需优化提示设计和用户表示。

## 摘要（原文）

> As Large Language Models (LLMs) are increasingly deployed in applications such as travel assistance and purchasing support, they are often required to make subjective choices on behalf of users in settings where no objectively correct answer exists. We study LLM decision-making in a travel-assistant context by presenting models with choice dilemmas and analyzing their responses using multinomial logit models to derive implied willingness to pay (WTP) estimates. These WTP values are subsequently compared to human benchmark values from the economics literature. In addition to a baseline setting, we examine how model behavior changes under more realistic conditions, including the provision of information about users' past choices and persona-based prompting. Our results show that while meaningful WTP values can be derived for larger LLMs, they also display systematic deviations at the attribute level. Additionally, they tend to overestimate human WTP overall, particularly when expensive options or business-oriented personas are introduced. Conditioning models on prior preferences for cheaper options yields valuations that are closer to human benchmarks. Overall, our findings highlight both the potential and the limitations of using LLMs for subjective decision support and underscore the importance of careful model selection, prompt design, and user representation when deploying such systems in practice.

