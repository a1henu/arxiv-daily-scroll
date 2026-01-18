---
layout: default
title: Model See, Model Do? Exposure-Aware Evaluation of Bug-vs-Fix Preference in Code LLMs
---

# Model See, Model Do? Exposure-Aware Evaluation of Bug-vs-Fix Preference in Code LLMs
**arXiv**：[2601.10496v1](https://arxiv.org/abs/2601.10496) · [PDF](https://arxiv.org/pdf/2601.10496.pdf)  
**作者**：Ali Al-Kaswan, Claudio Spiess, Prem Devanbu, Arie van Deursen, Maliheh Izadi  

**一句话要点**：提出暴露感知评估框架以量化训练数据暴露对代码LLM中bug与修复偏好的影响

**关键词**：代码大语言模型, bug修复偏好, 暴露感知评估, 训练数据影响, 成员测试, 代码生成

## 3 点简述
- 核心问题：代码LLM在生成或调试时可能偏好熟悉的错误代码而非正确修复，受训练数据暴露影响
- 方法要点：使用Data Portraits进行成员测试，基于ManySStuBs4J基准分层评估暴露情况
- 实验或效果：发现模型更常生成错误代码，暴露于错误示例时倾向加剧，但概率指标稳定偏好正确修复

## 摘要（原文）

> Large language models are increasingly used for code generation and debugging, but their outputs can still contain bugs, that originate from training data. Distinguishing whether an LLM prefers correct code, or a familiar incorrect version might be influenced by what it's been exposed to during training. We introduce an exposure-aware evaluation framework that quantifies how prior exposure to buggy versus fixed code influences a model's preference. Using the ManySStuBs4J benchmark, we apply Data Portraits for membership testing on the Stack-V2 corpus to estimate whether each buggy and fixed variant was seen during training. We then stratify examples by exposure and compare model preference using code completion as well as multiple likelihood-based scoring metrics We find that most examples (67%) have neither variant in the training data, and when only one is present, fixes are more frequently present than bugs. In model generations, models reproduce buggy lines far more often than fixes, with bug-exposed examples amplifying this tendency and fix-exposed examples showing only marginal improvement. In likelihood scoring, minimum and maximum token-probability metrics consistently prefer the fixed code across all conditions, indicating a stable bias toward correct fixes. In contrast, metrics like the Gini coefficient reverse preference when only the buggy variant was seen. Our results indicate that exposure can skew bug-fix evaluations and highlight the risk that LLMs may propagate memorised errors in practice.

