---
layout: default
title: Hearing to Translate: The Effectiveness of Speech Modality Integration into LLMs
---

# Hearing to Translate: The Effectiveness of Speech Modality Integration into LLMs
**arXiv**：[2512.16378v1](https://arxiv.org/abs/2512.16378) · [PDF](https://arxiv.org/pdf/2512.16378.pdf)  
**作者**：Sara Papi, Javier Garcia Gilabert, Zachary Hopton, Vilém Zouhar, Carlos Escolano, Gerard I. Gállego, Jorge Iranzo-Sánchez, Ahrii Kim, Dominik Macháček, Patricia Schmidtova, Maike Züfle  

**一句话要点**：提出Hearing to Translate测试套件，评估SpeechLLMs在语音翻译中的性能，发现级联系统仍最可靠。

**关键词**：语音大语言模型, 语音翻译, 级联系统, 多语言基准, 挑战条件评估

## 3 点简述
- 核心问题：SpeechLLMs集成语音模态是否能超越传统级联架构的语音翻译质量。
- 方法要点：构建首个全面测试套件，比较5个SpeechLLMs与16个直接和级联系统。
- 实验或效果：在16个基准、13种语言对和9种挑战条件下，级联系统整体表现最佳，SpeechLLMs仅在特定场景匹配。

## 摘要（原文）

> As Large Language Models (LLMs) expand beyond text, integrating speech as a native modality has given rise to SpeechLLMs, which aim to translate spoken language directly, thereby bypassing traditional transcription-based pipelines. Whether this integration improves speech-to-text translation quality over established cascaded architectures, however, remains an open question. We present Hearing to Translate, the first comprehensive test suite rigorously benchmarking 5 state-of-the-art SpeechLLMs against 16 strong direct and cascade systems that couple leading speech foundation models (SFM), with multilingual LLMs. Our analysis spans 16 benchmarks, 13 language pairs, and 9 challenging conditions, including disfluent, noisy, and long-form speech. Across this extensive evaluation, we find that cascaded systems remain the most reliable overall, while current SpeechLLMs only match cascades in selected settings and SFMs lag behind both, highlighting that integrating an LLM, either within the model or in a pipeline, is essential for high-quality speech translation.

