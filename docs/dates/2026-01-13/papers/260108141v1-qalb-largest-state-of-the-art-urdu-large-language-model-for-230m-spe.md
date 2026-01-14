---
layout: default
title: Qalb: Largest State-of-the-Art Urdu Large Language Model for 230M Speakers with Systematic Continued Pre-training
---

# Qalb: Largest State-of-the-Art Urdu Large Language Model for 230M Speakers with Systematic Continued Pre-training
**arXiv**：[2601.08141v1](https://arxiv.org/abs/2601.08141) · [PDF](https://arxiv.org/pdf/2601.08141.pdf)  
**作者**：Muhammad Taimoor Hassan, Jawad Ahmed, Muhammad Awais  

**一句话要点**：提出Qalb模型，通过持续预训练和指令微调解决乌尔都语大语言模型性能不足问题。

**关键词**：乌尔都语大语言模型, 持续预训练, 指令微调, 低资源语言适应, NLP基准测试, 多任务评估

## 3 点简述
- 乌尔都语在NLP中代表性不足，现有模型处理其复杂形态和脚本时表现不佳。
- 基于LLaMA 3.1 8B，采用两阶段方法：在19.7亿令牌数据集上持续预训练，再在Alif Urdu-instruct数据集上微调。
- 在乌尔都语基准测试中，Qalb加权平均得分90.34，超越先前最佳模型3.24分，并在七项任务中达到最优性能。

## 摘要（原文）

> Despite remarkable progress in large language models, Urdu-a language spoken by over 230 million people-remains critically underrepresented in modern NLP systems. Existing multilingual models demonstrate poor performance on Urdu-specific tasks, struggling with the language's complex morphology, right-to-left Nastaliq script, and rich literary traditions. Even the base LLaMA-3.1 8B-Instruct model shows limited capability in generating fluent, contextually appropriate Urdu text. We introduce Qalb, an Urdu language model developed through a two-stage approach: continued pre-training followed by supervised fine-tuning. Starting from LLaMA 3.1 8B, we perform continued pre-training on a dataset of 1.97 billion tokens. This corpus comprises 1.84 billion tokens of diverse Urdu text-spanning news archives, classical and contemporary literature, government documents, and social media-combined with 140 million tokens of English Wikipedia data to prevent catastrophic forgetting. We then fine-tune the resulting model on the Alif Urdu-instruct dataset. Through extensive evaluation on Urdu-specific benchmarks, Qalb demonstrates substantial improvements, achieving a weighted average score of 90.34 and outperforming the previous state-of-the-art Alif-1.0-Instruct model (87.1) by 3.24 points, while also surpassing the base LLaMA-3.1 8B-Instruct model by 44.64 points. Qalb achieves state-of-the-art performance with comprehensive evaluation across seven diverse tasks including Classification, Sentiment Analysis, and Reasoning. Our results demonstrate that continued pre-training on diverse, high-quality language data, combined with targeted instruction fine-tuning, effectively adapts foundation models to low-resource languages.

