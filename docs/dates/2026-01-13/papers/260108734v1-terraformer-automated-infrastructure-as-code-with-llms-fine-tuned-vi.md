---
layout: default
title: TerraFormer: Automated Infrastructure-as-Code with LLMs Fine-Tuned via Policy-Guided Verifier Feedback
---

# TerraFormer: Automated Infrastructure-as-Code with LLMs Fine-Tuned via Policy-Guided Verifier Feedback
**arXiv**：[2601.08734v1](https://arxiv.org/abs/2601.08734) · [PDF](https://arxiv.org/pdf/2601.08734.pdf)  
**作者**：Prithwish Jana, Sam Davidson, Bhavana Bhasker, Andrey Kan, Anoop Deoras, Laurent Callot  

**一句话要点**：提出TerraFormer框架，结合监督微调与验证器引导强化学习，以自动化基础设施即代码生成与变更。

**关键词**：基础设施即代码, 大语言模型微调, 验证器引导强化学习, 神经符号框架, 策略合规性

## 3 点简述
- 核心问题：大语言模型在自然语言到基础设施即代码转换中常产生错误配置。
- 方法要点：通过形式验证工具提供语法、可部署性和策略合规性反馈，进行神经符号框架设计。
- 实验或效果：在多个数据集上优于包括更大模型在内的17个先进模型，提升正确性达19.60%。

## 摘要（原文）

> Automating Infrastructure-as-Code (IaC) is challenging, and large language models (LLMs) often produce incorrect configurations from natural language (NL). We present TerraFormer, a neuro-symbolic framework for IaC generation and mutation that combines supervised fine-tuning with verifier-guided reinforcement learning, using formal verification tools to provide feedback on syntax, deployability, and policy compliance. We curate two large, high-quality NL-to-IaC datasets, TF-Gen (152k instances) and TF-Mutn (52k instances), via multi-stage verification and iterative LLM self-correction. Evaluations against 17 state-of-the-art LLMs, including ~50x larger models like Sonnet 3.7, DeepSeek-R1, and GPT-4.1, show that TerraFormer improves correctness over its base LLM by 15.94% on IaC-Eval, 11.65% on TF-Gen (Test), and 19.60% on TF-Mutn (Test). It outperforms larger models on both TF-Gen (Test) and TF-Mutn (Test), ranks third on IaC-Eval, and achieves top best-practices and security compliance.

