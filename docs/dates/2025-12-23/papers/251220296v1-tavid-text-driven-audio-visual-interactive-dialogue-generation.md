---
layout: default
title: TAVID: Text-Driven Audio-Visual Interactive Dialogue Generation
---

# TAVID: Text-Driven Audio-Visual Interactive Dialogue Generation
**arXiv**：[2512.20296v1](https://arxiv.org/abs/2512.20296) · [PDF](https://arxiv.org/pdf/2512.20296.pdf)  
**作者**：Ji-Hoon Kim, Junseok Ahn, Doyeop Kwak, Joon Son Chung, Shinji Watanabe  

**一句话要点**：提出TAVID框架以同步生成交互式视频和对话语音，解决多模态对话生成问题。

**关键词**：多模态对话生成, 音频-视觉交互, 同步生成, 交互式视频, 对话语音合成

## 3 点简述
- 核心问题：现有研究孤立处理说话或倾听头部生成，忽略音频-视觉交互的多模态耦合。
- 方法要点：通过运动映射器和说话者映射器，实现音频与视觉模态间的双向信息交换。
- 实验或效果：在面部真实性、倾听响应性、交互流畅性和语音质量四维度评估，实验证明有效性。

## 摘要（原文）

> The objective of this paper is to jointly synthesize interactive videos and conversational speech from text and reference images. With the ultimate goal of building human-like conversational systems, recent studies have explored talking or listening head generation as well as conversational speech generation. However, these works are typically studied in isolation, overlooking the multimodal nature of human conversation, which involves tightly coupled audio-visual interactions. In this paper, we introduce TAVID, a unified framework that generates both interactive faces and conversational speech in a synchronized manner. TAVID integrates face and speech generation pipelines through two cross-modal mappers (i.e., a motion mapper and a speaker mapper), which enable bidirectional exchange of complementary information between the audio and visual modalities. We evaluate our system across four dimensions: talking face realism, listening head responsiveness, dyadic interaction fluency, and speech quality. Extensive experiments demonstrate the effectiveness of our approach across all these aspects.

