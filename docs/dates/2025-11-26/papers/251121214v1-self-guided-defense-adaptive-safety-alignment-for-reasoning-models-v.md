---
layout: default
title: Self-Guided Defense: Adaptive Safety Alignment for Reasoning Models via Synthesized Guidelines
---

# Self-Guided Defense: Adaptive Safety Alignment for Reasoning Models via Synthesized Guidelines
**arXiv**：[2511.21214v1](https://arxiv.org/abs/2511.21214) · [PDF](https://arxiv.org/pdf/2511.21214.pdf)  
**作者**：Yuhang Wang, Yanxu Zhu, Dongyuan Lu, Jitao Sang  

**一句话要点**：提出SGASA框架以增强推理模型对对抗性越狱提示的安全防御

**关键词**：推理模型安全, 自适应对齐, 对抗性防御, 指南合成, 微调优化

## 3 点简述
- 核心问题：对抗性越狱提示隐蔽欺骗，易绕过安全机制生成有害内容
- 方法要点：通过数据预合成生成安全指南，结合SFT和DPO进行对齐微调
- 实验或效果：多数据集实验显示SGASA显著提升模型安全性和适应性

## 摘要（原文）

> Reasoning models have demonstrated remarkable capabilities in complex reasoning tasks. However, ensuring their safety against adversarial jailbreak prompts remains a critical challenge. Due to the covert and deceptive nature of such prompts, they can often evade built-in safety mechanisms and lead to the generation of harmful content. This underscores the need for an adaptive safety alignment approach that enables models to autonomously reinforce their defenses in response to adversarial inputs. This paper introduces the Synthesized Guideline-based Adaptive Safety Alignment (SGASA) framework, which internalizes model-generated safety guidelines to strengthen models' ability to enhance robustness against harmful adversarial prompts while minimizing unnecessary refusals of benign requests. SGASA consists of two key stages: Data Pre-synthesis, which generates safety guidelines and augmented prompts; and Alignment Fine-tuning, which leverages Supervised Fine-tuning (SFT) and Direct Preference Optimization (DPO) to embed these guidelines into the model. Extensive experiments across multiple datasets demonstrate that SGASA significantly improves model safety, validating its adaptive and scalable effectiveness.

