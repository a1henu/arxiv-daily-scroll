---
layout: default
title: AV-Dialog: Spoken Dialogue Models with Audio-Visual Input
---

# AV-Dialog: Spoken Dialogue Models with Audio-Visual Input
**arXiv**：[2511.11124v1](https://arxiv.org/abs/2511.11124) · [PDF](https://arxiv.org/pdf/2511.11124.pdf)  
**作者**：Tuochao Chen, Bandhav Veluri, Hongyu Gong, Shyamnath Gollakota  

**一句话要点**：提出AV-Dialog多模态对话框架，结合视听输入以提升嘈杂环境下的对话鲁棒性。

**关键词**：多模态对话, 视听融合, 轮转预测, 嘈杂环境鲁棒性, 说话者跟踪

## 3 点简述
- 核心问题：对话模型在嘈杂多说话者环境中响应不相关且轮转不自然。
- 方法要点：融合音频和视觉线索，进行多任务多阶段训练，实现说话者跟踪和轮转预测。
- 实验或效果：在干扰下优于纯音频模型，减少转录错误并提升人类评价对话质量。

## 摘要（原文）

> Dialogue models falter in noisy, multi-speaker environments, often producing irrelevant responses and awkward turn-taking. We present AV-Dialog, the first multimodal dialog framework that uses both audio and visual cues to track the target speaker, predict turn-taking, and generate coherent responses. By combining acoustic tokenization with multi-task, multi-stage training on monadic, synthetic, and real audio-visual dialogue datasets, AV-Dialog achieves robust streaming transcription, semantically grounded turn-boundary detection and accurate responses, resulting in a natural conversational flow. Experiments show that AV-Dialog outperforms audio-only models under interference, reducing transcription errors, improving turn-taking prediction, and enhancing human-rated dialogue quality. These results highlight the power of seeing as well as hearing for speaker-aware interaction, paving the way for {spoken} dialogue agents that perform {robustly} in real-world, noisy environments.

