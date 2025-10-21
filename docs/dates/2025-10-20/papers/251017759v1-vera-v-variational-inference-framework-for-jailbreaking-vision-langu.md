---
layout: default
title: VERA-V: Variational Inference Framework for Jailbreaking Vision-Language Models
---

# VERA-V: Variational Inference Framework for Jailbreaking Vision-Language Models
**arXiv**：[2510.17759v1](https://arxiv.org/abs/2510.17759) · [PDF](https://arxiv.org/pdf/2510.17759.pdf)  
**作者**：Qilin Liao, Anamika Lochab, Ruqi Zhang  

**一句话要点**：提出VERA-V变分推理框架以解决多模态模型越狱攻击问题

**关键词**：多模态模型安全, 变分推理, 对抗攻击, 视觉语言模型, 越狱发现, 后验分布学习

## 3 点简述
- 多模态视觉语言模型存在未充分探索的脆弱性，现有攻击方法依赖脆弱模板且覆盖范围窄
- 将越狱发现建模为学习文本-图像提示的联合后验分布，生成隐蔽对抗输入并集成多种策略
- 在HarmBench和HADES基准测试中，攻击成功率最高提升53.75%，优于现有方法

## 摘要（原文）

> Vision-Language Models (VLMs) extend large language models with visual
> reasoning, but their multimodal design also introduces new, underexplored
> vulnerabilities. Existing multimodal red-teaming methods largely rely on
> brittle templates, focus on single-attack settings, and expose only a narrow
> subset of vulnerabilities. To address these limitations, we introduce VERA-V, a
> variational inference framework that recasts multimodal jailbreak discovery as
> learning a joint posterior distribution over paired text-image prompts. This
> probabilistic view enables the generation of stealthy, coupled adversarial
> inputs that bypass model guardrails. We train a lightweight attacker to
> approximate the posterior, allowing efficient sampling of diverse jailbreaks
> and providing distributional insights into vulnerabilities. VERA-V further
> integrates three complementary strategies: (i) typography-based text prompts
> that embed harmful cues, (ii) diffusion-based image synthesis that introduces
> adversarial signals, and (iii) structured distractors to fragment VLM
> attention. Experiments on HarmBench and HADES benchmarks show that VERA-V
> consistently outperforms state-of-the-art baselines on both open-source and
> frontier VLMs, achieving up to 53.75% higher attack success rate (ASR) over the
> best baseline on GPT-4o.

