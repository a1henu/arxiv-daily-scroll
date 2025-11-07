---
layout: default
title: Text to Sketch Generation with Multi-Styles
---

# Text to Sketch Generation with Multi-Styles
**arXiv**：[2511.04123v1](https://arxiv.org/abs/2511.04123) · [PDF](https://arxiv.org/pdf/2511.04123.pdf)  
**作者**：Tengjie Li, Shikui Tu, Lei Xu  

**一句话要点**：提出基于扩散模型的免训练框架，实现文本到草图的精确多风格生成

**关键词**：草图生成, 扩散模型, 风格控制, 免训练框架, 多风格合成

## 3 点简述
- 现有方法缺乏对草图风格的精确控制机制，导致合成质量受限
- 采用参考特征辅助和风格-内容引导，减少内容泄漏并提升生成质量
- 实验表明该方法在风格对齐和灵活性方面优于现有方法

## 摘要（原文）

> Recent advances in vision-language models have facilitated progress in sketch
> generation. However, existing specialized methods primarily focus on generic
> synthesis and lack mechanisms for precise control over sketch styles. In this
> work, we propose a training-free framework based on diffusion models that
> enables explicit style guidance via textual prompts and referenced style
> sketches. Unlike previous style transfer methods that overwrite key and value
> matrices in self-attention, we incorporate the reference features as auxiliary
> information with linear smoothing and leverage a style-content guidance
> mechanism. This design effectively reduces content leakage from reference
> sketches and enhances synthesis quality, especially in cases with low
> structural similarity between reference and target sketches. Furthermore, we
> extend our framework to support controllable multi-style generation by
> integrating features from multiple reference sketches, coordinated via a joint
> AdaIN module. Extensive experiments demonstrate that our approach achieves
> high-quality sketch generation with accurate style alignment and improved
> flexibility in style control. The official implementation of M3S is available
> at https://github.com/CMACH508/M3S.

