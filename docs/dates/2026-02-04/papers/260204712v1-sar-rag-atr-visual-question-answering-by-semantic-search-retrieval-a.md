---
layout: default
title: SAR-RAG: ATR Visual Question Answering by Semantic Search, Retrieval, and MLLM Generation
---

# SAR-RAG: ATR Visual Question Answering by Semantic Search, Retrieval, and MLLM Generation
**arXiv**：[2602.04712v1](https://arxiv.org/abs/2602.04712) · [PDF](https://arxiv.org/pdf/2602.04712.pdf)  
**作者**：David F. Ramirez, Tim Overman, Kristen Jaskie, Joe Marvin, Andreas Spanias  

**一句话要点**：提出SAR-RAG方法，结合语义检索与多模态大语言模型，提升合成孔径雷达图像的目标识别精度。

**关键词**：合成孔径雷达目标识别, 检索增强生成, 多模态大语言模型, 语义搜索, 向量数据库, 图像检索

## 3 点简述
- 核心问题：合成孔径雷达图像中军事车辆目标识别困难，需区分相似类别。
- 方法要点：利用向量数据库存储语义嵌入，通过检索增强生成，结合多模态大语言模型进行上下文搜索。
- 实验或效果：在搜索检索指标、分类准确率和车辆尺寸回归上均优于基线方法，提升预测准确性。

## 摘要（原文）

> We present a visual-context image retrieval-augmented generation (ImageRAG) assisted AI agent for automatic target recognition (ATR) of synthetic aperture radar (SAR). SAR is a remote sensing method used in defense and security applications to detect and monitor the positions of military vehicles, which may appear indistinguishable in images. Researchers have extensively studied SAR ATR to improve the differentiation and identification of vehicle types, characteristics, and measurements. Test examples can be compared with known vehicle target types to improve recognition tasks. New methods enhance the capabilities of neural networks, transformer attention, and multimodal large language models. An agentic AI method may be developed to utilize a defined set of tools, such as searching through a library of similar examples. Our proposed method, SAR Retrieval-Augmented Generation (SAR-RAG), combines a multimodal large language model (MLLM) with a vector database of semantic embeddings to support contextual search for image exemplars with known qualities. By recovering past image examples with known true target types, our SAR-RAG system can compare similar vehicle categories, achieving improved ATR prediction accuracy. We evaluate this through search and retrieval metrics, categorical classification accuracy, and numeric regression of vehicle dimensions. These metrics all show improvements when SAR-RAG is added to an MLLM baseline method as an attached ATR memory bank.

