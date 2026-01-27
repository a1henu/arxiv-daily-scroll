---
layout: default
title: ARMOR: Agentic Reasoning for Methods Orchestration and Reparameterization for Robust Adversarial Attacks
---

# ARMOR: Agentic Reasoning for Methods Orchestration and Reparameterization for Robust Adversarial Attacks
**arXiv**：[2601.18386v1](https://arxiv.org/abs/2601.18386) · [PDF](https://arxiv.org/pdf/2601.18386.pdf)  
**作者**：Gabriel Lee Jun Rong, Christos Korgialas, Dion Jia Xu Ho, Pai Chet Ng, Xiaoxiao Miao, Konstantinos N. Plataniotis  

**一句话要点**：提出ARMOR框架，通过VLM和LLM引导的智能体协同生成对抗攻击，以解决现有自动化攻击套件缺乏战略适应和语义感知的问题。

**关键词**：对抗攻击, 智能体协同, 视觉语言模型, 大语言模型, 攻击合成, 语义感知

## 3 点简述
- 核心问题：现有自动化攻击套件作为静态集成运行，序列固定，缺乏战略适应和语义感知。
- 方法要点：ARMOR通过VLM引导的智能体协同生成扰动，利用LLM实时调参，在共享“混合台”上合成攻击。
- 实验或效果：在标准基准测试中，ARMOR提升了跨架构迁移性，可靠地欺骗黑盒和白盒目标，使用置信度和SSIM分数选择最佳攻击。

## 摘要（原文）

> Existing automated attack suites operate as static ensembles with fixed sequences, lacking strategic adaptation and semantic awareness. This paper introduces the Agentic Reasoning for Methods Orchestration and Reparameterization (ARMOR) framework to address these limitations. ARMOR orchestrates three canonical adversarial primitives, Carlini-Wagner (CW), Jacobian-based Saliency Map Attack (JSMA), and Spatially Transformed Attacks (STA) via Vision Language Models (VLM)-guided agents that collaboratively generate and synthesize perturbations through a shared ``Mixing Desk". Large Language Models (LLMs) adaptively tune and reparameterize parallel attack agents in a real-time, closed-loop system that exploits image-specific semantic vulnerabilities. On standard benchmarks, ARMOR achieves improved cross-architecture transfer and reliably fools both settings, delivering a blended output for blind targets and selecting the best attack or blended attacks for white-box targets using a confidence-and-SSIM score.

