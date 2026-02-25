---
layout: default
title: Communication-Inspired Tokenization for Structured Image Representations
---

# Communication-Inspired Tokenization for Structured Image Representations
**arXiv**：[2602.20731v1](https://arxiv.org/abs/2602.20731) · [PDF](https://arxiv.org/pdf/2602.20731.pdf)  
**作者**：Aram Davtyan, Yusuf Sahin, Yasaman Haghighi, Sebastian Stapf, Pablo Acuaviva, Alexandre Alahi, Paolo Favaro  

**一句话要点**：提出通信启发式标记化框架COMiT，以生成结构化视觉标记序列，提升组合泛化与关系推理能力。

**关键词**：离散图像标记化, 结构化视觉表示, 组合泛化, 关系推理, 通信启发式学习, 端到端训练

## 3 点简述
- 现有离散图像标记器主要优化重建与压缩，缺乏对象级语义结构捕获能力。
- COMiT通过迭代观察局部图像块和递归更新离散表示，构建结构化标记序列。
- 实验表明COMiT在组合泛化和关系推理上优于先前方法，标记结构更可解释。

## 摘要（原文）

> Discrete image tokenizers have emerged as a key component of modern vision and multimodal systems, providing a sequential interface for transformer-based architectures. However, most existing approaches remain primarily optimized for reconstruction and compression, often yielding tokens that capture local texture rather than object-level semantic structure. Inspired by the incremental and compositional nature of human communication, we introduce COMmunication inspired Tokenization (COMiT), a framework for learning structured discrete visual token sequences. COMiT constructs a latent message within a fixed token budget by iteratively observing localized image crops and recurrently updating its discrete representation. At each step, the model integrates new visual information while refining and reorganizing the existing token sequence. After several encoding iterations, the final message conditions a flow-matching decoder that reconstructs the full image. Both encoding and decoding are implemented within a single transformer model and trained end-to-end using a combination of flow-matching reconstruction and semantic representation alignment losses. Our experiments demonstrate that while semantic alignment provides grounding, attentive sequential tokenization is critical for inducing interpretable, object-centric token structure and substantially improving compositional generalization and relational reasoning over prior methods.

