---
layout: default
title: White-Box mHC: Electromagnetic Spectrum-Aware and Interpretable Stream Interactions for Hyperspectral Image Classification
---

# White-Box mHC: Electromagnetic Spectrum-Aware and Interpretable Stream Interactions for Hyperspectral Image Classification
**arXiv**：[2601.15757v1](https://arxiv.org/abs/2601.15757) · [PDF](https://arxiv.org/pdf/2601.15757.pdf)  
**作者**：Yimin Zhu, Lincoln Linlin Xu, Zhengsen Xu, Zack Dewis, Mabel Heffring, Saeid Taleghanidoozdoozan, Motasem Alkayid, Quinn Ledingham, Megan Greenwood  

**一句话要点**：提出电磁谱感知白盒mHC框架，以增强高光谱图像分类的可解释性。

**关键词**：高光谱图像分类, 可解释性学习, 白盒模型, 电磁谱感知, 超连接框架

## 3 点简述
- 问题：现有深度学习模型在高光谱图像分类中特征混合不透明，缺乏可解释性。
- 方法：ES-mHC通过结构化方向矩阵显式建模电磁谱分组间的交互，分离特征表示与交互结构。
- 效果：实验显示超连接矩阵呈现空间模式，提供模型内部动态的机制性洞察。

## 摘要（原文）

> In hyperspectral image classification (HSIC), most deep learning models rely on opaque spectral-spatial feature mixing, limiting their interpretability and hindering understanding of internal decision mechanisms. We present physical spectrum-aware white-box mHC, named ES-mHC, a hyper-connection framework that explicitly models interactions among different electromagnetic spectrum groupings (residual stream in mHC) interactions using structured, directional matrices. By separating feature representation from interaction structure, ES-mHC promotes electromagnetic spectrum grouping specialization, reduces redundancy, and exposes internal information flow that can be directly visualized and spatially analyzed. Using hyperspectral image classification as a representative testbed, we demonstrate that the learned hyper-connection matrices exhibit coherent spatial patterns and asymmetric interaction behaviors, providing mechanistic insight into the model internal dynamics. Furthermore, we find that increasing the expansion rate accelerates the emergence of structured interaction patterns. These results suggest that ES-mHC transforms HSIC from a purely black-box prediction task into a structurally transparent, partially white-box learning process.

