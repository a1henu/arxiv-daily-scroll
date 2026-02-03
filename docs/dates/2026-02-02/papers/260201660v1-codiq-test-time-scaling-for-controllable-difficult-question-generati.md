---
layout: default
title: CoDiQ: Test-Time Scaling for Controllable Difficult Question Generation
---

# CoDiQ: Test-Time Scaling for Controllable Difficult Question Generation
**arXiv**：[2602.01660v1](https://arxiv.org/abs/2602.01660) · [PDF](https://arxiv.org/pdf/2602.01660.pdf)  
**作者**：Zhongyuan Peng, Caijun Xu, Changyi Xiao, Shibo Hong, Eli Zhang, Stephen Huang, Yixin Cao  

**一句话要点**：提出CoDiQ框架，通过测试时缩放实现可控难度问题生成，以增强大型推理模型的训练效果。

**关键词**：可控难度问题生成, 测试时缩放, 大型推理模型, 竞赛级问题, 问题可解性, 推理能力增强

## 3 点简述
- 现有自动问题生成方法缺乏精确难度控制，计算成本高，难以大规模生成竞赛级问题。
- CoDiQ框架基于测试时缩放倾向，开发CoDiQ-Generator提升高难度问题生成上限，确保问题可解性。
- 构建CoDiQ-Corpus（44K竞赛级问题序列），人类评估显示其挑战性优于基准，训练LRMs显著提升推理性能。

## 摘要（原文）

> Large Reasoning Models (LRMs) benefit substantially from training on challenging competition-level questions. However, existing automated question synthesis methods lack precise difficulty control, incur high computational costs, and struggle to generate competition-level questions at scale. In this paper, we propose CoDiQ (Controllable Difficult Question Generation), a novel framework enabling fine-grained difficulty control via test-time scaling while ensuring question solvability. Specifically, first, we identify a test-time scaling tendency (extended reasoning token budget boosts difficulty but reduces solvability) and the intrinsic properties defining the upper bound of a model's ability to generate valid, high-difficulty questions. Then, we develop CoDiQ-Generator from Qwen3-8B, which improves the upper bound of difficult question generation, making it particularly well-suited for challenging question construction. Building on the CoDiQ framework, we build CoDiQ-Corpus (44K competition-grade question sequences). Human evaluations show these questions are significantly more challenging than LiveCodeBench/AIME with over 82% solvability. Training LRMs on CoDiQ-Corpus substantially improves reasoning performance, verifying that scaling controlled-difficulty training questions enhances reasoning capabilities. We open-source CoDiQ-Corpus, CoDiQ-Generator, and implementations to support related research.

