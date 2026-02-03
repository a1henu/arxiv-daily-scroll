---
layout: default
title: SIDiffAgent: Self-Improving Diffusion Agent
---

# SIDiffAgent: Self-Improving Diffusion Agent
**arXiv**：[2602.02051v1](https://arxiv.org/abs/2602.02051) · [PDF](https://arxiv.org/pdf/2602.02051.pdf)  
**作者**：Shivank Garg, Ayush Singh, Gaurav Kumar Nayak  

**一句话要点**：提出SIDiffAgent训练免费代理框架，以解决扩散模型在提示工程、生成质量与可控性方面的实际部署限制。

**关键词**：扩散模型, 代理框架, 提示工程, 伪影移除, 自我改进, 训练免费

## 3 点简述
- 核心问题：扩散模型对提示措辞敏感、语义解释模糊、生成存在解剖失真等伪影，且需要精心设计的输入提示。
- 方法要点：利用Qwen系列模型自主管理提示工程、检测纠正不良生成、执行细粒度伪影移除，并基于经验数据库实现迭代自我改进。
- 实验或效果：在GenAIBench上平均VQA得分0.884，显著优于开源、专有模型及代理方法。

## 摘要（原文）

> Text-to-image diffusion models have revolutionized generative AI, enabling high-quality and photorealistic image synthesis. However, their practical deployment remains hindered by several limitations: sensitivity to prompt phrasing, ambiguity in semantic interpretation (e.g., ``mouse" as animal vs. a computer peripheral), artifacts such as distorted anatomy, and the need for carefully engineered input prompts. Existing methods often require additional training and offer limited controllability, restricting their adaptability in real-world applications. We introduce Self-Improving Diffusion Agent (SIDiffAgent), a training-free agentic framework that leverages the Qwen family of models (Qwen-VL, Qwen-Image, Qwen-Edit, Qwen-Embedding) to address these challenges. SIDiffAgent autonomously manages prompt engineering, detects and corrects poor generations, and performs fine-grained artifact removal, yielding more reliable and consistent outputs. It further incorporates iterative self-improvement by storing a memory of previous experiences in a database. This database of past experiences is then used to inject prompt-based guidance at each stage of the agentic pipeline. \modelour achieved an average VQA score of 0.884 on GenAIBench, significantly outperforming open-source, proprietary models and agentic methods. We will publicly release our code upon acceptance.

