---
layout: default
title: Script Gap: Evaluating LLM Triage on Indian Languages in Native vs Roman Scripts in a Real World Setting
---

# Script Gap: Evaluating LLM Triage on Indian Languages in Native vs Roman Scripts in a Real World Setting
**arXiv**：[2512.10780v1](https://arxiv.org/abs/2512.10780) · [PDF](https://arxiv.org/pdf/2512.10780.pdf)  
**作者**：Manurag Khullar, Utkarsh Desai, Poorva Malviya, Aman Dalmia, Zheyuan Ryan Shi  

**一句话要点**：评估LLM在印度语言母语与罗马化脚本下的分诊性能，揭示真实场景中的脚本差距

**关键词**：大语言模型评估, 临床分诊, 印度语言处理, 罗马化文本, 真实世界数据, 性能差距

## 3 点简述
- 核心问题：LLM在印度临床应用中处理罗马化文本时性能下降，导致分诊错误风险
- 方法要点：基于真实用户查询数据集，比较LLM在五种印度语言和尼泊尔语的母语与罗马化脚本下的表现
- 实验或效果：罗马化消息的F1分数比母语脚本低5-12点，可能造成近200万额外分诊错误

## 摘要（原文）

> Large Language Models (LLMs) are increasingly deployed in high-stakes clinical applications in India. In many such settings, speakers of Indian languages frequently communicate using romanized text rather than native scripts, yet existing research rarely evaluates this orthographic variation using real-world data. We investigate how romanization impacts the reliability of LLMs in a critical domain: maternal and newborn healthcare triage. We benchmark leading LLMs on a real-world dataset of user-generated queries spanning five Indian languages and Nepali. Our results reveal consistent degradation in performance for romanized messages, with F1 scores trailing those of native scripts by 5-12 points. At our partner maternal health organization in India, this gap could cause nearly 2 million excess errors in triage. Crucially, this performance gap by scripts is not due to a failure in clinical reasoning. We demonstrate that LLMs often correctly infer the semantic intent of romanized queries. Nevertheless, their final classification outputs remain brittle in the presence of orthographic noise in romanized inputs. Our findings highlight a critical safety blind spot in LLM-based health systems: models that appear to understand romanized input may still fail to act on it reliably.

