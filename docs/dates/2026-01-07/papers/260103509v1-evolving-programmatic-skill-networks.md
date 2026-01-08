---
layout: default
title: Evolving Programmatic Skill Networks
---

# Evolving Programmatic Skill Networks
**arXiv**：[2601.03509v1](https://arxiv.org/abs/2601.03509) · [PDF](https://arxiv.org/pdf/2601.03509.pdf)  
**作者**：Haochen Shi, Xingdi Yuan, Bang Liu  

**一句话要点**：提出程序化技能网络以解决开放环境中的持续技能获取问题

**关键词**：持续学习, 程序化技能, 开放环境, 技能网络, 大语言模型

## 3 点简述
- 研究开放环境中的持续技能获取，需构建、优化和重用可执行技能库
- 引入程序化技能网络，技能为可执行符号程序，通过经验演化形成组合网络
- 在MineDojo和Crafter实验中展示技能重用、快速适应和强泛化能力

## 摘要（原文）

> We study continual skill acquisition in open-ended embodied environments where an agent must construct, refine, and reuse an expanding library of executable skills. We introduce the Programmatic Skill Network (PSN), a framework in which skills are executable symbolic programs forming a compositional network that evolves through experience. PSN defines three core mechanisms instantiated via large language models: (1)REFLECT for structured fault localization over skill compositions, (2) progressive optimization with maturity-aware update gating that stabilizes reliable skills while maintaining plasticity for uncertain ones, and (3) canonical structural refactoring under rollback validation that maintains network compactness. We further show that PSN's learning dynamics exhibit structural parallels to neural network training. Experiments on MineDojo and Crafter demonstrate robust skill reuse, rapid adaptation, and strong generalization across open-ended task distributions.\footnote{We plan to open-source the code.

