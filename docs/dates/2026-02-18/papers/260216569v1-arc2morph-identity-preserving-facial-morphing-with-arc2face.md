---
layout: default
title: Arc2Morph: Identity-Preserving Facial Morphing with Arc2Face
---

# Arc2Morph: Identity-Preserving Facial Morphing with Arc2Face
**arXiv**：[2602.16569v1](https://arxiv.org/abs/2602.16569) · [PDF](https://arxiv.org/pdf/2602.16569.pdf)  
**作者**：Nicolò Di Domenico, Annalisa Franco, Matteo Ferrara, Davide Maltoni  

**一句话要点**：提出基于Arc2Face的身份保持面部融合方法，以应对电子身份文档中的人脸识别威胁。

**关键词**：面部融合攻击, 身份保持, Arc2Face模型, 人脸识别安全, 深度学习融合

## 3 点简述
- 核心问题：面部融合攻击利用护照注册流程漏洞，威胁人脸识别系统安全。
- 方法要点：使用Arc2Face身份条件化基础模型，从紧凑身份表示合成逼真面部图像。
- 实验或效果：在多个数据集上验证，融合攻击潜力与基于地标方法相当，有效管理身份信息。

## 摘要（原文）

> Face morphing attacks are widely recognized as one of the most challenging threats to face recognition systems used in electronic identity documents. These attacks exploit a critical vulnerability in passport enrollment procedures adopted by many countries, where the facial image is often acquired without a supervised live capture process. In this paper, we propose a novel face morphing technique based on Arc2Face, an identity-conditioned face foundation model capable of synthesizing photorealistic facial images from compact identity representations. We demonstrate the effectiveness of the proposed approach by comparing the morphing attack potential metric on two large-scale sequestered face morphing attack detection datasets against several state-of-the-art morphing methods, as well as on two novel morphed face datasets derived from FEI and ONOT. Experimental results show that the proposed deep learning-based approach achieves a morphing attack potential comparable to that of landmark-based techniques, which have traditionally been regarded as the most challenging. These findings confirm the ability of the proposed method to effectively preserve and manage identity information during the morph generation process.

