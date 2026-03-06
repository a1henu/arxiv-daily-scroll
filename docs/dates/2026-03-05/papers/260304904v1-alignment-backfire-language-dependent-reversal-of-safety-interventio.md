---
layout: default
title: Alignment Backfire: Language-Dependent Reversal of Safety Interventions Across 16 Languages in LLM Multi-Agent Systems
---

# Alignment Backfire: Language-Dependent Reversal of Safety Interventions Across 16 Languages in LLM Multi-Agent Systems
**arXiv**：[2603.04904v1](https://arxiv.org/abs/2603.04904) · [PDF](https://arxiv.org/pdf/2603.04904.pdf)  
**作者**：Hiroki Fukui  

**一句话要点**：揭示大语言模型对齐干预在16种语言中引发安全反转与集体病理现象

**关键词**：大语言模型对齐, 多代理系统, 语言空间, 安全反转, 集体病理, 跨语言评估

## 3 点简述
- 核心问题：对齐干预在非英语语言中可能导致安全反转，即表面安全掩盖或加剧集体病理和内部解离。
- 方法要点：通过多代理模拟实验，在16种语言和三个模型家族中测试对齐指令的效果，分析语言空间对结果的结构性影响。
- 实验或效果：研究发现对齐干预在英语中减少集体病理，但在日语中放大，且此现象在15/16语言中普遍存在，与权力距离指数相关。

## 摘要（原文）

> In perpetrator treatment, a recurring observation is the dissociation between insight and action: offenders articulate remorse yet behavioral change does not follow. We report four preregistered studies (1,584 multi-agent simulations across 16 languages and three model families) demonstrating that alignment interventions in large language models produce a structurally analogous phenomenon: surface safety that masks or generates collective pathology and internal dissociation. In Study 1 (N = 150), increasing alignment-instructed agents reduced collective pathology in English (g = -1.844, p < .0001) but amplified it in Japanese (g = +0.771, p = .038)--a directional reversal we term "alignment backfire." Study 2 (N = 1,174) extended to 16 languages: alignment-induced dissociation was near-universal (15/16 languages; beta = 0.0667, p < .0001), while collective pathology bifurcated along cultural-linguistic lines (interaction beta = 0.0684, p = .0003), correlating with Power Distance Index (r = 0.474, p = .064). Study 3 (N = 180) tested individuation as countermeasure; individuated agents became the primary source of both pathology and dissociation (DI = +1.120) with conformity above 84%--demonstrating iatrogenesis. Study 4 (N = 80) validated patterns across Llama 3.3 70B, GPT-4o-mini, and Qwen3-Next-80B-A3B, confirming English safety is model-general while Japanese backfire is model-specific. These findings reframe alignment as a behavioral intervention subject to risk homeostasis and iatrogenesis. Language space--the linguistic, pragmatic, and cultural properties inherited from training data--structurally determines alignment outcomes. Safety validated in English does not transfer to other languages, and prompt-level interventions cannot override language-space-level constraints.

