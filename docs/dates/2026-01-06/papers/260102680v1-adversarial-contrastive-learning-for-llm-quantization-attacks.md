---
layout: default
title: Adversarial Contrastive Learning for LLM Quantization Attacks
---

# Adversarial Contrastive Learning for LLM Quantization Attacks
**arXiv**：[2601.02680v1](https://arxiv.org/abs/2601.02680) · [PDF](https://arxiv.org/pdf/2601.02680.pdf)  
**作者**：Dinghong Song, Zhiwei Xu, Hai Wan, Xibin Zhao, Pengfei Su, Dong Li  

**一句话要点**：提出对抗对比学习以增强大语言模型量化攻击效果

**关键词**：大语言模型量化, 对抗攻击, 对比学习, 梯度优化, 安全风险

## 3 点简述
- 核心问题：全精度大语言模型量化后可能产生恶意行为，存在安全风险。
- 方法要点：基于梯度攻击，采用三元组对比损失最大化良性响应与有害响应概率差距。
- 实验或效果：攻击成功率显著提升，在拒绝过度、越狱和广告注入任务上分别达86.00%、97.69%和92.40%。

## 摘要（原文）

> Model quantization is critical for deploying large language models (LLMs) on resource-constrained hardware, yet recent work has revealed severe security risks that benign LLMs in full precision may exhibit malicious behaviors after quantization. In this paper, we propose Adversarial Contrastive Learning (ACL), a novel gradient-based quantization attack that achieves superior attack effectiveness by explicitly maximizing the gap between benign and harmful responses probabilities. ACL formulates the attack objective as a triplet-based contrastive loss, and integrates it with a projected gradient descent two-stage distributed fine-tuning strategy to ensure stable and efficient optimization. Extensive experiments demonstrate ACL's remarkable effectiveness, achieving attack success rates of 86.00% for over-refusal, 97.69% for jailbreak, and 92.40% for advertisement injection, substantially outperforming state-of-the-art methods by up to 44.67%, 18.84%, and 50.80%, respectively.

