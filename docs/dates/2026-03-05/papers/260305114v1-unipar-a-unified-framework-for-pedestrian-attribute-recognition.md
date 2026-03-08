---
layout: default
title: UniPAR: A Unified Framework for Pedestrian Attribute Recognition
---

# UniPAR: A Unified Framework for Pedestrian Attribute Recognition
**arXiv**：[2603.05114v1](https://arxiv.org/abs/2603.05114) · [PDF](https://arxiv.org/pdf/2603.05114.pdf)  
**作者**：Minghe Xu, Rouying Wu, Jiarui Xu, Minhao Sun, Zikang Yan, Xiao Wang, ChiaWei Chu, Yu Li  

**一句话要点**：提出UniPAR统一框架，以解决行人属性识别中跨模态、跨数据集和跨场景的挑战。

**关键词**：行人属性识别, 统一框架, Transformer, 跨模态学习, 多数据集训练, 分阶段融合

## 3 点简述
- 核心问题：现有方法受限于单数据集模型，难以处理模态、属性和环境差异。
- 方法要点：采用统一数据调度和动态分类头，结合分阶段融合编码器对齐视觉与文本特征。
- 实验或效果：在多个基准数据集上性能媲美专用SOTA，多数据集训练增强跨域泛化和极端环境鲁棒性。

## 摘要（原文）

> Pedestrian Attribute Recognition is a foundational computer vision task that provides essential support for downstream applications, including person retrieval in video surveillance and intelligent retail analytics. However, existing research is frequently constrained by the ``one-model-per-dataset" paradigm and struggles to handle significant discrepancies across domains in terms of modalities, attribute definitions, and environmental scenarios. To address these challenges, we propose UniPAR, a unified Transformer-based framework for PAR. By incorporating a unified data scheduling strategy and a dynamic classification head, UniPAR enables a single model to simultaneously process diverse datasets from heterogeneous modalities, including RGB images, video sequences, and event streams. We also introduce an innovative phased fusion encoder that explicitly aligns visual features with textual attribute queries through a late deep fusion strategy. Experimental results on the widely used benchmark datasets, including MSP60K, DukeMTMC, and EventPAR, demonstrate that UniPAR achieves performance comparable to specialized SOTA methods. Furthermore, multi-dataset joint training significantly enhances the model's cross-domain generalization and recognition robustness in extreme environments characterized by low light and motion blur. The source code of this paper will be released on https://github.com/Event-AHU/OpenPAR

