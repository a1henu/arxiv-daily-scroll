---
layout: default
title: TrustMH-Bench: A Comprehensive Benchmark for Evaluating the Trustworthiness of Large Language Models in Mental Health
---

# TrustMH-Bench: A Comprehensive Benchmark for Evaluating the Trustworthiness of Large Language Models in Mental Health
**arXiv**：[2603.03047v1](https://arxiv.org/abs/2603.03047) · [PDF](https://arxiv.org/pdf/2603.03047.pdf)  
**作者**：Zixin Xiong, Ziteng Wang, Haotian Fan, Xinjie Zhang, Wenxuan Wang  

**一句话要点**：提出TrustMH-Bench基准，以系统评估心理健康领域大语言模型的可信度。

**关键词**：心理健康大语言模型, 可信度评估, 基准测试, 安全敏感领域, 量化指标

## 3 点简述
- 核心问题：现有评估范式未覆盖心理健康领域的高风险与安全敏感需求，模型可信度不足。
- 方法要点：建立领域规范到量化指标的映射，评估可靠性、危机识别等八个核心支柱。
- 实验或效果：测试12个模型，发现其在心理健康场景下可信度表现不佳，需系统性改进。

## 摘要（原文）

> While Large Language Models (LLMs) demonstrate significant potential in providing accessible mental health support, their practical deployment raises critical trustworthiness concerns due to the domains high-stakes and safety-sensitive nature. Existing evaluation paradigms for general-purpose LLMs fail to capture mental health-specific requirements, highlighting an urgent need to prioritize and enhance their trustworthiness. To address this, we propose TrustMH-Bench, a holistic framework designed to systematically quantify the trustworthiness of mental health LLMs. By establishing a deep mapping from domain-specific norms to quantitative evaluation metrics, TrustMH-Bench evaluates models across eight core pillars: Reliability, Crisis Identification and Escalation, Safety, Fairness, Privacy, Robustness, Anti-sycophancy, and Ethics. We conduct extensive experiments across six general-purpose LLMs and six specialized mental health models. Experimental results indicate that the evaluated models underperform across various trustworthiness dimensions in mental health scenarios, revealing significant deficiencies. Notably, even generally powerful models (e.g., GPT-5.1) fail to maintain consistently high performance across all dimensions. Consequently, systematically improving the trustworthiness of LLMs has become a critical task. Our data and code are released.

