---
layout: default
title: ER-MIA: Black-Box Adversarial Memory Injection Attacks on Long-Term Memory-Augmented Large Language Models
---

# ER-MIA: Black-Box Adversarial Memory Injection Attacks on Long-Term Memory-Augmented Large Language Models
**arXiv**：[2602.15344v1](https://arxiv.org/abs/2602.15344) · [PDF](https://arxiv.org/pdf/2602.15344.pdf)  
**作者**：Mitchell Piehl, Zhaohan Xi, Zuobin Xiong, Pan He, Muchao Ye  

**一句话要点**：提出ER-MIA框架，针对长时记忆增强大语言模型的黑盒对抗性记忆注入攻击。

**关键词**：长时记忆增强, 黑盒攻击, 对抗性记忆注入, 相似性检索, 大语言模型安全, 系统漏洞

## 3 点简述
- 核心问题：长时记忆增强LLMs的基于相似性检索机制存在安全漏洞，提供额外攻击面。
- 方法要点：ER-MIA框架形式化内容型和问题目标型攻击，包含可组合攻击原语和集成攻击。
- 实验或效果：在多种LLMs和记忆系统中验证攻击高成功率，揭示跨设计和场景的系统级风险。

## 摘要（原文）

> Large language models (LLMs) are increasingly augmented with long-term memory systems to overcome finite context windows and enable persistent reasoning across interactions. However, recent research finds that LLMs become more vulnerable because memory provides extra attack surfaces. In this paper, we present the first systematic study of black-box adversarial memory injection attacks that target the similarity-based retrieval mechanism in long-term memory-augmented LLMs. We introduce ER-MIA, a unified framework that exposes this vulnerability and formalizes two realistic attack settings: content-based attacks and question-targeted attacks. In these settings, ER-MIA includes an arsenal of composable attack primitives and ensemble attacks that achieve high success rates under minimal attacker assumptions. Extensive experiments across multiple LLMs and long-term memory systems demonstrate that similarity-based retrieval constitutes a fundamental and system-level vulnerability, revealing security risks that persist across memory designs and application scenarios.

