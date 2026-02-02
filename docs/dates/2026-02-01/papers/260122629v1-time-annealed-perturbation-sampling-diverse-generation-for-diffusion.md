---
layout: default
title: Time-Annealed Perturbation Sampling: Diverse Generation for Diffusion Language Models
---

# Time-Annealed Perturbation Sampling: Diverse Generation for Diffusion Language Models
**arXiv**：[2601.22629v1](https://arxiv.org/abs/2601.22629) · [PDF](https://arxiv.org/pdf/2601.22629.pdf)  
**作者**：Jingxuan Wu, Zhenglin Wan, Xingrui Yu, Yuzhe Yang, Yiqiao Huang, Ivor Tsang, Yang You  

**一句话要点**：提出时间退火扰动采样以增强扩散语言模型的生成多样性

**关键词**：扩散语言模型, 生成多样性, 推理策略, 时间退火采样, 语义控制

## 3 点简述
- 扩散语言模型在文本生成中多样性控制不足，早期去噪决定语义结构，后期聚焦词汇精炼。
- TAPS在推理时早期引入扰动促进语义分支，后期减少扰动保持流畅性和指令遵循，无需额外训练。
- 在LLaDA和TraDo等模型上验证，TAPS提升创意写作和推理任务的输出多样性，不损害生成质量。

## 摘要（原文）

> Diffusion language models (Diffusion-LMs) introduce an explicit temporal dimension into text generation, yet how this structure can be leveraged to control generation diversity for exploring multiple valid semantic or reasoning paths remains underexplored. In this paper, we show that Diffusion-LMs, like diffusion models in image generation, exhibit a temporal division of labor: early denoising steps largely determine the global semantic structure, while later steps focus on local lexical refinement. Building on this insight, we propose Time-Annealed Perturbation Sampling (TAPS), a training-free inference strategy that encourages semantic branching early in the diffusion process while progressively reducing perturbations to preserve fluency and instruction adherence. TAPS is compatible with both non-autoregressive and semi-autoregressive Diffusion backbones, demonstrated on LLaDA and TraDo in our paper, and consistently improves output diversity across creative writing and reasoning benchmarks without compromising generation quality.

