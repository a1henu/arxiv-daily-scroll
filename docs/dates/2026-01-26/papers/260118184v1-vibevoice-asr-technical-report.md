---
layout: default
title: VIBEVOICE-ASR Technical Report
---

# VIBEVOICE-ASR Technical Report
**arXiv**：[2601.18184v1](https://arxiv.org/abs/2601.18184) · [PDF](https://arxiv.org/pdf/2601.18184.pdf)  
**作者**：Zhiliang Peng, Jianwei Yu, Yaoyao Chang, Zilong Wang, Li Dong, Yingbo Hao, Yujie Tu, Chenyu Yang, Wenhui Wang, Songchen Xu, Yutao Sun, Hangbo Bao, Weijiang Xu, Yi Zhu, Zehua Wang, Ting Song, Yan Xia, Zewen Chi, Shaohan Huang, Liang Wang, Chuang Ding, Shuai Wang, Xie Chen, Furu Wei  

**一句话要点**：提出VibeVoice-ASR框架，以解决长音频中上下文碎片化和多说话者复杂性问题。

**关键词**：长音频语音理解, 端到端语音处理, 多语言语音识别, 说话人日志, 上下文注入机制

## 3 点简述
- 核心问题：长音频（如会议、播客）中的上下文碎片化和多说话者复杂性挑战。
- 方法要点：统一语音识别、说话人日志和时间戳为端到端生成任务，支持单次处理长达60分钟音频。
- 实验或效果：支持50多种语言，无需显式语言设置，通过提示机制提升领域术语和歧义字符准确性。

## 摘要（原文）

> This report presents VibeVoice-ASR, a general-purpose speech understanding framework built upon VibeVoice, designed to address the persistent challenges of context fragmentation and multi-speaker complexity in long-form audio (e.g., meetings, podcasts) that remain despite recent advancements in short-form speech recognition. Unlike traditional pipelined approaches that rely on audio chunking, VibeVoice-ASRsupports single-pass processing for up to 60 minutes of audio. It unifies Automatic Speech Recognition, Speaker Diarization, and Timestamping into a single end-to-end generation task. In addition, VibeVoice-ASR supports over 50 languages, requires no explicit language setting, and natively handles code-switching within and across utterances. Furthermore, we introduce a prompt-based context injection mechanism that allows users to supply customized conetxt, significantly improving accuracy on domain-specific terminology and polyphonic character disambiguation.

