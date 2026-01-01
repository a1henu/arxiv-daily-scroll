---
layout: default
title: Bi-C2R: Bidirectional Continual Compatible Representation for Re-indexing Free Lifelong Person Re-identification
---

# Bi-C2R: Bidirectional Continual Compatible Representation for Re-indexing Free Lifelong Person Re-identification
**arXiv**：[2512.25000v1](https://arxiv.org/abs/2512.25000) · [PDF](https://arxiv.org/pdf/2512.25000.pdf)  
**作者**：Zhenyu Cui, Jiahuan Zhou, Yuxin Peng  

**一句话要点**：提出Bi-C2R框架以解决免重索引终身行人重识别中的特征兼容性问题

**关键词**：终身行人重识别, 特征兼容性, 免重索引, 连续学习, 行人检索

## 3 点简述
- 核心问题：终身行人重识别中，模型更新导致新旧特征不兼容，需避免重索引历史图库
- 方法要点：设计双向连续兼容表示框架，持续更新旧模型提取的图库特征以实现兼容检索
- 实验或效果：理论分析和多基准实验验证，在RFL-ReID和传统L-ReID任务上取得领先性能

## 摘要（原文）

> Lifelong person Re-IDentification (L-ReID) exploits sequentially collected data to continuously train and update a ReID model, focusing on the overall performance of all data. Its main challenge is to avoid the catastrophic forgetting problem of old knowledge while training on new data. Existing L-ReID methods typically re-extract new features for all historical gallery images for inference after each update, known as "re-indexing". However, historical gallery data typically suffers from direct saving due to the data privacy issue and the high re-indexing costs for large-scale gallery images. As a result, it inevitably leads to incompatible retrieval between query features extracted by the updated model and gallery features extracted by those before the update, greatly impairing the re-identification performance. To tackle the above issue, this paper focuses on a new task called Re-index Free Lifelong person Re-IDentification (RFL-ReID), which requires performing lifelong person re-identification without re-indexing historical gallery images. Therefore, RFL-ReID is more challenging than L-ReID, requiring continuous learning and balancing new and old knowledge in diverse streaming data, and making the features output by the new and old models compatible with each other. To this end, we propose a Bidirectional Continuous Compatible Representation (Bi-C2R) framework to continuously update the gallery features extracted by the old model to perform efficient L-ReID in a compatible manner. We verify our proposed Bi-C2R method through theoretical analysis and extensive experiments on multiple benchmarks, which demonstrate that the proposed method can achieve leading performance on both the introduced RFL-ReID task and the traditional L-ReID task.

