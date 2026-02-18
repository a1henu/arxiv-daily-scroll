---
layout: default
title: Context-aware Skin Cancer Epithelial Cell Classification with Scalable Graph Transformers
---

# Context-aware Skin Cancer Epithelial Cell Classification with Scalable Graph Transformers
**arXiv**：[2602.15783v1](https://arxiv.org/abs/2602.15783) · [PDF](https://arxiv.org/pdf/2602.15783.pdf)  
**作者**：Lucas Sancéré, Noémie Moreau, Katarzyna Bozek  

**一句话要点**：提出基于全切片细胞图的可扩展图Transformer，用于皮肤癌上皮细胞分类，以解决组织级上下文缺失问题。

**关键词**：全切片图像分析, 图Transformer, 细胞分类, 上下文感知, 皮肤鳞状细胞癌, 可扩展模型

## 3 点简述
- 核心问题：全切片图像分析中，基于补丁的方法丢失组织级上下文，导致健康与肿瘤上皮细胞分类困难。
- 方法要点：构建全切片细胞图，应用可扩展图Transformer（SGFormer和DIFFormer）进行细胞分类。
- 实验或效果：在皮肤鳞状细胞癌数据集上，图Transformer模型优于图像基方法，平衡准确率达85%以上。

## 摘要（原文）

> Whole-slide images (WSIs) from cancer patients contain rich information that can be used for medical diagnosis or to follow treatment progress. To automate their analysis, numerous deep learning methods based on convolutional neural networks and Vision Transformers have been developed and have achieved strong performance in segmentation and classification tasks. However, due to the large size and complex cellular organization of WSIs, these models rely on patch-based representations, losing vital tissue-level context. We propose using scalable Graph Transformers on a full-WSI cell graph for classification. We evaluate this methodology on a challenging task: the classification of healthy versus tumor epithelial cells in cutaneous squamous cell carcinoma (cSCC), where both cell types exhibit very similar morphologies and are therefore difficult to differentiate for image-based approaches. We first compared image-based and graph-based methods on a single WSI. Graph Transformer models SGFormer and DIFFormer achieved balanced accuracies of $85.2 \pm 1.5$ ($\pm$ standard error) and $85.1 \pm 2.5$ in 3-fold cross-validation, respectively, whereas the best image-based method reached $81.2 \pm 3.0$. By evaluating several node feature configurations, we found that the most informative representation combined morphological and texture features as well as the cell classes of non-epithelial cells, highlighting the importance of the surrounding cellular context. We then extended our work to train on several WSIs from several patients. To address the computational constraints of image-based models, we extracted four $2560 \times 2560$ pixel patches from each image and converted them into graphs. In this setting, DIFFormer achieved a balanced accuracy of $83.6 \pm 1.9$ (3-fold cross-validation), while the state-of-the-art image-based model CellViT256 reached $78.1 \pm 0.5$.

