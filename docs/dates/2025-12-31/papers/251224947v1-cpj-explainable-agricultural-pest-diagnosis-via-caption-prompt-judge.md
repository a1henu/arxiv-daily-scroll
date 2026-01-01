---
layout: default
title: CPJ: Explainable Agricultural Pest Diagnosis via Caption-Prompt-Judge with LLM-Judged Refinement
---

# CPJ: Explainable Agricultural Pest Diagnosis via Caption-Prompt-Judge with LLM-Judged Refinement
**arXiv**：[2512.24947v1](https://arxiv.org/abs/2512.24947) · [PDF](https://arxiv.org/pdf/2512.24947.pdf)  
**作者**：Wentao Zhang, Tao Fang, Lina Lu, Lifei Wang, Weihe Zhong  

**一句话要点**：提出CPJ框架，通过无训练少样本方法增强农业病虫害VQA的可解释性和鲁棒性。

**关键词**：农业病虫害诊断, 视觉问答, 可解释人工智能, 少样本学习, 大语言模型

## 3 点简述
- 核心问题：现有农业病虫害诊断方法依赖监督微调，成本高且领域迁移性能差。
- 方法要点：使用视觉语言模型生成多角度图像描述，经LLM迭代优化后指导双答案VQA过程。
- 实验或效果：在CDDMBench上，CPJ显著提升疾病分类和问答分数，提供透明推理。

## 摘要（原文）

> Accurate and interpretable crop disease diagnosis is essential for agricultural decision-making, yet existing methods often rely on costly supervised fine-tuning and perform poorly under domain shifts. We propose Caption--Prompt--Judge (CPJ), a training-free few-shot framework that enhances Agri-Pest VQA through structured, interpretable image captions. CPJ employs large vision-language models to generate multi-angle captions, refined iteratively via an LLM-as-Judge module, which then inform a dual-answer VQA process for both recognition and management responses. Evaluated on CDDMBench, CPJ significantly improves performance: using GPT-5-mini captions, GPT-5-Nano achieves \textbf{+22.7} pp in disease classification and \textbf{+19.5} points in QA score over no-caption baselines. The framework provides transparent, evidence-based reasoning, advancing robust and explainable agricultural diagnosis without fine-tuning. Our code and data are publicly available at: https://github.com/CPJ-Agricultural/CPJ-Agricultural-Diagnosis.

