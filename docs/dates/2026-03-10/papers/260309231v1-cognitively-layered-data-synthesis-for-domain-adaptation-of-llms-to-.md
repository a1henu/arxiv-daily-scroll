---
layout: default
title: Cognitively Layered Data Synthesis for Domain Adaptation of LLMs to Space Situational Awareness
---

# Cognitively Layered Data Synthesis for Domain Adaptation of LLMs to Space Situational Awareness
**arXiv**：[2603.09231v1](https://arxiv.org/abs/2603.09231) · [PDF](https://arxiv.org/pdf/2603.09231.pdf)  
**作者**：Ding Linghu, Cheng Wang, Da Fan, Wei Shi, Kaifeng Yin, Xiaoliang Xue, Fan Yang, Haiyi Ren, Cong Zhang  

**一句话要点**：提出基于布鲁姆分类学的领域微调数据生成框架，以解决大语言模型在空间态势感知等复杂工程领域适应中的知识覆盖、认知深度和质量控制问题。

**关键词**：领域适应, 监督微调, 数据生成, 认知分层, 空间态势感知, 大语言模型

## 3 点简述
- 核心问题：大语言模型在空间态势感知等复杂工程领域适应困难，源于知识结构不对齐、认知监督缺失和数据质量与工程规范不符。
- 方法要点：通过结构化知识组织、认知分层问题建模和自动化质量控制，构建高质量监督微调数据集。
- 实验或效果：构建约23万样本的领域数据集，微调模型在领域测试集上BLEU-1相对提升显著，竞技场胜率82.21%，并保持通用基准性能。

## 摘要（原文）

> Large language models (LLMs) demonstrate exceptional performance on general-purpose tasks. however, transferring them to complex engineering domains such as space situational awareness (SSA) remains challenging owing to insufficient structural alignment with mission chains, the absence of higher-order cognitive supervision, and poor correspondence between data quality criteria and engineering specifications. The core bottleneck is the construction of high-quality supervised fine-tuning (SFT) datasets. To this end, we propose BD-FDG (Bloom's Taxonomy-based Domain-specific Fine-tuning Data Generation), a framework that addresses incomplete knowledge coverage, shallow cognitive depth, and limited quality controllability through three mechanisms: structured knowledge organization, cognitively layered question modeling, and automated quality control. The framework uses a knowledge tree to ensure structured corpus coverage, designs a question generation scheme spanning nine categories and six cognitive levels from Remember to Create to produce samples with a continuous difficulty gradient, and applies a multidimensional scoring pipeline to enforce domain rigor and consistency. Using BD-FDG, we construct SSA-SFT, a domain dataset of approximately 230K samples, and fine-tune Qwen3-8B to obtain SSA-LLM-8B. Experiments show that SSA-LLM-8B achieves relative BLEU-1 improvements of 144\% (no-think) and 176\% (think) on the domain test set and a win rate of 82.21\% over the baseline in arena comparisons, while largely preserving general benchmark performance (MMLU-Pro, MATH-500). These results validate SFT data construction driven by cognitive layering as an effective paradigm for complex engineering domains and provide a transferable framework for domain-specific LLM adaptation.

