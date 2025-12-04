---
layout: default
title: Harnessing Hypergraphs in Geometric Deep Learning for 3D RNA Inverse Folding
---

# Harnessing Hypergraphs in Geometric Deep Learning for 3D RNA Inverse Folding
**arXiv**：[2512.03592v1](https://arxiv.org/abs/2512.03592) · [PDF](https://arxiv.org/pdf/2512.03592.pdf)  
**作者**：Guang Yang, Lei Fan  

**一句话要点**：提出HyperRNA框架，利用超图几何深度学习解决3D RNA逆折叠问题

**关键词**：RNA逆折叠, 超图学习, 几何深度学习, 序列生成, 生物分子设计

## 3 点简述
- 核心问题：RNA逆折叠涉及从目标二级结构生成核苷酸序列，序列与结构关系复杂，挑战性强
- 方法要点：基于3-bead粗粒度表示构建图结构，通过注意力嵌入和超图编码器捕获高阶依赖，自回归解码生成序列
- 实验或效果：在PDBBind和RNAsolo数据集上评估，性能优于现有RNA设计方法，展示超图在RNA工程中的潜力

## 摘要（原文）

> The RNA inverse folding problem, a key challenge in RNA design, involves identifying nucleotide sequences that can fold into desired secondary structures, which are critical for ensuring molecular stability and function. The inherent complexity of this task stems from the intricate relationship between sequence and structure, making it particularly challenging. In this paper, we propose a framework, named HyperRNA, a generative model with an encoder-decoder architecture that leverages hypergraphs to design RNA sequences. Specifically, our HyperRNA model consists of three main components: preprocessing, encoding and decoding.
>   In the preprocessing stage, graph structures are constructed by extracting the atom coordinates of RNA backbone based on 3-bead coarse-grained representation. The encoding stage processes these graphs, capturing higher order dependencies and complex biomolecular interactions using an attention embedding module and a hypergraph-based encoder. Finally, the decoding stage generates the RNA sequence in an autoregressive manner. We conducted quantitative and qualitative experiments on the PDBBind and RNAsolo datasets to evaluate the inverse folding task for RNA sequence generation and RNA-protein complex sequence generation. The experimental results demonstrate that HyperRNA not only outperforms existing RNA design methods but also highlights the potential of leveraging hypergraphs in RNA engineering.

