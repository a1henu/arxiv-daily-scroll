---
layout: default
title: Detection of Illicit Content on Online Marketplaces using Large Language Models
---

# Detection of Illicit Content on Online Marketplaces using Large Language Models
**arXiv**：[2603.04707v1](https://arxiv.org/abs/2603.04707) · [PDF](https://arxiv.org/pdf/2603.04707.pdf)  
**作者**：Quoc Khoa Tran, Thanh Thi Nguyen, Campbell Wilson  

**一句话要点**：提出使用大语言模型检测在线市场非法内容，以解决传统方法在语义复杂性和多语言处理上的不足。

**关键词**：大语言模型, 非法内容检测, 在线市场, 多语言分类, 微调技术

## 3 点简述
- 核心问题：在线市场非法内容检测面临可扩展性、动态混淆和多语言挑战，传统方法效果有限。
- 方法要点：采用Llama 3.2和Gemma 3大语言模型，结合PEFT和量化微调，对比BERT和传统机器学习基线。
- 实验或效果：Llama 3.2在复杂多类分类中显著优于基线，为非法内容检测提供更有效工具。

## 摘要（原文）

> Online marketplaces, while revolutionizing global commerce, have inadvertently facilitated the proliferation of illicit activities, including drug trafficking, counterfeit sales, and cybercrimes. Traditional content moderation methods such as manual reviews and rule-based automated systems struggle with scalability, dynamic obfuscation techniques, and multilingual content. Conventional machine learning models, though effective in simpler contexts, often falter when confronting the semantic complexities and linguistic nuances characteristic of illicit marketplace communications. This research investigates the efficacy of Large Language Models (LLMs), specifically Meta's Llama 3.2 and Google's Gemma 3, in detecting and classifying illicit online marketplace content using the multilingual DUTA10K dataset. Employing fine-tuning techniques such as Parameter-Efficient Fine-Tuning (PEFT) and quantization, these models were systematically benchmarked against a foundational transformer-based model (BERT) and traditional machine learning baselines (Support Vector Machines and Naive Bayes). Experimental results reveal a task-dependent advantage for LLMs. In binary classification (illicit vs. non-illicit), Llama 3.2 demonstrated performance comparable to traditional methods. However, for complex, imbalanced multi-class classification involving 40 specific illicit categories, Llama 3.2 significantly surpassed all baseline models. These findings offer substantial practical implications for enhancing online safety, equipping law enforcement agencies, e-commerce platforms, and cybersecurity specialists with more effective, scalable, and adaptive tools for illicit content detection and moderation.

