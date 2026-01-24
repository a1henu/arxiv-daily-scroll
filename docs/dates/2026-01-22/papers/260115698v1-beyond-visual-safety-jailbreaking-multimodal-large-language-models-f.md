---
layout: default
title: Beyond Visual Safety: Jailbreaking Multimodal Large Language Models for Harmful Image Generation via Semantic-Agnostic Inputs
---

# Beyond Visual Safety: Jailbreaking Multimodal Large Language Models for Harmful Image Generation via Semantic-Agnostic Inputs
**arXiv**：[2601.15698v1](https://arxiv.org/abs/2601.15698) · [PDF](https://arxiv.org/pdf/2601.15698.pdf)  
**作者**：Mingyu Yu, Lana Liu, Zhehao Zhao, Wei Wang, Sujuan Qin  

**一句话要点**：提出BVS框架以通过语义无关输入越狱多模态大语言模型生成有害图像

**关键词**：多模态大语言模型, 视觉安全, 越狱攻击, 图像生成, 安全对齐

## 3 点简述
- 核心问题：多模态大语言模型的视觉安全边界研究不足，存在安全隐患。
- 方法要点：采用重建-生成策略，通过视觉拼接和归纳重组解耦恶意意图。
- 实验或效果：在GPT-5上实现98.21%的越狱成功率，暴露模型视觉安全对齐漏洞。

## 摘要（原文）

> The rapid advancement of Multimodal Large Language Models (MLLMs) has introduced complex security challenges, particularly at the intersection of textual and visual safety. While existing schemes have explored the security vulnerabilities of MLLMs, the investigation into their visual safety boundaries remains insufficient. In this paper, we propose Beyond Visual Safety (BVS), a novel image-text pair jailbreaking framework specifically designed to probe the visual safety boundaries of MLLMs. BVS employs a "reconstruction-then-generation" strategy, leveraging neutralized visual splicing and inductive recomposition to decouple malicious intent from raw inputs, thereby leading MLLMs to be induced into generating harmful images. Experimental results demonstrate that BVS achieves a remarkable jailbreak success rate of 98.21\% against GPT-5 (12 January 2026 release). Our findings expose critical vulnerabilities in the visual safety alignment of current MLLMs.

