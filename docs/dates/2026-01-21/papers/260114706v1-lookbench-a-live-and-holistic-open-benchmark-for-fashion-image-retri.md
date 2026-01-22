---
layout: default
title: LookBench: A Live and Holistic Open Benchmark for Fashion Image Retrieval
---

# LookBench: A Live and Holistic Open Benchmark for Fashion Image Retrieval
**arXiv**：[2601.14706v1](https://arxiv.org/abs/2601.14706) · [PDF](https://arxiv.org/pdf/2601.14706.pdf)  
**作者**：Chao Gao, Siqiao Xue, Yimin Peng, Jiwen Fu, Tingyi Gu, Shanshan Li, Fan Zhou  

**一句话要点**：提出LookBench实时基准，用于电商环境下的时尚图像检索评估。

**关键词**：时尚图像检索, 实时基准, 电商应用, 细粒度属性, AI生成图像, 性能评估

## 3 点简述
- 核心问题：现有基准难以反映实时电商趋势和多样化检索需求。
- 方法要点：结合实时产品图像和AI生成图像，基于细粒度属性分类构建测试集。
- 实验或效果：基准挑战性强，多数模型Recall@1低于60%，并计划半年度更新。

## 摘要（原文）

> In this paper, we present LookBench (We use the term "look" to reflect retrieval that mirrors how people shop -- finding the exact item, a close substitute, or a visually consistent alternative.), a live, holistic and challenging benchmark for fashion image retrieval in real e-commerce settings. LookBench includes both recent product images sourced from live websites and AI-generated fashion images, reflecting contemporary trends and use cases. Each test sample is time-stamped and we intend to update the benchmark periodically, enabling contamination-aware evaluation aligned with declared training cutoffs. Grounded in our fine-grained attribute taxonomy, LookBench covers single-item and outfit-level retrieval across. Our experiments reveal that LookBench poses a significant challenge on strong baselines, with many models achieving below $60\%$ Recall@1. Our proprietary model achieves the best performance on LookBench, and we release an open-source counterpart that ranks second, with both models attaining state-of-the-art results on legacy Fashion200K evaluations. LookBench is designed to be updated semi-annually with new test samples and progressively harder task variants, providing a durable measure of progress. We publicly release our leaderboard, dataset, evaluation code, and trained models.

