---
layout: default
title: Memory-guided Prototypical Co-occurrence Learning for Mixed Emotion Recognition
---

# Memory-guided Prototypical Co-occurrence Learning for Mixed Emotion Recognition
**arXiv**：[2602.20530v1](https://arxiv.org/abs/2602.20530) · [PDF](https://arxiv.org/pdf/2602.20530.pdf)  
**作者**：Ming Li, Yong-Jin Liu, Fang Liu, Huankun Sheng, Yeying Fan, Yixiang Wei, Minnan Luo, Weizhan Zhang, Wenping Wang  

**一句话要点**：提出MPCL框架以解决混合情感识别中情感共现模式建模不足的问题

**关键词**：混合情感识别, 多模态融合, 原型学习, 记忆机制, 情感分布预测, 共现模式建模

## 3 点简述
- 核心问题：现有模型忽略混合情感中的效价一致性和结构化相关性，难以处理真实世界多情感共存场景。
- 方法要点：通过多尺度关联记忆融合多模态信号，构建情感原型记忆库和原型关系蒸馏，引入记忆检索策略提取语义级共现关联。
- 实验或效果：在两个公开数据集上，MPCL在定量和定性评估中均优于现有方法，验证了其有效性。

## 摘要（原文）

> Emotion recognition from multi-modal physiological and behavioral signals plays a pivotal role in affective computing, yet most existing models remain constrained to the prediction of singular emotions in controlled laboratory settings. Real-world human emotional experiences, by contrast, are often characterized by the simultaneous presence of multiple affective states, spurring recent interest in mixed emotion recognition as an emotion distribution learning problem. Current approaches, however, often neglect the valence consistency and structured correlations inherent among coexisting emotions. To address this limitation, we propose a Memory-guided Prototypical Co-occurrence Learning (MPCL) framework that explicitly models emotion co-occurrence patterns. Specifically, we first fuse multi-modal signals via a multi-scale associative memory mechanism. To capture cross-modal semantic relationships, we construct emotion-specific prototype memory banks, yielding rich physiological and behavioral representations, and employ prototype relation distillation to ensure cross-modal alignment in the latent prototype space. Furthermore, inspired by human cognitive memory systems, we introduce a memory retrieval strategy to extract semantic-level co-occurrence associations across emotion categories. Through this bottom-up hierarchical abstraction process, our model learns affectively informative representations for accurate emotion distribution prediction. Comprehensive experiments on two public datasets demonstrate that MPCL consistently outperforms state-of-the-art methods in mixed emotion recognition, both quantitatively and qualitatively.

