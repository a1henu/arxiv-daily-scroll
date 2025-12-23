---
layout: default
title: Auto-Prompting with Retrieval Guidance for Frame Detection in Logistics
---

# Auto-Prompting with Retrieval Guidance for Frame Detection in Logistics
**arXiv**：[2512.19247v1](https://arxiv.org/abs/2512.19247) · [PDF](https://arxiv.org/pdf/2512.19247.pdf)  
**作者**：Do Minh Duc, Quan Xuan Truong, Nguyen Tat Dat, Nguyen Van Vinh  

**一句话要点**：提出基于检索引导的自动提示优化框架，以提升物流文本中框架检测的推理准确性。

**关键词**：物流文本分析, 提示工程优化, 检索增强生成, 思维链推理, 自动提示合成, 大语言模型应用

## 3 点简述
- 核心问题：物流文本中框架检测任务需高精度推理，传统提示工程效率低且效果不稳定。
- 方法要点：结合检索增强生成、少样本提示、思维链推理和自动思维链合成，通过LLM代理迭代优化提示。
- 实验或效果：在真实物流文本标注任务中，优化提示比基线提升推理准确率高达15%，并在多个LLM上验证通用性。

## 摘要（原文）

> Prompt engineering plays a critical role in adapting large language models (LLMs) to complex reasoning and labeling tasks without the need for extensive fine-tuning. In this paper, we propose a novel prompt optimization pipeline for frame detection in logistics texts, combining retrieval-augmented generation (RAG), few-shot prompting, chain-of-thought (CoT) reasoning, and automatic CoT synthesis (Auto-CoT) to generate highly effective task-specific prompts. Central to our approach is an LLM-based prompt optimizer agent that iteratively refines the prompts using retrieved examples, performance feedback, and internal self-evaluation. Our framework is evaluated on a real-world logistics text annotation task, where reasoning accuracy and labeling efficiency are critical. Experimental results show that the optimized prompts - particularly those enhanced via Auto-CoT and RAG - improve real-world inference accuracy by up to 15% compared to baseline zero-shot or static prompts. The system demonstrates consistent improvements across multiple LLMs, including GPT-4o, Qwen 2.5 (72B), and LLaMA 3.1 (70B), validating its generalizability and practical value. These findings suggest that structured prompt optimization is a viable alternative to full fine-tuning, offering scalable solutions for deploying LLMs in domain-specific NLP applications such as logistics.

