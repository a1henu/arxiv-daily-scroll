---
layout: default
title: NECromancer: Breathing Life into Skeletons via BVH Animation
---

# NECromancer: Breathing Life into Skeletons via BVH Animation
**arXiv**：[2602.06548v1](https://arxiv.org/abs/2602.06548) · [PDF](https://arxiv.org/pdf/2602.06548.pdf)  
**作者**：Mingxi Xu, Qi Wang, Zhengyu Wen, Phong Dao Thien, Zhengyu Li, Ning Zhang, Xiaoyu He, Wei Zhao, Kehong Gong, Mingyuan Zhang  

**一句话要点**：提出NECromancer通用运动分词器，基于BVH骨架实现跨形态运动分析与合成

**关键词**：运动分词, BVH动画, 骨架编码, 跨形态运动, 运动合成, 运动检索

## 3 点简述
- 现有运动分词方法局限于特定物种骨架，难以通用化处理多样形态
- NECromancer包含骨架编码器、拓扑无关分词器和统一数据集，直接处理任意BVH骨架
- 实验表明，该方法在压缩下实现高保真重建，支持跨物种运动迁移、生成和检索

## 摘要（原文）

> Motion tokenization is a key component of generalizable motion models, yet most existing approaches are restricted to species-specific skeletons, limiting their applicability across diverse morphologies. We propose NECromancer (NEC), a universal motion tokenizer that operates directly on arbitrary BVH skeletons. NEC consists of three components: (1) an Ontology-aware Skeletal Graph Encoder (OwO) that encodes structural priors from BVH files, including joint semantics, rest-pose offsets, and skeletal topology, into skeletal embeddings; (2) a Topology-Agnostic Tokenizer (TAT) that compresses motion sequences into a universal, topology-invariant discrete representation; and (3) the Unified BVH Universe (UvU), a large-scale dataset aggregating BVH motions across heterogeneous skeletons. Experiments show that NEC achieves high-fidelity reconstruction under substantial compression and effectively disentangles motion from skeletal structure. The resulting token space supports cross-species motion transfer, composition, denoising, generation with token-based models, and text-motion retrieval, establishing a unified framework for motion analysis and synthesis across diverse morphologies. Demo page: https://animotionlab.github.io/NECromancer/

