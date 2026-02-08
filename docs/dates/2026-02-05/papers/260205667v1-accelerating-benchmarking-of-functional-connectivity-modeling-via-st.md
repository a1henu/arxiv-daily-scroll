---
layout: default
title: Accelerating Benchmarking of Functional Connectivity Modeling via Structure-aware Core-set Selection
---

# Accelerating Benchmarking of Functional Connectivity Modeling via Structure-aware Core-set Selection
**arXiv**：[2602.05667v1](https://arxiv.org/abs/2602.05667) · [PDF](https://arxiv.org/pdf/2602.05667.pdf)  
**作者**：Ling Zhan, Zhen Li, Junjie Huang, Tao Jia  

**一句话要点**：提出结构感知核心集选择方法以加速功能连接建模的基准测试

**关键词**：功能连接建模, 核心集选择, 基准测试加速, 自监督学习, 结构感知学习, 神经科学计算

## 3 点简述
- 核心问题：大规模fMRI数据中功能连接建模方法基准测试计算成本过高，阻碍可重复神经科学评估。
- 方法要点：通过自监督学习框架SCLCS，利用自适应Transformer学习样本结构，引入结构扰动评分选择代表性核心集。
- 实验或效果：在REST-meta-MDD数据集上，仅用10%数据保持模型排名，排名一致性优于现有方法达23.2%。

## 摘要（原文）

> Benchmarking the hundreds of functional connectivity (FC) modeling methods on large-scale fMRI datasets is critical for reproducible neuroscience. However, the combinatorial explosion of model-data pairings makes exhaustive evaluation computationally prohibitive, preventing such assessments from becoming a routine pre-analysis step. To break this bottleneck, we reframe the challenge of FC benchmarking by selecting a small, representative core-set whose sole purpose is to preserve the relative performance ranking of FC operators. We formalize this as a ranking-preserving subset selection problem and propose Structure-aware Contrastive Learning for Core-set Selection (SCLCS), a self-supervised framework to select these core-sets. SCLCS first uses an adaptive Transformer to learn each sample's unique FC structure. It then introduces a novel Structural Perturbation Score (SPS) to quantify the stability of these learned structures during training, identifying samples that represent foundational connectivity archetypes. Finally, while SCLCS identifies stable samples via a top-k ranking, we further introduce a density-balanced sampling strategy as a necessary correction to promote diversity, ensuring the final core-set is both structurally robust and distributionally representative. On the large-scale REST-meta-MDD dataset, SCLCS preserves the ground-truth model ranking with just 10% of the data, outperforming state-of-the-art (SOTA) core-set selection methods by up to 23.2% in ranking consistency (nDCG@k). To our knowledge, this is the first work to formalize core-set selection for FC operator benchmarking, thereby making large-scale operators comparisons a feasible and integral part of computational neuroscience. Code is publicly available on https://github.com/lzhan94swu/SCLCS

