---
layout: default
title: SpatialGeo:Boosting Spatial Reasoning in Multimodal LLMs via Geometry-Semantics Fusion
---

# SpatialGeo:Boosting Spatial Reasoning in Multimodal LLMs via Geometry-Semantics Fusion
**arXiv**：[2511.17308v1](https://arxiv.org/abs/2511.17308) · [PDF](https://arxiv.org/pdf/2511.17308.pdf)  
**作者**：Jiajie Guo, Qingpeng Zhu, Jin Zeng, Xiaolong Wu, Changyong He, Weida Wang  

**一句话要点**：提出SpatialGeo通过几何-语义融合增强多模态大语言模型的空间推理能力

**关键词**：多模态大语言模型, 空间推理, 几何-语义融合, 视觉编码器, 分层适配器, 内存优化

## 3 点简述
- 核心问题：现有MLLMs空间推理能力弱，源于视觉编码器嵌入损失和空间模糊性。
- 方法要点：基于CLIP补充几何特征，使用分层适配器融合几何与语义特征。
- 实验或效果：在SpatialRGPT-Bench上准确率提升至少8.0%，推理内存成本降低约50%。

## 摘要（原文）

> Multimodal large language models (MLLMs) have achieved significant progress in image and language tasks due to the strong reasoning capability of large language models (LLMs). Nevertheless, most MLLMs suffer from limited spatial reasoning ability to interpret and infer spatial arrangements in three-dimensional space. In this work, we propose a novel vision encoder based on hierarchical fusion of geometry and semantics features, generating spatial-aware visual embedding and boosting the spatial grounding capability of MLLMs. Specifically, we first unveil that the spatial ambiguity shortcoming stems from the lossy embedding of the vision encoder utilized in most existing MLLMs (e.g., CLIP), restricted to instance-level semantic features. This motivates us to complement CLIP with the geometry features from vision-only self-supervised learning via a hierarchical adapter, enhancing the spatial awareness in the proposed SpatialGeo. The network is efficiently trained using pretrained LLaVA model and optimized with random feature dropping to avoid trivial solutions relying solely on the CLIP encoder. Experimental results show that SpatialGeo improves the accuracy in spatial reasoning tasks, enhancing state-of-the-art models by at least 8.0% in SpatialRGPT-Bench with approximately 50% less memory cost during inference. The source code is available via https://ricky-plus.github.io/SpatialGeoPages/.

