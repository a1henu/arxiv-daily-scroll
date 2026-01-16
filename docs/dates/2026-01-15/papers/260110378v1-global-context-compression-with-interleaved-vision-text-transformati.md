---
layout: default
title: Global Context Compression with Interleaved Vision-Text Transformation
---

# Global Context Compression with Interleaved Vision-Text Transformation
**arXiv**：[2601.10378v1](https://arxiv.org/abs/2601.10378) · [PDF](https://arxiv.org/pdf/2601.10378.pdf)  
**作者**：Dian Jiao, Jiaxin Duan, Shuai Zhao, Jiabing Leng, Yiran Zhang, Feng Huang  

**一句话要点**：提出VIST2模型，通过视觉-文本交错转换实现全局上下文压缩，以提升长文本生成效率。

**关键词**：全局上下文压缩, 视觉-文本交错转换, 长文本生成, Transformer模型, 计算效率优化

## 3 点简述
- 核心问题：现有视觉编码方法在推理阶段无法节省计算或内存成本，影响长文本处理效率。
- 方法要点：将文本块渲染为草图图像，交错视觉与文本编码，仅依赖视觉令牌预测下一个文本令牌分布。
- 实验或效果：在4倍压缩比下，模型在长写作任务中显著优于基线，实现生成加速、内存和计算量大幅减少。

## 摘要（原文）

> Recent achievements of vision-language models in end-to-end OCR point to a new avenue for low-loss compression of textual information. This motivates earlier works that render the Transformer's input into images for prefilling, which effectively reduces the number of tokens through visual encoding, thereby alleviating the quadratically increased Attention computations. However, this partial compression fails to save computational or memory costs at token-by-token inference. In this paper, we investigate global context compression, which saves tokens at both prefilling and inference stages. Consequently, we propose VIST2, a novel Transformer that interleaves input text chunks alongside their visual encoding, while depending exclusively on visual tokens in the pre-context to predict the next text token distribution. Around this idea, we render text chunks into sketch images and train VIST2 in multiple stages, starting from curriculum-scheduled pretraining for optical language modeling, followed by modal-interleaved instruction tuning. We conduct extensive experiments using VIST2 families scaled from 0.6B to 8B to explore the training recipe and hyperparameters. With a 4$\times$ compression ratio, the resulting models demonstrate significant superiority over baselines on long writing tasks, achieving, on average, a 3$\times$ speedup in first-token generation, 77% reduction in memory usage, and 74% reduction in FLOPS. Our codes and datasets will be public to support further studies.

