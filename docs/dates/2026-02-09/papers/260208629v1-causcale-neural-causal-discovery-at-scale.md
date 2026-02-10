---
layout: default
title: CauScale: Neural Causal Discovery at Scale
---

# CauScale: Neural Causal Discovery at Scale
**arXiv**：[2602.08629v1](https://arxiv.org/abs/2602.08629) · [PDF](https://arxiv.org/pdf/2602.08629.pdf)  
**作者**：Bo Peng, Sirui Chen, Jiaguo Tian, Yu Qiao, Chaochao Lu  

**一句话要点**：提出CauScale神经架构以解决大规模因果发现中的时空效率瓶颈

**关键词**：因果发现, 神经架构, 大规模图, 效率优化, 双流设计

## 3 点简述
- 核心问题：现有因果发现方法在扩展至大规模图时面临显著的时间和空间效率瓶颈。
- 方法要点：采用压缩单元和共享注意力权重提升效率，通过双流设计保持高准确性。
- 实验或效果：在500节点图上成功训练，推理速度提升4-13,000倍，准确率在分布内外数据上分别达99.6%和84.4%。

## 摘要（原文）

> Causal discovery is essential for advancing data-driven fields such as scientific AI and data analysis, yet existing approaches face significant time- and space-efficiency bottlenecks when scaling to large graphs. To address this challenge, we present CauScale, a neural architecture designed for efficient causal discovery that scales inference to graphs with up to 1000 nodes. CauScale improves time efficiency via a reduction unit that compresses data embeddings and improves space efficiency by adopting tied attention weights to avoid maintaining axis-specific attention maps. To keep high causal discovery accuracy, CauScale adopts a two-stream design: a data stream extracts relational evidence from high-dimensional observations, while a graph stream integrates statistical graph priors and preserves key structural signals. CauScale successfully scales to 500-node graphs during training, where prior work fails due to space limitations. Across testing data with varying graph scales and causal mechanisms, CauScale achieves 99.6% mAP on in-distribution data and 84.4% on out-of-distribution data, while delivering 4-13,000 times inference speedups over prior methods. Our project page is at https://github.com/OpenCausaLab/CauScale.

