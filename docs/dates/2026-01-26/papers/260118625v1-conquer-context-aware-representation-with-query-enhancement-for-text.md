---
layout: default
title: CONQUER: Context-Aware Representation with Query Enhancement for Text-Based Person Search
---

# CONQUER: Context-Aware Representation with Query Enhancement for Text-Based Person Search
**arXiv**：[2601.18625v1](https://arxiv.org/abs/2601.18625) · [PDF](https://arxiv.org/pdf/2601.18625.pdf)  
**作者**：Zequn Xie  

**一句话要点**：提出CONQUER框架，通过上下文感知表示与查询增强解决基于文本的行人搜索问题。

**关键词**：基于文本的行人搜索, 跨模态对齐, 查询增强, 最优传输, 上下文感知表示

## 3 点简述
- 核心问题：基于文本的行人搜索面临跨模态差异和模糊查询的挑战。
- 方法要点：采用两阶段框架，训练时通过多粒度编码和最优传输学习鲁棒嵌入，推理时通过即插即用模块增强查询。
- 实验或效果：在多个数据集上优于基线，在跨域和不完整查询场景中表现突出。

## 摘要（原文）

> Text-Based Person Search (TBPS) aims to retrieve pedestrian images from large galleries using natural language descriptions. This task, essential for public safety applications, is hindered by cross-modal discrepancies and ambiguous user queries. We introduce CONQUER, a two-stage framework designed to address these challenges by enhancing cross-modal alignment during training and adaptively refining queries at inference. During training, CONQUER employs multi-granularity encoding, complementary pair mining, and context-guided optimal matching based on Optimal Transport to learn robust embeddings. At inference, a plug-and-play query enhancement module refines vague or incomplete queries via anchor selection and attribute-driven enrichment, without requiring retraining of the backbone. Extensive experiments on CUHK-PEDES, ICFG-PEDES, and RSTPReid demonstrate that CONQUER consistently outperforms strong baselines in both Rank-1 accuracy and mAP, yielding notable improvements in cross-domain and incomplete-query scenarios. These results highlight CONQUER as a practical and effective solution for real-world TBPS deployment. Source code is available at https://github.com/zqxie77/CONQUER.

