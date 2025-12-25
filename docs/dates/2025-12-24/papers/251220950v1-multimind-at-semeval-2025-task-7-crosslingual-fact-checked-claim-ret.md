---
layout: default
title: MultiMind at SemEval-2025 Task 7: Crosslingual Fact-Checked Claim Retrieval via Multi-Source Alignment
---

# MultiMind at SemEval-2025 Task 7: Crosslingual Fact-Checked Claim Retrieval via Multi-Source Alignment
**arXiv**：[2512.20950v1](https://arxiv.org/abs/2512.20950) · [PDF](https://arxiv.org/pdf/2512.20950.pdf)  
**作者**：Mohammad Mahdi Abootorabi, Alireza Ghahramani Kure, Mohammadali Mohammadkhani, Sina Elahimanesh, Mohammad Ali Ali Panah  

**一句话要点**：提出TriAligner方法，通过多源对齐解决跨语言事实核查声明检索问题。

**关键词**：跨语言事实核查, 声明检索, 双编码器架构, 对比学习, 多源对齐, 数据增强

## 3 点简述
- 核心问题：在虚假信息快速传播时代，跨语言事实核查声明检索的准确性和效率至关重要。
- 方法要点：采用双编码器架构结合对比学习，整合多模态原生和翻译文本，通过多源对齐学习不同来源的相对重要性。
- 实验或效果：在单语和跨语言基准测试中，检索准确性和事实核查性能显著优于基线方法。

## 摘要（原文）

> This paper presents our system for SemEval-2025 Task 7: Multilingual and Crosslingual Fact-Checked Claim Retrieval. In an era where misinformation spreads rapidly, effective fact-checking is increasingly critical. We introduce TriAligner, a novel approach that leverages a dual-encoder architecture with contrastive learning and incorporates both native and English translations across different modalities. Our method effectively retrieves claims across multiple languages by learning the relative importance of different sources in alignment. To enhance robustness, we employ efficient data preprocessing and augmentation using large language models while incorporating hard negative sampling to improve representation learning. We evaluate our approach on monolingual and crosslingual benchmarks, demonstrating significant improvements in retrieval accuracy and fact-checking performance over baselines.

