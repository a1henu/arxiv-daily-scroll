---
layout: default
title: DNF: Dual-Layer Nested Fingerprinting for Large Language Model Intellectual Property Protection
---

# DNF: Dual-Layer Nested Fingerprinting for Large Language Model Intellectual Property Protection
**arXiv**：[2601.08223v1](https://arxiv.org/abs/2601.08223) · [PDF](https://arxiv.org/pdf/2601.08223.pdf)  
**作者**：Zhenhua Xu, Yiran Zhao, Mengting Zhong, Dezhang Kong, Changting Lin, Tong Qiao, Meng Han  

**一句话要点**：提出双层级嵌套指纹方法以解决黑盒部署下大语言模型知识产权保护问题

**关键词**：大语言模型, 知识产权保护, 黑盒指纹, 后门嵌入, 模型验证

## 3 点简述
- 核心问题：黑盒部署下大语言模型知识产权保护困难，现有指纹方法易被过滤或泄露
- 方法要点：通过耦合领域特定风格线索与隐式语义触发器，嵌入分层后门实现指纹
- 实验或效果：在多个模型上实现完美指纹激活，保持下游效用，且对检测攻击和微调相对鲁棒

## 摘要（原文）

> The rapid growth of large language models raises pressing concerns about intellectual property protection under black-box deployment. Existing backdoor-based fingerprints either rely on rare tokens -- leading to high-perplexity inputs susceptible to filtering -- or use fixed trigger-response mappings that are brittle to leakage and post-hoc adaptation. We propose \textsc{Dual-Layer Nested Fingerprinting} (DNF), a black-box method that embeds a hierarchical backdoor by coupling domain-specific stylistic cues with implicit semantic triggers. Across Mistral-7B, LLaMA-3-8B-Instruct, and Falcon3-7B-Instruct, DNF achieves perfect fingerprint activation while preserving downstream utility. Compared with existing methods, it uses lower-perplexity triggers, remains undetectable under fingerprint detection attacks, and is relatively robust to incremental fine-tuning and model merging. These results position DNF as a practical, stealthy, and resilient solution for LLM ownership verification and intellectual property protection.

