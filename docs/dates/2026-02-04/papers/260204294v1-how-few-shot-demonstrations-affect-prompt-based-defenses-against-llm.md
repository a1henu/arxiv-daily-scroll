---
layout: default
title: How Few-shot Demonstrations Affect Prompt-based Defenses Against LLM Jailbreak Attacks
---

# How Few-shot Demonstrations Affect Prompt-based Defenses Against LLM Jailbreak Attacks
**arXiv**：[2602.04294v1](https://arxiv.org/abs/2602.04294) · [PDF](https://arxiv.org/pdf/2602.04294.pdf)  
**作者**：Yanshu Wang, Shuaishuai Yang, Jingjing He, Tong Yang  

**一句话要点**：揭示少样本演示对基于提示的LLM越狱攻击防御的相反影响

**关键词**：大语言模型安全, 越狱攻击防御, 提示工程, 少样本学习, 安全基准评估

## 3 点简述
- 核心问题：少样本演示在基于提示的LLM安全防御中的作用不明确，可能影响安全性。
- 方法要点：通过综合评估，分析少样本演示对角色导向提示和任务导向提示的交互效应。
- 实验或效果：少样本演示提升角色导向提示安全率4.5%，但降低任务导向提示效果21.2%。

## 摘要（原文）

> Large Language Models (LLMs) face increasing threats from jailbreak attacks that bypass safety alignment. While prompt-based defenses such as Role-Oriented Prompts (RoP) and Task-Oriented Prompts (ToP) have shown effectiveness, the role of few-shot demonstrations in these defense strategies remains unclear. Prior work suggests that few-shot examples may compromise safety, but lacks investigation into how few-shot interacts with different system prompt strategies. In this paper, we conduct a comprehensive evaluation on multiple mainstream LLMs across four safety benchmarks (AdvBench, HarmBench, SG-Bench, XSTest) using six jailbreak attack methods. Our key finding reveals that few-shot demonstrations produce opposite effects on RoP and ToP: few-shot enhances RoP's safety rate by up to 4.5% through reinforcing role identity, while it degrades ToP's effectiveness by up to 21.2% through distracting attention from task instructions. Based on these findings, we provide practical recommendations for deploying prompt-based defenses in real-world LLM applications.

