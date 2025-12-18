---
layout: default
title: An Efficient and Effective Encoder Model for Vision and Language Tasks in the Remote Sensing Domain
---

# An Efficient and Effective Encoder Model for Vision and Language Tasks in the Remote Sensing Domain
**arXiv**：[2512.15531v1](https://arxiv.org/abs/2512.15531) · [PDF](https://arxiv.org/pdf/2512.15531.pdf)  
**作者**：João Daniel Silva, Joao Magalhaes, Devis Tuia, Bruno Martins  

**一句话要点**：提出GeoMELT模型，以编码器架构高效解决遥感领域多任务学习问题。

**关键词**：遥感视觉语言模型, 多任务学习, 编码器架构, 跨模态检索, 图像生成文本

## 3 点简述
- 核心问题：大型视觉语言模型在遥感任务中参数多、计算成本高，限制广泛应用。
- 方法要点：采用编码器架构，设计紧凑模型，统一处理图像生成文本和跨模态检索任务。
- 实验或效果：在基准测试中验证了模型的有效性和效率，参数少且性能佳。

## 摘要（原文）

> The remote sensing community has recently seen the emergence of methods based on Large Vision and Language Models (LVLMs) that can address multiple tasks at the intersection of computer vision and natural language processing. To fully exploit the potential of such models, a significant focus has been given to the collection of large amounts of training data that cover multiple remote sensing-specific tasks, such as image captioning or visual question answering. However, the cost of using and training LVLMs is high, due to the large number of parameters. While multiple parameter-efficient adaptation techniques have been explored, the computational costs of training and inference with these models can remain prohibitive for most institutions. In this work, we explore the use of encoder-only architectures and propose a model that can effectively address multi-task learning while remaining compact in terms of the number of parameters. In particular, our model tackles combinations of tasks that are not typically explored in a unified model: the generation of text from remote sensing images and cross-modal retrieval. The results of our GeoMELT model - named from Multi-task Efficient Learning Transformer - in established benchmarks confirm the efficacy and efficiency of the proposed approach.

