---
layout: default
title: CoDAR: Continuous Diffusion Language Models are More Powerful Than You Think
---

# CoDAR: Continuous Diffusion Language Models are More Powerful Than You Think
**arXiv**：[2603.02547v1](https://arxiv.org/abs/2603.02547) · [PDF](https://arxiv.org/pdf/2603.02547.pdf)  
**作者**：Junzhe Shen, Jieru Zhao, Ziwei He, Zhouhan Lin  

**一句话要点**：提出CoDAR框架，通过上下文自回归解码器提升连续扩散语言模型的生成质量

**关键词**：连续扩散语言模型, 词元舍入, 上下文自回归解码器, 生成质量提升, 嵌入空间扩散

## 3 点简述
- 核心问题：连续扩散语言模型因词元舍入瓶颈而落后于离散扩散方法
- 方法要点：采用两阶段框架，在嵌入空间保持连续扩散，学习上下文条件离散化解码器
- 实验或效果：在LM1B和OpenWebText上显著改进生成质量，与强离散模型竞争

## 摘要（原文）

> We study why continuous diffusion language models (DLMs) have lagged behind discrete diffusion approaches despite their appealing continuous generative dynamics. Under a controlled token--recovery study, we identify token rounding, the final projection from denoised embeddings to tokens, as a primary bottleneck. Building on these insights, we propose CoDAR (Continuous Diffusion with Contextual AutoRegressive Decoder), a two--stage framework that keeps diffusion entirely continuous in an embedding space while learning a strong, context--conditional discretizer: an autoregressive Transformer decoder that cross--attends to the denoised embedding sequence and performs contextualized rounding to tokens. Experiments on LM1B and OpenWebText demonstrate that CoDAR substantially improves generation quality over latent diffusion and becomes competitive with strong discrete DLMs, while exposing a simple decoder--temperature knob to navigate the fluency--diversity trade off.

