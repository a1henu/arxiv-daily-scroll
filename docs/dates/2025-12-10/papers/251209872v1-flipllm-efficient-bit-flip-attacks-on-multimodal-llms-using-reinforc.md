---
layout: default
title: FlipLLM: Efficient Bit-Flip Attacks on Multimodal LLMs using Reinforcement Learning
---

# FlipLLM: Efficient Bit-Flip Attacks on Multimodal LLMs using Reinforcement Learning
**arXiv**：[2512.09872v1](https://arxiv.org/abs/2512.09872) · [PDF](https://arxiv.org/pdf/2512.09872.pdf)  
**作者**：Khurram Khalil, Khaza Anuarul Hoque  

**一句话要点**：提出FlipLLM框架，利用强化学习高效发现多模态大模型的位翻转攻击漏洞。

**关键词**：位翻转攻击, 强化学习, 多模态大模型, 硬件安全, 漏洞发现, Q学习

## 3 点简述
- 核心问题：现有位翻转攻击发现方法泛化性差、难以扩展，无法高效分析大模型参数空间。
- 方法要点：结合敏感度引导的层剪枝与Q学习，将攻击发现建模为序列决策问题。
- 实验或效果：在LLaMA 3.1 8B和LLaVA等模型上，仅翻转少量位即可使准确率骤降，速度比现有方法快2.5倍。

## 摘要（原文）

> Generative Artificial Intelligence models, such as Large Language Models (LLMs) and Large Vision Models (VLMs), exhibit state-of-the-art performance but remain vulnerable to hardware-based threats, specifically bit-flip attacks (BFAs). Existing BFA discovery methods lack generalizability and struggle to scale, often failing to analyze the vast parameter space and complex interdependencies of modern foundation models in a reasonable time. This paper proposes FlipLLM, a reinforcement learning (RL) architecture-agnostic framework that formulates BFA discovery as a sequential decision-making problem. FlipLLM combines sensitivity-guided layer pruning with Q-learning to efficiently identify minimal, high-impact bit sets that can induce catastrophic failure. We demonstrate the effectiveness and generalizability of FlipLLM by applying it to a diverse set of models, including prominent text-only LLMs (GPT-2 Large, LLaMA 3.1 8B, and DeepSeek-V2 7B), VLMs such as LLaVA 1.6, and datasets, such as MMLU, MMLU-Pro, VQAv2, and TextVQA. Our results show that FlipLLM can identify critical bits that are vulnerable to BFAs up to 2.5x faster than SOTA methods. We demonstrate that flipping the FlipLLM-identified bits plummets the accuracy of LLaMA 3.1 8B from 69.9% to ~0.2%, and for LLaVA's VQA score from 78% to almost 0%, by flipping as few as 5 and 7 bits, respectively. Further analysis reveals that applying standard hardware protection mechanisms, such as ECC SECDED, to the FlipLLM-identified bit locations completely mitigates the BFA impact, demonstrating the practical value of our framework in guiding hardware-level defenses. FlipLLM offers the first scalable and adaptive methodology for exploring the BFA vulnerability of both language and multimodal foundation models, paving the way for comprehensive hardware-security evaluation.

