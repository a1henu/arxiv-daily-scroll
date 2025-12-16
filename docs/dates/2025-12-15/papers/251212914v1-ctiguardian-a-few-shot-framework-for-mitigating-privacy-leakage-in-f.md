---
layout: default
title: CTIGuardian: A Few-Shot Framework for Mitigating Privacy Leakage in Fine-Tuned LLMs
---

# CTIGuardian: A Few-Shot Framework for Mitigating Privacy Leakage in Fine-Tuned LLMs
**arXiv**：[2512.12914v1](https://arxiv.org/abs/2512.12914) · [PDF](https://arxiv.org/pdf/2512.12914.pdf)  
**作者**：Shashie Dilhara Batan Arachchige, Benjamin Zi Hao Zhao, Hassan Jameel Asghar, Dinusha Vatsalan, Dali Kaafar  

**一句话要点**：提出CTIGuardian框架，通过少样本隐私对齐缓解微调LLMs中的隐私泄露问题

**关键词**：隐私保护, 大语言模型微调, 少样本学习, 数据提取攻击, 隐私对齐, 网络安全威胁情报

## 3 点简述
- 微调LLMs时，专有数据集中的敏感信息易受数据提取攻击，需高效缓解方法
- 采用少样本监督实现隐私对齐，集成隐私分类器和重写器，基于同一LLM处理
- 在CTI用例中评估，相比NER基线，CTIGuardian提供更好的隐私-效用权衡

## 摘要（原文）

> Large Language Models (LLMs) are often fine-tuned to adapt their general-purpose knowledge to specific tasks and domains such as cyber threat intelligence (CTI). Fine-tuning is mostly done through proprietary datasets that may contain sensitive information. Owners expect their fine-tuned model to not inadvertently leak this information to potentially adversarial end users. Using CTI as a use case, we demonstrate that data-extraction attacks can recover sensitive information from fine-tuned models on CTI reports, underscoring the need for mitigation. Retraining the full model to eliminate this leakage is computationally expensive and impractical. We propose an alternative approach, which we call privacy alignment, inspired by safety alignment in LLMs. Just like safety alignment teaches the model to abide by safety constraints through a few examples, we enforce privacy alignment through few-shot supervision, integrating a privacy classifier and a privacy redactor, both handled by the same underlying LLM. We evaluate our system, called CTIGuardian, using GPT-4o mini and Mistral-7B Instruct models, benchmarking against Presidio, a named entity recognition (NER) baseline. Results show that CTIGuardian provides a better privacy-utility trade-off than NER based models. While we demonstrate its effectiveness on a CTI use case, the framework is generic enough to be applicable to other sensitive domains.

