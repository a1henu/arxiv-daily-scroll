---
layout: default
title: Measuring the Redundancy of Decoder Layers in SpeechLLMs
---

# Measuring the Redundancy of Decoder Layers in SpeechLLMs
**arXiv**：[2603.05121v1](https://arxiv.org/abs/2603.05121) · [PDF](https://arxiv.org/pdf/2603.05121.pdf)  
**作者**：Adel Moumen, Guangzhi Sun, Philip C Woodland  

**一句话要点**：测量SpeechLLMs解码器层冗余性，揭示跨任务与语言的全局冗余结构，支持剪枝部署。

**关键词**：语音大语言模型, 解码器冗余, 层剪枝, 自动语音识别, 语音翻译, 多任务学习

## 3 点简述
- 研究SpeechLLMs解码器容量冗余问题，发现其继承自预训练LLM，文本与语音输入冗余块相似。
- 通过剪枝解码器层并分析后剪枝愈合，测量冗余容量，7-8B模型仅需60%解码器层保持良好ASR性能。
- 推广至语音翻译，相同冗余层跨语音编码器、任务和语言存在，表明全局冗余结构，支持单剪枝多任务部署。

## 摘要（原文）

> Speech Large Language Models route speech encoder representations into an LLM decoder that typically accounts for over 90% of total parameters. We study how much of this decoder capacity is actually needed for speech tasks. Across two LLM families and three scales (1-8B), we show that decoder redundancy is largely inherited from the pretrained LLM: text and speech inputs yield similar redundant blocks. We then measure excess capacity by pruning decoder layers and analysing post-pruning healing to increase robustness. Our findings show that 7-8B models retain good ASR performance with only 60% of decoder layers, and the same trend extends to smaller scales with reduced pruning tolerance. We then generalise to speech translation, and show that the same blocks of layers are redundant across speech encoders, tasks and languages, indicating that a more global redundancy structure exists, enabling a single pruned and multi-tasks SpeechLLM backbone to be deployed.

