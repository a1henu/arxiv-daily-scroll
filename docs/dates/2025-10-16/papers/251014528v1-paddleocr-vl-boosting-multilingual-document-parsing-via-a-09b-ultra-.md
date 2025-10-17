---
layout: default
title: PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model
---

# PaddleOCR-VL: Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model
**arXiv**：[2510.14528v1](https://arxiv.org/abs/2510.14528) · [PDF](https://arxiv.org/pdf/2510.14528.pdf)  
**作者**：Cheng Cui, Ting Sun, Suyin Liang, Tingquan Gao, Zelun Zhang, Jiaxuan Liu, Xueqing Wang, Changda Zhou, Hongen Liu, Manhui Lin, Yue Zhang, Yubo Zhang, Handong Zheng, Jing Zhang, Jun Zhang, Yi Liu, Dianhai Yu, Yanjun Ma  

**一句话要点**：提出PaddleOCR-VL以提升多语言文档解析效率与准确性

**关键词**：文档解析, 视觉语言模型, 多语言支持, 资源效率, 元素识别

## 3 点简述
- 核心问题：多语言文档中复杂元素（如文本、表格、公式）的准确识别与解析。
- 方法要点：集成动态分辨率视觉编码器与语言模型，构建0.9B超紧凑视觉语言模型。
- 实验或效果：在公共与内部基准测试中实现SOTA性能，支持109种语言，推理速度快。

## 摘要（原文）

> In this report, we propose PaddleOCR-VL, a SOTA and resource-efficient model
> tailored for document parsing. Its core component is PaddleOCR-VL-0.9B, a
> compact yet powerful vision-language model (VLM) that integrates a NaViT-style
> dynamic resolution visual encoder with the ERNIE-4.5-0.3B language model to
> enable accurate element recognition. This innovative model efficiently supports
> 109 languages and excels in recognizing complex elements (e.g., text, tables,
> formulas, and charts), while maintaining minimal resource consumption. Through
> comprehensive evaluations on widely used public benchmarks and in-house
> benchmarks, PaddleOCR-VL achieves SOTA performance in both page-level document
> parsing and element-level recognition. It significantly outperforms existing
> solutions, exhibits strong competitiveness against top-tier VLMs, and delivers
> fast inference speeds. These strengths make it highly suitable for practical
> deployment in real-world scenarios.

