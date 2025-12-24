---
layout: default
title: AI Security Beyond Core Domains: Resume Screening as a Case Study of Adversarial Vulnerabilities in Specialized LLM Applications
---

# AI Security Beyond Core Domains: Resume Screening as a Case Study of Adversarial Vulnerabilities in Specialized LLM Applications
**arXiv**：[2512.20164v1](https://arxiv.org/abs/2512.20164) · [PDF](https://arxiv.org/pdf/2512.20164.pdf)  
**作者**：Honglin Mu, Jinghao Liu, Kaiyang Wan, Rui Xing, Xiuying Chen, Timothy Baldwin, Wanxiang Che  

**一句话要点**：提出FIDS防御机制，针对简历筛选中的LLM对抗指令漏洞，提升安全性

**关键词**：对抗攻击, 简历筛选, 大语言模型安全, 防御机制, LoRA适应

## 3 点简述
- 核心问题：LLM在简历筛选中易受隐藏对抗指令攻击，攻击成功率超80%
- 方法要点：结合提示防御与FIDS（基于LoRA的外来指令检测），训练时防御优于推理时
- 实验或效果：联合防御降低26.3%攻击率，FIDS减少15.4%攻击且误拒率增10.4%

## 摘要（原文）

> Large Language Models (LLMs) excel at text comprehension and generation, making them ideal for automated tasks like code review and content moderation. However, our research identifies a vulnerability: LLMs can be manipulated by "adversarial instructions" hidden in input data, such as resumes or code, causing them to deviate from their intended task. Notably, while defenses may exist for mature domains such as code review, they are often absent in other common applications such as resume screening and peer review. This paper introduces a benchmark to assess this vulnerability in resume screening, revealing attack success rates exceeding 80% for certain attack types. We evaluate two defense mechanisms: prompt-based defenses achieve 10.1% attack reduction with 12.5% false rejection increase, while our proposed FIDS (Foreign Instruction Detection through Separation) using LoRA adaptation achieves 15.4% attack reduction with 10.4% false rejection increase. The combined approach provides 26.3% attack reduction, demonstrating that training-time defenses outperform inference-time mitigations in both security and utility preservation.

