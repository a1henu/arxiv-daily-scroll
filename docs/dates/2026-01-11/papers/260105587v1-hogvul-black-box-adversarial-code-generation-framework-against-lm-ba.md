---
layout: default
title: HogVul: Black-box Adversarial Code Generation Framework Against LM-based Vulnerability Detectors
---

# HogVul: Black-box Adversarial Code Generation Framework Against LM-based Vulnerability Detectors
**arXiv**：[2601.05587v1](https://arxiv.org/abs/2601.05587) · [PDF](https://arxiv.org/pdf/2601.05587.pdf)  
**作者**：Jingxiao Yang, Ping He, Tianyu Du, Sun Bing, Xuhong Zhang  

**一句话要点**：提出HogVul框架，通过双通道优化策略生成对抗代码以攻击基于语言模型的漏洞检测器。

**关键词**：对抗攻击, 漏洞检测, 语言模型, 黑盒攻击, 粒子群优化, 代码生成

## 3 点简述
- 核心问题：基于语言模型的漏洞检测器易受词汇和语法扰动攻击，现有黑盒攻击策略孤立，搜索效率低。
- 方法要点：集成词汇和语法扰动，采用粒子群优化驱动的双通道优化策略，系统探索对抗代码空间。
- 实验或效果：在四个基准数据集上，攻击成功率平均提升26.05%，优于现有基线方法。

## 摘要（原文）

> Recent advances in software vulnerability detection have been driven by Language Model (LM)-based approaches. However, these models remain vulnerable to adversarial attacks that exploit lexical and syntax perturbations, allowing critical flaws to evade detection. Existing black-box attacks on LM-based vulnerability detectors primarily rely on isolated perturbation strategies, limiting their ability to efficiently explore the adversarial code space for optimal perturbations. To bridge this gap, we propose HogVul, a black-box adversarial code generation framework that integrates both lexical and syntax perturbations under a unified dual-channel optimization strategy driven by Particle Swarm Optimization (PSO). By systematically coordinating two-level perturbations, HogVul effectively expands the search space for adversarial examples, enhancing the attack efficacy. Extensive experiments on four benchmark datasets demonstrate that HogVul achieves an average attack success rate improvement of 26.05\% over state-of-the-art baseline methods. These findings highlight the potential of hybrid optimization strategies in exposing model vulnerabilities.

