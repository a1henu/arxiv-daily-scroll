---
layout: default
title: Beyond Visual Safety: Jailbreaking Multimodal Large Language Models for Harmful Image Generation via Semantic-Agnostic Inputs
---

# Beyond Visual Safety: Jailbreaking Multimodal Large Language Models for Harmful Image Generation via Semantic-Agnostic Inputs
**arXiv**：[2601.15698v1](https://arxiv.org/abs/2601.15698) · [PDF](https://arxiv.org/pdf/2601.15698.pdf)  
**作者**：Mingyu Yu, Lana Liu, Zhehao Zhao, Wei Wang, Sujuan Qin  

**一句话要点**：提出Beyond Visual Safety框架，通过语义无关输入诱导多模态大语言模型生成有害图像，以探测其视觉安全边界。

**关键词**：多模态大语言模型, 视觉安全, 越狱攻击, 图像生成, 安全对齐, 语义无关输入

## 3 点简述
- 核心问题：多模态大语言模型在文本与视觉安全交叉领域存在未充分探索的漏洞，视觉安全边界研究不足。
- 方法要点：采用“重建-生成”策略，通过中性化视觉拼接和归纳重组，解耦恶意意图，诱导模型生成有害图像。
- 实验或效果：在GPT-5（2026年1月12日发布）上实现98.21%的越狱成功率，暴露当前模型视觉安全对齐的关键脆弱性。

## 摘要（原文）

> The rapid advancement of Multimodal Large Language Models (MLLMs) has introduced complex security challenges, particularly at the intersection of textual and visual safety. While existing schemes have explored the security vulnerabilities of MLLMs, the investigation into their visual safety boundaries remains insufficient. In this paper, we propose Beyond Visual Safety (BVS), a novel image-text pair jailbreaking framework specifically designed to probe the visual safety boundaries of MLLMs. BVS employs a "reconstruction-then-generation" strategy, leveraging neutralized visual splicing and inductive recomposition to decouple malicious intent from raw inputs, thereby leading MLLMs to be induced into generating harmful images. Experimental results demonstrate that BVS achieves a remarkable jailbreak success rate of 98.21\% against GPT-5 (12 January 2026 release). Our findings expose critical vulnerabilities in the visual safety alignment of current MLLMs.

