---
layout: default
title: SE-DiCoW: Self-Enrolled Diarization-Conditioned Whisper
---

# SE-DiCoW: Self-Enrolled Diarization-Conditioned Whisper
**arXiv**：[2601.19194v1](https://arxiv.org/abs/2601.19194) · [PDF](https://arxiv.org/pdf/2601.19194.pdf)  
**作者**：Alexander Polok, Dominik Klement, Samuele Cornell, Matthew Wiesner, Jan Černocký, Sanjeev Khudanpur, Lukáš Burget  

**一句话要点**：提出SE-DiCoW以解决多说话人环境中说话人归属语音识别的重叠说话人歧义问题

**关键词**：说话人归属语音识别, 多说话人环境, 说话人日志, 跨注意力机制, 语音识别基准测试

## 3 点简述
- 核心问题：DiCoW中STNO掩码在说话人完全重叠时导致条件信息歧义，影响转录准确性
- 方法要点：利用说话人日志输出定位目标说话人最活跃的注册段，通过跨注意力层作为固定条件
- 实验或效果：在EMMA MT-ASR基准上，SE-DiCoW相比原始DiCoW将宏平均tcpWER相对降低52.4%

## 摘要（原文）

> Speaker-attributed automatic speech recognition (ASR) in multi-speaker environments remains a major challenge. While some approaches achieve strong performance when fine-tuned on specific domains, few systems generalize well across out-of-domain datasets. Our prior work, Diarization-Conditioned Whisper (DiCoW), leverages speaker diarization outputs as conditioning information and, with minimal fine-tuning, demonstrated strong multilingual and multi-domain performance. In this paper, we address a key limitation of DiCoW: ambiguity in Silence-Target-Non-target-Overlap (STNO) masks, where two or more fully overlapping speakers may have nearly identical conditioning despite differing transcriptions. We introduce SE-DiCoW (Self-Enrolled Diarization-Conditioned Whisper), which uses diarization output to locate an enrollment segment anywhere in the conversation where the target speaker is most active. This enrollment segment is used as fixed conditioning via cross-attention at each encoder layer. We further refine DiCoW with improved data segmentation, model initialization, and augmentation. Together, these advances yield substantial gains: SE-DiCoW reduces macro-averaged tcpWER by 52.4% relative to the original DiCoW on the EMMA MT-ASR benchmark.

