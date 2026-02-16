---
layout: default
title: Training-Free Acceleration for Document Parsing Vision-Language Model with Hierarchical Speculative Decoding
---

# Training-Free Acceleration for Document Parsing Vision-Language Model with Hierarchical Speculative Decoding
**arXiv**：[2602.12957v1](https://arxiv.org/abs/2602.12957) · [PDF](https://arxiv.org/pdf/2602.12957.pdf)  
**作者**：Wenhui Liao, Hongliang Li, Pengyu Xie, Xinyu Cai, Yufan Shen, Yi Xin, Qi Qin, Shenglong Ye, Tianbin Li, Ming Hu, Junjun He, Yihao Liu, Wenhai Wang, Min Dou, Bin Fu, Botian Shi, Yu Qiao, Lianwen Jin  

**一句话要点**：提出基于分层推测解码的无训练加速方法，以提升文档解析视觉语言模型的推理效率。

**关键词**：文档解析, 视觉语言模型, 推测解码, 无训练加速, 并行推理, 布局结构

## 3 点简述
- 核心问题：基于VLM的文档解析模型因自回归生成长序列导致推理延迟高。
- 方法要点：使用轻量级草稿模型预测未来令牌，并由VLM并行验证，结合文档布局分区实现并行解码。
- 实验或效果：在OmniDocBench上实现2.42倍无损加速，长文档任务加速比最高达4.89倍。

## 摘要（原文）

> Document parsing is a fundamental task in multimodal understanding, supporting a wide range of downstream applications such as information extraction and intelligent document analysis. Benefiting from strong semantic modeling and robust generalization, VLM-based end-to-end approaches have emerged as the mainstream paradigm in recent years. However, these models often suffer from substantial inference latency, as they must auto-regressively generate long token sequences when processing long-form documents. In this work, motivated by the extremely long outputs and complex layout structures commonly found in document parsing, we propose a training-free and highly efficient acceleration method. Inspired by speculative decoding, we employ a lightweight document parsing pipeline as a draft model to predict batches of future tokens, while the more accurate VLM verifies these draft predictions in parallel. Moreover, we further exploit the layout-structured nature of documents by partitioning each page into independent regions, enabling parallel decoding of each region using the same draft-verify strategy. The final predictions are then assembled according to the natural reading order. Experimental results demonstrate the effectiveness of our approach: on the general-purpose OmniDocBench, our method provides a 2.42x lossless acceleration for the dots.ocr model, and achieves up to 4.89x acceleration on long-document parsing tasks. We will release our code to facilitate reproducibility and future research.

