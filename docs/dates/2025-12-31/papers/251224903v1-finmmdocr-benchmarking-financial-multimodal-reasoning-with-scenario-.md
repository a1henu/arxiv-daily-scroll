---
layout: default
title: FinMMDocR: Benchmarking Financial Multimodal Reasoning with Scenario Awareness, Document Understanding, and Multi-Step Computation
---

# FinMMDocR: Benchmarking Financial Multimodal Reasoning with Scenario Awareness, Document Understanding, and Multi-Step Computation
**arXiv**：[2512.24903v1](https://arxiv.org/abs/2512.24903) · [PDF](https://arxiv.org/pdf/2512.24903.pdf)  
**作者**：Zichen Tang, Haihong E, Rongjin Li, Jiacheng Liu, Linwei Jia, Zhuodi Hao, Zhongjun Yang, Yuanze Li, Haolin Tian, Xinyi Hu, Peizhi Zhao, Yuan Liu, Zhengyu Wang, Xianghe Wang, Yiling Huang, Xueyuan Lin, Ruofei Bai, Zijian Xie, Qian Huang, Ruining Cao, Haocheng Gao  

**一句话要点**：提出FinMMDocR基准，评估多模态大语言模型在真实金融数值推理中的表现。

**关键词**：金融多模态推理, 场景感知, 文档理解, 多步计算, 基准评估, 检索增强生成

## 3 点简述
- 核心问题：现有基准在金融多模态推理中缺乏场景感知、文档理解和多步计算能力。
- 方法要点：构建包含1200个专家标注问题的双语多模态基准，涵盖12种金融场景和9类文档。
- 实验或效果：最佳模型准确率仅58.0%，显示任务挑战性，RAG方法性能差异显著。

## 摘要（原文）

> We introduce FinMMDocR, a novel bilingual multimodal benchmark for evaluating multimodal large language models (MLLMs) on real-world financial numerical reasoning. Compared to existing benchmarks, our work delivers three major advancements. (1) Scenario Awareness: 57.9% of 1,200 expert-annotated problems incorporate 12 types of implicit financial scenarios (e.g., Portfolio Management), challenging models to perform expert-level reasoning based on assumptions; (2) Document Understanding: 837 Chinese/English documents spanning 9 types (e.g., Company Research) average 50.8 pages with rich visual elements, significantly surpassing existing benchmarks in both breadth and depth of financial documents; (3) Multi-Step Computation: Problems demand 11-step reasoning on average (5.3 extraction + 5.7 calculation steps), with 65.0% requiring cross-page evidence (2.4 pages average). The best-performing MLLM achieves only 58.0% accuracy, and different retrieval-augmented generation (RAG) methods show significant performance variations on this task. We expect FinMMDocR to drive improvements in MLLMs and reasoning-enhanced methods on complex multimodal reasoning tasks in real-world scenarios.

