---
layout: default
title: DiT-JSCC: Rethinking Deep JSCC with Diffusion Transformers and Semantic Representations
---

# DiT-JSCC: Rethinking Deep JSCC with Diffusion Transformers and Semantic Representations
**arXiv**：[2601.03112v1](https://arxiv.org/abs/2601.03112) · [PDF](https://arxiv.org/pdf/2601.03112.pdf)  
**作者**：Kailin Tan, Jincheng Dai, Sixian Wang, Guo Lu, Shuo Shao, Kai Niu, Wenjun Zhang, Ping Zhang  

**一句话要点**：提出DiT-JSCC以解决极端无线信道下图像传输的语义一致性问题

**关键词**：生成式联合信源信道编码, 扩散变换器, 语义表示, 图像传输, 极端信道条件

## 3 点简述
- 核心问题：现有生成式联合信源信道编码中，编码器缺乏语义判别性，导致解码器生成结果语义不一致
- 方法要点：设计语义-细节双分支编码器与基于扩散变换器的生成式解码器，实现从粗到细的条件生成
- 实验或效果：在极端信道条件下，DiT-JSCC在语义一致性和视觉质量上优于现有方法

## 摘要（原文）

> Generative joint source-channel coding (GJSCC) has emerged as a new Deep JSCC paradigm for achieving high-fidelity and robust image transmission under extreme wireless channel conditions, such as ultra-low bandwidth and low signal-to-noise ratio. Recent studies commonly adopt diffusion models as generative decoders, but they frequently produce visually realistic results with limited semantic consistency. This limitation stems from a fundamental mismatch between reconstruction-oriented JSCC encoders and generative decoders, as the former lack explicit semantic discriminability and fail to provide reliable conditional cues. In this paper, we propose DiT-JSCC, a novel GJSCC backbone that can jointly learn a semantics-prioritized representation encoder and a diffusion transformer (DiT) based generative decoder, our open-source project aims to promote the future research in GJSCC. Specifically, we design a semantics-detail dual-branch encoder that aligns naturally with a coarse-to-fine conditional DiT decoder, prioritizing semantic consistency under extreme channel conditions. Moreover, a training-free adaptive bandwidth allocation strategy inspired by Kolmogorov complexity is introduced to further improve the transmission efficiency, thereby indeed redefining the notion of information value in the era of generative decoding. Extensive experiments demonstrate that DiT-JSCC consistently outperforms existing JSCC methods in both semantic consistency and visual quality, particularly in extreme regimes.

