---
layout: default
title: Multi-Turn Adaptive Prompting Attack on Large Vision-Language Models
---

# Multi-Turn Adaptive Prompting Attack on Large Vision-Language Models
**arXiv**：[2602.14399v1](https://arxiv.org/abs/2602.14399) · [PDF](https://arxiv.org/pdf/2602.14399.pdf)  
**作者**：In Chong Choi, Jiacheng Zhang, Feng Liu, Yiliao Song  

**一句话要点**：提出多轮自适应提示攻击MAPA，以提升对大型视觉语言模型的越狱攻击成功率。

**关键词**：多轮越狱攻击, 视觉语言模型安全, 自适应提示攻击, 恶意内容生成, 安全对齐防御

## 3 点简述
- 核心问题：现有多轮越狱攻击在视觉输入下易被安全对齐的LVLMs防御机制阻止。
- 方法要点：采用文本-视觉交替攻击动作和跨轮迭代优化轨迹，逐步放大恶意响应。
- 实验或效果：在多个基准模型上攻击成功率提升11-35%，优于现有方法。

## 摘要（原文）

> Multi-turn jailbreak attacks are effective against text-only large language models (LLMs) by gradually introducing malicious content across turns. When extended to large vision-language models (LVLMs), we find that naively adding visual inputs can cause existing multi-turn jailbreaks to be easily defended. For example, overly malicious visual input will easily trigger the defense mechanism of safety-aligned LVLMs, making the response more conservative. To address this, we propose MAPA: a multi-turn adaptive prompting attack that 1) at each turn, alternates text-vision attack actions to elicit the most malicious response; and 2) across turns, adjusts the attack trajectory through iterative back-and-forth refinement to gradually amplify response maliciousness. This two-level design enables MAPA to consistently outperform state-of-the-art methods, improving attack success rates by 11-35% on recent benchmarks against LLaVA-V1.6-Mistral-7B, Qwen2.5-VL-7B-Instruct, Llama-3.2-Vision-11B-Instruct and GPT-4o-mini.

