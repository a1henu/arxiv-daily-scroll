---
layout: default
title: RSATalker: Realistic Socially-Aware Talking Head Generation for Multi-Turn Conversation
---

# RSATalker: Realistic Socially-Aware Talking Head Generation for Multi-Turn Conversation
**arXiv**：[2601.10606v1](https://arxiv.org/abs/2601.10606) · [PDF](https://arxiv.org/pdf/2601.10606.pdf)  
**作者**：Peng Chen, Xiaobao Wei, Yi Yang, Naiming Yao, Hui Chen, Feng Tian  

**一句话要点**：提出RSATalker框架，利用3D高斯溅射实现多轮对话中真实且社交感知的说话头生成。

**关键词**：说话头生成, 3D高斯溅射, 社交感知, 多轮对话, 虚拟现实

## 3 点简述
- 现有方法在真实纹理或计算成本方面存在局限，且缺乏社交关系建模。
- 结合基于网格的3D面部运动驱动与3D高斯绑定渲染，并引入社交感知模块编码关系。
- 实验表明在真实性和社交感知方面达到先进水平，并发布数据集。

## 摘要（原文）

> Talking head generation is increasingly important in virtual reality (VR), especially for social scenarios involving multi-turn conversation. Existing approaches face notable limitations: mesh-based 3D methods can model dual-person dialogue but lack realistic textures, while large-model-based 2D methods produce natural appearances but incur prohibitive computational costs. Recently, 3D Gaussian Splatting (3DGS) based methods achieve efficient and realistic rendering but remain speaker-only and ignore social relationships. We introduce RSATalker, the first framework that leverages 3DGS for realistic and socially-aware talking head generation with support for multi-turn conversation. Our method first drives mesh-based 3D facial motion from speech, then binds 3D Gaussians to mesh facets to render high-fidelity 2D avatar videos. To capture interpersonal dynamics, we propose a socially-aware module that encodes social relationships, including blood and non-blood as well as equal and unequal, into high-level embeddings through a learnable query mechanism. We design a three-stage training paradigm and construct the RSATalker dataset with speech-mesh-image triplets annotated with social relationships. Extensive experiments demonstrate that RSATalker achieves state-of-the-art performance in both realism and social awareness. The code and dataset will be released.

