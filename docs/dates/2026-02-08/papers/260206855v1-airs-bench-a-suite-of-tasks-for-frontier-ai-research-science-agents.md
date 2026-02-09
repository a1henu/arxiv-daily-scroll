---
layout: default
title: AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents
---

# AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents
**arXiv**：[2602.06855v1](https://arxiv.org/abs/2602.06855) · [PDF](https://arxiv.org/pdf/2602.06855.pdf)  
**作者**：Alisia Lupidi, Bhavul Gauri, Thomas Simon Foster, Bassel Al Omari, Despoina Magka, Alberto Pepe, Alexis Audran-Reiss, Muna Aghamelu, Nicolas Baldwin, Lucia Cipolina-Kun, Jean-Christophe Gagnon-Audet, Chee Hau Leow, Sandra Lefdal, Hossam Mossalam, Abhinav Moudgil, Saba Nazir, Emanuel Tewolde, Isabel Urrego, Jordi Armengol Estape, Amar Budhiraja, Gaurav Chaurasia, Abhishek Charnalia, Derek Dunfield, Karen Hambardzumyan, Daniel Izcovich, Martin Josifoski, Ishita Mediratta, Kelvin Niu, Parth Pathak, Michael Shvartsman, Edan Toledo, Anton Protopopov, Roberta Raileanu, Alexander Miller, Tatiana Shavrina, Jakob Foerster, Yoram Bachrach  

**一句话要点**：提出AIRS-Bench基准套件以评估AI科研代理在完整研究生命周期中的能力

**关键词**：AI科研代理, 基准评估, 研究生命周期, 多领域任务, 开源基准

## 3 点简述
- 核心问题：缺乏评估AI科研代理在科学前沿任务中全周期能力的基准
- 方法要点：构建包含20个任务的套件，涵盖多领域，支持任务集成与框架比较
- 实验或效果：基线结果显示代理在4个任务中超越人类SOTA，但多数任务仍有改进空间

## 摘要（原文）

> LLM agents hold significant promise for advancing scientific research. To accelerate this progress, we introduce AIRS-Bench (the AI Research Science Benchmark), a suite of 20 tasks sourced from state-of-the-art machine learning papers. These tasks span diverse domains, including language modeling, mathematics, bioinformatics, and time series forecasting. AIRS-Bench tasks assess agentic capabilities over the full research lifecycle -- including idea generation, experiment analysis and iterative refinement -- without providing baseline code. The AIRS-Bench task format is versatile, enabling easy integration of new tasks and rigorous comparison across different agentic frameworks. We establish baselines using frontier models paired with both sequential and parallel scaffolds. Our results show that agents exceed human SOTA in four tasks but fail to match it in sixteen others. Even when agents surpass human benchmarks, they do not reach the theoretical performance ceiling for the underlying tasks. These findings indicate that AIRS-Bench is far from saturated and offers substantial room for improvement. We open-source the AIRS-Bench task definitions and evaluation code to catalyze further development in autonomous scientific research.

