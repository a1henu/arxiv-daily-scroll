---
layout: default
title: Any Model, Any Place, Any Time: Get Remote Sensing Foundation Model Embeddings On Demand
---

# Any Model, Any Place, Any Time: Get Remote Sensing Foundation Model Embeddings On Demand
**arXiv**：[2602.23678v1](https://arxiv.org/abs/2602.23678) · [PDF](https://arxiv.org/pdf/2602.23678.pdf)  
**作者**：Dingqi Ye, Daniel Kiv, Wei Hu, Jimeng Shi, Shaowen Wang  

**一句话要点**：提出rs-embed库以统一遥感基础模型嵌入的获取与比较

**关键词**：遥感基础模型, 嵌入检索, 统一接口, 批处理, 开源库

## 3 点简述
- 核心问题：模型格式、平台和输入数据异质性阻碍遥感基础模型的实用与公平比较
- 方法要点：提供基于感兴趣区域的统一接口，单行代码支持任意模型、位置和时间范围的嵌入检索
- 实验或效果：提供高效批处理，支持大规模嵌入生成与评估，代码已开源

## 摘要（原文）

> The remote sensing community is witnessing a rapid growth of foundation models, which provide powerful embeddings for a wide range of downstream tasks. However, practical adoption and fair comparison remain challenging due to substantial heterogeneity in model release formats, platforms and interfaces, and input data specifications. These inconsistencies significantly increase the cost of obtaining, using, and benchmarking embeddings across models. To address this issue, we propose rs-embed, a Python library that offers a unified, region of interst (ROI) centric interface: with a single line of code, users can retrieve embeddings from any supported model for any location and any time range. The library also provides efficient batch processing to enable large-scale embedding generation and evaluation. The code is available at: https://github.com/cybergis/rs-embed

