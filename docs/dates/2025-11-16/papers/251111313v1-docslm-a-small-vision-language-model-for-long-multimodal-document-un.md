---
layout: default
title: DocSLM: A Small Vision-Language Model for Long Multimodal Document Understanding
---

# DocSLM: A Small Vision-Language Model for Long Multimodal Document Understanding
**arXiv**：[2511.11313v1](https://arxiv.org/abs/2511.11313) · [PDF](https://arxiv.org/pdf/2511.11313.pdf)  
**作者**：Tanveer Hannan, Dimitrios Mallios, Parth Pathak, Faegheh Sardari, Thomas Seidl, Gedas Bertasius, Mohsen Fayyaz, Sunando Sengupta  

**一句话要点**：提出DocSLM小视觉语言模型以解决资源受限设备上的长多模态文档理解问题

**关键词**：小视觉语言模型, 长文档理解, 多模态压缩, 边缘设备部署, 流式处理, 不确定性校准

## 3 点简述
- 核心问题：大型视觉语言模型内存占用高，难以部署于资源受限边缘设备
- 方法要点：采用分层多模态压缩器和流式弃权机制，减少内存消耗并处理长输入
- 实验或效果：在多个基准测试中性能匹配或超越先进方法，显著降低视觉令牌、参数和延迟

## 摘要（原文）

> Large Vision-Language Models (LVLMs) have demonstrated strong multimodal reasoning capabilities on long and complex documents. However, their high memory footprint makes them impractical for deployment on resource-constrained edge devices. We present DocSLM, an efficient Small Vision-Language Model designed for long-document understanding under constrained memory resources. DocSLM incorporates a Hierarchical Multimodal Compressor that jointly encodes visual, textual, and layout information from each page into a fixed-length sequence, greatly reducing memory consumption while preserving both local and global semantics. To enable scalable processing over arbitrarily long inputs, we introduce a Streaming Abstention mechanism that operates on document segments sequentially and filters low-confidence responses using an entropy-based uncertainty calibrator. Across multiple long multimodal document benchmarks, DocSLM matches or surpasses state-of-the-art methods while using 82\% fewer visual tokens, 75\% fewer parameters, and 71\% lower latency, delivering reliable multimodal document understanding on lightweight edge devices. Code is available in the supplementary material.

