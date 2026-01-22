---
layout: default
title: RECAP: Resistance Capture in Text-based Mental Health Counseling with Large Language Models
---

# RECAP: Resistance Capture in Text-based Mental Health Counseling with Large Language Models
**arXiv**：[2601.14780v1](https://arxiv.org/abs/2601.14780) · [PDF](https://arxiv.org/pdf/2601.14780.pdf)  
**作者**：Anqi Li, Yuqian Chen, Yu Lu, Zhaoming Chen, Yuan Xie, Zhenzhong Lan  

**一句话要点**：提出RECAP框架，基于PsyFIRE理论检测文本心理咨询中的客户抵抗行为

**关键词**：文本心理咨询, 抵抗行为检测, 大型语言模型, 细粒度分类, 可解释性框架

## 3 点简述
- 核心问题：现有NLP方法简化抵抗类别，忽略干预序列动态，可解释性有限
- 方法要点：构建ClientResistance语料库，开发两阶段框架检测抵抗及细粒度类型并提供解释
- 实验或效果：RECAP在区分合作与抵抗上F1达91.25%，细粒度分类宏F1为66.58%，优于基线

## 摘要（原文）

> Recognizing and navigating client resistance is critical for effective mental health counseling, yet detecting such behaviors is particularly challenging in text-based interactions. Existing NLP approaches oversimplify resistance categories, ignore the sequential dynamics of therapeutic interventions, and offer limited interpretability.
>   To address these limitations, we propose PsyFIRE, a theoretically grounded framework capturing 13 fine-grained resistance behaviors alongside collaborative interactions. Based on PsyFIRE, we construct the ClientResistance corpus with 23,930 annotated utterances from real-world Chinese text-based counseling, each supported by context-specific rationales. Leveraging this dataset, we develop RECAP, a two-stage framework that detects resistance and fine-grained resistance types with explanations.
>   RECAP achieves 91.25% F1 for distinguishing collaboration and resistance and 66.58% macro-F1 for fine-grained resistance categories classification, outperforming leading prompt-based LLM baselines by over 20 points. Applied to a separate counseling dataset and a pilot study with 62 counselors, RECAP reveals the prevalence of resistance, its negative impact on therapeutic relationships and demonstrates its potential to improve counselors' understanding and intervention strategies.

