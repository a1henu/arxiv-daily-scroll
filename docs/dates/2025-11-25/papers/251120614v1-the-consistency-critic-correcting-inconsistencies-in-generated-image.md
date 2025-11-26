---
layout: default
title: The Consistency Critic: Correcting Inconsistencies in Generated Images via Reference-Guided Attentive Alignment
---

# The Consistency Critic: Correcting Inconsistencies in Generated Images via Reference-Guided Attentive Alignment
**arXiv**：[2511.20614v1](https://arxiv.org/abs/2511.20614) · [PDF](https://arxiv.org/pdf/2511.20614.pdf)  
**作者**：Ziheng Ouyang, Yiren Song, Yaoli Liu, Shihao Zhu, Qibin Hou, Ming-Ming Cheng, Mike Zheng Shou  

**一句话要点**：提出ImageCritic以解决生成图像细节不一致问题

**关键词**：图像生成一致性, 参考引导编辑, 注意力对齐, 细节编码, 后处理修正

## 3 点简述
- 核心问题：生成图像在细粒度细节上存在不一致性，影响定制化生成质量
- 方法要点：通过参考图像引导的注意力对齐和细节编码进行后编辑修正
- 实验或效果：在多种定制生成场景中显著改善细节问题，优于现有方法

## 摘要（原文）

> Previous works have explored various customized generation tasks given a reference image, but they still face limitations in generating consistent fine-grained details. In this paper, our aim is to solve the inconsistency problem of generated images by applying a reference-guided post-editing approach and present our ImageCritic. We first construct a dataset of reference-degraded-target triplets obtained via VLM-based selection and explicit degradation, which effectively simulates the common inaccuracies or inconsistencies observed in existing generation models. Furthermore, building on a thorough examination of the model's attention mechanisms and intrinsic representations, we accordingly devise an attention alignment loss and a detail encoder to precisely rectify inconsistencies. ImageCritic can be integrated into an agent framework to automatically detect inconsistencies and correct them with multi-round and local editing in complex scenarios. Extensive experiments demonstrate that ImageCritic can effectively resolve detail-related issues in various customized generation scenarios, providing significant improvements over existing methods.

