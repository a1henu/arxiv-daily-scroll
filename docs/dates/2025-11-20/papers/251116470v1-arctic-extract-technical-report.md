---
layout: default
title: Arctic-Extract Technical Report
---

# Arctic-Extract Technical Report
**arXiv**：[2511.16470v1](https://arxiv.org/abs/2511.16470) · [PDF](https://arxiv.org/pdf/2511.16470.pdf)  
**作者**：Mateusz Chiliński, Julita Ołtusek, Wojciech Jaśkowski  

**一句话要点**：提出Arctic-Extract模型，用于从业务文档中提取结构化数据，并部署于资源受限硬件。

**关键词**：文档理解, 结构化数据提取, 资源受限部署, 业务文档处理, 长文档处理

## 3 点简述
- 核心问题：从扫描或数字业务文档中提取问答、实体和表格等结构化数据。
- 方法要点：采用先进训练协议，模型仅6.6 GiB，可在A10 GPU等资源受限设备部署。
- 实验或效果：评估显示强文档理解性能，单GPU可处理多达125页A4文档。

## 摘要（原文）

> Arctic-Extract is a state-of-the-art model designed for extracting structural data (question answering, entities and tables) from scanned or digital-born business documents. Despite its SoTA capabilities, the model is deployable on resource-constrained hardware, weighting only 6.6 GiB, making it suitable for deployment on devices with limited resources, such as A10 GPUs with 24 GB of memory. Arctic-Extract can process up to 125 A4 pages on those GPUs, making suitable for long document processing. This paper highlights Arctic-Extract's training protocols and evaluation results, demonstrating its strong performance in document understanding.

