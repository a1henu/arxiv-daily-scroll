---
layout: default
title: SIGMMA: Hierarchical Graph-Based Multi-Scale Multi-modal Contrastive Alignment of Histopathology Image and Spatial Transcriptome
---

# SIGMMA: Hierarchical Graph-Based Multi-Scale Multi-modal Contrastive Alignment of Histopathology Image and Spatial Transcriptome
**arXiv**：[2511.15464v1](https://arxiv.org/abs/2511.15464) · [PDF](https://arxiv.org/pdf/2511.15464.pdf)  
**作者**：Dabin Jeong, Amirhossein Vahidi, Ciro Ramírez-Suástegui, Marie Moullet, Kevin Ly, Mohammad Vali Sanian, Sebastian Birk, Yinshui Chang, Adam Boxall, Daniyal Jafree, Lloyd Steele, Vijaya Baskar MS, Muzlifah Haniffa, Mohammad Lotfollahi  

**一句话要点**：提出SIGMMA框架以解决组织病理图像与空间转录组多尺度对齐问题

**关键词**：计算病理学, 多模态对齐, 图神经网络, 对比学习, 空间转录组学, 多尺度表示

## 3 点简述
- 现有方法在单尺度对齐HE图像与ST谱，忽略细胞结构层次
- SIGMMA通过多尺度对比对齐和图结构建模细胞交互
- 实验显示在基因预测和跨模态检索任务中性能显著提升

## 摘要（原文）

> Recent advances in computational pathology have leveraged vision-language models to learn joint representations of Hematoxylin and Eosin (HE) images with spatial transcriptomic (ST) profiles. However, existing approaches typically align HE tiles with their corresponding ST profiles at a single scale, overlooking fine-grained cellular structures and their spatial organization. To address this, we propose Sigmma, a multi-modal contrastive alignment framework for learning hierarchical representations of HE images and spatial transcriptome profiles across multiple scales. Sigmma introduces multi-scale contrastive alignment, ensuring that representations learned at different scales remain coherent across modalities. Furthermore, by representing cell interactions as a graph and integrating inter- and intra-subgraph relationships, our approach effectively captures cell-cell interactions, ranging from fine to coarse, within the tissue microenvironment. We demonstrate that Sigmm learns representations that better capture cross-modal correspondences, leading to an improvement of avg. 9.78\% in the gene-expression prediction task and avg. 26.93\% in the cross-modal retrieval task across datasets. We further show that it learns meaningful multi-tissue organization in downstream analyses.

