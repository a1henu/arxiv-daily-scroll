---
layout: default
title: IndexTTS 2.5 Technical Report
---

# IndexTTS 2.5 Technical Report
**arXiv**：[2601.03888v1](https://arxiv.org/abs/2601.03888) · [PDF](https://arxiv.org/pdf/2601.03888.pdf)  
**作者**：Yunpei Li, Xun Zhou, Jinchao Wang, Lu Wang, Yong Wu, Siyi Zhou, Yiquan Zhou, Jingchen Shu  

**一句话要点**：提出IndexTTS 2.5以增强零样本多语言情感语音合成的效率与质量

**关键词**：零样本语音合成, 多语言情感TTS, 非自回归生成, 语义编解码, 强化学习优化, Zipformer架构

## 3 点简述
- 核心问题：提升零样本多语言情感TTS的覆盖范围、推理速度和合成质量
- 方法要点：通过语义编解码压缩、架构升级、多语言扩展和强化学习优化实现改进
- 实验或效果：在保持WER和说话人相似度下，RTF提升2.28倍，支持中英日西语言

## 摘要（原文）

> In prior work, we introduced IndexTTS 2, a zero-shot neural text-to-speech foundation model comprising two core components: a transformer-based Text-to-Semantic (T2S) module and a non-autoregressive Semantic-to-Mel (S2M) module, which together enable faithful emotion replication and establish the first autoregressive duration-controllable generative paradigm. Building upon this, we present IndexTTS 2.5, which significantly enhances multilingual coverage, inference speed, and overall synthesis quality through four key improvements: 1) Semantic Codec Compression: we reduce the semantic codec frame rate from 50 Hz to 25 Hz, halving sequence length and substantially lowering both training and inference costs; 2) Architectural Upgrade: we replace the U-DiT-based backbone of the S2M module with a more efficient Zipformer-based modeling architecture, achieving notable parameter reduction and faster mel-spectrogram generation; 3) Multilingual Extension: We propose three explicit cross-lingual modeling strategies, boundary-aware alignment, token-level concatenation, and instruction-guided generation, establishing practical design principles for zero-shot multilingual emotional TTS that supports Chinese, English, Japanese, and Spanish, and enables robust emotion transfer even without target-language emotional training data; 4) Reinforcement Learning Optimization: we apply GRPO in post-training of the T2S module, improving pronunciation accuracy and natrualness. Experiments show that IndexTTS 2.5 not only supports broader language coverage but also replicates emotional prosody in unseen languages under the same zero-shot setting. IndexTTS 2.5 achieves a 2.28 times improvement in RTF while maintaining comparable WER and speaker similarity to IndexTTS 2.

