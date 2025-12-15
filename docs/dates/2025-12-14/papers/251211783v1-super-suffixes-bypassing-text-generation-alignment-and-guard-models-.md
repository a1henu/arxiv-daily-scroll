---
layout: default
title: Super Suffixes: Bypassing Text Generation Alignment and Guard Models Simultaneously
---

# Super Suffixes: Bypassing Text Generation Alignment and Guard Models Simultaneously
**arXiv**：[2512.11783v1](https://arxiv.org/abs/2512.11783) · [PDF](https://arxiv.org/pdf/2512.11783.pdf)  
**作者**：Andrew Adiletta, Kathryn Adiletta, Kemal Derya, Berk Sunar  

**一句话要点**：提出Super Suffixes以绕过文本生成对齐和防护模型，并设计DeltaGuard进行检测

**关键词**：对抗性攻击, 文本生成安全, 防护模型, 联合优化, 恶意检测

## 3 点简述
- 核心问题：大型语言模型面临对抗性输入威胁，防护模型如Llama Prompt Guard 2可能被绕过
- 方法要点：引入Super Suffixes后缀，通过联合优化技术同时绕过多种对齐目标和防护机制
- 实验或效果：在五个文本生成模型上成功绕过Llama Prompt Guard 2，DeltaGuard检测率提升至近100%

## 摘要（原文）

> The rapid deployment of Large Language Models (LLMs) has created an urgent need for enhanced security and privacy measures in Machine Learning (ML). LLMs are increasingly being used to process untrusted text inputs and even generate executable code, often while having access to sensitive system controls. To address these security concerns, several companies have introduced guard models, which are smaller, specialized models designed to protect text generation models from adversarial or malicious inputs. In this work, we advance the study of adversarial inputs by introducing Super Suffixes, suffixes capable of overriding multiple alignment objectives across various models with different tokenization schemes. We demonstrate their effectiveness, along with our joint optimization technique, by successfully bypassing the protection mechanisms of Llama Prompt Guard 2 on five different text generation models for malicious text and code generation. To the best of our knowledge, this is the first work to reveal that Llama Prompt Guard 2 can be compromised through joint optimization.
>   Additionally, by analyzing the changing similarity of a model's internal state to specific concept directions during token sequence processing, we propose an effective and lightweight method to detect Super Suffix attacks. We show that the cosine similarity between the residual stream and certain concept directions serves as a distinctive fingerprint of model intent. Our proposed countermeasure, DeltaGuard, significantly improves the detection of malicious prompts generated through Super Suffixes. It increases the non-benign classification rate to nearly 100%, making DeltaGuard a valuable addition to the guard model stack and enhancing robustness against adversarial prompt attacks.

