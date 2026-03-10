---
layout: default
title: Not Like Transformers: Drop the Beat Representation for Dance Generation with Mamba-Based Diffusion Model
---

# Not Like Transformers: Drop the Beat Representation for Dance Generation with Mamba-Based Diffusion Model
**arXiv**：[2603.08023v1](https://arxiv.org/abs/2603.08023) · [PDF](https://arxiv.org/pdf/2603.08023.pdf)  
**作者**：Sangjune Park, Inhyeok Choi, Donghyeon Soon, Youngwoo Jeon, Kyungdon Joo  

**一句话要点**：提出MambaDance，基于Mamba的扩散模型，以解决舞蹈生成中序列性、节奏性和音乐同步性不足的问题。

**关键词**：舞蹈生成, Mamba模型, 扩散模型, 音乐同步, 节拍表示, 序列建模

## 3 点简述
- 核心问题：现有方法难以捕捉舞蹈的序列性、节奏性和音乐同步性。
- 方法要点：采用Mamba替代Transformer，结合高斯节拍表示指导解码。
- 实验或效果：在AIST++和FineDance数据集上验证，从短到长舞蹈生成效果优于先前方法。

## 摘要（原文）

> Dance is a form of human motion characterized by emotional expression and communication, playing a role in various fields such as music, virtual reality, and content creation. Existing methods for dance generation often fail to adequately capture the inherently sequential, rhythmical, and music-synchronized characteristics of dance. In this paper, we propose \emph{MambaDance}, a new dance generation approach that leverages a Mamba-based diffusion model. Mamba, well-suited to handling long and autoregressive sequences, is integrated into our two-stage diffusion architecture, substituting off-the-shelf Transformer. Additionally, considering the critical role of musical beats in dance choreography, we propose a Gaussian-based beat representation to explicitly guide the decoding of dance sequences. Experiments on AIST++ and FineDance datasets for each sequence length show that our proposed method effectively generates plausible dance movements while reflecting essential characteristics, consistently from short to long dances, compared to the previous methods. Additional qualitative results and demo videos are available at \small{https://vision3d-lab.github.io/mambadance}.

