---
layout: default
title: ObjEmbed: Towards Universal Multimodal Object Embeddings
---

# ObjEmbed: Towards Universal Multimodal Object Embeddings
**arXiv**：[2602.01753v1](https://arxiv.org/abs/2602.01753) · [PDF](https://arxiv.org/pdf/2602.01753.pdf)  
**作者**：Shenghao Fu, Yukun Su, Fengyun Rao, Jing Lyu, Xiaohua Xie, Wei-Shi Zheng  

**一句话要点**：提出ObjEmbed模型，通过分解图像为区域嵌入以解决细粒度视觉-语言对齐问题。

**关键词**：多模态对象嵌入, 视觉-语言对齐, 细粒度检索, 区域级任务, 高效编码

## 3 点简述
- 核心问题：现有模型在图像区域与文本短语的细粒度对齐上表现不佳。
- 方法要点：生成对象嵌入和IoU嵌入，结合语义相似性与定位质量进行匹配。
- 实验或效果：在18个基准测试中表现优异，支持多种视觉理解任务。

## 摘要（原文）

> Aligning objects with corresponding textual descriptions is a fundamental challenge and a realistic requirement in vision-language understanding. While recent multimodal embedding models excel at global image-text alignment, they often struggle with fine-grained alignment between image regions and specific phrases. In this work, we present ObjEmbed, a novel MLLM embedding model that decomposes the input image into multiple regional embeddings, each corresponding to an individual object, along with global embeddings. It supports a wide range of visual understanding tasks like visual grounding, local image retrieval, and global image retrieval. ObjEmbed enjoys three key properties: (1) Object-Oriented Representation: It captures both semantic and spatial aspects of objects by generating two complementary embeddings for each region: an object embedding for semantic matching and an IoU embedding that predicts localization quality. The final object matching score combines semantic similarity with the predicted IoU, enabling more accurate retrieval. (2) Versatility: It seamlessly handles both region-level and image-level tasks. (3) Efficient Encoding: All objects in an image, along with the full image, are encoded in a single forward pass for high efficiency. Superior performance on 18 diverse benchmarks demonstrates its strong semantic discrimination.

