---
layout: default
title: Dolphin-v2: Universal Document Parsing via Scalable Anchor Prompting
---

# Dolphin-v2: Universal Document Parsing via Scalable Anchor Prompting
**arXiv**：[2602.05384v1](https://arxiv.org/abs/2602.05384) · [PDF](https://arxiv.org/pdf/2602.05384.pdf)  
**作者**：Hao Feng, Wei Shi, Ke Zhang, Xiang Fei, Lei Liao, Dingkang Yang, Yongkun Du, Xuecheng Wu, Jingqun Tang, Yang Liu, Hong Chen, Can Huang  

**一句话要点**：提出Dolphin-v2通过可扩展锚点提示实现通用文档解析，以解决文档类型多样化和布局扭曲问题。

**关键词**：文档解析, 视觉语言模型, 布局分析, 锚点提示, 并行处理, 代码块识别

## 3 点简述
- 核心问题：文档解析领域模型碎片化，现有方法依赖轴对齐边界框，难以处理拍摄文档的几何扭曲。
- 方法要点：采用两阶段解析，第一阶段联合文档类型分类与布局分析，第二阶段根据类型进行整体或元素级并行解析。
- 实验或效果：在OmniDocBench上整体提升14.78分，拍摄文档错误减少91%，支持21类元素检测和代码块识别。

## 摘要（原文）

> Document parsing has garnered widespread attention as vision-language models (VLMs) advance OCR capabilities. However, the field remains fragmented across dozens of specialized models with varying strengths, forcing users to navigate complex model selection and limiting system scalability. Moreover, existing two-stage approaches depend on axis-aligned bounding boxes for layout detection, failing to handle distorted or photographed documents effectively. To this end, we present Dolphin-v2, a two-stage document image parsing model that substantially improves upon the original Dolphin. In the first stage, Dolphin-v2 jointly performs document type classification (digital-born versus photographed) alongside layout analysis. For digital-born documents, it conducts finer-grained element detection with reading order prediction. In the second stage, we employ a hybrid parsing strategy: photographed documents are parsed holistically as complete pages to handle geometric distortions, while digital-born documents undergo element-wise parallel parsing guided by the detected layout anchors, enabling efficient content extraction. Compared with the original Dolphin, Dolphin-v2 introduces several crucial enhancements: (1) robust parsing of photographed documents via holistic page-level understanding, (2) finer-grained element detection (21 categories) with semantic attribute extraction such as author information and document metadata, and (3) code block recognition with indentation preservation, which existing systems typically lack. Comprehensive evaluations are conducted on DocPTBench, OmniDocBench, and our self-constructed RealDoc-160 benchmark. The results demonstrate substantial improvements: +14.78 points overall on the challenging OmniDocBench and 91% error reduction on photographed documents, while maintaining efficient inference through parallel processing.

