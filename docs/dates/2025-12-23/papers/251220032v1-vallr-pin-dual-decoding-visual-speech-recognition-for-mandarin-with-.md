---
layout: default
title: VALLR-Pin: Dual-Decoding Visual Speech Recognition for Mandarin with Pinyin-Guided LLM Refinement
---

# VALLR-Pin: Dual-Decoding Visual Speech Recognition for Mandarin with Pinyin-Guided LLM Refinement
**arXiv**：[2512.20032v1](https://arxiv.org/abs/2512.20032) · [PDF](https://arxiv.org/pdf/2512.20032.pdf)  
**作者**：Chang Sun, Dongliang Xie, Bo Qin, Hong Yang  

**一句话要点**：提出VALLR-Pin双解码视觉语音识别框架，结合拼音引导的LLM精炼以提升汉语唇读性能

**关键词**：视觉语音识别, 汉语唇读, 双解码器, 拼音引导, LLM精炼, 多任务学习

## 3 点简述
- 针对汉语唇读中视位模糊和同音词多的挑战，提出双解码器联合预测字符和拼音
- 利用LLM结合拼音输出和多候选文本进行歧义消解和转录精炼
- 通过合成噪声数据微调LLM，使其适应模型特定错误模式，提升整体性能

## 摘要（原文）

> Visual Speech Recognition aims to transcribe spoken words from silent lip-motion videos. This task is particularly challenging for Mandarin, as visemes are highly ambiguous and homophones are prevalent. We propose VALLR-Pin, a novel two-stage framework that extends the recent VALLR architecture from English to Mandarin. First, a shared video encoder feeds into dual decoders, which jointly predict both Chinese character sequences and their standard Pinyin romanization. The multi-task learning of character and phonetic outputs fosters robust visual-semantic representations. During inference, the text decoder generates multiple candidate transcripts. We construct a prompt by concatenating the Pinyin output with these candidate Chinese sequences and feed it to a large language model to resolve ambiguities and refine the transcription. This provides the LLM with explicit phonetic context to correct homophone-induced errors. Finally, we fine-tune the LLM on synthetic noisy examples: we generate imperfect Pinyin-text pairs from intermediate VALLR-Pin checkpoints using the training data, creating instruction-response pairs for error correction. This endows the LLM with awareness of our model's specific error patterns. In summary, VALLR-Pin synergizes visual features with phonetic and linguistic context to improve Mandarin lip-reading performance.

