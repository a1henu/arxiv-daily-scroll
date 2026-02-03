---
layout: default
title: DOGMA: Weaving Structural Information into Data-centric Single-cell Transcriptomics Analysis
---

# DOGMA: Weaving Structural Information into Data-centric Single-cell Transcriptomics Analysis
**arXiv**：[2602.01839v1](https://arxiv.org/abs/2602.01839) · [PDF](https://arxiv.org/pdf/2602.01839.pdf)  
**作者**：Ru Zhang, Xunkai Li, Yaxin Deng, Sicheng Liu, Daohan Su, Qiangqiang Dai, Hongchao Qin, Rong-Hua Li, Guoren Wang, Jia Li  

**一句话要点**：提出DOGMA框架，通过整合多级生物先验知识重塑单细胞转录组数据结构和语义

**关键词**：单细胞转录组学, 数据为中心AI, 图表示学习, 生物先验知识, 跨物种对齐

## 3 点简述
- 核心问题：现有方法忽视生物先验知识，导致图表示次优和计算开销大
- 方法要点：利用统计锚点、细胞本体和系统发育树实现确定性结构发现和跨物种对齐
- 实验或效果：在复杂多物种多器官基准测试中达到SOTA性能，计算成本显著降低

## 摘要（原文）

> Recently, data-centric AI methodology has been a dominant paradigm in single-cell transcriptomics analysis, which treats data representation rather than model complexity as the fundamental bottleneck. In the review of current studies, earlier sequence methods treat cells as independent entities and adapt prevalent ML models to analyze their directly inherited sequence data. Despite their simplicity and intuition, these methods overlook the latent intercellular relationships driven by the functional mechanisms of biological systems and the inherent quality issues of the raw sequence data. Therefore, a series of structured methods has emerged. Although they employ various heuristic rules to capture intricate intercellular relationships and enhance the raw sequencing data, these methods often neglect biological prior knowledge. This omission incurs substantial overhead and yields suboptimal graph representations, thereby hindering the utility of ML models.
>   To address them, we propose DOGMA, a holistic data-centric framework designed for the structural reshaping and semantic enhancement of raw data through multi-level biological prior knowledge. Transcending reliance on stochastic heuristics, DOGMA redefines graph construction by integrating Statistical Anchors with Cell Ontology and Phylogenetic Trees to enable deterministic structure discovery and robust cross-species alignment. Furthermore, Gene Ontology is utilized to bridge the feature-level semantic gap by incorporating functional priors. In complex multi-species and multi-organ benchmarks, DOGMA achieves SOTA performance, exhibiting superior zero-shot robustness and sample efficiency while operating with significantly lower computational cost.

