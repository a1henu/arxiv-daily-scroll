---
layout: default
title: Stop Tracking Me! Proactive Defense Against Attribute Inference Attack in LLMs
---

# Stop Tracking Me! Proactive Defense Against Attribute Inference Attack in LLMs
**arXiv**：[2602.11528v1](https://arxiv.org/abs/2602.11528) · [PDF](https://arxiv.org/pdf/2602.11528.pdf)  
**作者**：Dong Yan, Jian Liang, Ran He, Tieniu Tan  

**一句话要点**：提出TRACE-RPS框架以防御大语言模型中的属性推断攻击

**关键词**：属性推断攻击, 隐私保护, 大语言模型, 细粒度匿名化, 推理阻止优化

## 3 点简述
- 核心问题：现有匿名化防御粗粒度，无法阻止模型推理导致的隐私泄露
- 方法要点：结合细粒度匿名化TRACE与推理阻止优化RPS，诱导模型拒绝行为
- 实验或效果：在开源模型上，将属性推断准确率从约50%降至5%以下

## 摘要（原文）

> Recent studies have shown that large language models (LLMs) can infer private user attributes (e.g., age, location, gender) from user-generated text shared online, enabling rapid and large-scale privacy breaches. Existing anonymization-based defenses are coarse-grained, lacking word-level precision in anonymizing privacy-leaking elements. Moreover, they are inherently limited as altering user text to hide sensitive cues still allows attribute inference to occur through models' reasoning capabilities. To address these limitations, we propose a unified defense framework that combines fine-grained anonymization (TRACE) with inference-preventing optimization (RPS). TRACE leverages attention mechanisms and inference chain generation to identify and anonymize privacy-leaking textual elements, while RPS employs a lightweight two-stage optimization strategy to induce model rejection behaviors, thereby preventing attribute inference. Evaluations across diverse LLMs show that TRACE-RPS reduces attribute inference accuracy from around 50\% to below 5\% on open-source models. In addition, our approach offers strong cross-model generalization, prompt-variation robustness, and utility-privacy tradeoffs. Our code is available at https://github.com/Jasper-Yan/TRACE-RPS.

