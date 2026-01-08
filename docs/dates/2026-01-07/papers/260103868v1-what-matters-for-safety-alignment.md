---
layout: default
title: What Matters For Safety Alignment?
---

# What Matters For Safety Alignment?
**arXiv**：[2601.03868v1](https://arxiv.org/abs/2601.03868) · [PDF](https://arxiv.org/pdf/2601.03868.pdf)  
**作者**：Xing Li, Hui-Ling Zhen, Lihao Yin, Xianzhi Yu, Zhenhua Dong, Mingxuan Yuan  

**一句话要点**：评估大模型安全对齐的关键因素，揭示推理机制与攻击漏洞

**关键词**：安全对齐, 大语言模型, 越狱攻击, 推理机制, 模型评估

## 3 点简述
- 核心问题：探究影响LLMs和LRMs安全对齐的内在模型特性和外部攻击技术
- 方法要点：系统评估32个模型在5个安全数据集上，使用56种越狱和4种CoT攻击策略
- 实验或效果：发现集成推理机制提升安全性，CoT攻击可显著提高攻击成功率

## 摘要（原文）

> This paper presents a comprehensive empirical study on the safety alignment capabilities. We evaluate what matters for safety alignment in LLMs and LRMs to provide essential insights for developing more secure and reliable AI systems. We systematically investigate and compare the influence of six critical intrinsic model characteristics and three external attack techniques. Our large-scale evaluation is conducted using 32 recent, popular LLMs and LRMs across thirteen distinct model families, spanning a parameter scale from 3B to 235B. The assessment leverages five established safety datasets and probes model vulnerabilities with 56 jailbreak techniques and four CoT attack strategies, resulting in 4.6M API calls. Our key empirical findings are fourfold. First, we identify the LRMs GPT-OSS-20B, Qwen3-Next-80B-A3B-Thinking, and GPT-OSS-120B as the top-three safest models, which substantiates the significant advantage of integrated reasoning and self-reflection mechanisms for robust safety alignment. Second, post-training and knowledge distillation may lead to a systematic degradation of safety alignment. We thus argue that safety must be treated as an explicit constraint or a core optimization objective during these stages, not merely subordinated to the pursuit of general capability. Third, we reveal a pronounced vulnerability: employing a CoT attack via a response prefix can elevate the attack success rate by 3.34x on average and from 0.6% to 96.3% for Seed-OSS-36B-Instruct. This critical finding underscores the safety risks inherent in text-completion interfaces and features that allow user-defined response prefixes in LLM services, highlighting an urgent need for architectural and deployment safeguards. Fourth, roleplay, prompt injection, and gradient-based search for adversarial prompts are the predominant methodologies for eliciting unaligned behaviors in modern models.

