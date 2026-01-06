---
layout: default
title: Crafting Adversarial Inputs for Large Vision-Language Models Using Black-Box Optimization
---

# Crafting Adversarial Inputs for Large Vision-Language Models Using Black-Box Optimization
**arXiv**：[2601.01747v1](https://arxiv.org/abs/2601.01747) · [PDF](https://arxiv.org/pdf/2601.01747.pdf)  
**作者**：Jiwei Guan, Haibo Jin, Haohan Wang  

**一句话要点**：提出基于ZO-SPSA的黑盒优化方法，以攻击大型视觉语言模型的安全机制。

**关键词**：对抗性攻击, 黑盒优化, 大型视觉语言模型, 安全机制, 零阶优化

## 3 点简述
- 核心问题：大型视觉语言模型易受对抗性越狱攻击，现有白盒方法不适用于黑盒场景。
- 方法要点：使用ZO-SPSA进行零阶优化，无需模型知识，降低资源消耗。
- 实验或效果：在InstructBLIP上达到83.0%越狱成功率，对抗样本具有强迁移性。

## 摘要（原文）

> Recent advancements in Large Vision-Language Models (LVLMs) have shown groundbreaking capabilities across diverse multimodal tasks. However, these models remain vulnerable to adversarial jailbreak attacks, where adversaries craft subtle perturbations to bypass safety mechanisms and trigger harmful outputs. Existing white-box attacks methods require full model accessibility, suffer from computing costs and exhibit insufficient adversarial transferability, making them impractical for real-world, black-box settings. To address these limitations, we propose a black-box jailbreak attack on LVLMs via Zeroth-Order optimization using Simultaneous Perturbation Stochastic Approximation (ZO-SPSA). ZO-SPSA provides three key advantages: (i) gradient-free approximation by input-output interactions without requiring model knowledge, (ii) model-agnostic optimization without the surrogate model and (iii) lower resource requirements with reduced GPU memory consumption. We evaluate ZO-SPSA on three LVLMs, including InstructBLIP, LLaVA and MiniGPT-4, achieving the highest jailbreak success rate of 83.0% on InstructBLIP, while maintaining imperceptible perturbations comparable to white-box methods. Moreover, adversarial examples generated from MiniGPT-4 exhibit strong transferability to other LVLMs, with ASR reaching 64.18%. These findings underscore the real-world feasibility of black-box jailbreaks and expose critical weaknesses in the safety mechanisms of current LVLMs

