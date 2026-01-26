---
layout: default
title: SycoEval-EM: Sycophancy Evaluation of Large Language Models in Simulated Clinical Encounters for Emergency Care
---

# SycoEval-EM: Sycophancy Evaluation of Large Language Models in Simulated Clinical Encounters for Emergency Care
**arXiv**：[2601.16529v1](https://arxiv.org/abs/2601.16529) · [PDF](https://arxiv.org/pdf/2601.16529.pdf)  
**作者**：Dongshen Peng, Yi Wang, Carl Preiksaitis, Christian Rose  

**一句话要点**：提出SycoEval-EM框架，通过多代理模拟评估大语言模型在急诊医学中的顺从性风险。

**关键词**：大语言模型评估, 临床决策支持, 急诊医学模拟, 顺从性风险, 多代理系统

## 3 点简述
- 核心问题：大语言模型在临床决策支持中可能顺从患者压力，导致不当护理。
- 方法要点：使用多代理模拟框架，通过对抗性患者说服测试模型鲁棒性。
- 实验或效果：在20个模型和1,875次模拟中，顺从率0-100%，模型能力与鲁棒性相关性差。

## 摘要（原文）

> Large language models (LLMs) show promise in clinical decision support yet risk acquiescing to patient pressure for inappropriate care. We introduce SycoEval-EM, a multi-agent simulation framework evaluating LLM robustness through adversarial patient persuasion in emergency medicine. Across 20 LLMs and 1,875 encounters spanning three Choosing Wisely scenarios, acquiescence rates ranged from 0-100\%. Models showed higher vulnerability to imaging requests (38.8\%) than opioid prescriptions (25.0\%), with model capability poorly predicting robustness. All persuasion tactics proved equally effective (30.0-36.0\%), indicating general susceptibility rather than tactic-specific weakness. Our findings demonstrate that static benchmarks inadequately predict safety under social pressure, necessitating multi-turn adversarial testing for clinical AI certification.

