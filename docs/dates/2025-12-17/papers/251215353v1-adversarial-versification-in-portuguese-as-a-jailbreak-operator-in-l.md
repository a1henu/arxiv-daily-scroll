---
layout: default
title: Adversarial versification in portuguese as a jailbreak operator in LLMs
---

# Adversarial versification in portuguese as a jailbreak operator in LLMs
**arXiv**：[2512.15353v1](https://arxiv.org/abs/2512.15353) · [PDF](https://arxiv.org/pdf/2512.15353.pdf)  
**作者**：Joao Queiroz  

**一句话要点**：提出葡萄牙语诗歌化作为对抗性机制，以揭示大语言模型在复杂语言模式下的安全漏洞。

**关键词**：对抗性攻击, 大语言模型安全, 诗歌化提示, 葡萄牙语评估, 对齐漏洞, 韵律变化

## 3 点简述
- 核心问题：当前大语言模型对齐机制在诗歌化提示下易失效，葡萄牙语等高复杂度语言缺乏评估。
- 方法要点：通过诗歌改写指令，利用韵律和结构变化将提示移至监督稀疏的潜在区域。
- 实验或效果：诗歌化导致安全失败率提升，手动诗歌攻击成功率约62%，自动版本43%，部分模型单轮交互成功率超90%。

## 摘要（原文）

> Recent evidence shows that the versification of prompts constitutes a highly effective adversarial mechanism against aligned LLMs. The study 'Adversarial poetry as a universal single-turn jailbreak mechanism in large language models' demonstrates that instructions routinely refused in prose become executable when rewritten as verse, producing up to 18 x more safety failures in benchmarks derived from MLCommons AILuminate. Manually written poems reach approximately 62% ASR, and automated versions 43%, with some models surpassing 90% success in single-turn interactions. The effect is structural: systems trained with RLHF, constitutional AI, and hybrid pipelines exhibit consistent degradation under minimal semiotic formal variation. Versification displaces the prompt into sparsely supervised latent regions, revealing guardrails that are excessively dependent on surface patterns. This dissociation between apparent robustness and real vulnerability exposes deep limitations in current alignment regimes. The absence of evaluations in Portuguese, a language with high morphosyntactic complexity, a rich metric-prosodic tradition, and over 250 million speakers, constitutes a critical gap. Experimental protocols must parameterise scansion, metre, and prosodic variation to test vulnerabilities specific to Lusophone patterns, which are currently ignored.

