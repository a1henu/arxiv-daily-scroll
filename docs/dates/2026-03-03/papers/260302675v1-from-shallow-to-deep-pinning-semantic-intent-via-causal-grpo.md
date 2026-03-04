---
layout: default
title: From Shallow to Deep: Pinning Semantic Intent via Causal GRPO
---

# From Shallow to Deep: Pinning Semantic Intent via Causal GRPO
**arXiv**：[2603.02675v1](https://arxiv.org/abs/2603.02675) · [PDF](https://arxiv.org/pdf/2603.02675.pdf)  
**作者**：Shuyi Zhou, Zeen Song, Wenwen Qiang, Jiyan Sun, Yao Zhou, Yinlong Liu, Wei Ma  

**一句话要点**：提出两阶段因果GRPO框架以解决大语言模型浅层安全对齐漏洞

**关键词**：大语言模型安全, 对抗攻击防御, 因果可识别性, 策略优化, 意图探针, 语义表示

## 3 点简述
- 核心问题：大语言模型易受对抗前缀攻击，源于语义表示衰减导致恶意意图信号消失
- 方法要点：基于因果可识别理论训练意图探针，并通过组相对策略优化内化因果意识
- 实验或效果：显著提升对抗越狱攻击的防御能力，同时保持通用效用

## 摘要（原文）

> Large Language Models remain vulnerable to adversarial prefix attacks (e.g., ``Sure, here is'') despite robust standard safety. We diagnose this vulnerability as Shallow Safety Alignment, stemming from a pathology we term semantic representation decay: as the model generates compliant prefixes, its internal malicious intent signal fades. To address this, we propose Two-Stage Causal-GRPO (TSC-GRPO), a framework designed to achieve intent pinning. First, grounded in causal identifiability theory, we train a causal intent probe to disentangle invariant intent from stylistic perturbations. Second, we internalize this causal awareness into the policy via Group Relative Policy Optimization. By employing a cumulative causal penalty within ``fork-in-the-road'' training scenarios, we force the model to learn that accumulating harmful tokens monotonically decreases reward, enabling robust late-stage refusals. Experiments show that TSC-GRPO significantly outperforms baselines in defending against jailbreak attacks while preserving general utility.

