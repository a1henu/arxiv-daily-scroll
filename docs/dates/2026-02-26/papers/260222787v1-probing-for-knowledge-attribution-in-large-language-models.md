---
layout: default
title: Probing for Knowledge Attribution in Large Language Models
---

# Probing for Knowledge Attribution in Large Language Models
**arXiv**：[2602.22787v1](https://arxiv.org/abs/2602.22787) · [PDF](https://arxiv.org/pdf/2602.22787.pdf)  
**作者**：Ivo Brink, Alexander Boer, Dennis Ulmer  

**一句话要点**：提出基于探针的知识归因方法，以区分大语言模型输出中的知识来源

**关键词**：知识归因, 大语言模型, 幻觉检测, 自监督学习, 探针方法, 模型可解释性

## 3 点简述
- 核心问题：大语言模型输出幻觉源于知识来源混淆，需区分基于提示或内部知识
- 方法要点：利用自监督数据管道AttriWiki训练线性分类器探针，预测输出主导知识源
- 实验或效果：探针在多个模型上达0.96 Macro-F1，可迁移至外域基准，归因错误关联高错误率

## 摘要（原文）

> Large language models (LLMs) often generate fluent but unfounded claims, or hallucinations, which fall into two types: (i) faithfulness violations - misusing user context - and (ii) factuality violations - errors from internal knowledge. Proper mitigation depends on knowing whether a model's answer is based on the prompt or its internal weights. This work focuses on the problem of contributive attribution: identifying the dominant knowledge source behind each output. We show that a probe, a simple linear classifier trained on model hidden representations, can reliably predict contributive attribution. For its training, we introduce AttriWiki, a self-supervised data pipeline that prompts models to recall withheld entities from memory or read them from context, generating labelled examples automatically. Probes trained on AttriWiki data reveal a strong attribution signal, achieving up to 0.96 Macro-F1 on Llama-3.1-8B, Mistral-7B, and Qwen-7B, transferring to out-of-domain benchmarks (SQuAD, WebQuestions) with 0.94-0.99 Macro-F1 without retraining. Attribution mismatches raise error rates by up to 70%, demonstrating a direct link between knowledge source confusion and unfaithful answers. Yet, models may still respond incorrectly even when attribution is correct, highlighting the need for broader detection frameworks.

