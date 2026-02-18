---
layout: default
title: LEADER: Lightweight End-to-End Attention-Gated Dual Autoencoder for Robust Minutiae Extraction
---

# LEADER: Lightweight End-to-End Attention-Gated Dual Autoencoder for Robust Minutiae Extraction
**arXiv**：[2602.15493v1](https://arxiv.org/abs/2602.15493) · [PDF](https://arxiv.org/pdf/2602.15493.pdf)  
**作者**：Raffaele Cappelli, Matteo Ferrara  

**一句话要点**：提出LEADER轻量级端到端注意力门控双自编码器，用于鲁棒指纹细节点提取。

**关键词**：指纹识别, 细节点提取, 端到端学习, 注意力机制, 轻量级网络, 跨域泛化

## 3 点简述
- 指纹识别中细节点提取转向深度学习，但真正端到端方法稀缺。
- LEADER集成非极大值抑制和角度解码，仅用0.9M参数实现端到端推理。
- 在NIST SD27数据集上F1分数提升34%，推理速度优于商业软件。

## 摘要（原文）

> Minutiae extraction, a fundamental stage in fingerprint recognition, is increasingly shifting toward deep learning. However, truly end-to-end methods that eliminate separate preprocessing and postprocessing steps remain scarce. This paper introduces LEADER (Lightweight End-to-end Attention-gated Dual autoencodER), a neural network that maps raw fingerprint images to minutiae descriptors, including location, direction, and type. The proposed architecture integrates non-maximum suppression and angular decoding to enable complete end-to-end inference using only 0.9M parameters. It employs a novel "Castle-Moat-Rampart" ground-truth encoding and a dual-autoencoder structure, interconnected through an attention-gating mechanism. Experimental evaluations demonstrate state-of-the-art accuracy on plain fingerprints and robust cross-domain generalization to latent impressions. Specifically, LEADER attains a 34% higher F1-score on the NIST SD27 dataset compared to specialized latent minutiae extractors. Sample-level analysis on this challenging benchmark reveals an average rank of 2.07 among all compared methods, with LEADER securing the first-place position in 47% of the samples-more than doubling the frequency of the second-best extractor. The internal representations learned by the model align with established fingerprint domain features, such as segmentation masks, orientation fields, frequency maps, and skeletons. Inference requires 15ms on GPU and 322ms on CPU, outperforming leading commercial software in computational efficiency. The source code and pre-trained weights are publicly released to facilitate reproducibility.

