---
layout: default
title: WikiCLIP: An Efficient Contrastive Baseline for Open-domain Visual Entity Recognition
---

# WikiCLIP: An Efficient Contrastive Baseline for Open-domain Visual Entity Recognition
**arXiv**：[2603.09921v1](https://arxiv.org/abs/2603.09921) · [PDF](https://arxiv.org/pdf/2603.09921.pdf)  
**作者**：Shan Ning, Longtian Qiu, Jiaxuan Sun, Xuming He  

**一句话要点**：提出WikiCLIP对比学习框架以解决开放域视觉实体识别中生成方法计算成本高的问题

**关键词**：开放域视觉实体识别, 对比学习, 视觉引导知识适配器, 硬负样本合成, 大语言模型嵌入, 计算效率优化

## 3 点简述
- 核心问题：开放域视觉实体识别中生成方法计算成本高，限制可扩展性和实际部署
- 方法要点：利用大语言模型嵌入作为实体表示，通过视觉引导知识适配器对齐文本语义与视觉线索
- 实验或效果：在OVEN基准上显著超越基线，推理延迟降低近100倍，未见集性能提升16%

## 摘要（原文）

> Open-domain visual entity recognition (VER) seeks to associate images with entities in encyclopedic knowledge bases such as Wikipedia. Recent generative methods tailored for VER demonstrate strong performance but incur high computational costs, limiting their scalability and practical deployment. In this work, we revisit the contrastive paradigm for VER and introduce WikiCLIP, a simple yet effective framework that establishes a strong and efficient baseline for open-domain VER. WikiCLIP leverages large language model embeddings as knowledge-rich entity representations and enhances them with a Vision-Guided Knowledge Adaptor (VGKA) that aligns textual semantics with visual cues at the patch level. To further encourage fine-grained discrimination, a Hard Negative Synthesis Mechanism generates visually similar but semantically distinct negatives during training. Experimental results on popular open-domain VER benchmarks, such as OVEN, demonstrate that WikiCLIP significantly outperforms strong baselines. Specifically, WikiCLIP achieves a 16% improvement on the challenging OVEN unseen set, while reducing inference latency by nearly 100 times compared with the leading generative model, AutoVER. The project page is available at https://artanic30.github.io/project_pages/WikiCLIP/

