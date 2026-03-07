---
layout: default
title: A Simple Baseline for Unifying Understanding, Generation, and Editing via Vanilla Next-token Prediction
---

# A Simple Baseline for Unifying Understanding, Generation, and Editing via Vanilla Next-token Prediction
**arXiv**：[2603.04980v1](https://arxiv.org/abs/2603.04980) · [PDF](https://arxiv.org/pdf/2603.04980.pdf)  
**作者**：Jie Zhu, Hanghang Ma, Jia Wang, Yayong Guan, Yanbing Zeng, Lishuai Gao, Junqiang Wu, Jie Hu, Leye Wang  

**一句话要点**：提出Wallaroo，基于自回归模型统一多模态理解、图像生成与编辑。

**关键词**：自回归模型, 多模态统一, 图像生成, 图像编辑, 多分辨率支持, 双语支持

## 3 点简述
- 核心问题：多模态任务统一模型复杂，需简化架构以提升效率。
- 方法要点：采用自回归模型，通过四阶段训练策略解耦视觉编码路径。
- 实验或效果：在多个基准测试中表现竞争性或超越其他统一模型。

## 摘要（原文）

> In this work, we introduce Wallaroo, a simple autoregressive baseline that leverages next-token prediction to unify multi-modal understanding, image generation, and editing at the same time. Moreover, Wallaroo supports multi-resolution image input and output, as well as bilingual support for both Chinese and English. We decouple the visual encoding into separate pathways and apply a four-stage training strategy to reshape the model's capabilities. Experiments are conducted on various benchmarks where Wallaroo produces competitive performance or exceeds other unified models, suggesting the great potential of autoregressive models in unifying multi-modality understanding and generation. Our code is available at https://github.com/JiePKU/Wallaroo.

