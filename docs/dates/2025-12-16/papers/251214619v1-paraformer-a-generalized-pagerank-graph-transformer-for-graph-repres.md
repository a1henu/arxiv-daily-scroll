---
layout: default
title: ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation Learning
---

# ParaFormer: A Generalized PageRank Graph Transformer for Graph Representation Learning
**arXiv**：[2512.14619v1](https://arxiv.org/abs/2512.14619) · [PDF](https://arxiv.org/pdf/2512.14619.pdf)  
**作者**：Chaohao Yuan, Zhenjie Song, Ercan Engin Kuruoglu, Kangfei Zhao, Yang Liu, Deli Zhao, Hong Cheng, Yu Rong  

**一句话要点**：提出ParaFormer以解决图Transformer中的过平滑问题，通过PageRank增强注意力模块提升图表示学习性能。

**关键词**：图Transformer, 过平滑问题, PageRank注意力, 图表示学习, 节点分类, 图分类

## 3 点简述
- 核心问题：图Transformer的全局注意力机制导致严重过平滑，使节点表示难以区分。
- 方法要点：引入PageRank增强的注意力模块，模拟深度Transformer行为，作为自适应滤波器缓解过平滑。
- 实验或效果：在11个数据集上验证，节点分类和图分类任务均取得一致性能提升。

## 摘要（原文）

> Graph Transformers (GTs) have emerged as a promising graph learning tool, leveraging their all-pair connected property to effectively capture global information. To address the over-smoothing problem in deep GNNs, global attention was initially introduced, eliminating the necessity for using deep GNNs. However, through empirical and theoretical analysis, we verify that the introduced global attention exhibits severe over-smoothing, causing node representations to become indistinguishable due to its inherent low-pass filtering. This effect is even stronger than that observed in GNNs. To mitigate this, we propose PageRank Transformer (ParaFormer), which features a PageRank-enhanced attention module designed to mimic the behavior of deep Transformers. We theoretically and empirically demonstrate that ParaFormer mitigates over-smoothing by functioning as an adaptive-pass filter. Experiments show that ParaFormer achieves consistent performance improvements across both node classification and graph classification tasks on 11 datasets ranging from thousands to millions of nodes, validating its efficacy. The supplementary material, including code and appendix, can be found in https://github.com/chaohaoyuan/ParaFormer.

