---
layout: default
title: Why Does the LLM Stop Computing: An Empirical Study of User-Reported Failures in Open-Source LLMs
---

# Why Does the LLM Stop Computing: An Empirical Study of User-Reported Failures in Open-Source LLMs
**arXiv**：[2601.13655v1](https://arxiv.org/abs/2601.13655) · [PDF](https://arxiv.org/pdf/2601.13655.pdf)  
**作者**：Guangba Yu, Zirui Wang, Yujie Huang, Renyi Zhong, Yuedong Zhong, Yilun Wang, Michael R. Lyu  

**一句话要点**：实证研究开源LLM用户报告故障，揭示部署栈可靠性瓶颈

**关键词**：开源大语言模型, 部署可靠性, 故障分析, 实证研究, 生态系统脆弱性

## 3 点简述
- 核心问题：开源LLM用户管理部署的可靠性盲点，不同于黑盒API消费。
- 方法要点：分析705个真实故障，覆盖DeepSeek、Llama和Qwen生态系统。
- 实验或效果：识别诊断分歧、系统同质性和生命周期升级三大现象，提供可操作指导。

## 摘要（原文）

> The democratization of open-source Large Language Models (LLMs) allows users to fine-tune and deploy models on local infrastructure but exposes them to a First Mile deployment landscape. Unlike black-box API consumption, the reliability of user-managed orchestration remains a critical blind spot. To bridge this gap, we conduct the first large-scale empirical study of 705 real-world failures from the open-source DeepSeek, Llama, and Qwen ecosystems.
>   Our analysis reveals a paradigm shift: white-box orchestration relocates the reliability bottleneck from model algorithmic defects to the systemic fragility of the deployment stack. We identify three key phenomena: (1) Diagnostic Divergence: runtime crashes distinctively signal infrastructure friction, whereas incorrect functionality serves as a signature for internal tokenizer defects. (2) Systemic Homogeneity: Root causes converge across divergent series, confirming reliability barriers are inherent to the shared ecosystem rather than specific architectures. (3) Lifecycle Escalation: Barriers escalate from intrinsic configuration struggles during fine-tuning to compounded environmental incompatibilities during inference. Supported by our publicly available dataset, these insights provide actionable guidance for enhancing the reliability of the LLM landscape.

