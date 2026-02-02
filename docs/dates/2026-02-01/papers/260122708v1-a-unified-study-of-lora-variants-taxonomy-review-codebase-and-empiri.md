---
layout: default
title: A Unified Study of LoRA Variants: Taxonomy, Review, Codebase, and Empirical Evaluation
---

# A Unified Study of LoRA Variants: Taxonomy, Review, Codebase, and Empirical Evaluation
**arXiv**：[2601.22708v1](https://arxiv.org/abs/2601.22708) · [PDF](https://arxiv.org/pdf/2601.22708.pdf)  
**作者**：Haonan He, Jingqi Ye, Minglei Li, Zhengbo Wang, Tao Chen, Lei Bai, Peng Ye  

**一句话要点**：提出统一研究框架以整合LoRA变体，涵盖分类、理论、代码和评估。

**关键词**：低秩适应, 参数高效微调, LoRA变体, 统一框架, 模块化代码库, 超参数评估

## 3 点简述
- LoRA变体方法、理论、代码和评估碎片化问题突出。
- 建立四轴分类、统一理论框架和模块化代码库LoRAFactory。
- 大规模实验显示LoRA对学习率敏感，适当配置下性能优于多数变体。

## 摘要（原文）

> Low-Rank Adaptation (LoRA) is a fundamental parameter-efficient fine-tuning method that balances efficiency and performance in large-scale neural networks. However, the proliferation of LoRA variants has led to fragmentation in methodology, theory, code, and evaluation. To this end, this work presents the first unified study of LoRA variants, offering a systematic taxonomy, unified theoretical review, structured codebase, and standardized empirical assessment. First, we categorize LoRA variants along four principal axes: rank, optimization dynamics, initialization, and integration with Mixture-of-Experts. Then, we review their relationships and evolution within a common theoretical framework focused on low-rank update dynamics. Further, we introduce LoRAFactory, a modular codebase that implements variants through a unified interface, supporting plug-and-play experimentation and fine-grained analysis. Last, using this codebase, we conduct a large-scale evaluation across natural language generation, natural language understanding, and image classification tasks, systematically exploring key hyperparameters. Our results uncover several findings, notably: LoRA and its variants exhibit pronounced sensitivity to the choices of learning rate compared to other hyperparameters; moreover, with proper hyperparameter configurations, LoRA consistently matches or surpasses the performance of most of its variants.

