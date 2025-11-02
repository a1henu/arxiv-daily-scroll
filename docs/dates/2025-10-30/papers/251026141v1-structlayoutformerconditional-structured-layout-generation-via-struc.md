---
layout: default
title: StructLayoutFormer:Conditional Structured Layout Generation via Structure Serialization and Disentanglement
---

# StructLayoutFormer:Conditional Structured Layout Generation via Structure Serialization and Disentanglement
**arXiv**：[2510.26141v1](https://arxiv.org/abs/2510.26141) · [PDF](https://arxiv.org/pdf/2510.26141.pdf)  
**作者**：Xin Hu, Pengfei Xu, Jin Zhou, Hongbo Fu, Hui Huang  

**一句话要点**：提出StructLayoutFormer以解决结构化布局生成问题，通过序列化和解耦实现条件生成。

**关键词**：结构化布局生成, Transformer模型, 序列化表示, 条件生成, 布局结构解耦

## 3 点简述
- 现有数据驱动方法无法生成明确布局结构，需大量人工干预。
- 采用结构序列化和解耦方法，将结构信息与元素放置分离。
- 实验表明，在条件结构化布局生成中优于基线，并支持结构提取与迁移。

## 摘要（原文）

> Structured layouts are preferable in many 2D visual contents (\eg, GUIs,
> webpages) since the structural information allows convenient layout editing.
> Computational frameworks can help create structured layouts but require heavy
> labor input. Existing data-driven approaches are effective in automatically
> generating fixed layouts but fail to produce layout structures. We present
> StructLayoutFormer, a novel Transformer-based approach for conditional
> structured layout generation. We use a structure serialization scheme to
> represent structured layouts as sequences. To better control the structures of
> generated layouts, we disentangle the structural information from the element
> placements. Our approach is the first data-driven approach that achieves
> conditional structured layout generation and produces realistic layout
> structures explicitly. We compare our approach with existing data-driven layout
> generation approaches by including post-processing for structure extraction.
> Extensive experiments have shown that our approach exceeds these baselines in
> conditional structured layout generation. We also demonstrate that our approach
> is effective in extracting and transferring layout structures. The code is
> publicly available at %\href{https://github.com/Teagrus/StructLayoutFormer}
> {https://github.com/Teagrus/StructLayoutFormer}.

