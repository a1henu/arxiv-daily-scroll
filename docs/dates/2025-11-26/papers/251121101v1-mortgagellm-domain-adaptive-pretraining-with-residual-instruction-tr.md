---
layout: default
title: MortgageLLM: Domain-Adaptive Pretraining with Residual Instruction Transfer, Alignment Tuning, and Task-Specific Routing
---

# MortgageLLM: Domain-Adaptive Pretraining with Residual Instruction Transfer, Alignment Tuning, and Task-Specific Routing
**arXiv**：[2511.21101v1](https://arxiv.org/abs/2511.21101) · [PDF](https://arxiv.org/pdf/2511.21101.pdf)  
**作者**：Manish Jain, Satheesh Kumar Ponnambalam, Salman Faroz, Chandrakanth Lns, Vinay Sharma  

**一句话要点**：提出MortgageLLM以解决抵押金融领域大语言模型专业性与指令遵循的平衡问题

**关键词**：领域自适应预训练, 残差指令技术, 双专家架构, 任务路由机制, 抵押金融, 大语言模型

## 3 点简述
- 核心问题：大语言模型在抵押金融等专业领域应用时，需增强专业知识同时保持指令遵循能力
- 方法要点：采用双专家架构，结合残差指令技术，实现领域自适应预训练与任务路由
- 实验或效果：在领域基准测试中，模型在摘要、问答和分类任务上显著优于基线模型

## 摘要（原文）

> Large Language Models (LLMs) demonstrate exceptional capabilities across general domains, yet their application to specialized sectors such as mortgage finance requires domain-specific knowledge augmentation while preserving instruction-following fidelity. We present MortgageLLM, a novel domain-specific large language model that addresses this dual challenge. It is developed using a dual-track specialization framework from a single base model (LLaMA-3.1-8B). We opted for this dual-expert approach as a single multi-task model suffers from performance trade-offs, where optimizing for structured tasks (via SFT) degrades conversational fidelity (via DPO). Our dual-track method solves this by creating two specialists, allowing each to be optimally trained for its distinct capability. Our approach applies the instruction residual technique to restore instruction-following capabilities post-domain adaptation without supervised fine-tuning. We contribute: (1) application of this residual technique to the highly specialized mortgage finance domain; (2) a dual-expert architecture combining a conversational Q&A model and a structured task model for classification and summarization; and (3) an intelligent task routing mechanism using few-shot classification performed by one of the expert models itself. We validate our approach on domain-specific benchmarks, where our final model (MLM v2) significantly outperforms the base LLaMA-3.1-8B-Instruct, achieving an LLM-as-a-Judge summarization score of 4.58 (vs. 3.99), a Q&A score of 4.09 (vs. 4.0), and a classification score of 2.6 (vs. 1.2). On semantic similarity, our model achieved a BERTScore of 0.77 for summarization (vs. 0.74), 0.68 for Q&A (vs. 0.58), and 0.75 for classification (vs. 0.73), substantially outperforming baseline approaches.

