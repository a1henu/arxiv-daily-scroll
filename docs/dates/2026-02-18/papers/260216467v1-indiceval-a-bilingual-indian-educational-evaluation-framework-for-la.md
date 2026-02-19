---
layout: default
title: IndicEval: A Bilingual Indian Educational Evaluation Framework for Large Language Models
---

# IndicEval: A Bilingual Indian Educational Evaluation Framework for Large Language Models
**arXiv**：[2602.16467v1](https://arxiv.org/abs/2602.16467) · [PDF](https://arxiv.org/pdf/2602.16467.pdf)  
**作者**：Saurabh Bharti, Gaurav Azad, Abhinaw Jagtap, Nachiket Tapas  

**一句话要点**：提出IndicEval双语印度教育评估框架，以真实考试问题评估大语言模型在STEM和人文学科中的表现。

**关键词**：大语言模型评估, 双语教育基准, 真实考试数据, 思维链提示, 多语言性能下降, 自动化评估框架

## 3 点简述
- 核心问题：现有大语言模型评估缺乏反映真实学术严谨性和多语言复杂性的框架。
- 方法要点：基于UPSC、JEE和NEET真实考试问题，采用零样本、少样本和思维链提示策略进行自动化评估。
- 实验或效果：实验显示思维链提示提升推理准确性，模型间性能差异显著，印地语相比英语存在多语言性能下降。

## 摘要（原文）

> The rapid advancement of large language models (LLMs) necessitates evaluation frameworks that reflect real-world academic rigor and multilingual complexity. This paper introduces IndicEval, a scalable benchmarking platform designed to assess LLM performance using authentic high-stakes examination questions from UPSC, JEE, and NEET across STEM and humanities domains in both English and Hindi. Unlike synthetic benchmarks, IndicEval grounds evaluation in real examination standards, enabling realistic measurement of reasoning, domain knowledge, and bilingual adaptability. The framework automates assessment using Zero-Shot, Few-Shot, and Chain-of-Thought (CoT) prompting strategies and supports modular integration of new models and languages. Experiments conducted on Gemini 2.0 Flash, GPT-4, Claude, and LLaMA 3-70B reveal three major findings. First, CoT prompting consistently improves reasoning accuracy, with substantial gains across subjects and languages. Second, significant cross-model performance disparities persist, particularly in high-complexity examinations. Third, multilingual degradation remains a critical challenge, with marked accuracy drops in Hindi compared to English, especially under Zero-Shot conditions. These results highlight persistent gaps in bilingual reasoning and domain transfer. Overall, IndicEval provides a practice-oriented, extensible foundation for rigorous, equitable evaluation of LLMs in multilingual educational settings and offers actionable insights for improving reasoning robustness and language adaptability.

