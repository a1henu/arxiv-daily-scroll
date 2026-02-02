---
layout: default
title: Safer Policy Compliance with Dynamic Epistemic Fallback
---

# Safer Policy Compliance with Dynamic Epistemic Fallback
**arXiv**：[2601.23094v1](https://arxiv.org/abs/2601.23094) · [PDF](https://arxiv.org/pdf/2601.23094.pdf)  
**作者**：Joseph Marvin Imperial, Harish Tayyar Madabushi  

**一句话要点**：提出动态认知回退协议以增强大语言模型在恶意扰动政策文本下的合规安全性

**关键词**：大语言模型安全, 认知防御机制, 政策合规自动化, 动态安全协议, 恶意文本扰动

## 3 点简述
- 核心问题：大语言模型在自动化数据隐私法律合规等高风险任务中易受恶意扰动政策文本的欺骗攻击
- 方法要点：通过动态安全协议，利用单句文本提示引导模型标记不一致、拒绝合规并回退到参数知识
- 实验或效果：基于HIPAA和GDPR政策评估，协议有效提升前沿模型检测和拒绝扰动政策的能力，DeepSeek-R1在特定设置下达到100%检测率

## 摘要（原文）

> Humans develop a series of cognitive defenses, known as epistemic vigilance, to combat risks of deception and misinformation from everyday interactions. Developing safeguards for LLMs inspired by this mechanism might be particularly helpful for their application in high-stakes tasks such as automating compliance with data privacy laws. In this paper, we introduce Dynamic Epistemic Fallback (DEF), a dynamic safety protocol for improving an LLM's inference-time defenses against deceptive attacks that make use of maliciously perturbed policy texts. Through various levels of one-sentence textual cues, DEF nudges LLMs to flag inconsistencies, refuse compliance, and fallback to their parametric knowledge upon encountering perturbed policy texts. Using globally recognized legal policies such as HIPAA and GDPR, our empirical evaluations report that DEF effectively improves the capability of frontier LLMs to detect and refuse perturbed versions of policies, with DeepSeek-R1 achieving a 100% detection rate in one setting. This work encourages further efforts to develop cognitively inspired defenses to improve LLM robustness against forms of harm and deception that exploit legal artifacts.

