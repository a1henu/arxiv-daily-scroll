---
layout: default
title: Extracting books from production language models
---

# Extracting books from production language models
**arXiv**：[2601.02671v1](https://arxiv.org/abs/2601.02671) · [PDF](https://arxiv.org/pdf/2601.02671.pdf)  
**作者**：Ahmed Ahmed, A. Feder Cooper, Sanmi Koyejo, Percy Liang  

**一句话要点**：提出两阶段提取方法，评估生产级大语言模型对受版权训练数据的记忆与提取风险。

**关键词**：大语言模型, 数据提取, 记忆化, 版权风险, 越狱攻击, 生产级系统

## 3 点简述
- 核心问题：探究生产级大语言模型是否因安全措施而难以提取受版权训练数据。
- 方法要点：采用初始探测与迭代续写两阶段流程，包括最佳N次越狱技术。
- 实验或效果：在四个生产级模型上测试，提取成功率因模型而异，最高可达近原文复制。

## 摘要（原文）

> Many unresolved legal questions over LLMs and copyright center on memorization: whether specific training data have been encoded in the model's weights during training, and whether those memorized data can be extracted in the model's outputs. While many believe that LLMs do not memorize much of their training data, recent work shows that substantial amounts of copyrighted text can be extracted from open-weight models. However, it remains an open question if similar extraction is feasible for production LLMs, given the safety measures these systems implement. We investigate this question using a two-phase procedure: (1) an initial probe to test for extraction feasibility, which sometimes uses a Best-of-N (BoN) jailbreak, followed by (2) iterative continuation prompts to attempt to extract the book. We evaluate our procedure on four production LLMs -- Claude 3.7 Sonnet, GPT-4.1, Gemini 2.5 Pro, and Grok 3 -- and we measure extraction success with a score computed from a block-based approximation of longest common substring (nv-recall). With different per-LLM experimental configurations, we were able to extract varying amounts of text. For the Phase 1 probe, it was unnecessary to jailbreak Gemini 2.5 Pro and Grok 3 to extract text (e.g, nv-recall of 76.8% and 70.3%, respectively, for Harry Potter and the Sorcerer's Stone), while it was necessary for Claude 3.7 Sonnet and GPT-4.1. In some cases, jailbroken Claude 3.7 Sonnet outputs entire books near-verbatim (e.g., nv-recall=95.8%). GPT-4.1 requires significantly more BoN attempts (e.g., 20X), and eventually refuses to continue (e.g., nv-recall=4.0%). Taken together, our work highlights that, even with model- and system-level safeguards, extraction of (in-copyright) training data remains a risk for production LLMs.

