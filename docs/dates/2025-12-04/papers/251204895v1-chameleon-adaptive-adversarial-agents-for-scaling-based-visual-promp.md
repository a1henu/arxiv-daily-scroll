---
layout: default
title: Chameleon: Adaptive Adversarial Agents for Scaling-Based Visual Prompt Injection in Multimodal AI Systems
---

# Chameleon: Adaptive Adversarial Agents for Scaling-Based Visual Prompt Injection in Multimodal AI Systems
**arXiv**：[2512.04895v1](https://arxiv.org/abs/2512.04895) · [PDF](https://arxiv.org/pdf/2512.04895.pdf)  
**作者**：M Zeeshan, Saud Satti  

**一句话要点**：提出自适应对抗框架Chameleon以解决多模态AI系统中基于缩放的视觉提示注入漏洞

**关键词**：多模态AI安全, 视觉提示注入, 自适应对抗攻击, 图像缩放漏洞, 代理优化

## 3 点简述
- 核心问题：多模态AI系统依赖图像缩放预处理，易被恶意视觉提示利用，形成安全漏洞。
- 方法要点：Chameleon采用基于代理的迭代优化机制，动态调整图像扰动以对抗缩放操作。
- 实验或效果：在Gemini 2.5 Flash模型上，攻击成功率84.5%，显著优于静态攻击的32.1%。

## 摘要（原文）

> Multimodal Artificial Intelligence (AI) systems, particularly Vision-Language Models (VLMs), have become integral to critical applications ranging from autonomous decision-making to automated document processing. As these systems scale, they rely heavily on preprocessing pipelines to handle diverse inputs efficiently. However, this dependency on standard preprocessing operations, specifically image downscaling, creates a significant yet often overlooked security vulnerability. While intended for computational optimization, scaling algorithms can be exploited to conceal malicious visual prompts that are invisible to human observers but become active semantic instructions once processed by the model. Current adversarial strategies remain largely static, failing to account for the dynamic nature of modern agentic workflows. To address this gap, we propose Chameleon, a novel, adaptive adversarial framework designed to expose and exploit scaling vulnerabilities in production VLMs. Unlike traditional static attacks, Chameleon employs an iterative, agent-based optimization mechanism that dynamically refines image perturbations based on the target model's real-time feedback. This allows the framework to craft highly robust adversarial examples that survive standard downscaling operations to hijack downstream execution. We evaluate Chameleon against Gemini 2.5 Flash model. Our experiments demonstrate that Chameleon achieves an Attack Success Rate (ASR) of 84.5% across varying scaling factors, significantly outperforming static baseline attacks which average only 32.1%. Furthermore, we show that these attacks effectively compromise agentic pipelines, reducing decision-making accuracy by over 45% in multi-step tasks. Finally, we discuss the implications of these vulnerabilities and propose multi-scale consistency checks as a necessary defense mechanism.

