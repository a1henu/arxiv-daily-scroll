---
layout: default
title: SubQuad: Near-Quadratic-Free Structure Inference with Distribution-Balanced Objectives in Adaptive Receptor framework
---

# SubQuad: Near-Quadratic-Free Structure Inference with Distribution-Balanced Objectives in Adaptive Receptor framework
**arXiv**：[2602.17330v1](https://arxiv.org/abs/2602.17330) · [PDF](https://arxiv.org/pdf/2602.17330.pdf)  
**作者**：Rong Fu, Zijian Zhang, Wenxin Zhang, Kun Liu, Jiekai Wu, Xianda Li, Simon Fong  

**一句话要点**：提出SubQuad以解决自适应免疫库分析中的近二次计算成本和数据集不平衡问题

**关键词**：自适应免疫库分析, 近次二次检索, 公平约束聚类, GPU加速计算, 多模态融合, 生物信息学平台

## 3 点简述
- 核心问题：自适应免疫库群体规模分析受限于近二次亲和力评估成本和数据集不平衡，掩盖临床重要少数克隆型
- 方法要点：结合抗原感知近次二次检索、GPU加速亲和力核、学习多模态融合和公平约束聚类，实现端到端处理
- 实验或效果：在大规模病毒和肿瘤库上，提升吞吐量和内存效率，同时保持或改进召回率、聚类纯度和子群公平性

## 摘要（原文）

> Comparative analysis of adaptive immune repertoires at population scale is hampered by two practical bottlenecks: the near-quadratic cost of pairwise affinity evaluations and dataset imbalances that obscure clinically important minority clonotypes. We introduce SubQuad, an end-to-end pipeline that addresses these challenges by combining antigen-aware, near-subquadratic retrieval with GPU-accelerated affinity kernels, learned multimodal fusion, and fairness-constrained clustering. The system employs compact MinHash prefiltering to sharply reduce candidate comparisons, a differentiable gating module that adaptively weights complementary alignment and embedding channels on a per-pair basis, and an automated calibration routine that enforces proportional representation of rare antigen-specific subgroups. On large viral and tumor repertoires SubQuad achieves measured gains in throughput and peak memory usage while preserving or improving recall@k, cluster purity, and subgroup equity. By co-designing indexing, similarity fusion, and equity-aware objectives, SubQuad offers a scalable, bias-aware platform for repertoire mining and downstream translational tasks such as vaccine target prioritization and biomarker discovery.

