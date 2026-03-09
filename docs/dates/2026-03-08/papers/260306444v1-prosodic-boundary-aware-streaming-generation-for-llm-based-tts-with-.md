---
layout: default
title: Prosodic Boundary-Aware Streaming Generation for LLM-Based TTS with Streaming Text Input
---

# Prosodic Boundary-Aware Streaming Generation for LLM-Based TTS with Streaming Text Input
**arXiv**：[2603.06444v1](https://arxiv.org/abs/2603.06444) · [PDF](https://arxiv.org/pdf/2603.06444.pdf)  
**作者**：Changsong Liu, Tianrui Wang, Ye Ni, Yizhou Peng, Eng Siong Chng  

**一句话要点**：提出韵律边界感知后训练策略，以解决流式文本输入下LLM-TTS的韵律不自然和长文本崩溃问题。

**关键词**：流式文本转语音, 韵律边界感知, 后训练策略, 长文本合成, LLM-TTS, 滑动窗口提示

## 3 点简述
- 核心问题：流式TTS因缺少前瞻文本导致韵律不自然，且无界上下文引发长文本崩溃。
- 方法要点：基于弱时间对齐数据后训练，使模型在有限未来文本下学习在内容边界提前停止。
- 实验或效果：在长短文本合成中优于基线，长文本下词错误率绝对降低66.2%，说话人和情感相似度提升。

## 摘要（原文）

> Streaming TTS that receives streaming text is essential for interactive systems, yet this scheme faces two major challenges: unnatural prosody due to missing lookahead and long-form collapse due to unbounded context. We propose a prosodic-boundary-aware post-training strategy, adapting a pretrained LLM-based TTS model using weakly time-aligned data. Specifically, the model is adapted to learn early stopping at specified content boundaries when provided with limited future text. During inference, a sliding-window prompt carries forward previous text and speech tokens, ensuring bounded context and seamless concatenation. Evaluations show our method outperforms CosyVoice-Style interleaved baseline in both short and long-form scenarios. In long-text synthesis, especially, it achieves a 66.2% absolute reduction in word error rate (from 71.0% to 4.8%) and increases speaker and emotion similarity by 16.1% and 1.5% relatively, offering a robust solution for streaming TTS with incremental text.

