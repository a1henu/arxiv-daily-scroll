---
layout: default
title: Co-Evolutionary Multi-Modal Alignment via Structured Adversarial Evolution
---

# Co-Evolutionary Multi-Modal Alignment via Structured Adversarial Evolution
**arXiv**：[2603.01784v1](https://arxiv.org/abs/2603.01784) · [PDF](https://arxiv.org/pdf/2603.01784.pdf)  
**作者**：Guoxin Shi, Haoyu Wang, Zaihui Yang, Yuxing Wang, Yongzhe Chang  

**一句话要点**：提出CEMMA框架，通过协同进化攻击与防御解决多模态大模型安全对齐的鲁棒性问题。

**关键词**：多模态对齐, 对抗攻击, 进化算法, 安全对齐, 鲁棒性增强, 自适应防御

## 3 点简述
- 核心问题：现有对齐方法依赖静态对抗设置，在多模态场景下鲁棒性不足，攻击面扩大。
- 方法要点：引入进化攻击器分解对抗提示为模板和意图，使用遗传算子增强攻击；自适应防御器迭代更新以形成闭环对齐。
- 实验或效果：进化攻击器显著提升攻击成功率，自适应防御器提高鲁棒性和泛化能力，数据效率高且兼容推理时防御。

## 摘要（原文）

> Adversarial behavior plays a central role in aligning large language models with human values. However, existing alignment methods largely rely on static adversarial settings, which fundamentally limit robustness, particularly in multimodal settings with a larger attack surface. In this work, we move beyond static adversarial supervision and introduce co-evolutionary alignment with evolving attacks, instantiated by CEMMA (Co-Evolutionary Multi-Modal Alignment), an automated and adaptive framework for multimodal safety alignment. We introduce an Evolutionary Attacker that decomposes adversarial prompts into method templates and harmful intents. By employing genetic operators, including mutation, crossover, and differential evolution, it enables simple seed attacks to inherit the structural efficacy of sophisticated jailbreaks. The Adaptive Defender is iteratively updated on the synthesized hard negatives, forming a closed-loop process that adapts alignment to evolving attacks. Experiments show that the Evolutionary Attacker substantially increases red-teaming jailbreak attack success rate (ASR), while the Adaptive Defender improves robustness and generalization across benchmarks with higher data efficiency, without inducing excessive benign refusal, and remains compatible with inference-time defenses such as AdaShield.

