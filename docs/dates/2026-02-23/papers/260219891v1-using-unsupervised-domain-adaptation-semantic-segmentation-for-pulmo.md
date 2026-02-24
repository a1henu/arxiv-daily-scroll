---
layout: default
title: Using Unsupervised Domain Adaptation Semantic Segmentation for Pulmonary Embolism Detection in Computed Tomography Pulmonary Angiogram (CTPA) Images
---

# Using Unsupervised Domain Adaptation Semantic Segmentation for Pulmonary Embolism Detection in Computed Tomography Pulmonary Angiogram (CTPA) Images
**arXiv**：[2602.19891v1](https://arxiv.org/abs/2602.19891) · [PDF](https://arxiv.org/pdf/2602.19891.pdf)  
**作者**：Wen-Liang Lin, Yun-Chien Cheng  

**一句话要点**：提出基于Transformer和Mean-Teacher的无监督域适应框架，用于CTPA图像中肺栓塞的语义分割。

**关键词**：无监督域适应, 语义分割, 肺栓塞检测, Transformer, Mean-Teacher, 对比学习

## 3 点简述
- 核心问题：CTPA图像中肺栓塞检测受域偏移和标注成本高限制，阻碍实际部署。
- 方法要点：集成原型对齐、全局局部对比学习和注意力辅助局部预测模块，提升伪标签可靠性。
- 实验或效果：在跨中心数据集上IoU显著提升，并在跨模态任务中达到69.9% Dice分数，验证鲁棒性。

## 摘要（原文）

> While deep learning has demonstrated considerable promise in computer-aided diagnosis for pulmonary embolism (PE), practical deployment in Computed Tomography Pulmonary Angiography (CTPA) is often hindered by "domain shift" and the prohibitive cost of expert annotations. To address these challenges, an unsupervised domain adaptation (UDA) framework is proposed, utilizing a Transformer backbone and a Mean-Teacher architecture for cross-center semantic segmentation. The primary focus is placed on enhancing pseudo-label reliability by learning deep structural information within the feature space. Specifically, three modules are integrated and designed for this task: (1) a Prototype Alignment (PA) mechanism to reduce category-level distribution discrepancies; (2) Global and Local Contrastive Learning (GLCL) to capture both pixel-level topological relationships and global semantic representations; and (3) an Attention-based Auxiliary Local Prediction (AALP) module designed to reinforce sensitivity to small PE lesions by automatically extracting high-information slices from Transformer attention maps. Experimental validation conducted on cross-center datasets (FUMPE and CAD-PE) demonstrates significant performance gains. In the FUMPE -> CAD-PE task, the IoU increased from 0.1152 to 0.4153, while the CAD-PE -> FUMPE task saw an improvement from 0.1705 to 0.4302. Furthermore, the proposed method achieved a 69.9% Dice score in the CT -> MRI cross-modality task on the MMWHS dataset without utilizing any target-domain labels for model selection, confirming its robustness and generalizability for diverse clinical environments.

