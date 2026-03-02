---
layout: default
title: AgenticOCR: Parsing Only What You Need for Efficient Retrieval-Augmented Generation
---

# AgenticOCR: Parsing Only What You Need for Efficient Retrieval-Augmented Generation
**arXiv**：[2602.24134v1](https://arxiv.org/abs/2602.24134) · [PDF](https://arxiv.org/pdf/2602.24134.pdf)  
**作者**：Zhengren Wang, Dongsheng Ma, Huaping Zhong, Jiayu Li, Wentao Zhang, Bin Wang, Conghui He  

**一句话要点**：提出AgenticOCR，通过查询驱动的动态解析解决视觉文档RAG中页面级检索的上下文过载问题。

**关键词**：检索增强生成, 视觉文档解析, 动态OCR, 长文档理解, 查询驱动提取

## 3 点简述
- 核心问题：页面级检索引入过多无关上下文，导致生成器注意力过载和证据稀释。
- 方法要点：将OCR从静态全文本处理转变为查询驱动的按需提取，动态识别和解析感兴趣区域。
- 实验或效果：提升视觉RAG系统的效率和准确性，在长文档理解中达到专家级性能。

## 摘要（原文）

> The expansion of retrieval-augmented generation (RAG) into multimodal domains has intensified the challenge for processing complex visual documents, such as financial reports. While page-level chunking and retrieval is a natural starting point, it creates a critical bottleneck: delivering entire pages to the generator introduces excessive extraneous context. This not only overloads the generator's attention mechanism but also dilutes the most salient evidence. Moreover, compressing these information-rich pages into a limited visual token budget further increases the risk of hallucinations. To address this, we introduce AgenticOCR, a dynamic parsing paradigm that transforms optical character recognition (OCR) from a static, full-text process into a query-driven, on-demand extraction system. By autonomously analyzing document layout in a "thinking with images" manner, AgenticOCR identifies and selectively recognizes regions of interest. This approach performs on-demand decompression of visual tokens precisely where needed, effectively decoupling retrieval granularity from rigid page-level chunking. AgenticOCR has the potential to serve as the "third building block" of the visual document RAG stack, operating alongside and enhancing standard Embedding and Reranking modules. Experimental results demonstrate that AgenticOCR improves both the efficiency and accuracy of visual RAG systems, achieving expert-level performance in long document understanding. Code and models are available at https://github.com/OpenDataLab/AgenticOCR.

