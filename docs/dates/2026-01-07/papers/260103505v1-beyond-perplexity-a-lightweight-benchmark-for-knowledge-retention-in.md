---
layout: default
title: Beyond Perplexity: A Lightweight Benchmark for Knowledge Retention in Supervised Fine-Tuning
---

# Beyond Perplexity: A Lightweight Benchmark for Knowledge Retention in Supervised Fine-Tuning
**arXiv**：[2601.03505v1](https://arxiv.org/abs/2601.03505) · [PDF](https://arxiv.org/pdf/2601.03505.pdf)  
**作者**：Soheil Zibakhsh Shabgahi, Pedram Aghazadeh, Farinaz Koushanfar  

**一句话要点**：提出知识保留测试以解决监督微调中验证困惑度混淆风格模仿与事实内化的问题

**关键词**：监督微调, 知识保留, 评估框架, 对比示例, 低秩适应, 训练动态

## 3 点简述
- 核心问题：监督微调中验证困惑度无法区分风格模仿与事实内化，导致评估不准确
- 方法要点：引入知识保留测试，基于自动生成对比示例测量正确与错误续写的似然偏好，无需指令调优或生成解码
- 实验或效果：通过盲测与先知基线分析验证框架完整性，并分析低秩适应的训练动态以增强微调可解释性

## 摘要（原文）

> Supervised Fine-Tuning (SFT) is a standard approach for injecting domain knowledge into Large Language Models (LLMs). However, relying on validation perplexity to monitor training is often insufficient, as it confounds stylistic mimicry with genuine factual internalization. To address this, we introduce the Knowledge Retention (KR) Test , a lightweight, corpus-grounded evaluation framework designed to distinguish factual learning from linguistics. KR-Test utilizes automatically generated contrastive examples to measure likelihood preferences for correct versus incorrect continuations, requiring no instruction tuning or generative decoding. We validate the framework's integrity through a "blind vs. oracle" baseline analysis. Furthermore, we demonstrate the diagnostic capabilities of KR-Test by analyzing the training dynamics of Low-Rank Adaptation (LoRA). By exposing the fine-grained dissociation between linguistic convergence and knowledge retention, KR-Test enhances the interpretability of fine-tuning dynamics.

