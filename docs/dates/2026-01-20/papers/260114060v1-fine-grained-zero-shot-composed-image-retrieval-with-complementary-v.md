---
layout: default
title: Fine-Grained Zero-Shot Composed Image Retrieval with Complementary Visual-Semantic Integration
---

# Fine-Grained Zero-Shot Composed Image Retrieval with Complementary Visual-Semantic Integration
**arXiv**：[2601.14060v1](https://arxiv.org/abs/2601.14060) · [PDF](https://arxiv.org/pdf/2601.14060.pdf)  
**作者**：Yongcong Ye, Kai Zhang, Yanghai Zhang, Enhong Chen, Longfei Li, Jun Zhou  

**一句话要点**：提出CVSI方法，通过互补视觉-语义集成解决零样本组合图像检索中的细粒度变化捕获问题。

**关键词**：零样本组合图像检索, 视觉-语义集成, 细粒度检索, 互补信息提取, 伪令牌生成, 多模态查询

## 3 点简述
- 现有方法在零样本组合图像检索中难以有效整合视觉与语义信息，导致细粒度变化捕获不足。
- CVSI方法结合视觉信息提取、语义信息提取和互补信息检索三个组件，实现互补视觉-语义集成。
- 在CIRR、CIRCO和FashionIQ数据集上实验表明，CVSI显著优于现有先进方法。

## 摘要（原文）

> Zero-shot composed image retrieval (ZS-CIR) is a rapidly growing area with significant practical applications, allowing users to retrieve a target image by providing a reference image and a relative caption describing the desired modifications. Existing ZS-CIR methods often struggle to capture fine-grained changes and integrate visual and semantic information effectively. They primarily rely on either transforming the multimodal query into a single text using image-to-text models or employing large language models for target image description generation, approaches that often fail to capture complementary visual information and complete semantic context. To address these limitations, we propose a novel Fine-Grained Zero-Shot Composed Image Retrieval method with Complementary Visual-Semantic Integration (CVSI). Specifically, CVSI leverages three key components: (1) Visual Information Extraction, which not only extracts global image features but also uses a pre-trained mapping network to convert the image into a pseudo token, combining it with the modification text and the objects most likely to be added. (2) Semantic Information Extraction, which involves using a pre-trained captioning model to generate multiple captions for the reference image, followed by leveraging an LLM to generate the modified captions and the objects most likely to be added. (3) Complementary Information Retrieval, which integrates information extracted from both the query and database images to retrieve the target image, enabling the system to efficiently handle retrieval queries in a variety of situations. Extensive experiments on three public datasets (e.g., CIRR, CIRCO, and FashionIQ) demonstrate that CVSI significantly outperforms existing state-of-the-art methods. Our code is available at https://github.com/yyc6631/CVSI.

