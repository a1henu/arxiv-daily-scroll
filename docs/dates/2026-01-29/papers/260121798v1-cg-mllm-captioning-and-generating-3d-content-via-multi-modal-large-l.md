---
layout: default
title: CG-MLLM: Captioning and Generating 3D content via Multi-modal Large Language Models
---

# CG-MLLM: Captioning and Generating 3D content via Multi-modal Large Language Models
**arXiv**：[2601.21798v1](https://arxiv.org/abs/2601.21798) · [PDF](https://arxiv.org/pdf/2601.21798.pdf)  
**作者**：Junming Huang, Weiwei Xu  

**一句话要点**：提出CG-MLLM以解决3D内容生成中分辨率低和几何细节缺失的问题。

**关键词**：多模态大语言模型, 3D内容生成, 混合Transformer架构, 高分辨率3D, 3D VAE潜在空间, 长上下文交互

## 3 点简述
- 现有方法生成低分辨率网格或粗糙结构代理，无法原生捕获细粒度几何。
- 采用混合Transformer架构，TokenAR和BlockAR Transformer分别处理令牌级和块级内容。
- 实验显示CG-MLLM在生成高保真3D对象方面显著优于现有MLLM。

## 摘要（原文）

> Large Language Models(LLMs) have revolutionized text generation and multimodal perception, but their capabilities in 3D content generation remain underexplored. Existing methods compromise by producing either low-resolution meshes or coarse structural proxies, failing to capture fine-grained geometry natively. In this paper, we propose CG-MLLM, a novel Multi-modal Large Language Model (MLLM) capable of 3D captioning and high-resolution 3D generation in a single framework. Leveraging the Mixture-of-Transformer architecture, CG-MLLM decouples disparate modeling needs, where the Token-level Autoregressive (TokenAR) Transformer handles token-level content, and the Block-level Autoregressive (BlockAR) Transformer handles block-level content. By integrating a pre-trained vision-language backbone with a specialized 3D VAE latent space, CG-MLLM facilitates long-context interactions between standard tokens and spatial blocks within a single integrated architecture. Experimental results show that CG-MLLM significantly outperforms existing MLLMs in generating high-fidelity 3D objects, effectively bringing high-resolution 3D content creation into the mainstream LLM paradigm.

