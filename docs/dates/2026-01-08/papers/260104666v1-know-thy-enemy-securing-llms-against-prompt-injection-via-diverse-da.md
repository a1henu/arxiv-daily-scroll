---
layout: default
title: Know Thy Enemy: Securing LLMs Against Prompt Injection via Diverse Data Synthesis and Instruction-Level Chain-of-Thought Learning
---

# Know Thy Enemy: Securing LLMs Against Prompt Injection via Diverse Data Synthesis and Instruction-Level Chain-of-Thought Learning
**arXiv**：[2601.04666v1](https://arxiv.org/abs/2601.04666) · [PDF](https://arxiv.org/pdf/2601.04666.pdf)  
**作者**：Zhiyuan Chang, Mingyang Li, Yuekai Huang, Ziyou Jiang, Xiaojun Jia, Qian Xiong, Junjie Wang, Zhaoyang Li, Qing Wang  

**一句话要点**：提出InstruCoT方法，通过多样化数据合成和指令级思维链微调，增强LLMs抵御提示注入攻击的能力。

**关键词**：提示注入防御, 数据合成, 指令级思维链, LLM安全, 模型微调

## 3 点简述
- 核心问题：提示注入攻击通过多样向量注入恶意指令，且与上下文语义边界模糊，难以检测。
- 方法要点：合成多样化训练数据，采用指令级思维链微调，使LLMs能识别和拒绝恶意指令。
- 实验或效果：在行为偏差、隐私泄露和有害输出三个维度上显著优于基线，且保持模型实用性。

## 摘要（原文）

> Large language model (LLM)-integrated applications have become increasingly prevalent, yet face critical security vulnerabilities from prompt injection (PI) attacks. Defending against PI attacks faces two major issues: malicious instructions can be injected through diverse vectors, and injected instructions often lack clear semantic boundaries from the surrounding context, making them difficult to identify. To address these issues, we propose InstruCoT, a model enhancement method for PI defense that synthesizes diverse training data and employs instruction-level chain-of-thought fine-tuning, enabling LLMs to effectively identify and reject malicious instructions regardless of their source or position in the context. We evaluate InstruCoT across three critical dimensions: Behavior Deviation, Privacy Leakage, and Harmful Output. Experimental results across four LLMs demonstrate that InstruCoT significantly outperforms baselines in all dimensions while maintaining utility performance without degradation

