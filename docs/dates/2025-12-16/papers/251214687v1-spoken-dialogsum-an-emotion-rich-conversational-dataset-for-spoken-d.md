---
layout: default
title: Spoken DialogSum: An Emotion-Rich Conversational Dataset for Spoken Dialogue Summarization
---

# Spoken DialogSum: An Emotion-Rich Conversational Dataset for Spoken Dialogue Summarization
**arXiv**：[2512.14687v1](https://arxiv.org/abs/2512.14687) · [PDF](https://arxiv.org/pdf/2512.14687.pdf)  
**作者**：Yen-Ju Lu, Kunxiao Gao, Mingrui Liang, Helin Wang, Thomas Thebaud, Laureano Moro-Velazquez, Najim Dehak, Jesus Villalba  

**一句话要点**：提出Spoken DialogSum数据集，以解决语音对话摘要中缺乏语音、摘要与副语言线索对齐数据的问题。

**关键词**：语音对话摘要, 情感感知, 副语言线索, 音频语言模型, 数据集构建

## 3 点简述
- 核心问题：语音对话摘要研究缺乏同时包含原始音频、摘要和副语言标签（如情感）的数据集。
- 方法要点：通过LLM重写对话脚本并标注情感等特征，再用TTS合成对齐语音，构建首个对齐音频与情感摘要的语料库。
- 实验或效果：基线实验显示，端到端音频语言模型相比级联系统将情感摘要ROUGE-L提升了28%。

## 摘要（原文）

> Recent audio language models can follow long conversations. However, research on emotion-aware or spoken dialogue summarization is constrained by the lack of data that links speech, summaries, and paralinguistic cues. We introduce Spoken DialogSum, the first corpus aligning raw conversational audio with factual summaries, emotion-rich summaries, and utterance-level labels for speaker age, gender, and emotion. The dataset is built in two stages: first, an LLM rewrites DialogSum scripts with Switchboard-style fillers and back-channels, then tags each utterance with emotion, pitch, and speaking rate. Second, an expressive TTS engine synthesizes speech from the tagged scripts, aligned with paralinguistic labels. Spoken DialogSum comprises 13,460 emotion-diverse dialogues, each paired with both a factual and an emotion-focused summary. The dataset is available online at https://fatfat-emosum.github.io/EmoDialog-Sum-Audio-Samples/. Baselines show that an Audio-LLM raises emotional-summary ROUGE-L by 28% relative to a cascaded ASR-LLM system, confirming the value of end-to-end speech modeling.

