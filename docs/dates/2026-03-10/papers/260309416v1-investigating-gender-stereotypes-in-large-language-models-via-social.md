---
layout: default
title: Investigating Gender Stereotypes in Large Language Models via Social Determinants of Health
---

# Investigating Gender Stereotypes in Large Language Models via Social Determinants of Health
**arXiv**：[2603.09416v1](https://arxiv.org/abs/2603.09416) · [PDF](https://arxiv.org/pdf/2603.09416.pdf)  
**作者**：Trung Hieu Ngo, Adrien Bazoge, Solen Quiniou, Pierre-Antoine Gourraud, Emmanuel Morin  

**一句话要点**：通过社会健康决定因素探究大语言模型中的性别刻板印象

**关键词**：大语言模型, 性别偏见, 社会健康决定因素, 医疗记录分析, 交互评估

## 3 点简述
- 核心问题：大语言模型在医疗等敏感领域传播训练数据中的偏见，现有评估忽视社会健康决定因素间的交互作用。
- 方法要点：基于法国患者记录，探究性别与其他社会健康决定因素的交互关系，以评估模型偏见。
- 实验或效果：实验发现模型依赖嵌入的刻板印象进行性别化决策，评估交互作用可补充现有偏见评估方法。

## 摘要（原文）

> Large Language Models (LLMs) excel in Natural Language Processing (NLP) tasks, but they often propagate biases embedded in their training data, which is potentially impactful in sensitive domains like healthcare. While existing benchmarks evaluate biases related to individual social determinants of health (SDoH) such as gender or ethnicity, they often overlook interactions between these factors and lack context-specific assessments. This study investigates bias in LLMs by probing the relationships between gender and other SDoH in French patient records. Through a series of experiments, we found that embedded stereotypes can be probed using SDoH input and that LLMs rely on embedded stereotypes to make gendered decisions, suggesting that evaluating interactions among SDoH factors could usefully complement existing approaches to assessing LLM performance and bias.

