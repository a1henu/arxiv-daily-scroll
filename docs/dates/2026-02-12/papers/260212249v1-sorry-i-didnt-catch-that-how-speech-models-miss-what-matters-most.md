---
layout: default
title: "Sorry, I Didn't Catch That": How Speech Models Miss What Matters Most
---

# "Sorry, I Didn't Catch That": How Speech Models Miss What Matters Most
**arXiv**：[2602.12249v1](https://arxiv.org/abs/2602.12249) · [PDF](https://arxiv.org/pdf/2602.12249.pdf)  
**作者**：Kaitlyn Zhou, Martijn Bartelds, Federico Bianchi, James Zou  

**一句话要点**：提出合成数据生成方法以解决语音模型在真实高风险场景中的转录错误问题

**关键词**：语音识别, 高风险转录, 合成数据生成, 微调优化, 命名实体处理

## 3 点简述
- 核心问题：语音识别系统在标准基准上表现良好，但在真实高风险短话语（如美国街道名）中错误率高，平均达44%
- 方法要点：使用开源文本转语音模型生成多样化的命名实体发音，构建合成数据用于微调
- 实验或效果：微调后，非英语母语者的街道名转录准确率相对提升近60%，减少路由距离误差

## 摘要（原文）

> Despite speech recognition systems achieving low word error rates on standard benchmarks, they often fail on short, high-stakes utterances in real-world deployments. Here, we study this failure mode in a high-stakes task: the transcription of U.S. street names as spoken by U.S. participants. We evaluate 15 models from OpenAI, Deepgram, Google, and Microsoft on recordings from linguistically diverse U.S. speakers and find an average transcription error rate of 44%. We quantify the downstream impact of failed transcriptions by geographic locations and show that mis-transcriptions systematically cause errors for all speakers, but that routing distance errors are twice as large for non-English primary speakers compared to English primary speakers. To mitigate this harm, we introduce a synthetic data generation approach that produces diverse pronunciations of named entities using open-source text-to-speech models. Fine-tuning with less than 1,000 synthetic samples improves street name transcription accuracy by nearly 60% (relative to base models) for non-English primary speakers. Our results highlight a critical gap between benchmark performance and real-world reliability in speech systems and demonstrate a simple, scalable path to reducing high-stakes transcription errors.

