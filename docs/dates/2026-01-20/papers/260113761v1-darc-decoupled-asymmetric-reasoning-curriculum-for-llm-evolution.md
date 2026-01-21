---
layout: default
title: DARC: Decoupled Asymmetric Reasoning Curriculum for LLM Evolution
---

# DARC: Decoupled Asymmetric Reasoning Curriculum for LLM Evolution
**arXiv**：[2601.13761v1](https://arxiv.org/abs/2601.13761) · [PDF](https://arxiv.org/pdf/2601.13761.pdf)  
**作者**：Shengda Fan, Xuyan Ye, Yankai Lin  

**一句话要点**：提出DARC框架以解决大语言模型自对弈中的优化不稳定问题

**关键词**：自对弈优化, 非对称推理, 难度校准, 自蒸馏训练, 模型无关改进, 推理基准提升

## 3 点简述
- 核心问题：自对弈框架存在优化不稳定，源于提问者奖励反馈的非平稳性和求解器自生成伪标签的引导误差
- 方法要点：采用两阶段解耦非对称推理课程，先训练提问者生成难度校准问题，再通过非对称自蒸馏训练求解器
- 实验或效果：在九个推理基准和三个骨干模型上平均提升10.9分，无需人工标注接近全监督模型性能

## 摘要（原文）

> Self-play with large language models has emerged as a promising paradigm for achieving self-improving artificial intelligence. However, existing self-play frameworks often suffer from optimization instability, due to (i) non-stationary objectives induced by solver-dependent reward feedback for the Questioner, and (ii) bootstrapping errors from self-generated pseudo-labels used to supervise the Solver. To mitigate these challenges, we introduce DARC (Decoupled Asymmetric Reasoning Curriculum), a two-stage framework that stabilizes the self-evolution process. First, we train the Questioner to synthesize difficulty-calibrated questions, conditioned on explicit difficulty levels and external corpora. Second, we train the Solver with an asymmetric self-distillation mechanism, where a document-augmented teacher generates high-quality pseudo-labels to supervise the student Solver that lacks document access. Empirical results demonstrate that DARC is model-agnostic, yielding an average improvement of 10.9 points across nine reasoning benchmarks and three backbone models. Moreover, DARC consistently outperforms all baselines and approaches the performance of fully supervised models without relying on human annotations.The code is available at https://github.com/RUCBM/DARC.

