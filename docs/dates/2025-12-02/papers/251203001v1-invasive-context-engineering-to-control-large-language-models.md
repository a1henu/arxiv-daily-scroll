---
layout: default
title: Invasive Context Engineering to Control Large Language Models
---

# Invasive Context Engineering to Control Large Language Models
**arXiv**：[2512.03001v1](https://arxiv.org/abs/2512.03001) · [PDF](https://arxiv.org/pdf/2512.03001.pdf)  
**作者**：Thomas Rivasseau  

**一句话要点**：提出侵入式上下文工程以增强长上下文下大型语言模型的安全控制

**关键词**：侵入式上下文工程, 大型语言模型安全, 长上下文控制, 思维链安全, 模型鲁棒性

## 3 点简述
- 核心问题：长上下文下LLM易受滥用和越狱攻击，现有方法如偏好训练和过滤不足以保证安全。
- 方法要点：通过向LLM上下文插入控制语句作为侵入式工程，无需模型训练，可泛化至思维链过程防止策略性行为。
- 实验或效果：未知具体实验细节，但声称能部分解决长上下文安全保证问题，避免数据短缺陷阱。

## 摘要（原文）

> Current research on operator control of Large Language Models improves model robustness against adversarial attacks and misbehavior by training on preference examples, prompting, and input/output filtering. Despite good results, LLMs remain susceptible to abuse, and jailbreak probability increases with context length. There is a need for robust LLM security guarantees in long-context situations. We propose control sentences inserted into the LLM context as invasive context engineering to partially solve the problem. We suggest this technique can be generalized to the Chain-of-Thought process to prevent scheming. Invasive Context Engineering does not rely on LLM training, avoiding data shortage pitfalls which arise in training models for long context situations.

