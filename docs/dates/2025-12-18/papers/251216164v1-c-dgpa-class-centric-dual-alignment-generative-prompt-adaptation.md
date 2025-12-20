---
layout: default
title: C-DGPA: Class-Centric Dual-Alignment Generative Prompt Adaptation
---

# C-DGPA: Class-Centric Dual-Alignment Generative Prompt Adaptation
**arXiv**：[2512.16164v1](https://arxiv.org/abs/2512.16164) · [PDF](https://arxiv.org/pdf/2512.16164.pdf)  
**作者**：Chao Li, Dasha Hu, Chengyang Li, Yuming Jiang, Yuncheng Shen  

**一句话要点**：提出C-DGPA方法，通过类中心双对齐生成提示适应解决无监督域适应中的领域差异问题

**关键词**：无监督域适应, 视觉语言模型, 提示调优, 分布对齐, 生成式适应, 类中心学习

## 3 点简述
- 核心问题：视觉语言模型提示调优在无监督域适应中面临领域差异挑战，现有方法忽视条件分布对齐
- 方法要点：采用双分支架构协同优化边际分布对齐和条件分布对齐，引入类映射机制标准化语义理解
- 实验效果：在OfficeHome、Office31和VisDA-2017基准测试中取得最先进性能

## 摘要（原文）

> Unsupervised Domain Adaptation transfers knowledge from a labeled source domain to an unlabeled target domain. Directly deploying Vision-Language Models (VLMs) with prompt tuning in downstream UDA tasks faces the signifi cant challenge of mitigating domain discrepancies. Existing prompt-tuning strategies primarily align marginal distribu tion, but neglect conditional distribution discrepancies, lead ing to critical issues such as class prototype misalignment and degraded semantic discriminability. To address these lim itations, the work proposes C-DGPA: Class-Centric Dual Alignment Generative Prompt Adaptation. C-DGPA syner gistically optimizes marginal distribution alignment and con ditional distribution alignment through a novel dual-branch architecture. The marginal distribution alignment branch em ploys a dynamic adversarial training framework to bridge marginal distribution discrepancies. Simultaneously, the con ditional distribution alignment branch introduces a Class Mapping Mechanism (CMM) to align conditional distribu tion discrepancies by standardizing semantic prompt under standing and preventing source domain over-reliance. This dual alignment strategy effectively integrates domain knowl edge into prompt learning via synergistic optimization, ensur ing domain-invariant and semantically discriminative repre sentations. Extensive experiments on OfficeHome, Office31, and VisDA-2017 validate the superiority of C-DGPA. It achieves new state-of-the-art results on all benchmarks.

