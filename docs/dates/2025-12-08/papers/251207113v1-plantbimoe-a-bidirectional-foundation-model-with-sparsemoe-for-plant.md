---
layout: default
title: PlantBiMoE: A Bidirectional Foundation Model with SparseMoE for Plant Genomes
---

# PlantBiMoE: A Bidirectional Foundation Model with SparseMoE for Plant Genomes
**arXiv**：[2512.07113v1](https://arxiv.org/abs/2512.07113) · [PDF](https://arxiv.org/pdf/2512.07113.pdf)  
**作者**：Kepeng Lin, Qizhe Zhang, Rui Wang, Xuehai Hu, Wei Xu  

**一句话要点**：提出PlantBiMoE，结合双向Mamba与稀疏专家混合，以轻量高效建模植物基因组双向依赖性。

**关键词**：植物基因组语言模型, 双向Mamba, 稀疏专家混合, 计算生物学, 基因组基准测试, 轻量模型

## 3 点简述
- 核心问题：现有模型参数过大或无法有效建模DNA链双向性，限制植物基因组语言理解。
- 方法要点：集成双向Mamba捕获DNA正反向结构依赖，采用稀疏专家混合减少活跃参数提升效率。
- 实验或效果：在MPGB基准31个数据集上，20个表现最佳，平均性能优于现有模型，验证其有效性。

## 摘要（原文）

> Understanding the underlying linguistic rules of plant genomes remains a fundamental challenge in computational biology. Recent advances including AgroNT and PDLLMs have made notable progress although, they suffer from excessive parameter size and limited ability to model the bidirectional nature of DNA strands respectively. To address these limitations, we propose PlantBiMoE, a lightweight and expressive plant genome language model that integrates bidirectional Mamba and a Sparse Mixture-of-Experts (SparseMoE) framework. The bidirectional Mamba enables the model to effectively capture structural dependencies across both the forward and reverse DNA strands, while SparseMoE significantly reduces the number of active parameters, improving computational efficiency without sacrificing modeling capacity. We evaluated and tested our model on the Modified Plants Genome Benchmark (MPGB), an enhanced genomic benchmark, which consolidates 31 datasets across 11 representative tasks, with input sequence lengths ranging from 50 to 6,000 bp. Experimental results demonstrate that PlantBiMoE achieves the best performance on 20 out of 31 datasets and the average best when comparing with existing models. In summary, all above results demonstrate that our model can effectively represent plant genomic sequences, serving as a robust computational tool for diverse genomic tasks, while making substantive contributions to plant genomics, gene editing, and synthetic biology. The code is available at: https://github.com/HUST-Keep-Lin/PlantBiMoE

