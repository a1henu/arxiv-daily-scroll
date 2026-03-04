---
layout: default
title: Nodes Are Early, Edges Are Late: Probing Diagram Representations in Large Vision-Language Models
---

# Nodes Are Early, Edges Are Late: Probing Diagram Representations in Large Vision-Language Models
**arXiv**：[2603.02865v1](https://arxiv.org/abs/2603.02865) · [PDF](https://arxiv.org/pdf/2603.02865.pdf)  
**作者**：Haruto Yoshida, Keito Kudo, Yoichi Aoki, Ryota Tanaka, Itsumi Saito, Keisuke Sakaguchi, Kentaro Inui  

**一句话要点**：探究大视觉语言模型中节点与边缘表示的线性可分性差异，以解释关系理解局限

**关键词**：图表理解, 大视觉语言模型, 线性可分性, 节点表示, 边缘表示, 关系理解

## 3 点简述
- 核心问题：大视觉语言模型在图表理解中难以处理节点与有向边缘的关系，如箭头方向。
- 方法要点：使用基于有向图的合成图表数据集，探测模型内部表示的线性可分性。
- 实验或效果：发现边缘信息在视觉编码器中非线性可分，仅在语言模型文本令牌中线性编码；节点信息则早期线性编码。

## 摘要（原文）

> Large vision-language models (LVLMs) demonstrate strong performance on diagram understanding benchmarks, yet they still struggle with understanding relationships between elements, particularly those represented by nodes and directed edges (e.g., arrows and lines). To investigate the underlying causes of this limitation, we probe the internal representation of LVLMs using a carefully constructed synthetic diagram dataset based on directed graphs. Our probing experiments reveal that edge information is not linearly separable in the vision encoder and becomes linearly encoded only in the text tokens in the language model. In contrast, node information and global structural features are already linearly encoded in individual hidden states of the vision encoder. These findings suggest that the stage at which linearly separable representations are formed varies depending on the type of visual information. In particular, the delayed emergence of edge representations may help explain why LVLMs struggle with relational understanding, such as interpreting edge directions, which require more abstract, compositionally integrated processes.

