---
layout: default
title: MAD: Modality-Adaptive Decoding for Mitigating Cross-Modal Hallucinations in Multimodal Large Language Models
---

# MAD: Modality-Adaptive Decoding for Mitigating Cross-Modal Hallucinations in Multimodal Large Language Models
**arXiv**：[2601.21181v1](https://arxiv.org/abs/2601.21181) · [PDF](https://arxiv.org/pdf/2601.21181.pdf)  
**作者**：Sangyun Chung, Se Yeon Kim, Youngchae Chee, Yong Man Ro  

**一句话要点**：提出模态自适应解码以缓解多模态大语言模型中的跨模态幻觉问题

**关键词**：跨模态幻觉, 模态自适应解码, 多模态大语言模型, 对比解码, 音频视觉语言模型, 训练无关方法

## 3 点简述
- 核心问题：多模态大语言模型存在跨模态幻觉，即一个模态不当影响另一模态生成，导致输出虚假信息
- 方法要点：通过训练无关的自适应解码，基于任务需求加权模态特定分支，利用模型自评估模态相关性
- 实验或效果：在CMM和AVHBench上显著减少幻觉，如VideoLLaMA2-AV和Qwen2.5-Omni模型性能提升

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) suffer from cross-modal hallucinations, where one modality inappropriately influences generation about another, leading to fabricated output. This exposes a more fundamental deficiency in modality-interaction control. To address this, we propose Modality-Adaptive Decoding (MAD), a training-free method that adaptively weights modality-specific decoding branches based on task requirements. MAD leverages the model's inherent ability to self-assess modality relevance by querying which modalities are needed for each task. The extracted modality probabilities are then used to adaptively weight contrastive decoding branches, enabling the model to focus on relevant information while suppressing cross-modal interference. Extensive experiments on CMM and AVHBench demonstrate that MAD significantly reduces cross-modal hallucinations across multiple audio-visual language models (7.8\% and 2.0\% improvements for VideoLLaMA2-AV, 8.7\% and 4.7\% improvements for Qwen2.5-Omni). Our approach demonstrates that explicit modality awareness through self-assessment is crucial for robust multimodal reasoning, offering a principled extension to existing contrastive decoding methods. Our code is available at \href{https://github.com/top-yun/MAD}{https://github.com/top-yun/MAD}

