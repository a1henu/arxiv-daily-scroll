---
layout: default
title: DiffuSpeech: Silent Thought, Spoken Answer via Unified Speech-Text Diffusion
---

# DiffuSpeech: Silent Thought, Spoken Answer via Unified Speech-Text Diffusion
**arXiv**：[2601.22889v1](https://arxiv.org/abs/2601.22889) · [PDF](https://arxiv.org/pdf/2601.22889.pdf)  
**作者**：Yuxuan Lou, Ziming Wu, Yaochen Wang, Yong Liu, Yingxuan Ren, Fuming Lai, Shaobing Lian, Jie Tang, Yang You  

**一句话要点**：提出DiffuSpeech，通过统一语音-文本扩散模型实现“无声思考、有声回答”，提升语音问答准确性和质量。

**关键词**：语音-文本扩散模型, 无声思考, 语音问答, 推理轨迹, 联合生成, 掩码扩散

## 3 点简述
- 当前语音语言模型直接生成响应，缺乏显式推理，导致错误无法纠正。
- DiffuSpeech采用掩码扩散框架，联合生成文本推理轨迹和语音令牌，支持理解和生成。
- 实验显示，DiffuSpeech在语音问答准确性和TTS质量上达到最优，并保持语言理解能力。

## 摘要（原文）

> Current speech language models generate responses directly without explicit reasoning, leading to errors that cannot be corrected once audio is produced. We introduce \textbf{``Silent Thought, Spoken Answer''} -- a paradigm where speech LLMs generate internal text reasoning alongside spoken responses, with thinking traces informing speech quality. To realize this, we present \method{}, the first diffusion-based speech-text language model supporting both understanding and generation, unifying discrete text and tokenized speech under a single masked diffusion framework. Unlike autoregressive approaches, \method{} jointly generates reasoning traces and speech tokens through iterative denoising, with modality-specific masking schedules. We also construct \dataset{}, the first speech QA dataset with paired text reasoning traces, containing 26K samples totaling 319 hours. Experiments show \method{} achieves state-of-the-art speech-to-speech QA accuracy, outperforming the best baseline by up to 9 points, while attaining the best TTS quality among generative models (6.2\% WER) and preserving language understanding (66.2\% MMLU). Ablations confirm that both the diffusion architecture and thinking traces contribute to these gains.

