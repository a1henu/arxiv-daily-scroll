---
layout: default
title: MHB: Multimodal Handshape-aware Boundary Detection for Continuous Sign Language Recognition
---

# MHB: Multimodal Handshape-aware Boundary Detection for Continuous Sign Language Recognition
**arXiv**：[2511.19907v1](https://arxiv.org/abs/2511.19907) · [PDF](https://arxiv.org/pdf/2511.19907.pdf)  
**作者**：Mingyu Zhao, Zhanfu Yang, Yang Zhou, Zhaoyang Xia, Can Jin, Xiaoxiao He, Carol Neidle, Dimitris N. Metaxas  

**一句话要点**：提出多模态手形感知边界检测方法，用于连续手语识别中的符号分割与识别。

**关键词**：连续手语识别, 边界检测, 多模态融合, 手形分类, 3D骨骼特征

## 3 点简述
- 核心问题：连续手语视频中符号边界检测的准确性不足，影响识别性能。
- 方法要点：融合3D骨骼特征和手形分类器，通过多模态模块提升边界检测鲁棒性。
- 实验或效果：在ASLLRP语料库上评估，相比先前工作有显著改进。

## 摘要（原文）

> This paper presents a multimodal approach for continuous sign recognition that first uses machine learning to detect the start and end frames of signs in videos of American Sign Language (ASL) sentences, and then recognizes the segmented signs. For improved robustness, we use 3D skeletal features extracted from sign language videos to capture the convergence of sign properties and their dynamics, which tend to cluster at sign boundaries. Another focus of this work is the incorporation of information from 3D handshape for boundary detection. To detect handshapes normally expected at the beginning and end of signs, we pretrain a handshape classifier for 87 linguistically defined canonical handshape categories using a dataset that we created by integrating and normalizing several existing datasets. A multimodal fusion module is then used to unify the pretrained sign video segmentation framework and the handshape classification models. Finally, the estimated boundaries are used for sign recognition, where the recognition model is trained on a large database containing both citation-form isolated signs and signs pre-segmented (based on manual annotations) from continuous signing, as such signs often differ in certain respects. We evaluate our method on the ASLLRP corpus and demonstrate significant improvements over previous work.

