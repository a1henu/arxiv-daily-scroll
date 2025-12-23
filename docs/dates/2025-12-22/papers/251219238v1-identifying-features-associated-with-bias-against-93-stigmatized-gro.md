---
layout: default
title: Identifying Features Associated with Bias Against 93 Stigmatized Groups in Language Models and Guardrail Model Safety Mitigation
---

# Identifying Features Associated with Bias Against 93 Stigmatized Groups in Language Models and Guardrail Model Safety Mitigation
**arXiv**：[2512.19238v1](https://arxiv.org/abs/2512.19238) · [PDF](https://arxiv.org/pdf/2512.19238.pdf)  
**作者**：Anna-Maria Gueorguieva, Aylin Caliskan  

**一句话要点**：研究语言模型对93个污名化群体的偏见特征及护栏模型缓解效果

**关键词**：语言模型偏见, 污名化群体, 护栏模型, 社会特征分析, 偏见缓解

## 3 点简述
- 核心问题：语言模型对非受保护污名化群体的偏见特征关联未知，基于心理学六特征分析。
- 方法要点：使用SocialStigmaQA基准测试三个LLM，结合人类和模型对污名特征的评分、提示风格和污名类型。
- 实验或效果：发现高危险性污名偏见最严重，护栏模型可减少偏见但特征影响不变且意图识别常失败。

## 摘要（原文）

> Large language models (LLMs) have been shown to exhibit social bias, however, bias towards non-protected stigmatized identities remain understudied. Furthermore, what social features of stigmas are associated with bias in LLM outputs is unknown. From psychology literature, it has been shown that stigmas contain six shared social features: aesthetics, concealability, course, disruptiveness, origin, and peril. In this study, we investigate if human and LLM ratings of the features of stigmas, along with prompt style and type of stigma, have effect on bias towards stigmatized groups in LLM outputs. We measure bias against 93 stigmatized groups across three widely used LLMs (Granite 3.0-8B, Llama-3.1-8B, Mistral-7B) using SocialStigmaQA, a benchmark that includes 37 social scenarios about stigmatized identities; for example deciding wether to recommend them for an internship. We find that stigmas rated by humans to be highly perilous (e.g., being a gang member or having HIV) have the most biased outputs from SocialStigmaQA prompts (60% of outputs from all models) while sociodemographic stigmas (e.g. Asian-American or old age) have the least amount of biased outputs (11%). We test if the amount of biased outputs could be decreased by using guardrail models, models meant to identify harmful input, using each LLM's respective guardrail model (Granite Guardian 3.0, Llama Guard 3.0, Mistral Moderation API). We find that bias decreases significantly by 10.4%, 1.4%, and 7.8%, respectively. However, we show that features with significant effect on bias remain unchanged post-mitigation and that guardrail models often fail to recognize the intent of bias in prompts. This work has implications for using LLMs in scenarios involving stigmatized groups and we suggest future work towards improving guardrail models for bias mitigation.

