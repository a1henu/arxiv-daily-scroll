---
layout: default
title: Iterative Prompt Refinement for Dyslexia-Friendly Text Summarization Using GPT-4o
---

# Iterative Prompt Refinement for Dyslexia-Friendly Text Summarization Using GPT-4o
**arXiv**：[2602.22524v1](https://arxiv.org/abs/2602.22524) · [PDF](https://arxiv.org/pdf/2602.22524.pdf)  
**作者**：Samay Bhojwani, Swarnima Kain, Lisong Xu  

**一句话要点**：提出基于GPT-4o的迭代提示优化方法，用于生成适合阅读障碍者的文本摘要。

**关键词**：阅读障碍辅助, 文本摘要, GPT-4o, 迭代提示优化, 可读性评估

## 3 点简述
- 核心问题：阅读障碍影响全球约10%人口，现有辅助技术未充分解决语言复杂性障碍。
- 方法要点：构建迭代提示优化流程，以GPT-4o为基础，针对可读性目标进行自动调整。
- 实验或效果：在约2000个新闻样本上测试，多数摘要能在四次尝试内达到可读性阈值，综合得分稳定在0.55左右。

## 摘要（原文）

> Dyslexia affects approximately 10% of the global population and presents persistent challenges in reading fluency and text comprehension. While existing assistive technologies address visual presentation, linguistic complexity remains a substantial barrier to equitable access. This paper presents an empirical study on dyslexia-friendly text summarization using an iterative prompt-based refinement pipeline built on GPT-4o. We evaluate the pipeline on approximately 2,000 news article samples, applying a readability target of Flesch Reading Ease >= 90. Results show that the majority of summaries meet the readability threshold within four attempts, with many succeeding on the first try. A composite score combining readability and semantic fidelity shows stable performance across the dataset, ranging from 0.13 to 0.73 with a typical value near 0.55. These findings establish an empirical baseline for accessibility-driven NLP summarization and motivate further human-centered evaluation with dyslexic readers.

