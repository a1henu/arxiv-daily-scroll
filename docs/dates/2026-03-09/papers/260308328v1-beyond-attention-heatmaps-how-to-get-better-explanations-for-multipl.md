---
layout: default
title: Beyond Attention Heatmaps: How to Get Better Explanations for Multiple Instance Learning Models in Histopathology
---

# Beyond Attention Heatmaps: How to Get Better Explanations for Multiple Instance Learning Models in Histopathology
**arXiv**：[2603.08328v1](https://arxiv.org/abs/2603.08328) · [PDF](https://arxiv.org/pdf/2603.08328.pdf)  
**作者**：Mina Jamshidi Idaji, Julius Hense, Tom Neuhäuser, Augustin Krause, Yanqing Luo, Oliver Eberle, Thomas Schnake, Laure Ciernik, Farnoush Rezaei Jafari, Reza Vahidimajd, Jonas Dippel, Christoph Walz, Frederick Klauschen, Andreas Mock, Klaus-Robert Müller  

**一句话要点**：提出评估框架以提升组织病理学中多实例学习模型热图解释的可靠性

**关键词**：多实例学习, 组织病理学, 可解释人工智能, 热图评估, 模型验证, 生物标志物发现

## 3 点简述
- 核心问题：热图在验证多实例学习模型和发现生物标志物中广泛使用，但其有效性缺乏系统评估。
- 方法要点：引入无需额外标签的通用框架，大规模基准测试六种解释方法，涵盖不同任务类型和模型架构。
- 实验或效果：发现扰动、层相关传播和积分梯度方法优于注意力热图，能更可靠反映模型决策机制，并展示生物验证潜力。

## 摘要（原文）

> Multiple instance learning (MIL) has enabled substantial progress in computational histopathology, where a large amount of patches from gigapixel whole slide images are aggregated into slide-level predictions. Heatmaps are widely used to validate MIL models and to discover tissue biomarkers. Yet, the validity of these heatmaps has barely been investigated. In this work, we introduce a general framework for evaluating the quality of MIL heatmaps without requiring additional labels. We conduct a large-scale benchmark experiment to assess six explanation methods across histopathology task types (classification, regression, survival), MIL model architectures (Attention-, Transformer-, Mamba-based), and patch encoder backbones (UNI2, Virchow2). Our results show that explanation quality mostly depends on MIL model architecture and task type, with perturbation ("Single"), layer-wise relevance propagation (LRP), and integrated gradients (IG) consistently outperforming attention-based and gradient-based saliency heatmaps, which often fail to reflect model decision mechanisms. We further demonstrate the advanced capabilities of the best-performing explanation methods: (i) We provide a proof-of-concept that MIL heatmaps of a bulk gene expression prediction model can be correlated with spatial transcriptomics for biological validation, and (ii) showcase the discovery of distinct model strategies for predicting human papillomavirus (HPV) infection from head and neck cancer slides. Our work highlights the importance of validating MIL heatmaps and establishes that improved explainability can enable more reliable model validation and yield biological insights, making a case for a broader adoption of explainable AI in digital pathology. Our code is provided in a public GitHub repository: https://github.com/bifold-pathomics/xMIL/tree/xmil-journal

