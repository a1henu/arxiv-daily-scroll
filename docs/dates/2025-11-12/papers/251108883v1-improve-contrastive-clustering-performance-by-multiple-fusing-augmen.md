---
layout: default
title: Improve Contrastive Clustering Performance by Multiple Fusing-Augmenting ViT Blocks
---

# Improve Contrastive Clustering Performance by Multiple Fusing-Augmenting ViT Blocks
**arXiv**：[2511.08883v1](https://arxiv.org/abs/2511.08883) · [PDF](https://arxiv.org/pdf/2511.08883.pdf)  
**作者**：Cheng Wang, Shuisheng Zhou, Fengjiao Peng, Jin Sheng, Feng Ye, Yinli Dong  

**一句话要点**：提出多融合增强ViT块以提升对比聚类性能

**关键词**：对比聚类, 视觉变换器, 特征融合, 数据增强, 图像聚类

## 3 点简述
- 现有对比学习网络未充分利用正样本对的互补性提取聚类特征
- 设计MFAVBs，通过ViT融合正样本特征并多次增强
- 在七个数据集上实验，聚类性能优于现有技术

## 摘要（原文）

> In the field of image clustering, the widely used contrastive learning networks improve clustering performance by maximizing the similarity between positive pairs and the dissimilarity of negative pairs of the inputs. Extant contrastive learning networks, whose two encoders often implicitly interact with each other by parameter sharing or momentum updating, may not fully exploit the complementarity and similarity of the positive pairs to extract clustering features from input data. To explicitly fuse the learned features of positive pairs, we design a novel multiple fusing-augmenting ViT blocks (MFAVBs) based on the excellent feature learning ability of Vision Transformers (ViT). Firstly, two preprocessed augmentions as positive pairs are separately fed into two shared-weight ViTs, then their output features are fused to input into a larger ViT. Secondly, the learned features are split into a pair of new augmented positive samples and passed to the next FAVBs, enabling multiple fusion and augmention through MFAVBs operations. Finally, the learned features are projected into both instance-level and clustering-level spaces to calculate the cross-entropy loss, followed by parameter updates by backpropagation to finalize the training process. To further enhance ability of the model to distinguish between similar images, our input data for the network we propose is preprocessed augmentions with features extracted from the CLIP pretrained model. Our experiments on seven public datasets demonstrate that MFAVBs serving as the backbone for contrastive clustering outperforms the state-of-the-art techniques in terms of clustering performance.

