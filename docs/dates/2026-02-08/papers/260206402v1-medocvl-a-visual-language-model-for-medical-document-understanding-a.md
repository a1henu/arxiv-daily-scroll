---
layout: default
title: MeDocVL: A Visual Language Model for Medical Document Understanding and Parsing
---

# MeDocVL: A Visual Language Model for Medical Document Understanding and Parsing
**arXiv**：[2602.06402v1](https://arxiv.org/abs/2602.06402) · [PDF](https://arxiv.org/pdf/2602.06402.pdf)  
**作者**：Wenjie Wang, Wei Wu, Ying Liu, Yuan Zhao, Xiaole Lv, Liang Diao, Zengjian Fan, Wenfeng Xie, Ziling Lin, De Shi, Lin Huang, Kaihe Xu, Hong Li  

**一句话要点**：提出MeDocVL视觉语言模型，通过训练驱动标签精炼和噪声感知混合后训练，解决医疗文档OCR在复杂布局和噪声标注下的解析难题。

**关键词**：医疗文档解析, 视觉语言模型, 噪声标注处理, 训练驱动标签精炼, 混合后训练策略, OCR增强

## 3 点简述
- 核心问题：医疗文档OCR面临复杂布局、专业术语和噪声标注挑战，需严格字段级精确匹配。
- 方法要点：结合训练驱动标签精炼构建高质量监督，采用噪声感知混合后训练策略，集成强化学习和监督微调。
- 实验或效果：在医疗发票基准测试中优于传统OCR系统和强VLM基线，在噪声监督下达到最先进性能。

## 摘要（原文）

> Medical document OCR is challenging due to complex layouts, domain-specific terminology, and noisy annotations, while requiring strict field-level exact matching. Existing OCR systems and general-purpose vision-language models often fail to reliably parse such documents. We propose MeDocVL, a post-trained vision-language model for query-driven medical document parsing. Our framework combines Training-driven Label Refinement to construct high-quality supervision from noisy annotations, with a Noise-aware Hybrid Post-training strategy that integrates reinforcement learning and supervised fine-tuning to achieve robust and precise extraction. Experiments on medical invoice benchmarks show that MeDocVL consistently outperforms conventional OCR systems and strong VLM baselines, achieving state-of-the-art performance under noisy supervision.

