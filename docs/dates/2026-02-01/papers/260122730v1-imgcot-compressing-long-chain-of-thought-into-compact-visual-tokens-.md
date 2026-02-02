---
layout: default
title: ImgCoT: Compressing Long Chain of Thought into Compact Visual Tokens for Efficient Reasoning of Large Language Model
---

# ImgCoT: Compressing Long Chain of Thought into Compact Visual Tokens for Efficient Reasoning of Large Language Model
**arXiv**：[2601.22730v1](https://arxiv.org/abs/2601.22730) · [PDF](https://arxiv.org/pdf/2601.22730.pdf)  
**作者**：Xiaoshu Chen, Sihang Zhou, Ke Liang, Taichun Zhou, Xinwang Liu  

**一句话要点**：提出ImgCoT，通过将思维链压缩为视觉令牌以提升大语言模型推理效率

**关键词**：思维链压缩, 视觉令牌, 大语言模型推理, 空间偏置, 混合推理

## 3 点简述
- 核心问题：现有方法压缩思维链时保留语言特征，限制了逻辑抽象和推理结构捕捉。
- 方法要点：将思维链渲染为图像作为重建目标，引入空间偏置以捕获全局推理结构；并提出松散版本结合关键文本步骤保留细节。
- 实验或效果：在多个数据集和大语言模型上验证了ImgCoT的有效性，实现高效推理。

## 摘要（原文）

> Compressing long chains of thought (CoT) into compact latent tokens is crucial for efficient reasoning with large language models (LLMs). Recent studies employ autoencoders to achieve this by reconstructing textual CoT from latent tokens, thus encoding CoT semantics. However, treating textual CoT as the reconstruction target forces latent tokens to preserve surface-level linguistic features (e.g., word choice and syntax), introducing a strong linguistic inductive bias that prioritizes linguistic form over reasoning structure and limits logical abstraction. Thus, we propose ImgCoT that replaces the reconstruction target from textual CoT to the visual CoT obtained by rendering CoT into images. This substitutes linguistic bias with spatial inductive bias, i.e., a tendency to model spatial layouts of the reasoning steps in visual CoT, enabling latent tokens to better capture global reasoning structure. Moreover, although visual latent tokens encode abstract reasoning structure, they may blur reasoning details. We thus propose a loose ImgCoT, a hybrid reasoning that augments visual latent tokens with a few key textual reasoning steps, selected based on low token log-likelihood. This design allows LLMs to retain both global reasoning structure and fine-grained reasoning details with fewer tokens than the complete CoT. Extensive experiments across multiple datasets and LLMs demonstrate the effectiveness of the two versions of ImgCoT.

