---
layout: default
title: Multimodal LLMs for Historical Dataset Construction from Archival Image Scans: German Patents (1877-1918)
---

# Multimodal LLMs for Historical Dataset Construction from Archival Image Scans: German Patents (1877-1918)
**arXiv**：[2512.19675v1](https://arxiv.org/abs/2512.19675) · [PDF](https://arxiv.org/pdf/2512.19675.pdf)  
**作者**：Niclas Griesshaber, Jochen Streb  

**一句话要点**：利用多模态大语言模型从档案图像扫描构建德国专利历史数据集（1877-1918）

**关键词**：多模态大语言模型, 历史数据集构建, 档案图像处理, 专利数据提取, 经济史研究, LLM管道

## 3 点简述
- 核心问题：从复杂字体和布局的档案图像中高效构建高质量历史数据集。
- 方法要点：基于Gemini-2.5-Pro和Gemini-2.5-Flash-Lite的多模态LLM管道处理图像扫描。
- 实验或效果：相比人工，数据集质量可能更高，速度提升795倍以上，成本降低205倍。

## 摘要（原文）

> We leverage multimodal large language models (LLMs) to construct a dataset of 306,070 German patents (1877-1918) from 9,562 archival image scans using our LLM-based pipeline powered by Gemini-2.5-Pro and Gemini-2.5-Flash-Lite. Our benchmarking exercise provides tentative evidence that multimodal LLMs can create higher quality datasets than our research assistants, while also being more than 795 times faster and 205 times cheaper in constructing the patent dataset from our image corpus. About 20 to 50 patent entries are embedded on each page, arranged in a double-column format and printed in Gothic and Roman fonts. The font and layout complexity of our primary source material suggests to us that multimodal LLMs are a paradigm shift in how datasets are constructed in economic history. We open-source our benchmarking and patent datasets as well as our LLM-based data pipeline, which can be easily adapted to other image corpora using LLM-assisted coding tools, lowering the barriers for less technical researchers. Finally, we explain the economics of deploying LLMs for historical dataset construction and conclude by speculating on the potential implications for the field of economic history.

