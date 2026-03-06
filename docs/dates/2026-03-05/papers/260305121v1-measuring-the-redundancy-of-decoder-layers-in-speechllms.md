---
layout: default
title: Measuring the Redundancy of Decoder Layers in SpeechLLMs
---

# Measuring the Redundancy of Decoder Layers in SpeechLLMs
**arXiv**：[2603.05121v1](https://arxiv.org/abs/2603.05121) · [PDF](https://arxiv.org/pdf/2603.05121.pdf)  
**作者**：Adel Moumen, Guangzhi Sun, Philip C Woodland  

**一句话要点**：测量SpeechLLMs解码器层冗余性，揭示跨任务与语言的全局冗余结构。

**关键词**：语音大语言模型, 解码器冗余, 层剪枝, 自动语音识别, 语音翻译, 多任务学习

## 3 点简述
- 研究SpeechLLMs中解码器层冗余问题，解码器参数占比超90%。
- 通过剪枝解码器层分析冗余，发现冗余继承自预训练LLM，文本与语音输入相似。
- 实验显示7-8B模型仅需60%解码器层保持ASR性能，冗余结构跨任务、语言通用。

## 摘要（原文）

> Speech Large Language Models route speech encoder representations into an LLM decoder that typically accounts for over 90% of total parameters. We study how much of this decoder capacity is actually needed for speech tasks. Across two LLM families and three scales (1-8B), we show that decoder redundancy is largely inherited from the pretrained LLM: text and speech inputs yield similar redundant blocks. We then measure excess capacity by pruning decoder layers and analysing post-pruning healing to increase robustness. Our findings show that 7-8B models retain good ASR performance with only 60% of decoder layers, and the same trend extends to smaller scales with reduced pruning tolerance. We then generalise to speech translation, and show that the same blocks of layers are redundant across speech encoders, tasks and languages, indicating that a more global redundancy structure exists, enabling a single pruned and multi-tasks SpeechLLM backbone to be deployed.

