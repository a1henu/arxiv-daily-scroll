---
layout: default
title: Designing UNICORN: a Unified Benchmark for Imaging in Computational Pathology, Radiology, and Natural Language
---

# Designing UNICORN: a Unified Benchmark for Imaging in Computational Pathology, Radiology, and Natural Language
**arXiv**：[2603.02790v1](https://arxiv.org/abs/2603.02790) · [PDF](https://arxiv.org/pdf/2603.02790.pdf)  
**作者**：Michelle Stegeman, Lena Philipp, Fennie van der Graaf, Marina D'Amato, Clément Grisi, Luc Builtjes, Joeran S. Bosma, Judith Lefkes, Rianne A. Weber, James A. Meakin, Thomas Koopman, Anne Mickan, Mathias Prokop, Ewoud J. Smit, Geert Litjens, Jeroen van der Laak, Bram van Ginneken, Maarten de Rooij, Henkjan Huisman, Colin Jacobs, Francesco Ciompi, Alessa Hering  

**一句话要点**：提出UNICORN统一基准以评估医学基础模型在计算病理学、放射学和自然语言中的跨模态泛化能力

**关键词**：医学基础模型, 跨模态泛化, 少样本适应, 统一评估基准, 隔离测试集, 多模态医学成像

## 3 点简述
- 核心问题：缺乏公开、标准化、可复现的评估框架，现有基准在任务、器官或模态上碎片化，限制跨任务泛化评估。
- 方法要点：基于两步框架构建基准，解耦模型推理与任务特定评估，使用标准化少样本适应和间接访问的隔离测试集。
- 实验或效果：数据集覆盖2400多名患者，包括3700多个视觉案例和2400多份临床报告，支持多任务、多模态评估和UNICORN Score聚合指标。

## 摘要（原文）

> Medical foundation models show promise to learn broadly generalizable features from large, diverse datasets. This could be the base for reliable cross-modality generalization and rapid adaptation to new, task-specific goals, with only a few task-specific examples. Yet, evidence for this is limited by the lack of public, standardized, and reproducible evaluation frameworks, as existing public benchmarks are often fragmented across task-, organ-, or modality-specific settings, limiting assessment of cross-task generalization. We introduce UNICORN, a public benchmark designed to systematically evaluate medical foundation models under a unified protocol. To isolate representation quality, we built the benchmark on a novel two-step framework that decouples model inference from task-specific evaluation based on standardized few-shot adaptation. As a central design choice, we constructed indirectly accessible sequestered test sets derived from clinically relevant cohorts, along with standardized evaluation code and a submission interface on an open benchmarking platform. Performance is aggregated into a single UNICORN Score, a new metric that we introduce to support direct comparison of foundation models across diverse medical domains, modalities, and task types. The UNICORN test dataset includes data from more than 2,400 patients, including over 3,700 vision cases and over 2,400 clinical reports collected from 17 institutions across eight countries. The benchmark spans eight anatomical regions and four imaging modalities. Both task-specific and aggregated leaderboards enable accessible, standardized, and reproducible evaluation. By standardizing multi-task, multi-modality assessment, UNICORN establishes a foundation for reproducible benchmarking of medical foundation models. Data, baseline methods, and the evaluation platform are publicly available via unicorn.grand-challenge.org.

