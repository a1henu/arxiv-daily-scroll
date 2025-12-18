---
layout: default
title: DiffusionVL: Translating Any Autoregressive Models into Diffusion Vision Language Models
---

# DiffusionVL: Translating Any Autoregressive Models into Diffusion Vision Language Models
**arXiv**：[2512.15713v1](https://arxiv.org/abs/2512.15713) · [PDF](https://arxiv.org/pdf/2512.15713.pdf)  
**作者**：Lunbin Zeng, Jingfeng Yao, Bencheng Liao, Hongyuan Tao, Wenyu Liu, Xinggang Wang  

**一句话要点**：提出DiffusionVL，将任意自回归模型转换为扩散视觉语言模型，提升性能与推理速度。

**关键词**：扩散视觉语言模型, 自回归模型转换, 块解码设计, 推理加速, 视觉指令调优

## 3 点简述
- 核心问题：扩散视觉语言模型性能落后于主流自回归模型，需基于现有强大模型构建。
- 方法要点：通过简单微调，将自回归预训练模型适配到扩散范式，并引入块解码设计支持任意长度生成。
- 实验或效果：训练数据少于5%，在MMMU-Pro和MME基准上性能提升超34%，推理速度加倍。

## 摘要（原文）

> In recent multimodal research, the diffusion paradigm has emerged as a promising alternative to the autoregressive paradigm (AR), owing to its unique decoding advantages. However, due to the capability limitations of the base diffusion language model, the performance of the diffusion vision language model (dVLM) still lags significantly behind that of mainstream models. This leads to a simple yet fundamental question: Is it possible to construct dVLMs based on existing powerful AR models? In response, we propose DiffusionVL, a dVLM family that could be translated from any powerful AR models. Through simple fine-tuning, we successfully adapt AR pre-trained models into the diffusion paradigm. This approach yields two key observations: (1) The paradigm shift from AR-based multimodal models to diffusion is remarkably effective. (2) Direct conversion of an AR language model to a dVLM is also feasible, achieving performance competitive with LLaVA-style visual-instruction-tuning. Further, we introduce a block-decoding design into dVLMs that supports arbitrary-length generation and KV cache reuse, achieving a significant inference speedup. We conduct a large number of experiments. Despite training with less than 5% of the data required by prior methods, DiffusionVL achieves a comprehensive performance improvement-a 34.4% gain on the MMMU-Pro (vision) bench and 37.5% gain on the MME (Cog.) bench-alongside a 2x inference speedup. The model and code are released at https://github.com/hustvl/DiffusionVL.

