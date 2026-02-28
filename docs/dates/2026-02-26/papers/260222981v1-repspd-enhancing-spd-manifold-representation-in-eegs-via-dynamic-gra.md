---
layout: default
title: RepSPD: Enhancing SPD Manifold Representation in EEGs via Dynamic Graphs
---

# RepSPD: Enhancing SPD Manifold Representation in EEGs via Dynamic Graphs
**arXiv**：[2602.22981v1](https://arxiv.org/abs/2602.22981) · [PDF](https://arxiv.org/pdf/2602.22981.pdf)  
**作者**：Haohui Jia, Zheng Chen, Lingwei Zhu, Xu Cao, Yasuko Matsubara, Takashi Matsubara, Yasushi Sakurai  

**一句话要点**：提出RepSPD模型，通过动态图增强EEG中SPD流形表示，提升脑活动解码性能。

**关键词**：脑电图解码, 黎曼流形学习, 几何深度学习, 动态图神经网络, 对称正定矩阵

## 3 点简述
- 核心问题：现有SPD方法忽略EEG频率同步和脑区局部拓扑结构，导致表示不充分。
- 方法要点：在黎曼流形上使用交叉注意力机制，结合图功能连接特征调制SPD几何属性。
- 实验或效果：实验显示RepSPD显著优于现有EEG表示方法，具有更强鲁棒性和泛化能力。

## 摘要（原文）

> Decoding brain activity from electroencephalography (EEG) is crucial for neuroscience and clinical applications. Among recent advances in deep learning for EEG, geometric learning stands out as its theoretical underpinnings on symmetric positive definite (SPD) allows revealing structural connectivity analysis in a physics-grounded manner. However, current SPD-based methods focus predominantly on statistical aggregation of EEGs, with frequency-specific synchronization and local topological structures of brain regions neglected. Given this, we propose RepSPD, a novel geometric deep learning (GDL)-based model. RepSPD implements a cross-attention mechanism on the Riemannian manifold to modulate the geometric attributes of SPD with graph-derived functional connectivity features. On top of this, we introduce a global bidirectional alignment strategy to reshape tangent-space embeddings, mitigating geometric distortions caused by curvature and thereby enhancing geometric consistency. Extensive experiments demonstrate that our proposed framework significantly outperforms existing EEG representation methods, exhibiting superior robustness and generalization capabilities.

