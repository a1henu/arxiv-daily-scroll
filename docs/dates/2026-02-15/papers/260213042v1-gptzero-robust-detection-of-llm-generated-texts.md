---
layout: default
title: GPTZero: Robust Detection of LLM-Generated Texts
---

# GPTZero: Robust Detection of LLM-Generated Texts
**arXiv**：[2602.13042v1](https://arxiv.org/abs/2602.13042) · [PDF](https://arxiv.org/pdf/2602.13042.pdf)  
**作者**：George Alexandru Adam, Alexander Cui, Edwin Thomas, Emily Napier, Nazar Shmatko, Jacob Schnell, Jacob Junqi Tian, Alekhya Dronavalli, Edward Tian, Dongwon Lee  

**一句话要点**：提出GPTZero以解决LLM生成文本的检测问题，提供可靠的人机文本区分方案。

**关键词**：AI文本检测, 多任务架构, 对抗鲁棒性, 可解释性, 红队测试

## 3 点简述
- 核心问题：LLM生成文本的兴起引发技能评估、低质内容与错误信息传播等担忧。
- 方法要点：采用分层多任务架构，支持灵活的人机文本分类，实现可解释检测。
- 实验或效果：在多个领域达到先进准确度，通过多层自动红队测试增强对抗攻击和改写的鲁棒性。

## 摘要（原文）

> While historical considerations surrounding text authenticity revolved primarily around plagiarism, the advent of large language models (LLMs) has introduced a new challenge: distinguishing human-authored from AI-generated text. This shift raises significant concerns, including the undermining of skill evaluations, the mass-production of low-quality content, and the proliferation of misinformation. Addressing these issues, we introduce GPTZero a state-of-the-art industrial AI detection solution, offering reliable discernment between human and LLM-generated text. Our key contributions include: introducing a hierarchical, multi-task architecture enabling a flexible taxonomy of human and AI texts, demonstrating state-of-the-art accuracy on a variety of domains with granular predictions, and achieving superior robustness to adversarial attacks and paraphrasing via multi-tiered automated red teaming. GPTZero offers accurate and explainable detection, and educates users on its responsible use, ensuring fair and transparent assessment of text.

