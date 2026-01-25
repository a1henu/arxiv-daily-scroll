---
layout: default
title: Rethinking Composed Image Retrieval Evaluation: A Fine-Grained Benchmark from Image Editing
---

# Rethinking Composed Image Retrieval Evaluation: A Fine-Grained Benchmark from Image Editing
**arXiv**：[2601.16125v1](https://arxiv.org/abs/2601.16125) · [PDF](https://arxiv.org/pdf/2601.16125.pdf)  
**作者**：Tingyu Song, Yanzhao Zhang, Mingxin Li, Zhuoning Guo, Dingkun Long, Pengjun Xie, Siyue Zhang, Yilun Zhao, Shu Wu  

**一句话要点**：提出EDIR细粒度基准以解决组合图像检索评估不足的问题

**关键词**：组合图像检索, 细粒度基准, 图像编辑, 多模态嵌入, 评估方法

## 3 点简述
- 当前组合图像检索基准类别有限，无法反映真实场景多样性
- 利用图像编辑控制修改类型和内容，构建涵盖5,000查询的EDIR基准
- 评估13个模型显示能力差距，实验揭示现有基准的模态偏见和类别覆盖不足

## 摘要（原文）

> Composed Image Retrieval (CIR) is a pivotal and complex task in multimodal understanding. Current CIR benchmarks typically feature limited query categories and fail to capture the diverse requirements of real-world scenarios. To bridge this evaluation gap, we leverage image editing to achieve precise control over modification types and content, enabling a pipeline for synthesizing queries across a broad spectrum of categories. Using this pipeline, we construct EDIR, a novel fine-grained CIR benchmark. EDIR encompasses 5,000 high-quality queries structured across five main categories and fifteen subcategories. Our comprehensive evaluation of 13 multimodal embedding models reveals a significant capability gap; even state-of-the-art models (e.g., RzenEmbed and GME) struggle to perform consistently across all subcategories, highlighting the rigorous nature of our benchmark. Through comparative analysis, we further uncover inherent limitations in existing benchmarks, such as modality biases and insufficient categorical coverage. Furthermore, an in-domain training experiment demonstrates the feasibility of our benchmark. This experiment clarifies the task challenges by distinguishing between categories that are solvable with targeted data and those that expose intrinsic limitations of current model architectures.

